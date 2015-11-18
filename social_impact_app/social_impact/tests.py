from django.test import TestCase
from django.utils import timezone
from social_impact.models import Complaint, Answers

class ComplaintTestCase(TestCase):
    def setUp(self):
        c = Complaint.objects.create(complaint_text="I feel like I have fever today", pub_date=timezone.now())
        c.save()

        c.answers_set.create(choice_text='Go to ther nearest clinic to be diagnaised first', votes=8)
        c.answers_set.create(choice_text='Buy grandpa', votes=1)
        q = c.answers_set.create(choice_text='Go take a breake at a sonar', votes=0)

    def test_animals_can_speak(self):
        """Complaint with different answers"""
        complaint = Complaint.objects.get(pk=1)

        answers = complaint.answers_set.all()
        self.assertEqual(complaint.complaint_text, 'I feel like I have fever today')  # Testing for question being asked
        # self.assertEqual(answers, 'Answers: Go to ther nearest clinic to be diagnaised first, Answers: Buy grandpa, Answers: Go take a breake at a sonar')  # Testing for answers
        print answers
