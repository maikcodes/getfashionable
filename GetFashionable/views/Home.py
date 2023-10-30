from django.views import View
from django.shortcuts import render
from ..mocks import get_mocked_images


class Home(View):
    def most_recent(request):
        images = get_mocked_images()
        context = {
            'images': images,
        }
        return render(request, 'getfashionable/pages/home.html', context)
