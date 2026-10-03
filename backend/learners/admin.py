from django.contrib import admin

from .models import (
    Accreditation,
    Enrolment,
    LearnerProfile,
    Qualification,
    QualificationAccreditation,
)


@admin.register(LearnerProfile)
class LearnerProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "national_id", "email", "created_at")
    search_fields = ("first_name", "last_name", "national_id", "email")


@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ("qualification_id", "title", "nqf_level")
    search_fields = ("qualification_id", "title")


@admin.register(Accreditation)
class AccreditationAdmin(admin.ModelAdmin):
    list_display = ("sdp_code", "accreditation_start_date", "accreditation_end_date")
    search_fields = ("sdp_code", "accreditation_number")


@admin.register(QualificationAccreditation)
class QualificationAccreditationAdmin(admin.ModelAdmin):
    list_display = ("provider", "qualification", "accreditation_start_date", "accreditation_end_date")
    list_filter = ("qualification",)


@admin.register(Enrolment)
class EnrolmentAdmin(admin.ModelAdmin):
    list_display = (
        "learner",
        "qualification",
        "statement_of_results_status",
        "learner_readiness_for_eisa_type",
        "date_stamp",
    )
    list_filter = ("statement_of_results_status", "learner_readiness_for_eisa_type")
    search_fields = ("learner__first_name", "learner__last_name", "qualification__qualification_id")