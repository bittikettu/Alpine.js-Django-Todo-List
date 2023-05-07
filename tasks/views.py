from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from django.shortcuts import get_object_or_404
from tasks.models import Task, Person, TasksDone
from http import HTTPStatus
from django.core.cache import cache
import logging
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import requires_csrf_token
from django.db.models import Sum

def user_balance(request):
    userq = Person.objects.get(username='admin')
    unpaid = Task.objects.filter(tasksdone__person=userq, tasksdone__paid=False, tasksdone__done=True).aggregate(Sum('price'))
    paid = Task.objects.filter(tasksdone__person=userq, tasksdone__paid=True, tasksdone__done=True).aggregate(Sum('price'))
    
    balance = [{"d":paid['price__sum']},{"d":unpaid['price__sum']},{"d":userq.username}]
    
    print(balance)
    return JsonResponse(status=HTTPStatus.OK, data=balance, safe=False)

def task_list(request):

    logging.debug(cache.get('tasks'))
    # print(cache.get('tasks'))
    # kakke = cache.get('tasks')
    # if(kakke == None):

    tasks = [{"id": task.id,
              "title": task.title,
              "added": task.added,
              "price": task.price,
              "completed": task.completed} for task in Task.objects.filter(deleted=False).exclude(tasksdone__done=True)]

    # cache.set('tasks', tasks, 30)

    # test = Task.objects.filter(deleted=False)
    # print(test)

    return JsonResponse(status=HTTPStatus.OK, data=tasks, safe=False)

# @csrf_exempt


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

# @csrf_exempt


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    # task.delete()
    task.deleted = True
    task.save()
    return JsonResponse(status=HTTPStatus.NO_CONTENT, data={'message': 'task deleted'})

# @csrf_exempt


def update_task_status(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    status = request.POST.get('status')
    user = request.POST.get('user')
    userq = Person.objects.get(username=user)

    try:
        obj = TasksDone.objects.get(person=userq, task=task)
        obj.done = int(status)
    except TasksDone.DoesNotExist:
        obj = TasksDone(person=userq, task=task)
        obj.done = int(status)

    obj.save()
    if not status:
        return JsonResponse(status=HTTPStatus.BAD_REQUEST, data={'error': 'status is required'})
    task.completed = int(status)
    task.save()
    # sum = TasksDone.objects.filter(person=userq,paid=False).aggregate(Sum('price'))
    test = Task.objects.filter(
        tasksdone__person=userq, tasksdone__paid=False, tasksdone__done=True).aggregate(Sum('price'))
    print(test)
    return JsonResponse(status=HTTPStatus.NO_CONTENT, data={'message': 'task status updated'})


def index(request):
    return render(request, 'index.html')
