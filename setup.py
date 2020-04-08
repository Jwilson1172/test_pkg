import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="testpkgjwilson",
    version="0.0.2",
    author="Joseph Wilson",
    author_email="jw59615@gmail.com",
    description="placeholder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/______",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Free for non-commercial use",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
