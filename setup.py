import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aa_test_package", # Replace with your own username
    version="0.0.2",
    author="Finn Upham",
    author_email="finn.upham@gmail.com",
    description="A tess package for activity analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/finn42/aa_test_package.git",
    package_dir={'': 'example_pkg'},
    packages=setuptools.find_packages(where='example_pkg'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)