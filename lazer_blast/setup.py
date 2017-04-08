from setuptools import setup, find_packages

with open('README.md', 'r') as fin:
    readme = fin.read()

setup(
    name='lazer_blast',
    version='0.0.0',
    description='A 2D game for our CPS410 class',
    long_description=readme,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': [
            'lazerblast = lazer_blast.driver:main',
        ],
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
