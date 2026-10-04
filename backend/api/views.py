from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from learners.services.leisa_export import LeisaExportError, generate_leisa_workbook

from .permissions import IsSDPAdministrator


class LeisaExportView(APIView):
    permission_classes = [IsSDPAdministrator]

    def post(self, request):
        try:
            filename, buffer = generate_leisa_workbook()
        except LeisaExportError as exc:
            return Response(
                {
                    "detail": "Some enrolments failed validation and were not exported.",
                    "errors": exc.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        response = HttpResponse(
            buffer.getvalue(),
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        response["Content-Disposition"] = f'attachment; filename="{filename}"'
        return response