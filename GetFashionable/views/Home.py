from django.db.models import F, ExpressionWrapper, fields
from django.shortcuts import render
from django.views import View

from ..models import Design


class Home(View):
    def most_recent(request):
        images = Design.objects.all().order_by('-created_at')

        image_info_list = []

        for image in images:

            image_info = {
                'width': image.image_width,
                'height': image.image_height,
                'url': image.image.url or '',
                'id': image.id
            }

            image_info_list.append(image_info)

        context = {
            'images': image_info_list,
            'show_header': True,
        }
        return render(request, 'getfashionable/pages/home.html', context)
