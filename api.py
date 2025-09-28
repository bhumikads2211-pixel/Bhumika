import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loginmodules.settings')

def handle(event, context):
    application = get_wsgi_application()
    return application(event, context)
