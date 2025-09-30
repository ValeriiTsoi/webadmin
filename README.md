# webadmin

Django-based user admin GUI + separate Auth (FastAPI/JWT), containerized, deploy via Helm/Terraform to k3s.

## Local run

```powershell
docker compose build
docker compose up -d
docker compose exec webadmin python manage.py migrate
docker compose exec webadmin python manage.py createsuperuser
# http://localhost:33333  -> {"status":"ok"}
# http://localhost:33333/admin
