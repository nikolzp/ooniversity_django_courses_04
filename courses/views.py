 # -*- coding: utf-8 -*-
from django.shortcuts import render
from courses.models import Course, Lesson

def detail(request, course_id):
	cours = Course.objects.get(id=course_id)
	les = Lesson.objects.filter(course_id = course_id)
	return render(request, 'courses/detail.html', {'cours':cours,'les':les})
