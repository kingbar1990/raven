from django.contrib import admin

from .models.model_app_users import User
from .models.model_app_surgeries import Surgery
from tenant.utils import tenant_from_request, set_tenant_schema_for_request


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ["full_name", "email", "info"]

    def get_queryset(self, request, *args, **kwargs):
        set_tenant_schema_for_request(request)
        queryset = super().get_queryset(request, *args, **kwargs)
        tenant = tenant_from_request(request)
        queryset = queryset.filter(tenant=tenant)
        return queryset

    def save_model(self, request, obj, form, change):
        set_tenant_schema_for_request(request)
        tenant = tenant_from_request(request)
        obj.tenant = tenant
        super().save_model(request, obj, form, change)


@admin.register(Surgery)
class SurgeryAdmin(admin.ModelAdmin):
    fields = ["name"]

    def get_queryset(self, request, *args, **kwargs):
        set_tenant_schema_for_request(request)
        queryset = super().get_queryset(request, *args, **kwargs)
        tenant = tenant_from_request(request)
        queryset = queryset.filter(tenant=tenant)
        return queryset

    def save_model(self, request, obj, form, change):
        set_tenant_schema_for_request(request)
        tenant = tenant_from_request(request)
        obj.tenant = tenant
        super().save_model(request, obj, form, change)