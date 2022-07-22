from django.urls import path
from resume.views import *

urlpatterns = [
    path('portofolio-homepage', index_page, name='homepage'),
    path('user-login/', LoginUser.as_view(), name='login'),
    path('upload-personal-project', upload_project, name='upload'),
    path('edit-uploaded-project/<str:pk>/', edit_project, name='edit_project'),
    path('logout/', LogoutUser.as_view(), name='logout'),

]