from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.models import CustomUser
from .forms import CustomUserCreationForm
from config.settings import EMAIL_HOST_USER


class CustomUserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        send_mail(
            subject='Спасибо за регистрацию',
            message='Вы успешно зарегистрировались.',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)
