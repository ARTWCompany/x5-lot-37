from .client_serializers import (
    ClientSerializer,
    ClientCreateSerializer,
)
from .auth_serializer import LogInSerializer
from .department_serializers import (
    DepartmentSerializer,
    DepartmentCommunicationSerializer,
)
from .comminication_serializers import (
    CommunicationKindSerializer,
    CommunicationSourceSerializer,
    CommunicationSerializer,
    CommunicationBookingSerializer
)
from .custom_user_serializers import (
    CustomUserSerializer,
    CustomUserCommunicationSerializer,
)
