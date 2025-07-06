from django.shortcuts import render
import string
import random 
# Create your views here.
def home(request):
    password = ''
    error = ''
    if request.method == 'POST':
        try:
            plen = int(request.POST.get('length'))
            if plen < 4:
                error  = "Password length must be at least 4 characters."
            else:
                s = string.ascii_letters + string.digits + string.punctuation 
                password = ''.join(random.sample(s, plen))
        except:
            error = "Invalid input. Please enter a valid number for password length."
    return render(request, 'home.html', {'password': password, 'error':error})    
        