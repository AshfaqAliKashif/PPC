from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from . models import College, StudentAdmissionForm
from datetime import datetime

# Create your views here.
def index(request):
	return render(request, 'BackEndBase.html')
def collegedashboard(request):
	return render(request, 'teacher-dashboard.html')
def studentdashboard(request):
	return render(request, 'student-dashboard.html')
def studentlist(request):
    students = StudentAdmissionForm.objects.all()
    return render(request, 'students.html', {'students': students})
def studentdetail(request):
	return render(request, 'student-details.html')
def addstudent(request):
    if request.user.is_authenticated:
        request.session.set_expiry(1800)
        if request.method=="POST":
            saverecord=StudentAdmissionForm()
            saverecord.First_Name=request.POST.get('First_Name')
            saverecord.Last_Name=request.POST.get('Last_Name')
            saverecord.Fathers_Name=request.POST.get('Fathers_Name')
            # Parse and convert the date string
            date_of_birth_str = request.POST.get('Date_of_Birth')
            date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d').date()
            saverecord.Date_of_Birth = date_of_birth
            saverecord.Religion=request.POST.get('Religion')  
            saverecord.Qualification=request.POST.get('Qualification')  
            saverecord.Matric_Image=request.FILES.get('Matric_Image')  
            saverecord.Student_Image=request.FILES.get('Student_Image')  
            saverecord.Student_CNIC_Image=request.FILES.get('Student_CNIC_Image')  
            saverecord.Institution_Admission_Letter=request.FILES.get('Institution_Admission_Letter')  
            saverecord.Permanent_Address=request.POST.get('Permanent_Address')  
            saverecord.Student_email=request.POST.get('Student_email')  
            saverecord.Student_mobile=request.POST.get('Student_mobile')  
            saverecord.save()
            messages.success(request, f'Student Name {saverecord.First_Name} is created successfully')
            return redirect('addstudent')
        else:
            return render(request, 'add-student.html')
    else:
        return HttpResponseRedirect('/login/')
	
def editstudent(request):
	return render(request, 'edit-student.html')
def collegelist(request):
	return render(request, 'teachers.html')
def collegedetails(request):
	return render(request, 'teacher-details.html')
def addcollege(request):
    if request.user.is_authenticated:
        request.session.set_expiry(1800)
        if request.method=="POST":
            saverecord=College()
            saverecord.college_name=request.POST.get('college_name')
            saverecord.college_mobile=request.POST.get('college_mobile')
            saverecord.contact_no=request.POST.get('contact_no')
            saverecord.college_site=request.POST.get('college_site')
            saverecord.person_name=request.POST.get('person_name')  
            saverecord.email=request.POST.get('email')  
            saverecord.College_Address=request.POST.get('College_Address')  
            # saverecord.college_division=request.POST.get('college_division')  
            # saverecord.college_district=request.POST.get('college_district')  
            # saverecord.college_town=request.POST.get('college_town')  
            saverecord.save()
            messages.success(request, f'College Name {saverecord.college_name} is created successfully')
            return redirect('addcollege')
        else:
            return render(request, 'add-teacher.html')
    else:
        return HttpResponseRedirect('/login/')

def editcollege(request):
	return render(request, 'edit-teacher.html')
def subjectdetails(request):
	return render(request, 'subjects.html')
def addsubject(request):
	return render(request, 'add-subject.html')
def editsubject(request):
	return render(request, 'edit-subject.html')
def feescollections(request):
	return render(request, 'fees-collections.html')
def expenses(request):
	return render(request, 'expenses.html')
def salary(request):
	return render(request, 'salary.html')
def addfeescollection(request):
	return render(request, 'add-fees-collection.html')
def addexpenses(request):
	return render(request, 'add-expenses.html')
def addsalary(request):
	return render(request, 'add-salary.html')
def exam(request):
	return render(request, 'exam.html')
def notification(request):
	return render(request, 'notification.html')
def profile(request):
	if request.user.is_authenticated:
		return render(request, 'profile.html', {'name':request.user})
	else:
		return HttpResponseRedirect('/login/')
def inbox(request):
	return render(request, 'inbox.html')

def login_page(request):
	if not request.user.is_authenticated:
		if request.method =="POST":
			fm = AuthenticationForm(request=request, data=request.POST)
			if fm.is_valid():
				uname = fm.cleaned_data['username']
				upass = fm.cleaned_data['password']
				user = authenticate(username=uname, password=upass)
				if user is not None:
					login (request, user)
					messages.success(request, 'Logged in Successfully !!')
					return HttpResponseRedirect('/profile/')
		else:
			fm = AuthenticationForm()
		return render(request, 'login.html', {'form':fm})
	else:
		return HttpResponseRedirect('/profile/')
def register(request):
	if request.method == "POST":
		fm = SignUpForm(request.POST)
		if fm.is_valid():
			messages.success(request, 'Account Created Successfully !!')
			fm.save()
	else:
		fm =SignUpForm()
	return render(request, 'register.html', {'form':fm})
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/login/')
def user_change_pass(request):
	if request.method == "POST":
		fm = PasswordChangeForm(user=request.user, data=request.POST)
		if fm.is_valid():
			fm.save()
			return HttpResponseRedirect('/profile/')
	else:
		fm = PasswordChangeForm(user=request.user)
	return render(request, 'profile.html', {'form': fm})
def forgotpassword(request):
	return render(request, 'forgot-password.html')
