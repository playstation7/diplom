import datetime

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

import diploms
from diploms.models import Message, Comment, Vacansia, City, Interview, News
from diploms.forms import CommentForm, InterviewForm, MessageForm  # , VacansiaForm
from django.contrib import messages as mes


# Create your views here.
def index(request):
    news = News.objects.order_by("date_published")[:3]
    context = {'news': news}
    return render(request, 'diploms/index.html', context)


def about(request):
    comments = Comment.objects.order_by('-date_added')
    for comment in comments:
        if compare_owner_user(comment.owner, request.user):
            comment.is_editing = True
        else:
            comment.is_editing = False
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.owner = request.user
            new_comment.save()
            return redirect('about')

    context = {
        'form': form,
        'comments': comments,
    }
    return render(request, 'diploms/about.html', context)


def partner(request):
    return render(request, 'diploms/partner.html')


def connect(request):
    return render(request, 'diploms/connect.html')

@login_required
def messages(request):
    messages = Message.objects.filter(owner=request.user)
    context = {'messages': messages}
    return render(request, 'diploms/messages.html', context)


def compare_owner_user(owner, user):
    if owner == user:
        return True
    else:
        return False

@login_required
def delete(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if not compare_owner_user(comment.owner, request.user):
        raise Http404
    comment.delete()
    mes.success(request, 'Ваш комментарий был успешно удален!')
    return redirect('about')

@login_required
def edit(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if not compare_owner_user(comment.owner, request.user):
        raise Http404
    if request.method != 'POST':
        form = CommentForm(instance=comment)
    else:
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            mes.success(request, 'Комментарий успешно изменен.')
            return redirect('about')
    context = {
        'comment': comment,
        'form': form,
    }
    return render(request, 'diploms/edit.html', context)


def vacansies(request):
    if request.POST.get('city') and request.POST.get('city') != 'Любой':
        city_name = request.POST.get('city')
        try:
            picked_city = City.objects.get(city=city_name)
            vacs = Vacansia.objects.filter(is_active=True, city=picked_city)
        except diploms.models.City.DoesNotExist:
            vacs = None

    else:
        vacs = Vacansia.objects.filter(is_active=True)

    cities = City.objects.all()
    context = {
        'vacs': vacs,
        'cities': cities,

    }
    return render(request, 'diploms/vacansies.html', context)


@login_required
def vacansia(request, vacansia_id):
    vacansia_h = Vacansia.objects.get(id=vacansia_id)
    form = InterviewForm()

    available_times = [datetime.time(i, 0, 0).isoformat(timespec='minutes') for i in range(9, 16)]
    context = {
        'today': str(datetime.datetime.date(datetime.datetime.today() + datetime.timedelta(1))),
        'max_date': str(datetime.datetime.date(datetime.datetime.today() + datetime.timedelta(8))),
        'available_times': available_times,
        'vacansia': vacansia_h,
        'form': form,
    }
    if request.method == 'POST':
        if Interview.objects.filter(date=request.POST.get('date'), time=request.POST.get('time')):
            mes.error(request, 'Выбранное время уже занято!Выберите другое время!')
            return render(request, 'diploms/vacansia.html', context)
        else:
            form = InterviewForm(data=request.POST)
            if form.is_valid():
                new_сandidate = form.save(commit=False)
                new_сandidate.сandidate = request.user
                new_сandidate.save()
                mes.success(request, 'Запись на собеседование прошла успешно.Ожидайте звонка.')
                return render(request, 'diploms/vacansia.html', context)
    return render(request, 'diploms/vacansia.html', context)


def news(request):
    newsSet = News.objects.order_by("date_published")
    context = {'news': newsSet}
    return render(request, 'diploms/news.html', context)


def new(request, new_id):
    new = News.objects.get(id=new_id)
    context = {'new': new}
    return render(request, 'diploms/new.html', context)

@login_required
def support(request):
    if request.method != 'POST':
        form = MessageForm()
    else:
        form = MessageForm(request.POST,request.FILES)
        if form.is_valid():
            new_mes = form.save(commit=False)
            new_mes.owner = request.user

            new_mes.save()
            mes.success(request,'Ваше обращение успешно отправлено')
            return redirect('support')
    context = {
        'form': form
    }
    return render(request, 'diploms/support.html', context)
