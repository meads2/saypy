from setuptools import setup, find_packages



setup(
    name='saypy',
    author='Matt Eads',
    version='0.0.1',
    description='A very pointless, yet very friendly Python package.',
    long_description_content_type="text/markdown",
    packages=find_packages(),
    tests_requires=['pytest'],
    entry_points={
        'console_scripts': ['saypy=saypy.__main__:main']
    }
)
