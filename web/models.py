from django.db import models

# Create your models here.


class Departments(models.Model):
    department = models.CharField(max_length=100)
    def __str__(self):
        return self.department


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    pic = models.ImageField(upload_to="img")

    def __str__(self):
        return self.title

class Event(models.Model):
    pic = models.ImageField(upload_to="img")
    event = models.CharField(max_length=500)
    date = models.CharField(max_length=200)
    time = models.CharField(max_length=100)
    venue = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    details = models.CharField(max_length=2000)

    def __str__(self):
        return self.event


class Career(models.Model):
    post = models.CharField(max_length=500)
    type = models.CharField(max_length=100)
    location = models.CharField(max_length=300)
    lastdate = models.DateField(null=True)
    salary = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    requirements = models.CharField(max_length=2000)

    def __str__(self):
        return self.post


class CareerApplication(models.Model):
    name = models.CharField(max_length=250)
    post =models.ForeignKey(Career, on_delete=models.CASCADE)
    location = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    cv = models.FileField(upload_to="img/file")
    moreinfo = models.CharField(max_length=2000)




class Courses(models.Model):
    banner = models.ImageField(upload_to="img")
    course = models.CharField(max_length=500)
    dep = models.ForeignKey(Departments, on_delete=models.CASCADE)
    seats = models.IntegerField()
    duration = models.IntegerField()
    details = models.CharField(max_length=2000)
    def __str__(self):
        return self.course

class Faculty(models.Model):
    name = models.CharField(max_length=250)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    designation = models.CharField(max_length=250)

    def __str__(self):
        return self.designation
