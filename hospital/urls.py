from django.urls import path
from . import views
from knox.views import LogoutView, LogoutAllView


urlpatterns = [
    path("doctor/", views.DoctorViews.as_view()),
    path("doctor/<int:id>", views.DoctorViews.as_view()),
    path("nurse/", views.NurseViews.as_view()),
    path("nurse/<int:id>", views.NurseViews.as_view()),
    path("room/", views.RoomViews.as_view()),
    path("room/<int:id>", views.RoomViews.as_view()),
    path("bed/", views.BedViews.as_view()),
    path("bed/<int:id>", views.BedViews.as_view()),
    path("patient/", views.PatientViews.as_view()),
    path("patient/<int:id>", views.PatientViews.as_view()),

    path('register/', views.register_api),
    path('login/', views.login_api),
    path('user/', views.get_user_data),
    path('logout/', LogoutView.as_view()),
    path('logoutall/', LogoutAllView.as_view())

]
