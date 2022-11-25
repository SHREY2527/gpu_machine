from django.shortcuts import render, redirect,HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserloginForm
from .models import Status
from django.core.mail import EmailMultiAlternatives,EmailMessage
from django.template.loader import get_template,render_to_string
from django.template import Context,loader
import requests 





# def index(request):
#      if request.method == 'POST':
#        fm = UserloginForm(request.POST)
#        first_name = request.POST['first_name']
#        return redirect(request,'/index.html',{'first_name':first_name},{'form':fm})




# def login(request):
#     # form_class = UserloginForm
#     # Context = {
#     #     'form':form_class
#     # }
    
#     if request.method == 'POST':
#         form_class = UserloginForm(request.POST)
#         if form_class.is_valid():
#             return render(request,'login.html',{'form': form_class})
#     else:
#         form_class = UserloginForm()
#     return render(request,'login.html')
# def login(request):
#     context = {}
#     form = UserloginForm(request.POST or None)
#     context['form'] = form
#     if request.POST:
#         if form.is_valid():
#             nome = request.POST.get('first_name')
#             print(nome)
#     return render(request, "login.html", context)








# def login(request):
#     researcher = None 
#     study = None
#     form_class = UserloginForm
#     Context = {
#         'form':form_class
#     }
    
#     if request.method == 'POST':
#         fm = form_class(request.POST)
#         if fm.is_valid():
#             nome = request.POST.get('first_name')
#             email = request.POST.get('email')
#             msg = request.POST.get('last_name')

#     return render(request,'login.html',Context)

# def logout_request(request):
    
#         fm = UserloginForm(request.POST)
#         # firstname= fm.cleaned_data("first_name")
#         if request.method == "POST"and fm.is_valid():
#             # fm = UserloginForm(request.POST)
#             Context = {'fms': fm}
#         # context= {'form': fm, 'firstname': firstname}
#         # logout(request)
#         # messages.info(request, "Logged out successfully!")
#         return render(request,'logout.html')



# def show(request):
#     stds = user.objects.all()
#     context = {
#         'std':stds
#     }
#     return render(request,'show.html',context)






  # if request.method == 'POST':
        # model = Status(request.POST) 
        # id = Status.object.get('S_id')
        # if id == 3:
    # html_content = '<p>This is an <strong>important</strong> message.</p>'
    # text_content = 'This is an important message.'





def GPU_status(request):
    # if request.method == "POST":
        # id = Status.objects.get('S_id')
        # if id == 3:
            plaintext = get_template('mail.txt')
            htmly= get_template('mail.html')
                
            subject = 'GPU is on ideal position'
            text_content = plaintext.render()
            html_content = htmly.render()
            msg = EmailMultiAlternatives(subject, text_content,to =['shrey.kshatrainfotech@gmail.com'])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            # request.META.get('https://mail.google.com/mail')
            return HttpResponse("done")

# def off_gpu(request):
    # url = 'https://mail.google.com/mail'        
#     return requests.get(url).json()

def off_gpu(request):
    print("---------------")
    
    return redirect("machine_status/api_call/templates/base.html")

def running_gpu(request):
    return HttpResponse("succesfully submite it")


# for call the function using button
#  HTML FILE
#    <button type="button" class="mybtn" href="{% url 'recognize_me'%}">Open 
#     Camera</button> // THIS IS THE BUTTON TO BE CLICKED

#  url.py
#   from .import views
#   path('/recognize', views.recognize, name='recognize_me')