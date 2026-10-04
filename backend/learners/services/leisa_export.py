"""
Generates the QCTO LEISA (Learner Enrolment and Readiness for EISA) file.

Spec: QCTO "Data Load Specifications for SDPs and ACs" (effective 1 June 2022)
https://www.qcto.org.za/assets/data-loading-specification-document.pdf

This is pure logic — no HTTP, no CLI concerns — so it can be called
identically from the API endpoint and the management command.
"""
import io
from datetime import date

from django.core.exceptions import ValidationError
from openpyxl import Workbook
from openpyxl.styles import Font

from learners.models import Enrolment

# Column order exactly as per the LEISA spec (columns A through AQ).
# Do not reorder, add, or remove columns — QCTO's loader expects this
# exact layout.
LEISA_COLUMNS = [
    "SDP Code",
    "Qualification Id",
    "National ID",
    "Learner Alternate ID",
    "Alternative ID Type",
    "Equity Code",
    "Nationality Code",
    "Home Language Code",
    "Gender Code",
    "Citizen Resident Status Code",
    "Socioeconomic Status Code",
    "Disability Status Code",
    "Disability Rating",
    "Immigrant Status",
    "Learner Last Name",
    "Learner First Name",
    "Learner Middle Name",
    "Learner Title",
    "Learner Birth Date",
    "Learner Home Address 1",
    "Learner Home Address 2",
    "Learner Home Address 3",
    "Learner Postal Address 1",
    "Learner Postal Address 2",
    "Learner Postal Address 3",
    "Home Postal Code",
    "Postal Postal Code",
    "Phone Number",
    "Cell Phone Number",
    "Fax Number",
    "Email Address",
    "Province Code",
    "STATSSA Area Code",
    "POPI Act Agree",
    "POPI Act Date",
    "Expected Training Completion Date",
    "Statement of Results Status",
    "SOR Issue Date",
    "Assessment Centre Code",
    "Learner Readiness for EISA Type",
    "FLC",
    "FLC Statement of Result Number",
    "Date Stamp",
]


class LeisaExportError(Exception):
    """Raised when one or more enrolments fail validation and the
    export is refused rather than sending incomplete/invalid data to
    QCTO."""

    def __init__(self, errors):
        self.errors = errors
        super().__init__(f"{len(errors)} enrolment(s) failed validation")


def _fmt_date(value):
    """QCTO requires dates as literal YYYYMMDD text, not Excel date values."""
    if not value:
        return ""
    return value.strftime("%Y%m%d")


def _row_for_enrolment(enrolment):
    learner = enrolment.learner
    return [
        enrolment.sdp_code,
        enrolment.qualification.qualification_id,
        learner.national_id,
        learner.learner_alternate_id,
        learner.alternative_id_type,
        learner.equity_code,
        learner.nationality_code,
        learner.home_language_code,
        learner.gender,
        learner.citizen_resident_status,
        learner.socioeconomic_status_code,
        learner.disability_status_code,
        learner.disability_rating,
        learner.immigrant_status,
        learner.last_name,
        learner.first_name,
        learner.middle_name,
        learner.title,
        _fmt_date(learner.birth_date),
        learner.home_address_1,
        learner.home_address_2,
        learner.home_address_3,
        learner.postal_address_1,
        learner.postal_address_2,
        learner.postal_address_3,
        learner.home_postal_code,
        learner.postal_postal_code,
        learner.phone,
        learner.cell,
        learner.fax,
        learner.email,
        learner.province_code,
        learner.statssa_area_code,
        learner.popi_act_agree,
        _fmt_date(learner.popi_act_date),
        _fmt_date(enrolment.expected_training_completion_date),
        enrolment.statement_of_results_status,
        _fmt_date(enrolment.statement_of_results_date),
        enrolment.assessment_centre_code,
        enrolment.learner_readiness_for_eisa_type,
        enrolment.flc_status,
        enrolment.flc_certificate_number,
        _fmt_date(enrolment.date_stamp),
    ]


def generate_leisa_workbook(enrolments=None, sdp_name="Knowescape"):
    """
    Builds the LEISA workbook in memory.

    Returns (filename, BytesIO) on success. Raises LeisaExportError if
    any enrolment fails full_clean() — nothing invalid should ever
    reach a QCTO submission, so the whole export is refused rather
    than silently skipping or sending bad rows.
    """
    if enrolments is None:
        enrolments = Enrolment.objects.select_related(
            "learner", "qualification", "accreditation"
        ).all()

    errors = []
    valid_rows = []

    for enrolment in enrolments:
        try:
            enrolment.full_clean()
        except ValidationError as exc:
            errors.append({"enrolment_id": enrolment.pk, "errors": exc.message_dict})
        else:
            valid_rows.append(_row_for_enrolment(enrolment))

    if errors:
        raise LeisaExportError(errors)

    wb = Workbook()
    ws = wb.active
    ws.title = "LEISA"

    header_font = Font(bold=True)
    for col_idx, header in enumerate(LEISA_COLUMNS, start=1):
        cell = ws.cell(row=1, column=col_idx, value=header)
        cell.font = header_font

    for row_idx, row_values in enumerate(valid_rows, start=2):
        for col_idx, value in enumerate(row_values, start=1):
            cell = ws.cell(row=row_idx, column=col_idx, value=value)
            # Force every cell to Excel's Text format — QCTO's spec
            # requires values as text, not real dates/numbers (a
            # postal code like "0184" would otherwise lose its
            # leading zero, and dates would serialize wrong).
            cell.number_format = "@"

    buffer = io.BytesIO()
    wb.save(buffer)
    buffer.seek(0)

    filename = f"LEISA{date.today().strftime('%Y%m%d')}-{sdp_name}.xlsx"
    return filename, buffer