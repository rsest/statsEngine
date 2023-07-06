#! /usr/bin/env python

import setuptools

description = 'Python Statistical Engine.'

setuptools.setup(
    install_requires=["numpy==1.17.1",
                      "pandas==0.24.0",
                      "scipy==1.10.0",
                      "matplotlib==3.1.1",
                      "plotly==4.1.0"],
    name='statisticEngine',
    version='0.0.1',
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
    ]
)
