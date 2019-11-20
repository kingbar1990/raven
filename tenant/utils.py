from django.db import connection

from .models import Tenant

# Set your tenant name
def get_tenants_map():
    tenants = {
        "raven.localhost": "raven",
        
    }
    return tenants

def hostname_from_request(request):
    return request.get_host().split(':')[0].lower()

def tenant_from_request(request):
    hostname = hostname_from_request(request)
    subdomain_prefix = hostname.split('.')[0]
    return Tenant.objects.filter(subdomain_prefix=subdomain_prefix).first()

def tenant_schema_from_request(request):
    hostname = hostname_from_request(request)
    tenants_map = get_tenants_map()
    return tenants_map.get(hostname)

def set_tenant_schema_for_request(request):
    schema = tenant_schema_from_request(request)
    with connection.cursor() as cursor:
        cursor.execute(f"SET search_path to {schema}")