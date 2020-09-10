from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    url(r'^$', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    url(r'^register-option/$', views.RegisterOption, name="register_option"),
    url(r'^student_register/$', views.StudentRegister, name="student_register"),
    url(r'^tutor_register/$', views.TutorRegister, name="tutor_register"),
    url(r"^student_update/$", views.profile, name='student_update'),
    url(r'^logout/$', views.logoutUser, name="logout"),
]