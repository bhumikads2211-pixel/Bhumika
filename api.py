import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loginmodules.settings')

app = get_wsgi_application()
handler = app  # expose 'handler' as expected by Vercel
