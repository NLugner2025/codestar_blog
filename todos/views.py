from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from todos.models import YourModel
from todos.utils import create_notification


def create_item(request):
if request.method == 'POST':
item = YourModel.objects.create(name=request.POST['Notification'])
		create_notification(
			request.user, f"Item '{item.name}' created successfully."
		)
		return redirect('home')


def update_item(request, item_id):
	item = YourModel.objects.get(id=item_id)
	if request.method == 'POST':
		item.name = request.POST['Notification']
		item.save()
		create_notification(request.user, f"Item '{item.name}' updated successfully.")
		return redirect('home')

def delete_item(request, item_id):
    item = YourModel.objects.get(id=item_id)
    item.delete()
    create_notification(request.user, f"Item '{item.name}' deleted successfully.")
    return redirect('home')

def mark_notifications_as_read(request):
    request.user.notification_set.filter(is_read=False).update(is_read=True)
    return redirect('home')
from .models import Todo


class HomePage(TemplateView):
	template_name = 'index.html'


class ListTodo(LoginRequiredMixin, ListView):
	model = Todo
	template_name = 'tasks/todo_list.html'
	context_object_name = 'todos'
	paginate_by = 5

	def get_queryset(self):
		return Todo.objects.filter(created_by=self.request.user)


class CreateTodo(LoginRequiredMixin, CreateView):
	model = Todo
	fields = ['title', 'completed']
	template_name = 'tasks/create_todo.html'

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super().form_valid(form)


class UpdateTodo(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
	model = Todo
	fields = ['title', 'completed']
	template_name = 'tasks/update_todo.html'
	success_url = reverse_lazy('list-todo')
	
	def test_func(self):
		todo = self.get_object()
		if self.request.user == todo.created_by:
			return True
		else:
			return False


class DeleteTodo(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
	model = Todo
	template_name = 'tasks/delete_todo.html'
	success_url = reverse_lazy('list-todo')

	def test_func(self):
		todo = self.get_object()
		if self.request.user == todo.created_by:
			return True
		else:
			return False
def mark_notifications_as_read(request):
    request.user.notification_set.filter(is_read=False).update(is_read=True)
    return redirect('home')
