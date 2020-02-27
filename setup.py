from setuptools import setup

setup(
    name='towncrier',
    packages=['towncrier'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)