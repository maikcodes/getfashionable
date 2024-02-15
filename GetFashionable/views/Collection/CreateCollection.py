from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from GetFashionable.models import Design

from ...forms.Collection import CreateCollectionForm, DesignFormSet


@method_decorator(
    login_required(login_url=reverse_lazy('getfashionable:home')),
    name='dispatch'
)
class CreateCollection(CreateView):
    template_name = 'getfashionable/pages/collection/create.html'
    form_class = CreateCollectionForm
    success_url = reverse_lazy('getfashionable:home')
    context = {}

    def get(self, request):
        form = self.form_class()
        formset = DesignFormSet(queryset=Design.objects.none())
        self.context = {
            'form': form,
            'formset': formset,
            'show_header': True,
        }
        return render(request, self.template_name, self.context)

    def post(self, request):
        form = self.form_class(request.POST)
        formset = DesignFormSet(
            request.POST, request.FILES, queryset=Design.objects.none())
        if form.is_valid() and formset.is_valid():
            collection = form.save(commit=False)
            collection.user = request.user
            collection.save()
            designs = formset.save(commit=False)
            for design in designs:
                design.collection = collection
                design.user = request.user
                design.save()
            return redirect(self.success_url)
        self.context = {
            'form': form,
            'formset': formset,
            'show_header': True,
        }
        return render(request, self.template_name, self.context)
