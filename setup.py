#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='snormpy',
    version='0.5.4',
    description='Wrapper around pysnmp4 for easier SNMP querying',
    author='Dennis Kaarsemaker, Mike Bryant, Mihai Limbășan',
    author_email='mihailim@users.noreply.github.com',
    url='https://github.com/mihailim/python-snormpy',
    download_url='https://github.com/mihailim/python-snormpy/releases',
    license='GPL3',
    keywords='snmp',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: System :: Monitoring',
        'Topic :: Software Development'
    ],
    package_dir={'': 'src'},
    py_modules=['snormpy'],
    install_requires=['pysnmp>=4.2.3', 'pysnmp-mibs'],
)
