from setuptools import setup, find_packages
from setuptools.extension import Extension
from codecs import open
from os import path
import os
import platform

from Cython.Build import cythonize

# Determine base path
here = path.abspath(path.dirname(__file__))

# Load README as long description
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Helper to extract version
def get_version():
    for line in open(os.path.join(os.path.dirname(__file__), 'PyRuSH', '__init__.py')).read().splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")

# Compiler directives for Cython
COMPILER_DIRECTIVES = {
    "language_level": 3,
    "embedsignature": True,
    "annotation_typing": False,
}

# Adjust compile flags based on OS
if platform.system() == 'Windows':
    extra_compile_args = ["/std:c++14"]
else:
    extra_compile_args = ["-std=c++11"]

# Include directories for compilation
dir_path = path.dirname(path.realpath(__file__))
include_dirs = [dir_path + "/PyRuSH", dir_path]

# Cython extension modules
extensions = [
    Extension(
        'PyRuSH.StaticSentencizerFun',
        sources=['PyRuSH/StaticSentencizerFun.pyx'],
        include_dirs=include_dirs,
        language='c++',
        extra_compile_args=extra_compile_args,
    )
]

# Final setup
setup(
    name='PyRuSH',
    version=get_version(),
    description='A fast implementation of RuSH (Rule-based sentence Segmenter using Hashing).',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Jianlin',
    author_email='jianlinshi.cn@gmail.com',
    url='https://github.com/killerexcipio/PyRuSH-alt',
    packages=find_packages(),
    python_requires='>=3.6, <3.13',
    install_requires=[
        "jpype1>=1.4.1",
        "spacy>=3.0"
    ],
    ext_modules=cythonize(extensions, compiler_directives=COMPILER_DIRECTIVES),
    package_data={
        '': ['*.pyx', '*.pxd', '*.so', '*.dll', '*.lib', '*.cpp', '*.c',
             '../conf/rush_rules.tsv', '../requirements.txt']
    },
    zip_safe=False,
    include_package_data=True,
    license='Apache License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
    ],
)
