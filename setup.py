import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aa_test_package", # Replace with your own username
    version="0.0.8",
    author="Finn Upham",
    author_email="finn.upham@gmail.com",
    description="A test package for activity analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/finn42/aa_test_package.git",
    packages=setuptools.find_packages(include=['activityanalysis_test', 'activityanalysis_test.*']),
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