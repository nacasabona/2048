from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    

setup(
    packages=find_packages(),
    name='2048',
    version='0.01',
    install_requires=requirements,
    url='https://github.com/nacasabona/2048',
    python_requires='>=3.7',
    license='MIT',
    author='Nicolás Casabona and Juan Schandin',
    author_email='n.a.casabona@gmail.com, juan.schandin@filo.uba.ar',
    description='2048 Clone'
)