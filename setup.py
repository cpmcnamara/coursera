"""
Setup configuration for the Agentic BOM Engineering book repository.
"""
from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='agentic-bom-engineering-medtech',
    version='0.1.0',
    author='cpmcnamara',
    description='A pragmatic, engineering-first book on applying agentic automation to Bill of Materials (BOM) management and engineering change in medical technology organizations.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cpmcnamara/coursera',
    packages=find_packages(exclude=['tests*']),
    python_requires='>=3.8',
    install_requires=[
        'markdown>=3.4.4',
    ],
    extras_require={
        'dev': [
            'pytest>=7.4.3',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Documentation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
