import os
import setuptools

with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf8") as readme:
    README = readme.read()

setuptools.setup(
    name="django-sass-compiler",
    version="1.1.0",
    author="Jacek B. Budzynski",
    author_email="jacek.b.budzynski@gmail.com",
    url="https://github.com/jaberbu/django-sass-compiler",
    description="Simplify the use of Sass in Django.",
    long_description=README,
    long_description_content_type="text/markdown",
    license="BSD license",
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=[
        "django",
        "libsass"
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: Spanish",
        "Natural Language :: Polish",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Framework :: Django",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 3.0",
        "Environment :: Web Environment",
    ],
)
