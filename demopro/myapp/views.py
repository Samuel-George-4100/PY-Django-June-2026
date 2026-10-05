from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from myapp.models import Student
from json import loads
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
#API views

class GoodMorning(View):

    def get(self, request):
        data={"Message":"Good Morning"} #python Dictionary
        return JsonResponse(data)


class GoodEvening(View):

    def get(self, request):
        data = {"Message": "Good Evening"}
        return JsonResponse(data)

class HelloWorld(View):

    def get(self, request):
        data={"Message":"Hello World"}
        return JsonResponse(data)


class UserDetails(View):
    def get(self, request):
        data = [

            {"Name":"Arun", 'age':23, "place":"ekm"},
            {"Name": "Amal", 'age': 24, "place": "tvm"},
            {"Name": "Anu", 'age': 25, "place": "ekm"}

        ]
        return JsonResponse(data,safe=False)


class StudentDetails(View):

    def get(self, request):
        s = Student.objects.all().values()
        print(s)
        print(type(s)) #queryset of student objects

        data = list(s) #converts queryset into list format
        print(data)
        return JsonResponse(data,safe=False)

#APIview for creating new student record
@method_decorator(csrf_exempt,name='dispatch')
class StudentCreate(View):

    def post(self, request):

        data = loads(request.body)#converts json into python native types

        r = data['rollnumber']
        n = data['name']
        a = data['age']
        p = data['place']
        m = data['marks']

        s=Student.objects.create(rollnumber=r,name=n,age=a,place=p,marks=m)
        s.save()
        return JsonResponse({"Message":"Student Created"})

#API view for reading specific record

class StudentDetail(View):

    def get(self, request, i):
        s=list(Student.objects.filter(id=i).values())#json to dictionary
        if s: # [data]
            return JsonResponse(s,safe=False)
        else: # []
            return JsonResponse({"Message":"Student not found"})

@method_decorator(csrf_exempt,name='dispatch')
class StudentDelete(View):

    def delete(self, request, i):
        s = Student.objects.get(id=i)
        s.delete()
        return JsonResponse({"Message":"Student Deleted"})

#full updation

import json
@method_decorator(csrf_exempt,name='dispatch')
class StudentFullUpdate(View):

    def put(self, request, i):#request.body- data coming from client app
        data = json.loads(request.body)#loads used to translate coming json data into python native/dictionary
        print(data)
        try:
            s=Student.objects.get(id=i)
            s.rollnumber=data['rollnumber']
            s.name=data['name']
            s.age=data['age']
            s.place=data['place']
            s.marks=data['marks']
            s.save()
            return JsonResponse({"Message":"Student Updated"})
        except:
            return JsonResponse({"Message":"Student not found"})

@method_decorator(csrf_exempt,name='dispatch')

class StudentPartialUpdate(View):
    def patch(self, request, i):
        data = json.loads(request.body)
        try:
            s=Student.objects.get(id=i)
            if 'rollnumber' in data:
                s.rollnumber=data['rollnumber']
            if 'name' in data:
                s.name=data['name']
            if 'age' in data:
                s.age=data['age']
            if 'place' in data:
                s.place=data['place']
            if 'marks' in data:
                s.marks=data['marks']
            s.save()
            return JsonResponse({"Message":"Student Updated"})
        except:
            return JsonResponse({"Message":"Student not found"})