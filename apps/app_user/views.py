from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from core.models.model_app_users import User
from .serializers import UserSerializer
from tenant.utils import tenant_from_request, set_tenant_schema_for_request


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        set_tenant_schema_for_request(self.request)
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)

    def destroy(self, request, *args, **kwargs):
        set_tenant_schema_for_request(self.request)
        user = User.objects.get(pk=self.kwargs["pk"])
        return super().destroy(request, *args, **kwargs)