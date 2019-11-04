from django.shortcuts import render
from .models import *
# Create your views here.

from django.http import HttpResponse

def teacher(request):
    return render(request, 'teacher.html')

def logout(request):
    if request.COOKIES.get("loggedIn"):
        response = render(request,'operatorLogin.html')
        response.delete_cookie("loggedIn")
        return response
    else:
        render(request,'operatorLogin.html')

def addNewTable(request):
    branch_name = request.GET['branch']
    year = request.GET['year']
    section = request.GET['section']

    branch = Branch.objects.get(branch_name=branch_name, year=year)
    tb=TimeTable.objects.filter(branch_name=branch,year=year,section=section)
    if len(tb)!=0:
        return render(request, 'errorPage.html',{'message':"Table Already Exists"})
    subjects = branch.subjects
    subjects = subjects.split('-')
    return render(request, 'table.html', {'subjects': subjects,'branch':branch_name,'year':year,'section':section})
def operator(request):
    if request.COOKIES.get("loggedIn"):
        return render(request, 'operatot.html')
    else:
        return render(request, 'operatorLogin.html')

def operatorLogIn(request):
    uname=request.POST['uname']
    password=request.POST['password']
    print(uname,password)
    user=Admin.objects.filter(username=uname)
    if len(user)==0:
        return render(request, 'errorPage.html', {'message': "Wrong Credentials"})
    reqPass=Admin.objects.get(username=uname)
    if reqPass.password==password:
        response = render(request, 'operatot.html')
        response.set_cookie("loggedIn", True)
        return response
    else:
        return render(request, 'errorPage.html',{'message':"Wrong Credentials"})
def student(request):
    return render(request, 'student.html')

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    subjects=['A','B','C','D']
    res=''
    for s in subjects:
        res+='<option value="'+str(s)+'">'+str(s)+'</option>'
    return render(request, 'index.html',{'subjects':subjects})

def put_into_db(request):
    table=[]
    branch_name = request.POST['branch']
    year = request.POST['year']
    section = request.POST['section']
    for i in range(1,7):
        res=''
        for j in range(1,8):
            res+=request.POST['tb'+str(j)+str(i)]+'-'
        table.append(res[:-1])
    branch = Branch.objects.get(branch_name=branch_name, year=year)
    tb=TimeTable(branch_name=branch,year=year,section=section,monday=table[0],tuesday=table[1],wednesday=table[2],thursday=table[3],friday=table[4],saturday=table[5])
    tb.save()

    tbTotal=get_timetable(branch,section,year)
    tbTotal['branch']=branch_name
    tbTotal['year']=year
    tbTotal['section']=section
    return render(request, 'tableView.html', tbTotal)

def get_timetable(branch,section,year):

    tb=TimeTable.objects.get(branch_name=branch,year=year,section=section)
    table=[tb.monday,tb.tuesday,tb.wednesday,tb.thursday,tb.friday,tb.saturday]
    d={}
    for i in range(1,7):
        day=table[i-1].split('-')
        for j in range(1,8):
            d['tb'+str(j)+str(i)]=day[j-1]
    return d

def view_timetable(request):
    branch_name = request.GET['branch']
    year = request.GET['year']
    section = request.GET['section']
    branch = Branch.objects.get(branch_name=branch_name, year=year)
    tbTotal = get_timetable(branch, section, year)
    tbTotal['branch'] = branch_name
    tbTotal['year'] = year
    tbTotal['section'] = section
    return render(request, 'tableView.html', tbTotal)

def show_table_to_modify(request):
    branch_name = request.GET['branch']
    year = request.GET['year']
    section = request.GET['section']

    branch = Branch.objects.get(branch_name=branch_name, year=year)
    tb = TimeTable.objects.filter(branch_name=branch, year=year, section=section)
    if len(tb) == 0:
        return render(request, 'errorPage.html',{'message':"Table Doesnot Exist"})
    subjects = branch.subjects
    subjects = subjects.split('-')
    return render(request, 'modifyTable.html', {'subjects': subjects, 'branch': branch_name, 'year': year, 'section': section})

def modify_TimeTable(request):
    branch_name = request.POST['branch']
    year = request.POST['year']
    section = request.POST['section']
    branch = Branch.objects.get(branch_name=branch_name, year=year)
    tb=TimeTable.objects.get(branch_name=branch,year=year,section=section)
    table=[]
    for i in range(1,7):
        res=''
        for j in range(1,8):
            res+=request.POST['tb'+str(j)+str(i)]+'-'
        table.append(res[:-1])
    tb.monday=table[0]
    tb.tuesday = table[1]
    tb.wednesday = table[2]
    tb.thursday = table[3]
    tb.friday = table[4]
    tb.saturday = table[5]
    tb.save()
    view_timetable(request)

def removeTable(request):
    branch_name = request.POST['branch']
    year = request.POST['year']
    section = request.POST['section']
    branch = Branch.objects.get(branch_name=branch_name, year=year)
    tb = TimeTable.objects.filter(branch_name=branch, year=year, section=section)
    if len(tb)==0:
        return render(request, 'errorPage.html', {'message': "Table doesnot exist"})
    tb.delete()
    return render(request, 'errorPage.html', {'message': "Successfully Deleted"})

def add_branch(request):
    branch_name = request.POST['branch']
    year = request.POST['year']
    subjects = request.POST['subjects']
    b=Branch.objects.filter(branch_name=branch_name,year=year,subjects=subjects)
    if len(b)!=0:
        return render(request, 'errorPage.html', {'message': "Already exists"})
    b=Branch(branch_name=branch_name,year=year,subjects=subjects)
    b.save()
    return render(request, 'errorPage.html', {'message': "Successfully Added"})

def remove_branch(request):
    branch_name = request.POST['branch']
    year = request.POST['year']
    branch = Branch.objects.filter(branch_name=branch_name, year=year)
    if len(branch)==0:
        return render(request, 'errorPage.html', {'message': "No Branch exists"})
    branch.delete()
    return render(request, 'errorPage.html', {'message': "Successfully Deleted"})


def add_subject(request):
    subject = request.POST['subject']
    s=Subject.objects.filter(name=subject)
    if len(s)!=0:
        return render(request, 'errorPage.html', {'message': "Subject Already Exists"})
    s=Subject(name=subject)
    s.save()
    return render(request, 'errorPage.html', {'message': "Subject Successfully Addes"})

def removeSubject(request):
    subject = request.POST['subject']
    sub=Subject.objects.filter(name=subject)
    if len(sub)==0:
        return render(request, 'errorPage.html', {'message': "Subject Doesnot Exists"})
    sub.delete()
    return render(request, 'errorPage.html', {'message': "Subject Successfully Deleted"})

def add_student(request):
    rollno=request.POST['rollno']
    branch=request.POST['branch']
    section=request.POST['section']
    year=request.POST['year']
    std=Student.objects.filter(rollno=rollno)
    if len(std)!=0:
        return render(request, 'errorPage.html', {'message': "Student Already Exists"})
    branch=Branch.objects.get(branch_name=branch,year=year)
    std=Student(rollno=rollno,branch=branch,section=section)
    std.save()
    return render(request, 'errorPage.html', {'message': "Student Successfully Added"})

def showTimetable_toStudent(request):
    rollno = request.GET['rollno']
    student=Student.objects.get(rollno=rollno)
    branch=student.branch
    section=student.section
    year=branch.year
    tbTotal = get_timetable(branch, section, year)
    tbTotal['branch'] = branch.branch_name
    tbTotal['year'] = year
    tbTotal['section'] = section
    return render(request, 'tableView.html', tbTotal)

