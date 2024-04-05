from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from api.views import (
    DepartmentViewSet,
    CommunicationKindViewSet,
    SignUpView,
    LogInView,
    ClientViewSet,
    CustomUserViewSet,
    CommunicationSourceViewSet,
    CommunicationViewSet,
    DepartmentCommunicationViewSet,
)

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('log-in/', LogInView.as_view(), name='log_in'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet, basename='departments')
router.register(r'communication-rules', DepartmentCommunicationViewSet, basename='communication-rules')
router.register(r'communication-kinds', CommunicationKindViewSet, basename='communications-kinds')
router.register(r'communication-sources', CommunicationSourceViewSet, basename='communication-sources')
router.register(r'communications', CommunicationViewSet, basename='communications')
router.register(r'clients', ClientViewSet, basename='clients')
router.register(r'custom-users', CustomUserViewSet, basename='custom-users')
urlpatterns += router.urls
