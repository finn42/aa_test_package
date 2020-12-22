import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aa_test_package", # Replace with your own username
    version="0.0.1",
    author="Finn Upham",
    author_email="finn.upham@gmail.com",
    description="A tess package for activity analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/finn42/aa_test_package.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)