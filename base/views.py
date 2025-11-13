# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
# from django.contrib.auth.views import LogoutView

# from django.contrib.auth.views import LoginView

# from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import Task
# # Create your views here.

# class CustomLoginView(LoginView):
#     template_name = 'base/login.html'
#     fields = '__all__'
#     redirect_authenticated_user = True
    
#     def get_success_url(self):
#         return reverse_lazy('tasks')
    
# class CustomLogoutView(LogoutView):
#     # This allows GET requests (e.g., when clicking a logout link)
#     def get(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)
# class TaskList(LoginRequiredMixin, ListView):
#     model = Task
#     context_object_name = 'tasks'
    
# class TaskDetail(LoginRequiredMixin, DetailView):
#     model = Task
#     context_object_name = 'task'
#     template_name = 'base/task.html'    
    
# class TaskCreate(LoginRequiredMixin, CreateView):    
#     model = Task
#     fields = '__all__'
#     success_url = reverse_lazy('tasks')
    
# class TaskUpdate(LoginRequiredMixin, UpdateView): 
#     model = Task  
#     fields = '__all__'
#     success_url = reverse_lazy('tasks')
    
# class DeleteView(LoginRequiredMixin, DeleteView):
#     model = Task
#     context_object_name = 'task'
#     success_url = reverse_lazy('tasks')   
from django.contrib.auth import logout
from django.shortcuts import redirect

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

# class CustomLogoutView(LogoutView):
#     def get(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)

def logout_user(request):
    """Logs the user out and redirects to the login page."""
    logout(request)
    return redirect('login')

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
