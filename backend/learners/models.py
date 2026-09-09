from django.db import models

# Create your models here.
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.db import models


class LearnerProfile(models.Model):

    class AlternativeIdType(models.TextChoices):
        PASSPORT = "527", "Passport / Foreign ID"
        NONE = "533", "None"
        REFUGEE = "565", "Refugee"
        WORK_PERMIT = "538", "Work Permit"
        BIRTH_CERTIFICATE = "540", "Birth Certificate"
        ALTERNATE_TO_NATIONAL = "570", "Alternate ID → National ID"

    class Gender(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"

    class PopiConsent(models.TextChoices):
        YES = "Yes", "Yes"
        NO = "No", "No"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="learner_profile",
    )

    # QCTO identification
    national_id = models.CharField(
        max_length=13,
        blank=True,
        validators=[
            RegexValidator(
                regex=r"^\d{13}$",
                message="National ID must contain exactly 13 digits.",
            )
        ],
    )

    learner_alternate_id = models.CharField(
        max_length=100,
        blank=True,
    )

    alternative_id_type = models.CharField(
        max_length=3,
        choices=AlternativeIdType.choices,
        blank=True,
    )

    # Demographics
    equity_code = models.CharField(
        max_length=3,
        blank=True,
    )

    nationality_code = models.CharField(
        max_length=10,
        blank=True,
    )

    home_language_code = models.CharField(
        max_length=10,
        blank=True,
    )

    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        blank=True,
    )

    citizen_resident_status = models.CharField(
        max_length=3,
        blank=True,
    )

    socioeconomic_status_code = models.CharField(
        max_length=3,
        blank=True,
    )

    disability_status_code = models.CharField(
        max_length=3,
        blank=True,
    )

    disability_rating = models.CharField(
        max_length=2,
        blank=True,
    )

    immigrant_status = models.CharField(
        max_length=2,
        blank=True,
    )

    # Learner identity
    last_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(
        max_length=150,
        blank=True,
    )
    title = models.CharField(
        max_length=20,
        blank=True,
    )

    birth_date = models.DateField()

    # Home address
    home_address_1 = models.CharField(max_length=255)
    home_address_2 = models.CharField(
        max_length=255,
        blank=True,
    )
    home_address_3 = models.CharField(
        max_length=255,
        blank=True,
    )

    # Postal address
    postal_address_1 = models.CharField(max_length=255)
    postal_address_2 = models.CharField(
        max_length=255,
        blank=True,
    )
    postal_address_3 = models.CharField(
        max_length=255,
        blank=True,
    )

    home_postal_code = models.CharField(
        max_length=4,
        blank=True,
        validators=[
            RegexValidator(
                regex=r"^\d{4}$",
                message="Postal code must contain exactly 4 digits.",
            )
        ],
    )

    postal_postal_code = models.CharField(
        max_length=4,
        blank=True,
        validators=[
            RegexValidator(
                regex=r"^\d{4}$",
                message="Postal code must contain exactly 4 digits.",
            )
        ],
    )

    # Contact
    phone = models.CharField(
        max_length=30,
        blank=True,
    )

    cell = models.CharField(
        max_length=30,
        blank=True,
    )

    fax = models.CharField(
        max_length=30,
        blank=True,
    )

    email = models.EmailField()

    # Geographic
    province_code = models.CharField(
        max_length=1,
        blank=True,
    )

    statssa_area_code = models.CharField(
        max_length=20,
        blank=True,
    )

    # POPIA
    popi_act_agree = models.CharField(
        max_length=3,
        choices=PopiConsent.choices,
    )

    popi_act_date = models.DateField(
        null=True,
        blank=True,
    )

    # Training / QCTO
    expected_training_completion_date = models.DateField(
        null=True,
        blank=True,
    )

    statement_of_results_status = models.CharField(
        max_length=2,
        blank=True,
    )

    statement_of_results_date = models.DateField(
        null=True,
        blank=True,
    )

    assessment_centre_code = models.CharField(
        max_length=50,
        blank=True,
    )

    learner_readiness_for_eisa_type = models.CharField(
        max_length=1,
        blank=True,
    )

    flc_status = models.CharField(
        max_length=20,
        blank=True,
    )

    flc_certificate_number = models.CharField(
        max_length=100,
        blank=True,
    )

    date_stamp = models.DateField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        errors = {}

        if self.alternative_id_type == self.AlternativeIdType.NONE:
            if self.learner_alternate_id:
                errors["learner_alternate_id"] = (
                    "Alternate ID must be blank when Alternative ID Type is None."
                )

        if self.popi_act_agree == self.PopiConsent.YES and not self.popi_act_date:
            errors["popi_act_date"] = (
                "POPI Act Date is required when POPI Act Agree is Yes."
            )

        if self.popi_act_agree == self.PopiConsent.NO and self.popi_act_date:
            errors["popi_act_date"] = (
                "POPI Act Date must be blank when POPI Act Agree is No."
            )

        if self.statement_of_results_status == "01":
            if not self.statement_of_results_date:
                errors["statement_of_results_date"] = (
                    "Statement of Results Date is required when status is 01."
                )

        if self.disability_status_code and self.disability_status_code != "N":
            if not self.disability_rating:
                errors["disability_rating"] = (
                    "Disability Rating is required when disability status indicates a disability."
                )

        if errors:
            raise ValidationError(errors)