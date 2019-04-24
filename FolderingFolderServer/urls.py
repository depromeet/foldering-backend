from django.conf.urls import include
from rest_framework.routers import DefaultRouter 
from .views import LinkViewSet, TextViewSet, ImageViewSet, FolderViewSet
from django.urls import path

router = DefaultRouter() 
router.register('Link', LinkViewSet) 
urlpatterns = [ 
    path('', include(router.urls)), 
] 
router.register('Text', TextViewSet) 
urlpatterns = [ 
    path('', include(router.urls)), 
] 
router.register('Image', ImageViewSet) 
urlpatterns = [ 
    path('', include(router.urls)), 
] 
router.register('Folder', FolderViewSet) 
urlpatterns = [ 
    path('', include(router.urls)), 
] 