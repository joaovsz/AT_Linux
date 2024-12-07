from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("vector.pyx", language_level="3", annotate=True)
)

