from django.contrib import admin
from django.urls import path, include
from django.conf import settings  
from django.conf.urls.static import static

from Skills import views as skills_views
from Nav import views as home_views
from Projects import views as pro_views
from Certificates import views as certificates_views
from Contact import views as contact_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_views.navbar, name="home"),
    path("Cv_Download/", home_views.Cv_fun, name="Cv_Download"),
    path("Skills/", skills_views.skills_fun, name="skills"),
    path("Projects/", pro_views.pro_fun, name="projects"),
    path("Certificates/", certificates_views.certificates_fun, name="certificates"),
    path("Contact/", contact_views.contact_fun, name="contact"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)