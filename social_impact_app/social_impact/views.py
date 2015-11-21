from django.shortcuts import get_object_or_404, render
from .models import Complaint


def index(request):
    latest_complaint_list = Complaint.objects.order_by('-pub_date')[:5]
    context = {'latest_complaint_list': latest_complaint_list, }
    return render(request, 'user/complaint.html', context)


def answer(request, complaint_id):
    complaint = get_object_or_404(Complaint, pk=complaint_id)
    return render(request, 'user/answers.html', {'complaint': complaint})
# def detail(request, complaint_id):
#     return HttpResponse("You're looking at question %s." % complaint_id)


# def results(request, complaint_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % complaint_id)


# def vote(request, complaint_id):
#     return HttpResponse("You're voting on question %s." % complaint_id)
