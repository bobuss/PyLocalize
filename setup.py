try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Very useless HTTP localization service',
    'author': 'Bertrand Tornil',
    'version': '0.1',
    'install_requires': ['Bottle', 'GeoIP'],
    'packages': ['py_localize'],
    'scripts': ['python localize/app.py'],
    'name': 'py_localize'
}

setup(**config)