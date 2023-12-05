from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _


def index(request):
    # Translators: This message comments stuff for translation
    output = _("Welcome to my site.")
    print(output)
    return render(request, "index.html", context={})
