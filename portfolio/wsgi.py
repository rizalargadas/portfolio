from whitenoise import WhiteNoise
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

application = get_wsgi_application()

application = WhiteNoise(application, root=os.path.join(
    os.path.dirname(os.path.dirname(__file__)), 'media'), prefix='/media/')
