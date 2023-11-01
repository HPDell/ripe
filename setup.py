from setuptools import setup, find_packages

setup(
    name='ripe',
    author='HPDell',
    version='0.1.0',
    description='A cli tool for managing R packages',
    packages=find_packages(where='ripe'),
    entry_points={
        'console_scripts': [
            'rip = ripe:main'
        ]
    }
)
