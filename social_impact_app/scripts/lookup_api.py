from social_impact.models import Complaint, Answers


def run():
    complaint = Complaint.objects.all()
