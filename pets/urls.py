from django.urls import path

from pets.views import OwnerView, DogsView

urlpatterns = [
    path('', OwnerView.as_view()),
    path('dogs/', DogsView.as_view()),
]
