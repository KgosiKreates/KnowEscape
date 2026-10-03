from django.conf import settings
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class LearnerProfile(models.Model):
    """
    Learner-level demographic, identity, and contact data.

    This model intentionally excludes anything specific to a single
    qualification/enrolment (SOR status, EISA readiness, FLC, etc.) —
    those live on Enrolment, since a learner may be enrolled in more
    than one qualification over time and each enrolment has its own
    QCTO submission state.

    Field names and allowed codes are sourced from the QCTO
    "Data Load Specifications for SDPs and ACs" (Learner Enrolment and
    Readiness for EISA file), effective 1 June 2022:
    https://www.qcto.org.za/assets/data-loading-specification-document.pdf
    """

    class AlternativeIdType(models.TextChoices):
        PASSPORT = "527", "Passport / Foreign ID"
        NONE = "533", "None"
        REFUGEE = "565", "Refugee"
        WORK_PERMIT = "538", "Work Permit"
        BIRTH_CERTIFICATE = "540", "Birth Certificate"
        ALTERNATE_TO_NATIONAL = "570", "Alternate ID → National ID"

    class EquityCode(models.TextChoices):
        BLACK_AFRICAN = "BA", "Black African"
        COLOURED = "BC", "Coloured"
        INDIAN_ASIAN = "BI", "Indian/Asian"
        OTHER = "Oth", "Other"
        UNKNOWN = "U", "Unknown"
        WHITE = "Wh", "White"

    class NationalityCode(models.TextChoices):
        UNSPECIFIED = "U", "Unspecified"
        SOUTH_AFRICA = "SA", "South Africa"
        SADC_EXCEPT_SA = "SDC", "SADC except SA"
        NAMIBIA = "NAM", "Namibia"
        BOTSWANA = "BOT", "Botswana"
        ZIMBABWE = "ZIM", "Zimbabwe"
        ANGOLA = "ANG", "Angola"
        MOZAMBIQUE = "MOZ", "Mozambique"
        LESOTHO = "LES", "Lesotho"
        SWAZILAND = "SWA", "Swaziland"
        MALAWI = "MAL", "Malawi"
        ZAMBIA = "ZAM", "Zambia"
        MAURITIUS = "MAU", "Mauritius"
        TANZANIA = "TAN", "Tanzania"
        SEYCHELLES = "SEY", "Seychelles"
        ZAIRE = "ZAI", "Zaire"
        REST_OF_AFRICA = "ROA", "Rest of Africa"
        EUROPE = "EUR", "European countries"
        ASIA = "AIS", "Asian countries"
        NORTH_AMERICA = "NOR", "North American countries"
        CENTRAL_SOUTH_AMERICA = "SOU", "Central and South American countries"
        AUSTRALIA_OCEANIA = "AUS", "Australia Oceania countries"
        OTHER_OCEANIA = "OOC", "Other and rest of Oceania"
        NOT_APPLICABLE = "NOT", "N/A: Institution"

    class HomeLanguageCode(models.TextChoices):
        ENGLISH = "Eng", "English"
        AFRIKAANS = "Afr", "Afrikaans"
        OTHER = "Oth", "Other"
        SASL = "SASL", "South African Sign Language"
        SEPEDI = "Sep", "sePedi"
        SESOTHO = "Ses", "seSotho"
        SETSWANA = "Set", "seTswana"
        SISWATI = "Swa", "siSwati"
        TSHIVENDA = "Tsh", "tshiVenda"
        ISIXHOSA = "Xho", "isiXhosa"
        XITSONGA = "Xit", "xiTsonga"
        ISIZULU = "Zul", "isiZulu"
        ISINDEBELE = "Nde", "isiNdebele"

    class Gender(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"

    class CitizenResidentStatus(models.TextChoices):
        SOUTH_AFRICA = "SA", "South Africa"
        OTHER = "O", "Other"
        DUAL = "D", "Dual (SA plus other)"
        PERMANENT_RESIDENT = "PR", "Permanent Resident"
        UNKNOWN = "U", "Unknown"

    class SocioeconomicStatusCode(models.TextChoices):
        EMPLOYED = "01", "Employed"
        UNEMPLOYED_LOOKING = "02", "Unemployed, looking for work"
        NOT_WORKING_NOT_LOOKING = "03", "Not working – not looking for work"
        HOMEMAKER = "04", "Home-maker (not working)"
        SCHOLAR_STUDENT = "06", "Scholar/student (not working)"
        PENSIONER = "07", "Pensioner/retired (not working)"
        DISABLED_NOT_WORKING = "08", "Not working – disabled person"
        NOT_WORKING_NOT_WISHING = "09", "Not working – not wishing to work"
        NOT_WORKING_NEC = "10", "Not working – Not elsewhere classified"
        NA_AGED_UNDER_15 = "97", "N/A: Aged <15"
        NA_INSTITUTION = "98", "N/A: Institution"
        UNSPECIFIED = "U", "Unspecified"

    class DisabilityStatusCode(models.TextChoices):
        NONE = "N", "None"
        SIGHT = "01", "Sight (even with glasses)"
        HEARING = "02", "Hearing (even with a hearing aid)"
        COMMUNICATION = "03", "Communication (talking, listening)"
        PHYSICAL = "04", "Physical (moving, standing, grasping)"
        INTELLECTUAL = "05", "Intellectual (difficulties in learning); retardation"
        EMOTIONAL = "06", "Emotional (behavioural or psychological)"
        MULTIPLE = "07", "Multiple"
        UNSPECIFIED = "09", "Disabled but Unspecified"

    class DisabilityRating(models.TextChoices):
        NO_DIFFICULTY = "01", "No difficulty"
        SOME_DIFFICULTY = "02", "Some difficulty"
        A_LOT_OF_DIFFICULTY = "03", "A lot of difficulty"
        CANNOT_DO_AT_ALL = "04", "Cannot do at all"
        CANNOT_YET_BE_DETERMINED = "06", "Cannot yet be determined"
        MAY_BE_MULTIPLE = "60", "May be part of multiple difficulties (TBC)"
        MAY_HAVE_DIFFICULTY = "70", "May have difficulty (TBC)"
        FORMER_DIFFICULTY_NONE_NOW = "80", "Former difficulty - none now"

    class ImmigrantStatus(models.TextChoices):
        IMMIGRANT = "01", "Immigrant"
        REFUGEE = "02", "Refugee"
        SA_CITIZEN = "03", "SA Citizen"

    class Title(models.TextChoices):
        MR = "Mr", "Mr"
        MRS = "Mrs", "Mrs"
        MS = "Ms", "Ms"
        MISS = "Miss", "Miss"
        DR = "Dr", "Dr"
        PROF = "Prof", "Prof"

    class ProvinceCode(models.TextChoices):
        WESTERN_CAPE = "1", "Western Cape"
        EASTERN_CAPE = "2", "Eastern Cape"
        NORTHERN_CAPE = "3", "Northern Cape"
        FREE_STATE = "4", "Free State"
        KWAZULU_NATAL = "5", "Kwazulu Natal"
        NORTH_WEST = "6", "North West"
        GAUTENG = "7", "Gauteng"
        MPUMALANGA = "8", "Mpumalanga"
        LIMPOPO = "9", "Limpopo"
        SA_NATIONAL_UNSPECIFIED = "N", "SA National (province unspecified)"
        OUTSIDE_SA = "X", "Outside SA"

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
        choices=EquityCode.choices,
    )

    nationality_code = models.CharField(
        max_length=10,
        choices=NationalityCode.choices,
    )

    home_language_code = models.CharField(
        max_length=10,
        choices=HomeLanguageCode.choices,
    )

    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
    )

    citizen_resident_status = models.CharField(
        max_length=3,
        choices=CitizenResidentStatus.choices,
    )

    socioeconomic_status_code = models.CharField(
        max_length=2,
        choices=SocioeconomicStatusCode.choices,
    )

    disability_status_code = models.CharField(
        max_length=2,
        choices=DisabilityStatusCode.choices,
    )

    disability_rating = models.CharField(
        max_length=2,
        choices=DisabilityRating.choices,
        blank=True,
    )

    immigrant_status = models.CharField(
        max_length=2,
        choices=ImmigrantStatus.choices,
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
        choices=Title.choices,
    )

    birth_date = models.DateField()

    # Home address
    home_address_1 = models.CharField(max_length=255)
    home_address_2 = models.CharField(max_length=255)
    home_address_3 = models.CharField(
        max_length=255,
        blank=True,
    )

    # Postal address
    postal_address_1 = models.CharField(max_length=255)
    postal_address_2 = models.CharField(max_length=255)
    postal_address_3 = models.CharField(
        max_length=255,
        blank=True,
    )

    home_postal_code = models.CharField(
        max_length=4,
        validators=[
            RegexValidator(
                regex=r"^\d{4}$",
                message="Postal code must contain exactly 4 digits.",
            )
        ],
    )

    postal_postal_code = models.CharField(
        max_length=4,
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

    # Not QCTO-required (spec marks it optional), but required here for
    # portal login/notifications — an intentional product requirement,
    # not a QCTO compliance field.
    email = models.EmailField()

    # Geographic
    province_code = models.CharField(
        max_length=1,
        choices=ProvinceCode.choices,
    )

    # NOTE: the full STATS SA area code list is a separate official
    # reference dataset not included in the LEISA field spec itself.
    # Left as free text pending that list; must still be non-blank.
    statssa_area_code = models.CharField(max_length=20)

    # POPIA
    popi_act_agree = models.CharField(
        max_length=3,
        choices=PopiConsent.choices,
    )

    popi_act_date = models.DateField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        errors = {}

        if not self.national_id and not self.learner_alternate_id:
            errors["national_id"] = (
                "Either National ID or Learner Alternate ID must be provided."
            )

        if self.alternative_id_type == self.AlternativeIdType.NONE:
            if self.learner_alternate_id:
                errors["learner_alternate_id"] = (
                    "Alternate ID must be blank when Alternative ID Type is None."
                )

        if self.national_id and not self.learner_alternate_id:
            if self.alternative_id_type != self.AlternativeIdType.NONE:
                errors["alternative_id_type"] = (
                    "Must be 533 (None) when National ID is supplied and "
                    "Learner Alternate ID is blank."
                )

        if self.popi_act_agree == self.PopiConsent.YES and not self.popi_act_date:
            errors["popi_act_date"] = (
                "POPI Act Date is required when POPI Act Agree is Yes."
            )

        if self.popi_act_agree == self.PopiConsent.NO and self.popi_act_date:
            errors["popi_act_date"] = (
                "POPI Act Date must be blank when POPI Act Agree is No."
            )

        if self.disability_status_code and self.disability_status_code != self.DisabilityStatusCode.NONE:
            if not self.disability_rating:
                errors["disability_rating"] = (
                    "Disability Rating is required when disability status indicates a disability."
                )

        if errors:
            raise ValidationError(errors)


class Qualification(models.Model):
    """
    A QCTO-registered Occupational Qualification.

    qualification_id must match the actual Qualification ID format for
    which the SDP/Assessment Centre is accredited on the QCTO MIS
    system, and be an active, registered qualification on the OQSF of
    the NQF (LEISA spec, Column B).
    """

    qualification_id = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=255)
    nqf_level = models.PositiveSmallIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.qualification_id} — {self.title}"


class Accreditation(models.Model):
    """
    A Skills Development Provider's overall QCTO accreditation.

    The LEISA spec states: "the Date of capturing or achievement or
    reporting will only be valid if it is within the Accreditation
    Period." This is the overall SDP-level period; the specific
    qualifications the SDP may enrol learners against — each with
    its own accreditation window — are tracked separately on
    QualificationAccreditation.
    """

    sdp_code = models.CharField(
        max_length=50,
        unique=True,
        help_text="Unique code provided to the SDP by a QCTO official.",
    )
    accreditation_number = models.CharField(
        max_length=50,
        blank=True,
        help_text="Used in place of an SDP code only when no code has been issued.",
    )
    accreditation_start_date = models.DateField()
    accreditation_end_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sdp_code

    def clean(self):
        if self.accreditation_end_date <= self.accreditation_start_date:
            raise ValidationError(
                {"accreditation_end_date": "Must be after the accreditation start date."}
            )


class QualificationAccreditation(models.Model):
    """
    A specific qualification an Accreditation (SDP) is accredited to
    deliver, with its own accreditation start/end date — QCTO
    accredits providers qualification-by-qualification, not as a
    single blanket approval.
    """

    provider = models.ForeignKey(
        Accreditation,
        on_delete=models.PROTECT,
        related_name="qualification_accreditations",
    )
    qualification = models.ForeignKey(
        Qualification,
        on_delete=models.PROTECT,
        related_name="accreditations",
    )
    accreditation_start_date = models.DateField()
    accreditation_end_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["provider", "qualification"],
                name="unique_provider_qualification_accreditation",
            )
        ]

    def __str__(self):
        return f"{self.provider.sdp_code} — {self.qualification.qualification_id}"

    def clean(self):
        if self.accreditation_end_date <= self.accreditation_start_date:
            raise ValidationError(
                {"accreditation_end_date": "Must be after the accreditation start date."}
            )


class Enrolment(models.Model):
    """
    A learner's enrolment against a single qualification.

    Carries every field from the LEISA spec that is scoped to a
    specific (learner × qualification) submission row, rather than to
    the learner as a person.
    """

    class StatementOfResultsStatus(models.TextChoices):
        ISSUED = "01", "Statement of Results issued"
        NOT_YET_ISSUED = "02", "Statement of Results not yet issued"

    class ReadinessForEisaType(models.TextChoices):
        ENROLLED = "1", "Enrolled"
        RPL_ACCESS_BY_SDP = "2", "RPL for Access to EISA determined by SDP"
        MIXED_MODE = "3", "Mixed Mode to EISA"
        SDP_TRAINING_ASSESSMENT = "4", "SDP Training and assessment for readiness to EISA"
        SDP_ELEARNING = "5", "SDP e-learning training and assessment for readiness to EISA"
        RPL_ACCESS_BY_ASSESSMENT_PARTNER = "6", "RPL for Access to EISA determined by Assessment Partner/Quality Partner"

    class FLCStatus(models.TextChoices):
        FLC_CERTIFICATE = "01", "FLC certificate (competent)"
        RPL = "02", "RPL"
        GRADE_12_EQUIVALENT = "03", "Grade 12/NCV Level 4 Maths/English pass"
        NOT_YET_COMPETENT = "04", "Not yet competent"
        FLC_NOT_COMPLETED = "05", "FLC not completed yet"
        NOT_APPLICABLE = "06", "Not applicable (qualification on NQF 5 and above)"
        ENROLLED_FOR_FLC = "07", "Enrolled for FLC"
        N3_MATHS_BUSINESS_LANGUAGE = "08", "N3 Mathematics and Business Language"

    learner = models.ForeignKey(
        LearnerProfile,
        on_delete=models.PROTECT,
        related_name="enrolments",
    )

    qualification = models.ForeignKey(
        Qualification,
        on_delete=models.PROTECT,
        related_name="enrolments",
    )

    # Links to the SDP's accreditation record rather than storing the
    # SDP code as a bare string, so it can't drift out of sync and so
    # the accreditation-period check below has something to check
    # against.
    accreditation = models.ForeignKey(
        Accreditation,
        on_delete=models.PROTECT,
        related_name="enrolments",
    )

    expected_training_completion_date = models.DateField()

    statement_of_results_status = models.CharField(
        max_length=2,
        choices=StatementOfResultsStatus.choices,
    )

    statement_of_results_date = models.DateField(
        null=True,
        blank=True,
    )

    # Conditional per spec — required only once the learner is
    # referred for EISA at a specific centre.
    assessment_centre_code = models.CharField(
        max_length=50,
        blank=True,
    )

    learner_readiness_for_eisa_type = models.CharField(
        max_length=1,
        choices=ReadinessForEisaType.choices,
    )

    flc_status = models.CharField(
        max_length=2,
        choices=FLCStatus.choices,
    )

    flc_certificate_number = models.CharField(max_length=100)

    # Date this record was last updated, as submitted to QCTO.
    # Auto-populated so it's always present, satisfying the spec's
    # "Yes – QCTO" requirement without needing manual upkeep.
    date_stamp = models.DateField(auto_now=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["learner", "qualification"],
                name="unique_learner_qualification_enrolment",
            )
        ]

    def __str__(self):
        return f"{self.learner} — {self.qualification.qualification_id}"

    @property
    def sdp_code(self):
        """Convenience accessor — the SDP code lives on Accreditation, not duplicated here."""
        return self.accreditation.sdp_code

    def clean(self):
        errors = {}

        if self.statement_of_results_status == self.StatementOfResultsStatus.ISSUED:
            if not self.statement_of_results_date:
                errors["statement_of_results_date"] = (
                    "Statement of Results Date is required when status is 01 (issued)."
                )
        elif self.statement_of_results_status == self.StatementOfResultsStatus.NOT_YET_ISSUED:
            if self.statement_of_results_date:
                errors["statement_of_results_date"] = (
                    "Statement of Results Date must be blank when status is 02 (not yet issued)."
                )

        if self.learner_readiness_for_eisa_type == self.ReadinessForEisaType.ENROLLED:
            if self.statement_of_results_status != self.StatementOfResultsStatus.NOT_YET_ISSUED:
                errors["statement_of_results_status"] = (
                    "Must be 02 (not yet issued) while EISA readiness type is 1 (Enrolled)."
                )
        elif self.learner_readiness_for_eisa_type:
            if self.statement_of_results_status != self.StatementOfResultsStatus.ISSUED:
                errors["statement_of_results_status"] = (
                    "Must be 01 (issued) once EISA readiness type is anything other than 1 (Enrolled)."
                )

        # LEISA spec: "the Date of capturing or achievement or reporting
        # will only be valid if it is within the Accreditation Period."
        if self.accreditation_id and self.qualification_id:
            try:
                qual_accreditation = QualificationAccreditation.objects.get(
                    provider=self.accreditation, qualification=self.qualification
                )
            except QualificationAccreditation.DoesNotExist:
                errors["qualification"] = (
                    "This provider has no QualificationAccreditation record for this "
                    "qualification — QCTO will reject any submission for it."
                )
            else:
                today = timezone.now().date()
                if not (qual_accreditation.accreditation_start_date <= today <= qual_accreditation.accreditation_end_date):
                    errors["qualification"] = (
                        "Today's date falls outside this qualification's accreditation "
                        "period — the submission would be invalid per QCTO's Accreditation "
                        "Period rule."
                    )
                if (
                    self.expected_training_completion_date
                    and self.expected_training_completion_date > qual_accreditation.accreditation_end_date
                ):
                    errors["expected_training_completion_date"] = (
                        "Falls after this qualification's accreditation end date."
                    )

        if errors:
            raise ValidationError(errors)