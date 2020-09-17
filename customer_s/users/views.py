from django.shortcuts import render ,redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, PdfForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Document
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
@login_required(login_url='/login')

def profile(request):
    if request.method=="POST":
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES ,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("/profile")


    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)


    context={"u_form":u_form,
             "p_form":p_form
             }
    return render(request,'users/profile.html',context)

class PdfListView(LoginRequiredMixin, ListView):
    model = Document
    template_name='users/document_form.html'


class PdfListView(LoginRequiredMixin, ListView):
    model = Document
    template_name='users/document_form.html'
    context_object_name= 'document'
    def get_queryset(self):
        queryset = Document.objects.all()
        user = self.request.user


        if not user.is_superuser:
            queryset = queryset.filter(
                created_by=user
            )

        return queryset


class PdfCreateView(LoginRequiredMixin, CreateView):
    model = Document
    fields = ['title', 'pdf']
    template_name='users/profile.html'

    def get_success_url(self):
        return reverse('pdf-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created! Please log in.")
            return redirect("/login")
    else:
        form=UserRegisterForm()
    return render(request, 'users/register.html',{"form":form})

def update_profile(request):
    if request.method=="POST":
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES ,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated!")
        return redirect("/profile")
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)

    context={"u_form":u_form,
             "p_form":p_form,
             }
    return render(request,'users/update_profile.html',context)
