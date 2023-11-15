import os
import sys
import platform

# путь к проекту
sys.path.insert(0, '/home/c/ch36216/my_site/public_html/recipes')
# путь к фреймворку
sys.path.insert(0, '/home/c/ch36216/my_site/public_html/recipes/recipes')
# путь к виртуальному окружению
python_version = ".".join(platform.python_version_tuple()[:2])
sys.path.insert(0, f"/home/c/ch36216/my_site/venv/lib/python{python_version}/site-packages")
os.environ["DJANGO_SETTINGS_MODULE"] = "recipes.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()