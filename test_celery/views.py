from django.http import HttpResponse
from django.shortcuts import render

from .tasks import send_exam_invitation


# Create your views here.


def test(request):
    print("test --  send_exam_invitation")
    send_exam_invitation.delay()
    return HttpResponse("You're looking at question.")
