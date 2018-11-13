# Create your views here.
from django.shortcuts  import render_to_response, get_object_or_404
from chorechart.models import task, rule
from django.views.generic.list_detail import object_list 
def index(request):
	latest_task_list = task.objects.all().order_by('-date')[:5]
	return render_to_response('chorechart/index.html', {'latest_task_list': latest_task_list})
	