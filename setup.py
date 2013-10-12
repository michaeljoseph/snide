import re
from setuptools import setup

init_py = open('snide/__init__.py').read()
metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", init_py))
metadata['doc'] = re.findall('"""(.+)"""', init_py)[0]

setup(
    name='snide',
    version=metadata['version'],
    description=metadata['doc'],
    author=metadata['author'],
    author_email=metadata['email'],
    url=metadata['url'],
    packages=['snide'],
    include_package_data=True,
    install_requires=[
        'markdown2 < 3.0.0',
    ],
    test_suite='nose.collector',
    license=open('LICENSE').read(),
)
