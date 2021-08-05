from rest_framework import routers

from todos.api.views import TodoViewSet


router = routers.SimpleRouter()
router.register(prefix=r'todos', viewset=TodoViewSet, basename='todos')
urlpatterns = router.urls
