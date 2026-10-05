from django.shortcuts import render
from django.views import View
import math
# Create your views here.
class Home(View):

    def get(self, request):
        return render(request, 'home.html')

class Add(View):

    def get(self, request):
        return render (request, 'form.html')

    def post(self, request):
        data = request.POST
        num1 = int(data['num1'])
        num2 = int(data['num2'])
        addition = num1 + num2
        context = {'sum': addition}
        return render(request, 'form.html', context)

class Fact(View):

    def get(self,request):
        return render(request, 'fact.html')

    def post(self, request):
        data = request.POST
        num1 = int(data['number'])
        factorial = math.factorial(num1)
        context = {'result': factorial}
        return render(request, 'fact.html', context)

class BMI(View):

    def get(self, request):
        return render(request, 'bmi.html')

    def post(self, request):
        data = request.POST
        height = int(data['height'])
        weight = int(data['weight'])
        bmi = weight/(height*height)
        context = {'result': bmi}
        return render(request, 'bmi.html', context)