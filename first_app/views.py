from django.shortcuts import render
from django.http import HttpResponse,Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

course_dictionary = {
    "python" : "Python course page",
    "kotlin" : "Kotlin course page",
    "swift" : "Swift course page",
    "java" : "Java course page",
}

def index(request):
    return HttpResponse("This is first Django projecty, first index")

def about(request):
    return HttpResponse("This is first Django projecty, about")


def course(request, item):
    try:
        course = course_dictionary[item]
        return HttpResponse(course)
    except:
        return HttpResponseNotFound("404 PAGE NOT FOUND!")
        #raise Http404("Nout found!")
    #return HttpResponse(course_dictionary.get(item,"404 Not found!"))


def multiply_view(request, num1, num2):
    return HttpResponse(f"{num1} * {num2} = {num1 * num2}")


def course_number(request, num1):
    course_list = list(course_dictionary.keys())
    try:
        course = course_list[num1]
        page_to_go = reverse("course",args=[course])
        return HttpResponseRedirect(page_to_go)
    except:
        return HttpResponseNotFound("404 PAGE NOT FOUND!")
    #if num1 == 10:
        #return HttpResponseRedirect("/first_app/kotlin")
    #else:
      #  return HttpResponseNotFound("404 PAGE NOT FOUND!")

def carp(request, num1, num2):
    page_to_go = reverse("multiply",args=[num1,num2])
    return HttpResponseRedirect(page_to_go)