from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from django.shortcuts import get_object_or_404
from tasks.models import Task
from http import HTTPStatus
from django.core.cache import cache
import logging

def task_list(request):
    
    logging.debug(cache.get('tasks'))
    #print(cache.get('tasks'))
    #kakke = cache.get('tasks')
    #if(kakke == None):
    tasks = [{"id": task.id,
            "title": task.title,
            "added": task.added,
            "price": task.price,
            "completed": task.completed} for task in Task.objects.filter(deleted=False)]
    cache.set('tasks', tasks, 30)
    #else:
    #    print("kakkesta")
    #    tasks = kakke
    return JsonResponse(status=HTTPStatus.OK, data=tasks, safe=False)

def create_task(request):
    title = request.POST.get('title')
    price = request.POST.get('price')
    logging.debug(title)
    if not title:
        return JsonResponse(status=HTTPStatus.BAD_REQUEST, data={'error': 'title is required'})
    task = Task.objects.create(title=title, price=price)
    return JsonResponse(status=HTTPStatus.CREATED, data={'title': task.title,
                                          'price': task.price,
                                          'completed': task.completed,
                                          'added': task.added,
                                          'id': task.id}, safe=False)

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    #task.delete()
    task.deleted = True
    task.save()
    return JsonResponse(status=HTTPStatus.NO_CONTENT, data={'message': 'task deleted'})

def update_task_status(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    status = request.POST.get('status')
    if not status:
        return JsonResponse(status=HTTPStatus.BAD_REQUEST, data={'error': 'status is required'})
    task.completed = int(status)
    task.save()
    return JsonResponse(status=HTTPStatus.NO_CONTENT, data={'message': 'task status updated'})

def index(request):
    return render(request, 'index.html')