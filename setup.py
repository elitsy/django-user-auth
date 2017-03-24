import os

from setuptools import setup, find_packages

version = __import__('user_auth').get_version()


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_requires_list(filename):
    s = open(filename).read().split("\n")
    dependenses = []
    if len(s):
        for pkg in s:
            if pkg.strip() == '' or pkg.startswith("#"):
                continue
            if pkg.startswith("-e"):
                continue
                try:
                    p = pkg.split("#egg=")[1]
                    dependenses += [p, ]
                except:
                    continue
            else:
                dependenses += [pkg, ]
    return dependenses


setup(
    name='django-user-auth',
    version=version,
    description="user auth application for django",
    long_description=read('README.rst'),
    keywords="user, auth",
    author="Alex Kamedov",
    author_email="alex@kamedov.ru",
    url='https://github.com/elitsy/django-user-auth',
    license="New BSD License",
    platforms=["any"],
    classifiers=["Development Status :: 4 - Beta",
                   "Environment :: Web Environment",
                   "Framework :: Django",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Utilities"],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=get_requires_list('requirements.txt'),
)
