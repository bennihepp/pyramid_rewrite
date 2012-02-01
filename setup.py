import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()


setup(
    name='pyramid_rewrite',
    version='0.1',
    description='Small pyramid extension for rewriting urls',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    packages=find_packages(),
    install_requires=['pyramid>=1.3a6'],
    author='Benjamin Hepp',
    author_email='benjamin.hepp@gmail.com',
    license='BSD',
    url='https://github.com/bennihepp/pyramid_rewrite',
    keywords='pyramid rewrite pylons web',
)

