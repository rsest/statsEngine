#! /usr/bin/env python

import setuptools

from statistics import __version__ as version

description = 'Python Statistical Engine.'

setuptools.setup(
        name='statsEngine',
        version=version,
        description='{0}'.format(description),
        author='Rodrigo Sestari',
        url='https://github.com/rsest/statsEngine',
        packages=['statsEngine'],
        license='MIT',
        classifiers=[
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.6',
        ],
)