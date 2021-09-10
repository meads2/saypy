from setuptools import setup, find_packages



setup(
    name='saypy',
    author='Matt Eads',
    description='A very pointless, yet very friendly Python package.',
    packages=find_packages(),
    tests_requires=['pytest'],
    entry_points={
        'console_scripts': ['saypy=saypy.__main__:main']
    }
)
