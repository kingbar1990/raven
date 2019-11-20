from rest_framework import viewsets

from core.models.model_app_surgeries import Surgery
from .serializers import SurgerySerializer
from tenant.utils import set_tenant_schema_for_request, tenant_from_request


class SurgeryViewSet(viewsets.ModelViewSet):
    queryset = Surgery.objects.all()
    serializer_class = SurgerySerializer

    def get_queryset(self):
        set_tenant_schema_for_request(self.request)
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)

    def destroy(self, request, *args, **kwargs):
        set_tenant_schema_for_request(self.request)
        surgery = Surgery.objects.get(pk=self.kwargs["pk"])
        return super().destroy(request, *args, **kwargs)