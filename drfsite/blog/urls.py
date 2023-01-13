from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import PostAPIList, PostAPIUpdate, PostAPIDetailView, PostAPIDestroy
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'post', PostViewSet, basename='post')

urlpatterns = [
    path('api/v1/post/', PostAPIList.as_view()),
    path('api/v1/post/<int:pk>/', PostAPIUpdate.as_view()),
    path('api/v1/post_delete/<int:pk>', PostAPIDestroy.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'auth/', include('djoser.urls.authtoken')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('api/v1/', include(router.urls))
    #path('api/v1/post_list/', PostViewSet.as_view({'get': 'list'}), name='post_list'),
    #path('api/v1/post_list/<int:pk>/', PostViewSet.as_view({'put': 'update'}), name='post_listt'),
]
