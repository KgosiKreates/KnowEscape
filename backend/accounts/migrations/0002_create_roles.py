from django.db import migrations


ROLES = [
    "Learner",
    "Facilitator",
    "Assessor",
    "Moderator",
    "SDP Administrator",
]


def create_roles(apps, schema_editor):
    Group = apps.get_model("auth", "Group")

    for role in ROLES:
        Group.objects.get_or_create(name=role)


def remove_roles(apps, schema_editor):
    Group = apps.get_model("auth", "Group")

    Group.objects.filter(name__in=ROLES).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_roles, remove_roles),
    ]