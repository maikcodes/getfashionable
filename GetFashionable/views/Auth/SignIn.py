from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from ...forms import SignInForm


class SignIn(generic.View):
    form_class = SignInForm
    success_url = reverse_lazy('getfashionable:home')
    template_name = "getfashionable/pages/auth/login.html"
    context = {
    }

    def get(self, request):
        form = self.form_class
        self.context = {
            'form': form
        }
        return render(request, self.template_name, self.context)

    def post(self, request):
        if request.method == 'POST':
            print(request.POST)
            form = SignInForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(username=username, password=password)
                
                print('✅', user)
                # user_image = UserImage.objects.get(user, user)
                # user['user_image'] = user_image.image.url
                # print('✅', user)

                if user is not None:
                    login(request, user)
                    return redirect('getfashionable:home')
                else:
                    print(request, 'user is none')
                    messages.error(request, 'user is none')
            else:
                print(request, 'form is not valid')
                messages.error(request, 'form is not valid')

        self.context = {
            'form': SignInForm()
        }
        return render(request, self.template_name, self.context)
