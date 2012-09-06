# coding=utf-8
"""Python packaging."""
import os
from setuptools import setup


def read_relative_file(filename):
    """Returns contents of the given file, which path is supposed relative
    to this module."""
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


NAME = 'django-js-error-hook'
README = read_relative_file('README.rst')
VERSION = read_relative_file('VERSION').strip()
PACKAGES = ['django_js_error_hook']
REQUIRES = ['django>=1.4']


setup(name=NAME,
      version=VERSION,
      description='Generic handler for hooking client side javascript error.',
      long_description=README,
      classifiers=['Development Status :: 1 - Planning',
                   'License :: OSI Approved :: BSD License',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 2.6',
                   'Framework :: Django',
                   ],
      keywords='class-based view, generic view, js error hooking',
      author='Jonathan Dorival',
      author_email='jonathan.dorival@novapost.fr',
      url='https://github.com/jojax/%s' % NAME,
      license='BSD',
      packages=PACKAGES,
      include_package_data=True,
      zip_safe=False,
      install_requires=REQUIRES,
      )
