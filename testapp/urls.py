from rest_framework.routers import DefaultRouter

from views import MyViewSet


router = DefaultRouter()
router.register(r'test-model', MyViewSet)
urlpatterns = router.urls
