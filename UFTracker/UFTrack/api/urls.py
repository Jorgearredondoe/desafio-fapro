from django.urls import include, path
from rest_framework.routers import DefaultRouter

from UFTrack.api import views as view


router = DefaultRouter()
router.register(r'uf', view.UFView, basename='uf')

urlpatterns = [
    path('uf/<str:date>/',
         view.UFDetailAPIView.as_view(),
         name='UFDetail'),

    path('', include(router.urls)),
]
