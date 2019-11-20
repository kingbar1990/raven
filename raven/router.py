from rest_framework import routers

from apps.app_user import views as users_views
from apps.app_surgeries import views as surgeries_views

router = routers.DefaultRouter()
router.register('users', users_views.UserViewSet)
router.register('surgeries', surgeries_views.SurgeryViewSet)

urlpatterns = router.urls