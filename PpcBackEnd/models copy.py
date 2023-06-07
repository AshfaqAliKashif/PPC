from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class Division(models.Model):
    Division_ID= models.IntegerField()
    Division_Name = models.CharField(max_length=255)

    def __str__(self):
        return self.Division_Name

class District(models.Model):
    District_ID = models.IntegerField()
    Division_ID = models.ForeignKey(Division, on_delete=models.CASCADE)
    District_Code = models.IntegerField()
    District_Name = models.CharField(max_length=255)
    Latitude = models.FloatField()
    Longitude = models.FloatField()

    def __str__(self):
        return self.District_Name

class Town(models.Model):
    Town_ID = models.IntegerField()
    District_ID = models.ForeignKey(District, on_delete=models.CASCADE, related_name="District")
    Town_Name = models.CharField(max_length=255)

    def __str__(self):
        return self.Town_Name


class CustomUser(AbstractUser):
    HOD = '1'
    COLLEGE = '2'
    STUDENT = '3'
    
    EMAIL_TO_USER_TYPE_MAP = {
        'hod': HOD,
        'college': COLLEGE,
        'student': STUDENT
    }
    user_type_data = ((HOD, "HOD"), (COLLEGE, "College"), (STUDENT, "Student"))
    user_type = models.CharField(default=3, choices=user_type_data, max_length=10)

class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class College(models.Model):
    College_ID = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE, blank=True, null=True)
    college_name = models.CharField(max_length=255)
    College_Address = models.CharField(max_length=255)
    college_mobile = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=20)
    college_site = models.URLField()
    person_name = models.CharField (max_length=100)
    email = models.EmailField (max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    objects = models.Manager()
    def __str__(self):
        return self.college_name



class Role(models.Model):
    Role_ID = models.IntegerField()
    Role_Name = models.CharField(max_length=255)

    def __str__(self):
        return self.Role_Name

class Designation(models.Model):
    Designation_ID = models.IntegerField()
    Designation_Name = models.CharField(max_length=255)
    def __str__(self):
        return self.Designation_Name

class Department(models.Model):
    Department_ID = models.IntegerField()
    Department_Name = models.CharField(max_length=255)
    Designation_ID = models.ForeignKey(Designation, on_delete=models.CASCADE, related_name="designation")

    def __str__(self):
        return self.Department_Name

# class Usertbl(AbstractBaseUser):
#     USERNAME_FIELD = 'username'
#     username = models.CharField(max_length=255, unique=True)
#     NormalizedUserName = models.CharField(max_length=255)
#     Email = models.EmailField(max_length=254, unique=True)
#     EmailConfirmed = models.BooleanField()
#     NormalizedEmail = models.EmailField(max_length=254)
#     PasswordHash = models.CharField(max_length=254)
#     SecurityStamp = models.CharField(max_length=254)
#     ConcurrencyStamp = models.CharField(max_length=254)
#     PhoneNumber = models.CharField(max_length=15)
#     PhoneNumberConfirmed = models.BooleanField()
#     password = models.CharField(max_length=255)
#     CNIC = models.CharField(max_length=15)
#     FirstName = models.CharField(max_length=100)
#     LastName = models.CharField(max_length=100)
#     FullName = models.CharField(max_length=200)
#     ProfileImage = models.ImageField(upload_to="profile")
#     Gender = models.CharField(max_length=50)
#     DivisionCode = models.ForeignKey(Division, on_delete=models.CASCADE, related_name="DivisionCode")
#     DistrictCode = models.ForeignKey(District, on_delete=models.CASCADE, related_name="DistrictCode")
#     TownCode = models.ForeignKey(Town, on_delete=models.CASCADE, related_name="TownCode")
#     Department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="designation")    
#     LastLoginDetail = models.DateTimeField(blank=True, null=True)  
#     created_at = models.DateTimeField(auto_now_add=True)
#     created_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_created')
#     updated_at = models.DateTimeField(auto_now=True)
#     updated_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_updated') 
#     IsDisabled = models.BooleanField()
#     role = models.ForeignKey(Role, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.name
    
   
# for updating the profile of the college
# class College(models.Model):
#     College_ID = models.AutoField(primary_key=True)
    # Profile_Image = models.ImageField(upload_to="College/")
    # college_name = models.CharField(max_length=255)
    # College_Address = models.CharField(max_length=255)
    # college_mobile = models.CharField(max_length=20)
    # contact_no = models.CharField(max_length=20)
    # college_site = models.URLField()
    # person_name = models.CharField (max_length=100)
    # email = models.EmailField (max_length=100)
    # College_Admin_Password = models.CharField (max_length=100)
    # Division_ID = models.ForeignKey(Division, on_delete=models.CASCADE)
    # District_ID = models.ForeignKey(District, on_delete=models.CASCADE)
    # Town_ID = models.ForeignKey(Town, on_delete=models.CASCADE)
    # Total_Seats = models.IntegerField()

    # def __str__(self):
    #     return self.College_Name

class Session(models.Model):
    year = models.IntegerField(unique=True)
    session_start_year = models.DateField()
    session_end_year = models.DateField()
    closing_date = models.DateField()

    def __str__(self):
        return str(self.year)

class StudentAdmissionForm(models.Model):
    Std_id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE,blank=True, null=True)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Full_Name = models.CharField(max_length=200)
    Fathers_Name = models.CharField(max_length=100)
    Date_of_Birth = models.DateField()
    Religion = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, blank=True, null=True)
    Qualification = models.CharField(max_length=200)
    Matric_Image = models.ImageField(upload_to='admsn_images/')
    Student_Image = models.ImageField(upload_to='admsn_images/')
    Student_CNIC_Image = models.ImageField(upload_to='admsn_images/')
    Institution_Admission_Letter = models.ImageField('admsn_images/')
    Permanent_Address = models.CharField(max_length=254)
    Student_email=models.EmailField(max_length=100, null=True)
    Student_mobile=models.CharField(max_length=15, null=True)
    College_Name = models.ForeignKey('College', on_delete=models.CASCADE, null=True)
    Session = models.ForeignKey('Session', on_delete=models.CASCADE, null=True)
    profile_pic = models.ImageField(upload_to='profile/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    objects = models.Manager() 
    def __str__(self):
        return f"{self.full_name}'s Admission Form"
# class StudentAdmissionForm(models.Model):
#     Std_id = models.AutoField(primary_key=True)
#     First_Name = models.CharField(max_length=100)
#     Last_Name = models.CharField(max_length=100)
#     Full_Name = models.CharField(max_length=200)
#     Fathers_Name = models.CharField(max_length=100)
#     Date_of_Birth = models.DateField()
#     Religion = models.CharField(max_length=100)
    # Caste = models.CharField(max_length=100)
    # Qualification = models.CharField(max_length=200)
    # Matric_Image = models.ImageField(upload_to='admsn_images/')
    # Student_Image = models.ImageField(upload_to='admsn_images/')
    # Student_CNIC_Image = models.ImageField(upload_to='admsn_images/')
    # Institution_Admission_Letter = models.ImageField('admsn_images/')
    # Permanent_Address = models.CharField(max_length=254)
    # Student_email=models.EmailField(max_length=100, null=True)
    # Student_mobile=models.CharField(max_length=15, null=True)
    # College_Name = models.ForeignKey('College', on_delete=models.CASCADE, null=True)
    # Session = models.ForeignKey('Session', on_delete=models.CASCADE, null=True)

    # def __str__(self):
    #     return f"{self.full_name}'s Admission Form"


# class Examination(BaseModel):
#     session = models.ForeignKey(Session, on_delete=models.CASCADE)
#     college = models.ForeignKey(College, on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.session)

# class Renewal(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     degree_type = models.CharField(max_length=255)
#     renewal_date = models.DateField()

#     def __str__(self):
#         return self.student.name

# class DocumentType(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name



# class Course(models.Model):
#     name = models.CharField(max_length=255)
#     duration = models.IntegerField()  # In years

#     def __str__(self):
#         return self.name

# class SupplementaryExam(models.Model):
#     session = models.ForeignKey(Session, on_delete=models.CASCADE)
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.student.name

# class DegreeType(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class StudentDocument(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
#     document = models.FileField(upload_to=get_student_directory_path)

#     def __str__(self):
#         return self.document_type.name
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created:
        # Check the user_type and insert the data in respective tables
        if instance.user_type == 1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type == 2:
            College.objects.create(admin=instance)
        if instance.user_type == 3:
            StudentAdmissionForm.objects.create(admin=instance,session_year_id=Session.objects.get(id=1), address="", profile_pic="", gender="")
    

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()
    if instance.user_type == 2:
        instance.staffs.save()
    if instance.user_type == 3:
        instance.students.save()