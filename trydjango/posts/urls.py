from django.urls import path 
from . import views
app_name ='posts' 
urlpatterns =[
   path("hello/",views.post_home,name ="index"),
   path("name/",views.my_name, name ="name"),
   path("try/",views.web ,name ="try"),
   path("<id>/",views.post_detail ,name="detail"),
   path("<id>/edit",views.post_update ,name="update"),
   path("create/",views.post_create, name ="djangoforms"),
   path("<id>/delete",views.post_delete,name="delete")
]