from setuptools import setup

setup(
    name='corgi',
    version='0.1',
    description='Stock Ticker',
    url='http://github.com/aranair/corgi',
    author='Boa Ho Man',
    author_email='boa.homan@gmail.com',
    license='MIT',
    install_requires=[
        'urwid',
        'HTMLParser',
        'simplejson',
        ],
    zip_safe=False,
    py_modules=['corgi'],
    entry_points={ 'console_scripts': ['corgi=corgi:cli'] },
)
