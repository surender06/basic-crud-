from django.urls import path
from .views import YogaListView,SignUpCreateView,YogaUpdateView,YogaDeleteView,YogaCreateView
from .models import Yoga
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path("",YogaCreateView.as_view(),name='create'),
    path("Signup",SignUpCreateView.as_view(),name='signup'),
    path("list/",YogaListView.as_view(),name='list'),
    path("delete/<int:pk>/",YogaDeleteView.as_view(),name='delete'),
    path("edit/<int:pk>/",YogaUpdateView.as_view(),name='edit'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)