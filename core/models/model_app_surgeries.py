from django.db import models

from tenant.models import TenantAwareModel


class Surgery(TenantAwareModel):
    name = models.CharField(max_length=200, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Surgeries"