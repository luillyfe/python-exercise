from setuptools import setup, find_packages


setup(
    name='python_exercise',
    version='1.0.0',
    author="Fermin Blanco",
    author_email="luillyfe89@gmail.com",
    maintainer='https://github.com/ModusCreateOrg',
    license='MIT',
    url='https://github.com/ModusCreateOrg/python-exercise',
    package_dir={'': 'src'},
    include_package_data=True,
    packages=find_packages('src'),
    install_requires = [
    ],
    entry_points={
        'console_script': [
            'python-exercise = python_exercise.__main__:main'
        ]
    }
)
