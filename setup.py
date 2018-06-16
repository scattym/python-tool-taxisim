from setuptools import setup, find_packages

setup(
      name='taxisim',
      version='1.0.dev0',
      description=('Project to simulate taxi meter devices.'),
      url='https://bitbucket.org/mjclark1/python-tool-taxisim.git',
      author='Matt Clark',
      author_email='mattjclark0407@hotmail.com',
      license='Copyright (C) Matthew Clark - All Rights Reserved',
      scripts=[
            'scripts/taxisim',
      ],
      packages=find_packages(),
      install_requires=[
            'serial',
      ],
      zip_safe=False
)
