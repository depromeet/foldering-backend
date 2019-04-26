from django.conf.urls import include
from django.urls import path

from FolderingFolderServer import views


urlpatterns = [
    #  [GET]    폴더 리스트 보기   /api/folder/{userId}
    path('<int:userId>/', views.FolderListView.as_view()),
    #  [POST]   새로운 폴더 생성   /api/folder/{userId}/create
    path('<int:userId>/create/', views.FolderCreateView.as_view()),

]

# from django.conf.urls import include
# from rest_framework.routers import DefaultRouter
# from .views import LinkViewSet, TextViewSet, ImageViewSet, FolderViewSet
# from django.urls import path
#
# router = DefaultRouter()
# router.register('Link', LinkViewSet)
# urlpatterns = [
#     path('', include(router.urls)),
# ]
# router.register('Text', TextViewSet)
# urlpatterns = [
#     path('', include(router.urls)),
# ]
# router.register('Image', ImageViewSet)
# urlpatterns = [
#     path('', include(router.urls)),
# ]
# router.register('Folder', FolderViewSet)
# urlpatterns = [
#     path('', include(router.urls)),
# ]