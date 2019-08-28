"""flashshipper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf.urls import url
from django.conf import settings
from django.views.static import serve 
from Overview.views import home, create_request, verify_phone_number, generate_view
#from Overview.views import new_page 


urlpatterns = [
    path('admin/', admin.site.urls),
	path('', home),
    path('create_request', create_request),
    path('verify_phone_number', verify_phone_number),
    path('print_label/<int:customer_request_id>/', generate_view),       #dynamic url, take customer_request_id as argument 

    #path('new_page.html', new_page),

]

#upload file path. Change this when deploy to server
if settings.DEBUG:
    urlpatterns+= [
        url(r'^uploaded_label/(?P<path>.*)$', serve,{ 
            'document_root': settings.MEDIA_ROOT,
        })
    ]