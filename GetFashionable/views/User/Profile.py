from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic

from ...models import UserImage, Design


class Profile(generic.View):
    def get(self, request, username):
        user = User.objects.get(username=username)
        user_image = UserImage.objects.get(user=user)

        images = Design.objects.filter(user=user).order_by('-created_at')

        image_info_list = []

        for image in images:

            image_info = {
                'width': image.image_width,
                'height': image.image_height,
                'url': image.image.url or '',
                'id': image.id
            }

            image_info_list.append(image_info)

        user_params = {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'image': user_image.image.url,
            'designs': image_info_list
        }

        context = {
            'profile_user': user_params,
            'show_header': True,
        }

        return render(request, 'getfashionable/pages/user/profile.html', context)
