from django.shortcuts import render

from django.template import RequestContext, loader
from django.http import HttpResponse

from shapes.models import Triangle, Parallelogram

def home(request):
    context = {}
    return render(request, 'form.html', context)

def getShape(shapeName):
    if shapeName == 'triangle':
        return Triangle()
    elif shapeName == 'parallelogram':
        return Parallelogram()
    else:
        raise NotImplementedError("This shape is not implemented")

def calculate(request):
    shapeName = request.GET.get('shape', '')
    shape = getShape(shapeName)
    dimensions = request.GET.get('dimensions', '')
    area = shape.calculateArea(dimensions)
    perimeter = shape.calculatePerimeter(dimensions)
    context = {'shape': shapeName, 'dimensions': dimensions, 'area': area, 'perimeter': perimeter}
    return render(request, 'results.html', context)

def save(request):
    shapeName = request.GET.get('shape', '')
    shape = getShape(shapeName)
    dimensions = request.GET.get('dimensions', '')
    shape.area = shape.calculateArea(dimensions)
    shape.perimeter = shape.calculatePerimeter(dimensions)
    shape.save()
    context = {'id': shape.id}
    return render(request, 'saved.html', context)