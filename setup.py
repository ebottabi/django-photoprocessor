#/usr/bin/env python
import os
import sys
import photoprocessor

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if 'publish' in sys.argv:
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='django-photoprocessor',
    version=photoprocessor.__version__,
    description='Automated image processing for Django.',
    author='Jason Kraus',
    author_email='jasonk@cukerinteractive.com',
    license='BSD',
    url='http://github.com/cuker/django-photoprocessor/',
    packages=[
        'photoprocessor',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities'
    ]
)
