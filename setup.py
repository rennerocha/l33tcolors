from setuptools import setup

setup(
    name='l33tcolors',
    version='0.1',
    author='Renne Rocha',
    author_email='renne@rennerocha.com',
    description=('Provides a list of valid HTML colors in L33T speak.'),
    license='Beerware',
    keywords='l33t',
    url='https://github.com/rennerocha/l33tcolors',
    py_modules=['l33tcolors'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        l33tcolors=src:l33tcolors
    ''',
)
