from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import generic



class SignOut(generic.View):
    def get(self, request):
        logout(request)
        return redirect('getfashionable:home')