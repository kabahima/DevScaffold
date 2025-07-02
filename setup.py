from setuptools import setup, find_packages

setup(
    name='devsetup',
    version='1.0.0',
    description='Cross-platform CLI dev setup tool',
    packages=find_packages(),
    install_requires=[
        'questionary',
        'rich',
    ],
    entry_points={
        'console_scripts': [
            'devsetup=devsetup.cli:main'
        ],
    },
)
