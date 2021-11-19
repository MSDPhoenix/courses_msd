from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import *

def courses_page(request):
    context = {
        'courses':Course.objects.all()
    }
    return render(request,'courses_page.html',context)

def add_course(request):
    # errors = {}
    errors = Course.objects.validator(request.POST)
    # errors2 = Description.objects.description_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        course_name = request.POST['name']
        description = request.POST['description']
        course=Course.objects.create(course_name=course_name)
        Description.objects.create(course=course,body=description)
    return redirect('/')

def comments_page(request,course_id):
    course = Course.objects.get(id=course_id)
    context = {
        'course_id' : course_id,
        'name' : course.course_name,
        'description' : course.description.body,
        'comments' : course.comments.all()
    }
    return render(request,'comments_page.html',context)

def post_comment(request,course_id):
    course=Course.objects.get(id=course_id)
    Comment.objects.create(comment=request.POST['comment'],course=course)
    return redirect('/courses/comments/'+str(course_id))

def delete_comment(request,course_id,comment_id):
    comment=Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('/courses/comments/'+str(course_id))

def delete_page(request,course_id):
    course=Course.objects.get(id=course_id)
    context = {
        'name':course.course_name,
        'description':course.description.body,
        'course_id':course.id
    }
    return render(request,'delete_page.html',context)

def remove_course_from_database(request,course_id):
    course=Course.objects.get(id=course_id)
    course.delete()
    return redirect('/')