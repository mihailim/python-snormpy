import os
from setuptools import setup
 
setup(name='snormpy',
    version="0.5.3",
    description='Wrapper around pysnmp4 for easier snmp querying',
    author='Dennis Kaarsemaker',
    author_email='dennis@kaarsemaker.net',
    py_modules=['snormpy'],
    url='http://github.com/LeaChimUK/python-snormpy',
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: System :: Monitoring",
        "Topic :: Software Development"
    ],
    #install_requires='pysnmp',
)
