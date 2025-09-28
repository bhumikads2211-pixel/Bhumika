from django.urls import path
from .views import Webpg ,Login,Course,Certificate,Questions

urlpatterns = [
    path('webpg', Webpg), 
    path('login/', Login),
    path('courses/',Course),
    path('certificates/',Certificate),
    path('questions/',Questions),
]

