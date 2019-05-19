from distutils.core import setup

setup(
    name='pysnake',
    version='1.0',
    author='Carlos Porta',
    author_email='cmaciasporta@gmail.com',
    description=open('README.md').read(),
    long_description=open('README.md').read(),
    py_modules=['pysnake.cli', 'pysnake.game'],
    license='BSD',
    extras_require={'pysnake.cli': 'readchar'}
)
