from django.urls import path,re_path
from django.views.generic.base import RedirectView
# from django.conf.urls import url
from .views import off_gpu
from . import views
# from django.urls import include, re_path
urlpatterns = [
      # path("logout/", views.logout_request, name="logout"),
      # path("", views.login, name="login"),
      path("",views.id,name="id"),
      path("gpu/",views.GPU_status,name = "gpu"),
      path('off_gpu/',views.off_gpu,name="http://127.0.0.1:8000/off_gpu"),              
      # re_path(r'^off_gpu/$',off_gpu, name='off_gpu'),
      path('running_gpu/',views.running_gpu,name='http://127.0.0.1:8000/running_gpu'),

] 