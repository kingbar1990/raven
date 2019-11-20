from django.contrib.postgres.fields import JSONField
from django.db import models

from tenant.models import TenantAwareModel


class User(TenantAwareModel):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    info = JSONField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.full_name, self.email)