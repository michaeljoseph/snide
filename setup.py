from setuptools import setup

import snide

setup(
    name=snide.__name__,
    version=snide.__version__,
    description='Snide: a remark.js parser in python',
    author='Michael Joseph',
    author_email='michaeljoseph@gmail.com',
    url=snide.__url__,
    packages=['snide'],
    package_dir={'snide': 'snide'},
    include_package_data=True,
    install_requires=[
        'markdown2 < 3.0.0',
    ],
    test_suite='nose.collector',
    license=open('LICENSE').read(),
)
