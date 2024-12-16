from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

extra_compile_args = ['-fopenmp']
extra_link_args = ['-fopenmp']

extensions = [
    Extension(
        "vector",
        ["vector.pyx"],
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args,
        include_dirs=[np.get_include()] 
    )
]

setup(
    ext_modules = cythonize(extensions, language_level="3", annotate=True),
)
