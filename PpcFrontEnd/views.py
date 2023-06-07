from django.shortcuts import render,HttpResponse, redirect,HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout

def home(request):
	return render(request, 'index.html')
def about(request):
	return render(request, 'About.html')
def contact(request):
	return render(request, 'Contact.html')
def institutionsList(request):
	return render(request, 'institutionsList.html')
def do_login(request):
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

def download(request):
	return render(request, 'Downloads.html')
def Tenders(request):
	return render(request, 'Tenders.html')
def sitemap(request):
	return render(request, 'SiteMap.html')
def Faqs(request):
	return render(request, 'Faqs.html')
def Notifications(request):
	return render(request, 'Notifications.html')
def Budget(request):
	return render(request, 'Budget.html')
def Services(request):
	return render(request, 'Services.html')
def Functions(request):
	return render(request, 'Functions.html')
def Examination(request):
	return render(request, 'Examination.html')
def PharmD(request):
	return render(request, 'MedicalUniversities.html')
def technician(request):
	return render(request, 'MedicalColleges.html')
def PharmacyAssistant(request):
	return render(request, 'TertiaryHospitals.html')
def GoodStandingCertificate(request):
	return render(request, 'HealthPolicy.html')
def base(request):
	return render(request, 'base.html')