from django.views import View
from django.shortcuts import render
from ..mocks import get_mocked_images
from django.http import HttpResponseRedirect
from django.urls import reverse


class Home(View):
    def most_recent(request):
        images = get_mocked_images()
        context = {
            'images': images,
        }
        return render(request, 'getfashionable/pages/home.html', context)
        # return HttpResponseRedirect(reverse('getfashionable:home'))
