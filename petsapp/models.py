from django.db import models

# Create your models here.
# Creating table below
class Pets(models.Model): #models is imported up that why we used and Model is a bultin function in models that why we used models.Model
    gender_option = (("Male","Male"),("Female","Female")) # this help to give us dropdown
    type=(("D","Dog"),("C","Cat")) #new column added
    animal_type=models.CharField(max_length=25,choices=type,default="NA") #new column added thats why default value is NA
    name = models.CharField(max_length=15)
    species = models.CharField(max_length=15)
    breed = models.CharField(max_length=15) 
    age = models.IntegerField()
    gender= models.CharField(max_length=10,choices=gender_option)
    price=models.FloatField(default=0) #new column added thats why default value is 0 
    image= models.ImageField(upload_to="media")
    description=models.TextField(max_length=1500)
 
    class Meta: # help to create a table in db.sqlite
        db_table="PetsTable" # db.sqlite table name (PetsTable)


class Student(models.Model): # creating new model or a table
    student_name=models.CharField(max_length=20)
    student_age=models.IntegerField()
    student_email=models.EmailField()
    student_location=models.CharField(max_length=10)
    student_course=models.CharField(max_length=20)

class Courses(models.Model):
    cname=models.CharField(max_length=20)
    sname=models.ManyToManyField(Student)


class Author(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Books(models.Model):
    title= models.CharField(max_length=50)
    author=models.ForeignKey(Author,on_delete=models.CASCADE) #foreignkey has been used for fetching data class Author or a table and used cascade for deleting process.

