# Create your views here.
from django.shortcuts import render_to_response

from comments.models import Comment

def index(request):
    return render_to_response('comments.html', {'comments': Comment.objects.filter(parent=None)})
