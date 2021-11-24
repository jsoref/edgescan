from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='edgescan',
    version='0.1.0',
    author='Tyler Fisher',
    author_email='tylerfisher@tylerfisher.ca',
    description="An API client for EdgeScan",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        'Topic :: Security',
    ],
    packages=find_packages(),
    install_requires=[],
)