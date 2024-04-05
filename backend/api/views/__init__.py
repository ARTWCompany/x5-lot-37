from .auth_views import LogInView
from .client_views import SignUpView, ClientViewSet
from .department_views import (
    DepartmentViewSet,
    DepartmentCommunicationViewSet,
)
from .communication_views import (
    CommunicationKindViewSet,
    CommunicationSourceViewSet,
    CommunicationViewSet,
)
from .custom_user_views import CustomUserViewSet
