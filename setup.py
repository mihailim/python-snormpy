import os
from setuptools import setup
 
setup(name='snormpy',
    version="0.5.3",
    description='Wrapper around pysnmp4 for easier snmp querying',
    author='Dennis Kaarsemaker, Mike Bryant, Mihai Limbășan',
    author_email='mihailim@users.noreply.github.com',
    py_modules=['snormpy'],
    url='https://github.com/mihailim/python-snormpy',
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: System :: Monitoring",
        "Topic :: Software Development"
    ],
    #install_requires='pysnmp',
)
