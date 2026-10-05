from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from employee_crud.employees.models import Employee
from django.views import View
import json
# Create your views here.
class EmployeeList(View):
    def get(self,request):
        employees=Employee.objects.all().values()
        data=list(employees)
        return JsonResponse(data,safe=False)

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCreate(View):
    def post(self,request):
        data=json.loads(request.body)
        e=data['empid']
        n=data['name']
        a=data['age']
        p=data['place']
        g=data['gender']
        j=data['joining_date']
        s=data['salary']
        d=data['designation']
        c=Employee.objects.create(empid=e,name=n,age=a,place=p,gender=g,joining_date=j,salary=s,designation=d)
        c.save()
        return JsonResponse({"Message":"Employee Created"})

class EmployeeRetrieve(View):
    def get(self,request,id):
        e=list(Employee.objects.filter(id=id).values())
        if e:
            return JsonResponse(e,safe=False)
        else:
            return JsonResponse({"Message":"Employee not found"})

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeFullUpdate(View):
    def put(self,request,id):
        data=json.loads(request.body)
        try:
            obj=Employee.objects.get(id=id)
            obj.name=data['name']
            obj.age=data['age']
            obj.place=data['place']
            obj.gender=data['gender']
            obj.joining_date=data['joining_date']
            obj.salary=data['salary']
            obj.designation=data['designation']
            obj.save()
            return JsonResponse({"Message":"Employee Updated"})
        except:
            return JsonResponse({"Message":"Employee not found"})

@method_decorator(csrf_exempt,name='dispatch')
class EmployeePartialUpdate(View):
    def patch(self,request,id):
        data=json.loads(request.body)
        try:
            obj=Employee.objects.get(id=id)
            if 'empid' in data:
                obj.empid=data['empid']
            if 'name' in data:
                obj.name=data['name']
            if 'age' in data:
                obj.age=data['age']
            if 'place' in data:
                obj.place=data['place']
            if 'gender' in data:
                obj.gender=data['gender']
            if 'joining_date' in data:
                obj.joining_date=data['joining_date']
            if 'salary' in data:
                obj.salary=data['salary']
            if 'designation' in data:
                obj.designation=data['designation']
            return JsonResponse({"Message":"Employee Partially Updated"})
        except:
            return JsonResponse({"Message":"Employee not found"})


