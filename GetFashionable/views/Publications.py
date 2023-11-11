from django.views import View
from django.shortcuts import render

from ..models import Design, UserImage


class Publications(View):
    def publication_detail(request, id):

        design = Design.objects.get(id=id)
        user = design.user
        user_image = UserImage.objects.get(user=user)

        context = {
            'publication': {
                'author': {
                    'username': user.username,
                    'name': f'{user.first_name} {user.last_name}',
                    'image_url': user_image.image.url,
                },
                'description': design.name,
                'image': {
                    'height': design.image_height,
                    'width': design.image_width,
                    'url': design.image.url
                },
            },
            'show_header': True,
        }
        return render(request, 'getfashionable/pages/publication_detail.html', context)
