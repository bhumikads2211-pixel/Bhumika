from django.core.wsgi import get_wsgi_application
from vercel_wsgi import handle
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loginmodules.settings')

application = get_wsgi_application()
app = handle(application)
