from django.shortcuts import render
from .forms import contactForm, InputForm
# Create your views here.
def home(request):
        if request.method == 'POST':
        #print(request.POST)
                name = request.POST.get('username')
                email = request.POST.get('email')
                select = request.POST.get('select')
                return render(request, 'home.html', {'name' : name, 'email': email, 'select' : select})
        else:
                return render(request, 'home.html')



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



