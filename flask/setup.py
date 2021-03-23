from setuptools import setup, find_packages

setup(
    name='flaskapi',
    author='Bjoern Winkler',
    description='A flask API example app',
    packages=['flaskapi'],
    # packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
