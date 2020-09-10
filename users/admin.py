from django.contrib import admin
from .models import Tutor, Student, Course,NotesMaterial,VideoMaterial

# Register your models here.

class TutorAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Tutor)


class StudentAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Student)

class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Course)

class NotesMaterialAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(NotesMaterial)

class VideoMaterialAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(VideoMaterial)