from setuptools import setup

setup(
    name="4devs",
    version='0.1',
    packages=['four_devs', 'four_devs.events', 'main'],
    install_requires=[
        'Click',
        "selenium==4.1.5",
        "python-decouple==3.6",
        "requests==2.27.1",
        "beautifulsoup4==4.11.1",
        "lxml==4.8.0",
        "unidecode==1.3.4"
    ],
    entry_points='''
        [console_scripts]
        4devs=main.main:start
    ''',
)
