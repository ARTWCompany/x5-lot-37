from django_filters import FilterSet

from users.models import CustomUser


class CustomUserFilterSet(FilterSet):

    class Meta:
        model = CustomUser
        fields = ('email', 'name',)
