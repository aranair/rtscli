from setuptools import setup

setup(
    name='rtscli',
    version='0.3.1',
    description='A realtime stocks ticker that runs in CLI',
    url='http://github.com/aranair/rtscli',
    author='Boa Ho Man',
    author_email='boa.homan@gmail.com',
    license='MIT',
    install_requires=[
        'urwid',
        'HTMLParser',
        'simplejson',
        ],
    zip_safe=False,
    py_modules=['rtscli'],
    entry_points={
        'console_scripts': [
            'rtscli = rtscli:cli'
        ]
    },
)
