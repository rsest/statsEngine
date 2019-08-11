#! /usr/bin/env python

import setuptools

from statisticEngine import __version__ as version

description = 'Python Statistical Engine.'

setuptools.setup(
    name='statisticEngine',
    version=version,
    description='{0}'.format(description),
    author='Rodrigo Sestari',
    url='https://github.com/rsest/statsEngine',
    packages=['statisticEngine'],
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
    ], install_requires=["numpy == 1.17.0",
                         "pandas == 0.24.0",
                         "scipy == 1.3.1",
                         "matplotlib == 3.1.1",
                         "plotly == 4.1.0"],
)
