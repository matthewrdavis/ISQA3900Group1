from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from .forms import *
from django.shortcuts import render, get_object_or_404
from .models import CustomUser


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

@login_required
def customUser_view(request, pk):
    customuser = CustomUser.objects.filter(pk=pk)
    return render(request, 'users/account.html', {"CustomUser": customuser})

@login_required
def account_edit(request, pk):
    account = get_object_or_404(CustomUser, pk=pk)
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=account)
        if form.is_valid():
            account = form.save(commit=False)
            account.save()
            accounts = CustomUser.objects.filter(pk=pk)
            return render(request, 'users/account.html', {'accounts': accounts})
    else:
        # print("else")
        form = CustomUserChangeForm(instance=account)
    return render(request, 'users/account_edit.html', {'form': form})


#class customUserView(LoginRequiredMixin, ListView):
#    model = CustomUser
#    template_name = 'account.html'
#    fields = ('username','email','first_name','last_name')