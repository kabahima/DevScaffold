from setuptools import setup, find_packages

setup(
    name='devsetup',
    version='0.1',
    py_modules=['devsetup'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=['questionary', 'rich'],
    entry_points='''
        [console_scripts]
        devsetup=devsetup.cli:main
    ''',
)
