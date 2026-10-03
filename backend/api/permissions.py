from rest_framework.permissions import BasePermission

SDP_ADMINISTRATOR = "SDP Administrator"


class HasRole(BasePermission):
    """
    Base class for role-based permissions, backed by Django Groups.

    SDP Administrator always passes any role check — by design, it's a
    superset of every other role (can do everything a Learner,
    Facilitator, Assessor, or Moderator can, plus admin-only actions).
    Subclasses only need to set `group_name`.
    """

    group_name = None
    message = "You do not have the required role for this action."

    def has_permission(self, request, view):
        user = request.user
        if not (user and user.is_authenticated):
            return False
        if user.groups.filter(name=SDP_ADMINISTRATOR).exists():
            return True
        return user.groups.filter(name=self.group_name).exists()


class IsLearner(HasRole):
    group_name = "Learner"


class IsFacilitator(HasRole):
    group_name = "Facilitator"


class IsAssessor(HasRole):
    group_name = "Assessor"


class IsModerator(HasRole):
    group_name = "Moderator"


class IsSDPAdministrator(BasePermission):
    """
    Strict admin-only check — no fallback. Use this (not HasRole) for
    actions that are genuinely admin-exclusive: managing Qualification
    or Accreditation records, triggering QCTO exports, creating
    Facilitator/Assessor/Moderator accounts.
    """

    message = "Only SDP Administrators can perform this action."

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(name=SDP_ADMINISTRATOR).exists()
        )