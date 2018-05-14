from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ety',
    version='0.0.0',
    description='find the etymological origins of a word',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jmsv/ety-python',
    author='James Vickery',
    author_email='dev@jamesvickery.net',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='etymology origins english language words',
    packages=['ety'],
    extras_require = {
        'dev': ['flake8'],
    },
    package_data={
        'ety': ['package_data.dat'],
    },
    entry_points={
        'console_scripts': [
            'ety=ety:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/jmsv/ety-python/issues',
        'Source': 'https://github.com/jmsv/ety-python',
    },
)
