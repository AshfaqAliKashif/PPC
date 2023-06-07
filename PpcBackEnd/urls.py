from django.contrib import admin
from django.urls import path, include
from . import views as backendurls

urlpatterns = [
    path('maindashboard/', backendurls.index, name="index"),
    path('admindashboard/', backendurls.index, name="index"),
    path('collegedashboard/', backendurls.collegedashboard, name="collegedashboard"),
    path('subjectdetails/', backendurls.subjectdetails, name="subjectdetails"),
    path('addsubject/', backendurls.addsubject, name="addsubject"),
    path('editsubject/', backendurls.editsubject, name="editsubject"),    
    path('feescollections/', backendurls.feescollections, name="feescollections"),    
    path('expenses/', backendurls.expenses, name="expenses"),    
    path('salary/', backendurls.salary, name="salary"),    
    path('addfeescollection/', backendurls.addfeescollection, name="addfeescollection"),    
    path('addexpenses/', backendurls.addexpenses, name="addexpenses"),    
    path('addsalary/', backendurls.addsalary, name="addsalary"),    
    path('exam/', backendurls.exam, name="exam"),
    path('notification/', backendurls.notification, name="notification"),    
    path('profile/', backendurls.profile, name="profile"),    
    path('inbox/', backendurls.inbox, name="inbox"),    
    path('login/', backendurls.login_page, name="login"),   
    path('logout/', backendurls.user_logout, name='logout'), 
    path('register/', backendurls.register, name="register"),    
    path('forgotpassword/', backendurls.forgotpassword, name="forgotpassword"),    
    path('changepass/', backendurls.user_change_pass, name="changepass"),   
    
    # URLS for Student
    path('studentdashboard/', backendurls.studentdashboard, name="studentdashboard"),
    path('studentlist/', backendurls.studentlist, name="studentlist"),
    path('studentdetail/', backendurls.studentdetail, name="studentdetail"),
    path('addstudent/', backendurls.addstudent, name="addstudent"),
    path('editstudent/', backendurls.editstudent, name="editstudent"), 
    # URLS for College
    path('collegelist/', backendurls.collegelist, name="collegelist"),
    path('collegedetail/', backendurls.collegedetails, name="collegedetails"),
    path('addcollege/', backendurls.addcollege, name="addcollege"),
    path('editcollege/', backendurls.editcollege, name="editcollege"),
]



