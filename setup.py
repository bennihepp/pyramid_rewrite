from setuptools import setup, find_packages
setup(
    name = 'pyramid_rewrite',
    version = '0.1',
    packages = find_packages(),
    install_requires = ['pyramid>=1.3a6'],
    author = 'Benjamin Hepp',
    author_email = 'benjamin.hepp@gmail.com',
    license = 'BSD',
    keywords = 'pyramid rewrite',
)

