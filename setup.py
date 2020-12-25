from os.path import basename, splitext
from setuptools import find_packages, setup

README_PATH = "README.md"

setup(
    name = 'renkler',
    packages = ['.'],
    version = '0.0.1',
    license="MIT License",
    description = 'pythonla kullanılmak için hazirlanmış türkçe terminal renkleri',
    author = 'Berkay Küçük',
    author_email = 'berkay@berkaykucuk.com.tr',
    url = 'https://github.com/bksec/renkler',
    zip_safe=False,
    keywords = ['renkler', 'colours','renk'],
    classifiers = [],
)