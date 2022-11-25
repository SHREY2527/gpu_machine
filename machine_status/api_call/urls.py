from django.urls import path,re_path
from django.views.generic.base import RedirectView
# from django.conf.urls import url
from .views import off_gpu
from . import views
# from django.urls import include, re_path
urlpatterns = [
      # path("logout/", views.logout_request, name="logout"),
      # path("", views.login, name="login"),
      path("",views.GPU_status),
      path('off_gpu/',views.off_gpu,name="off_gpu"),              
      # re_path(r'^off_gpu/$',off_gpu, name='off_gpu'),
      path('running_gpu/',views.running_gpu,name='running_gpu'),

] 