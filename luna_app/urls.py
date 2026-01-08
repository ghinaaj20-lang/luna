from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ContentViewSet, CommentViewSet, CosmicEventViewSet,
    RegisterView, LoginView, LogoutView, UserProfileView
)
# from .views import api_login, api_logout, api_register

router = DefaultRouter()
router.register(r'content', ContentViewSet, basename='content')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'events', CosmicEventViewSet, basename='event')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),  # Keep only DRF version
    path('login/', LoginView.as_view(), name='login'),           # Keep only DRF version  
    path('logout/', LogoutView.as_view(), name='logout'),        # Keep only DRF version
    path('profile/', UserProfileView.as_view(), name='api_profile'),  # API endpoint for profile data
]

# urlpatterns = [
#     path('', include(router.urls)),
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('profile/', UserProfileView.as_view(), name='profile'),
#     path('feed/', ContentViewSet.as_view({'get': 'feed'}), name='feed'), this in not found in the previous one
#     path('login/', api_login, name='api_login'),
#     path('logout/', api_logout, name='api_logout'),
#     path('register/', api_register, name='api_register'),
# ]