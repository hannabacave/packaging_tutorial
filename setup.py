from setuptools import setup
from biketrauma import __version__ as current_version

setup(
  name='biketrauma',
  version=current_version,
  description='Visualization of a bicycle accident db',
  url='https://github.com/hannabacave/packaging_tutorial',
  author='hannabacave',
  author_email='hannabacave@gmail.com',
  license='MIT',
  packages=['biketrauma','biketrauma.io', 'biketrauma.preprocess', 'biketrauma.vis'],
  zip_safe=False
)