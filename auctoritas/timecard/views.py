import form as form
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.utils.http import is_safe_url
from django.views.generic import CreateView, FormView
from .admin import UserCreationForm, LoginForm, GuestForm
from .models import User_Info


def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context = {
        "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        username       = form.cleaned_data.get("username")
        new_guest_username = User_Info.objects.create(username=username)
        request.session['guest_username'] = new_guest_username.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("/register/")
    return redirect("/register/")


class LoginView(FormView):
   form_class = LoginForm
   success_url = '/'
   template_name = 'timecard/login.html'
   def form_valid(self, form):
       request = self.request
       next_ = request.GET.get('next')
       next_post = request.POST.get('next')
       redirect_path = next_ or next_post or None
       username = form.cleaned_data.get("username")
       password = form.cleaned_data.get("password")
       user = authenticate(request, username=username, password=password)
       if user is not None:
           login(request, user)
           try:
               del request.session['guest_username']
           except:
               pass
           if is_safe_url(redirect_path, request.get_host()):
               return  redirect(redirect_path)
           else:
               return redirect("/")
       return super(LoginView, self).form_invalid(form)

'''def login_form(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        form.set_password(user)
        user.save()
    context = {'form' : form}
    return render(request, "timecard/login.html", context)'''
# Create your views here.
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'timecard/register.html'
    success_url = '/'