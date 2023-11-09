from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic

from ...models import UserImage


class Profile(generic.View):
    def get(self, request, username):
        user = User.objects.get(username = username)
        user_image = UserImage.objects.get(user=user)
        print(user, user_image)
        

        user_params = {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'image': user_image.image.url
        }

        context = {
            'profile_user': user_params,
            'show_header': True,
        }
        print(context)
        return render(request, 'getfashionable/pages/user/profile.html', context)
