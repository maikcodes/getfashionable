from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import CreateView

from PIL import Image

from ...forms.Design import CreateDesignForm


@method_decorator(
    login_required(login_url=reverse_lazy('getfashionable:home')),
    name='dispatch'
)
class CreateDesign(CreateView):
    template_name = 'getfashionable/pages/design/create.html'
    form_class = CreateDesignForm
    success_url = reverse_lazy('getfashionable:home')
    context = {}

    def get(self, request):
        self.context = {
            'form': self.form_class,
            'show_header': True,
        }
        return render(request, self.template_name, self.context)
    
    def form_valid(self, form):
        user = self.request.user

        image_loaded = self.request.FILES.get('image')

        if image_loaded.content_type.startswith('image'):
            image = Image.open(image_loaded)
            image_width, image_height = image.size

            design = form.save(commit=False)
            design.image_width = image_width
            design.image_height = image_height
            design.user = user
            design.save()

        return super().form_valid(form)
