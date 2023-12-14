from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
# from .forms import CreateUserForm
from .forms import CustomUserCreationForm
from .models import User

def index(request):
    return render(request, "index.html", context={})


def users(request):
    users = User.objects.all()
    return render(
        request,
        "users.html",
        context={'users': users}
    )


class UserCreateFormView(View):
    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        return render(request, 'create_user.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        print(request.POST)
        print(f'form is valid: ', form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('create_user')
        return render(request, 'create_user.html', {'form': form})


# def create_user(request):
#     form = CreateUserForm()
#     if request.method == 'GET':
#         return render(request, 'create_user.html', {'form': form})
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():  # Если данные корректные, то сохраняем данные формы
#             form.save()
#         return redirect('users')



