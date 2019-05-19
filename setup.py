from distutils.core import setup

setup(
    name='pysnake',
    version='1.0',
    packages=['pysnake'],
    license='BSD',
    long_description_content_type='text/markdown',
    package_dir={'pysnake': 'pysnake'},
    long_description=open('README.md').read(),
    extras_require={'readchar'}
)
