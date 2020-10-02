from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="Home Page"),
    path("form",views.forms_view,name="Form Page"),
    path("model",views.models_view,name="Model Page"),

]
