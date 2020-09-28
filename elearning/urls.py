from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r"^student_profile/$", views.StudentProfile, name="student_profile"),
    url(r"^tutor_profile/$", views.TutorProfile, name="tutor_profile"),
    url(r"^courses/$", views.Courses, name="courses"),
    url(r'^courses/notes/all/(\d+)/$', views.Materials, name="notes"),
    url(r'^courses/videos/all/(\d+)/$', views.VideoTutorials, name="video_tutorials")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)