"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

# ( Line 12 Help ) Use include() to add paths from the catalog Application

from django.urls import include

urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

# Add with the special function (RedirectView) the URL (127.0.0.1:8000/catalog) to the root of our mainsite (127.0.0.1:8000)

from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)), # Leave in blank the first function parameter, for '/' implicite. Not necessary especify the "/"
]

#Serve static files as CSS, JavaScript and images. With the next code. Use static() to add url mapping to serve static files during development ( only )
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#We have extend the urlpatterns list with the "+=" operator use. We can simplify code with the next code!!! :

# urlpatterns = [
#       path('admin/', admin.site.urls),
#       path('catalog/', include('catalog.urls')),
#       path('/', RedirectView.as_view(url='/catalog/', permanent=True)),
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Is we coding as before, we need to use imports : from django.urls import include, from django.conf import settings, etc...

# We gonna create a file in catalog folder, named as urls.py