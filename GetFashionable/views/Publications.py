from django.views import View
from django.shortcuts import render
from ..mocks import get_mock_image_url


class Publications(View):
    def publication_detail(request, id):
        image_url = get_mock_image_url(height=100, width=100)
        context = {
            'publication': {
                'author': {
                    'name': 'Lorem Ipsum',
                    'image_url': 'getfashionable/images/user.jpg',
                },
                'description': 'In this collection I put all of my creativity using retro colors for women and men night gallery 🔥.',
                'image': {
                    'height': 100,
                    'width': 100,
                    'url': image_url
                },
            },
            'show_header': True,
        }
        return render(request, 'getfashionable/pages/publication_detail.html', context)
