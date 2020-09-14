from rest_framework.routers import DefaultRouter

from v1 import views

router = DefaultRouter()
router.register(prefix='pokemon', viewset=views.PokemonViewSet, basename='pokemon')
urlpatterns = router.urls
