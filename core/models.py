from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
import random

# The user model exists in all django projects. It contains the following attributes:
# Username, email, first name, last name, and staff status. These attributes are the only attributes that
# can exist in the user model.

current_user = get_user_model()


def generate_ticket_number():
    number = random.randint(1000, 9999)
    return int(f"{timezone.now().strftime('%y%m%d')}{number}")


# Note: Django automatically creates an id for every model

class Project(models.Model):
    name = models.CharField(max_length=100)  # <- This doesn't exist in our original ER model
    description = models.TextField(max_length=1000, null=True)
    status = models.CharField(max_length=50, null=True)
    start_date = models.DateField()

    def __str__(self):
        return self.name


# When creating an admin model, we must set staff status to true in the current user model
class Admin(models.Model):
    user = models.ForeignKey(current_user, on_delete=models.CASCADE)
    no_projects = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Team(models.Model):
    team_number = models.AutoField(primary_key=True)
    number_of_people = models.IntegerField(default=0)


class Collaborator(models.Model):
    user = models.ForeignKey(current_user, on_delete=models.CASCADE)
    team_number = models.ForeignKey(Team, to_field='team_number', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username


class Ticket(models.Model):
    ticket_number = models.IntegerField(default=generate_ticket_number, primary_key=True, editable=False)
    author = models.CharField(max_length=100, null=True)
    date = models.DateField(null=True)
    status = models.CharField(max_length=50, null=True)
    priority = models.CharField(max_length=50, null=True)
    project_id = models.ForeignKey(Project, to_field='id', on_delete=models.CASCADE)
    admin_id = models.ForeignKey(Admin, to_field='id', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ticket_number)


class Bug(models.Model):
    date = models.DateField(null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=1000, null=True)
    project_id = models.ForeignKey(Project, to_field='id', on_delete=models.CASCADE)
    user = models.ForeignKey(current_user, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class FeatureRequest(models.Model):
    date = models.DateField(null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=1000, null=True)
    project_id = models.ForeignKey(Project, to_field='id', on_delete=models.CASCADE)
    user = models.ForeignKey(current_user, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class FeatureTicket(models.Model):
    feature_id = models.ForeignKey(FeatureRequest, to_field='id', on_delete=models.CASCADE)
    ticket_number = models.OneToOneField(Ticket, to_field='ticket_number', on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.feature_id)


class BugTicket(models.Model):
    bug_id = models.ForeignKey(Bug, to_field='id', on_delete=models.CASCADE)
    ticket_number = models.OneToOneField(Ticket, to_field='ticket_number', on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.bug_id)


class ProgressReport(models.Model):
    ticket_number = models.OneToOneField(Ticket, to_field='ticket_number', on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.ticket_number)


class ProgressContent(models.Model):
    ticket_number = models.ForeignKey(ProgressReport, to_field='ticket_number', on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField(max_length=1000)

    class Meta:
        unique_together = (("ticket_number", "date", "description"),)


class WorksOn(models.Model):
    team_number = models.ForeignKey(Team, to_field='team_number', on_delete=models.CASCADE)
    ticket_number = models.ForeignKey(ProgressReport, to_field='ticket_number', on_delete=models.CASCADE)

    class Meta:
        unique_together = (("team_number", "ticket_number"),)


class Complete(models.Model):
    collaborator_id = models.ForeignKey(Collaborator, to_field='id', on_delete=models.CASCADE)
    ticket_number = models.ForeignKey(ProgressReport, to_field='ticket_number', on_delete=models.CASCADE)

    class Meta:
        unique_together = (("collaborator_id", "ticket_number"),)


class Assign (models.Model):
    team_number = models.ForeignKey(Team, to_field='team_number', on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, to_field='id', on_delete=models.CASCADE)
    admin_id = models.ForeignKey(Admin, to_field='id', on_delete=models.CASCADE)

    class Meta:
        unique_together = (("team_number", "admin_id", "project_id"),)
