from django.urls import reverse_lazy
from django.views import generic
from ...forms import SignUpForm
from ...models import UserImage


class SignUp(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('getfashionable:home')
    template_name = "getfashionable/pages/auth/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)

        if self.request.FILES.get('user_image'):
            user_image = UserImage(
                user=self.object, image=self.request.FILES.get('user_image'))
            user_image.save()

        return response
