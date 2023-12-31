from django.conf.urls.static import static
from PlagiatChecker import settings

from django.contrib import admin
from django.urls import path
from .views import index
from accounts.views import login_user,register_user,logout_user
from plagiatDocuments.views import plagiatDocument
from plagiatLocal.views import plagiatLocal
from plagiatOnline.views import plagiatOnline

urlpatterns = [
    path("", login_user, name="login_user"),
    path("dashboard/", index, name="index"),
    path("register/", register_user, name="register_user"),
    path("logout/", logout_user, name="logout"),
    path('admin/', admin.site.urls),
    
    # Ekobo et Ferdinand
    path("plagiatDocument/", plagiatDocument, name="plagiatDocument"),
    
    
    # Dimitri et 45 
    path("plagiatLocal/", plagiatLocal ,name="plagiatLocal"),
    
    
    # Gallagher
    path("plagiatOnline/", plagiatOnline ,name="plagiatOnline"),    

]
