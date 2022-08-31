from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="fast-haversine",
    version="1.0",
    rust_extensions=[
        RustExtension("fast_haversine.fast_haversine", binding=Binding.PyO3)
    ],
    packages=["fast_haversine"],
    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False,
)
