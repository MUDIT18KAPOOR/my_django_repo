from django.shortcuts import render
from .forms import basic
from .models import id,detail

# Create your views here.
def index(req):
    dict = {"insert_me":"Template_Tag"}
    return render (req,"my_app/index.html",context=dict)

def forms_view(req):
    dict = {"form":basic}

    if req.method=="POST":
        form = basic(req.POST)

        if form.is_valid():
            print("NAME :" +form.cleaned_data["FirstName"])
            print("LastName :" +form.cleaned_data["LastName"])
            print("Email :" +form.cleaned_data["Email"])
            print("Text :" +form.cleaned_data["Text"])

    return render (req,"my_app/forms_view.html",context=dict)


def models_view(req):
    id_list = id.objects.order_by("top_name")
    details_list= detail.objects.order_by("location")
    dict={"id":id_list,"detail": details_list}
    return render (req,"my_app/models_view.html",context=dict)
