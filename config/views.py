from django.contrib.auth.views import LogoutView as LogoutViewFromAuth
from django.shortcuts import render


def logout(request):
    if request.method == "POST":
        # Instantiate the LogoutView and then call its as_view() method
        logout_view = LogoutViewFromAuth.as_view()
        return logout_view(request)
    else:
        return render(request, 'registration/logged_out.html')