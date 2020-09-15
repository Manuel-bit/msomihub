from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=200, null=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=200, null=False)
    image = models.ImageField( default="profile_pics/default.jpg" ,upload_to='profile_pics')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,  *args, **kwargs):
        super(Student, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Course(models.Model):
    title = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=200, null=False)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.title

class NotesMaterial(models.Model):
    note_content = models.FileField(null = True, upload_to='notes')
    note_title = models.CharField(max_length=200, null=False)
    note_description = models.CharField(max_length=200, null=False)
    course = models.OneToOneField(Course, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.note_title

class VideoMaterial(models.Model):
    video_title = models.CharField(max_length=200, null=False)
    video_url = models.CharField(max_length=50, null=False)
    course = models.OneToOneField(Course, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.video_title
