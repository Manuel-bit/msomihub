from django.contrib import admin
from .models import Tutor, Student, Course,NotesMaterial,VideoMaterial
from embed_video.admin import AdminVideoMixin

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

class VideoMaterialAdmin(AdminVideoMixin, admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(VideoMaterial)