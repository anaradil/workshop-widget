from __future__ import unicode_literals

from setuptools import setup, find_packages


setup(
    name='fedora-hubs-workshop-widget',
    version='0.0.1',
    description='An example widget for Fedora Hubs',
    long_description="This example widget is used in the Hubs widget workshop.",
    author='Aurelien Bompard',
    author_email='abompard@fedoraproject.org',
    url="https://pagure.io/fedora-hubs-widget-workshop",
    download_url="https://pagure.io/fedora-hubs-widget-workshop",
    license='AGPLv3+',
    install_requires=[
        "fedora-hubs",
	"python-bugzilla"
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
