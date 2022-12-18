from rest_framework import routers
from .api import CommentViewSet

router = routers.DefaultRouter()
router.register("api/comment", CommentViewSet, "comments")

urlpatterns=router.urls