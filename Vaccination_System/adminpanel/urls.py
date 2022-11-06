from django.contrib.auth import views
from django.urls import path
from .views import PatientList , PatientCreate , PatientDelete , PatientUpdate , VaccineCreate , VaccineUpdate , VaccineDelete , VaccineList , Profile , SearchList , StatusControl , PatientCard

app_name = "adminpanel"
urlpatterns = [
    path("login/", views.LoginView.as_view(), name = "login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    # path(
    #     "password_change/", views.PasswordChangeView.as_view(), name="password_change"
    # ),
    # path(
    #     "password_change/done/",
    #     views.PasswordChangeDoneView.as_view(),
    #     name="password_change_done",
    # ),
    # path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    # path(
    #     "password_reset/done/",
    #     views.PasswordResetDoneView.as_view(),
    #     name="password_reset_done",
    # ),
    # path(
    #     "reset/<uidb64>/<token>/",
    #     views.PasswordResetConfirmView.as_view(),
    #     name="password_reset_confirm",
    # ),
    # path(
    #     "reset/done/",
    #     views.PasswordResetCompleteView.as_view(),
    #     name="password_reset_complete",
    # ),
]

urlpatterns += [
    path("", PatientList.as_view() , name = "home") ,
    path("patient/create", PatientCreate.as_view() , name = "patient_create") ,
    path("patient/update/<int:pk>", PatientUpdate.as_view() , name="patient_update") ,
    path("patient/delete/<int:pk>", PatientDelete.as_view() , name="patient_delete") ,
    path("vaccine_list", VaccineList.as_view() , name = "vaccine_list") ,\
    path("vaccine/create", VaccineCreate.as_view() , name = "vaccine_create") ,
    path("vaccine/update/<int:pk>", VaccineUpdate.as_view() , name="vaccine_update") ,
    path("vaccine/delete/<int:pk>", VaccineDelete.as_view() , name="vaccine_delete") ,
    path("profile/", Profile.as_view() , name="profile"),
    path('search/' , SearchList.as_view() , name="search"),
    path('status_control/' , StatusControl , name="status_control"),
    path('preview/<int:pk>' , PatientCard.as_view() , name='preview'),
]