from django.core.management.base import BaseCommand, CommandError

from learners.services.leisa_export import LeisaExportError, generate_leisa_workbook


class Command(BaseCommand):
    help = (
        "Generates the QCTO LEISA file and writes it to the given output "
        "directory. Primarily for manual/scripted recovery use — the normal "
        "trigger is the authenticated /api/exports/leisa/ endpoint."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--output-dir", default=".", help="Directory to write the LEISA file to."
        )
        parser.add_argument(
            "--sdp-name", default="Knowescape", help="SDP name used in the output filename."
        )

    def handle(self, *args, **options):
        try:
            filename, buffer = generate_leisa_workbook(sdp_name=options["sdp_name"])
        except LeisaExportError as exc:
            self.stderr.write(self.style.ERROR(f"{len(exc.errors)} enrolment(s) failed validation:"))
            for err in exc.errors:
                self.stderr.write(f"  Enrolment {err['enrolment_id']}: {err['errors']}")
            raise CommandError("Export aborted — fix the invalid enrolments above and try again.")

        output_path = f"{options['output_dir'].rstrip('/')}/{filename}"
        with open(output_path, "wb") as f:
            f.write(buffer.getvalue())

        self.stdout.write(self.style.SUCCESS(f"Wrote {output_path}"))