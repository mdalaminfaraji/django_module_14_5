from django.shortcuts import render
from .forms import contactForm, InputForm
from .import models , forms
# Create your views here.
def home(request):
        geekModel=models.GeeksModel.objects.all()
        return render(request, 'home.html', {"data":geekModel})



def submit_form(request):
    return render(request, 'form.html')

def about(request):
        if request.method == 'POST':
        #print(request.POST)
                name = request.POST.get('username')
                email = request.POST.get('email')
                select = request.POST.get('select')
                return render(request, 'about.html', {'name' : name, 'email': email, 'select' : select})
        else:
                return render(request, 'about.html')      
        
def DjangoForm(request):
        form=contactForm(request.POST)
        if form.is_valid():
                print(form.cleaned_data)
        return render(request, 'practice_form.html', {'form':form})

def geekForm(request):
        form=InputForm(request.POST)
        if form.is_valid():
                print(form.cleaned_data)
        return render(request, 'geekForGeek.html', {'form':form})


def add_geekModel(request):
        if request.method=='POST':
                form=forms.GeeksForm(request.POST)
                if form.is_valid():
                        form.save()
        else:
                form=forms.GeeksForm()
        return render(request, 'add_form.html', {'form':form})



