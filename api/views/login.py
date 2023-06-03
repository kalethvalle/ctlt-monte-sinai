from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import View

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('api:home')
        
        return render(
            request,
            template_name='CtlT/login.html'
        )
    
    def post(self, request):
        data = request.POST
        username = data.get('email')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('api:home')

        return render(
            request,
            template_name='CtlT/login.html',
            context={
                "message": "Email o contraseña son incorrectos" 
            }
        )