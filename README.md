# RAVEN project

## Getting started

1. Inside the project folder create a hidden environment file called `.env`
   with <a href="#env-file">these contents</a>
2. Inside the project folder run in the console `docker-compose up`
3. Check if the `api-server` & `db-server` are up: `docker ps`.

### ENV file

```text
# generic
PYTHONUNBUFFERED=true

# for postgres
POSTGRES_DB=some_db_name
POSTGRES_USER=some_db_user
POSTGRES_PASSWORD=some_hard_password
```

### CLI

1. To access the DB: `docker-compose exec api-server python3 manage.py dbshell`
2. To run all tests: `docker-compose exec api-server python3 manage.py test`

### Multi tenant applications

1. Run migration: `docker-compose exec api-server python3 manage.py migrate`
2. Create a superuser: `docker-compose exec api-server python3 manage.py createsuperuser`
3. Set your tenant name to the get_tenants_map function in tenant/utils.py file
4. Implement your tenant schema: `docker-compose exec api-server python3 manage.py migrate_tenant_schemas`
5. Create a superuser from the console to your tenant_name: `docker-compose exec api-server python3 tenant_context_manage.py tenant_name createsuperuser`
6. Access the admin interface at `tenant_name.localhost:8000/admin`
