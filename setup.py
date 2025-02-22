import os
from setuptools import setup, find_packages

setup(
    name='carma',
    version='0.0.4',
    license='MIT',
    author='Zeio Nara',
    author_email='zeionara@gmail.com',
    packages=find_packages(),
    description='Cli tool for managing cloud mail.ru storage',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/zeionara/karma',
    project_urls={
        'Documentation': 'https://github.com/zeionara/karma#readme',
        'Bug Reports': 'https://github.com/zeionara/karma/issues',
        'Source Code': 'https://github.com/zeionara/karma'
    },
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11"
    ],
    install_requires = ['click', 'requests'],
    package_data={
        '': [
            'api_config.json'
        ]
    },
    include_package_data=True
)
