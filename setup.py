import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="etime", 
    version="0.4",
    author="Amaljith kuttamath",
    author_email="kuttamath.amaljith@gmail.com",
    description="A simple package to calculate the execution time of certain lines of code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amaljithkuttamath/exectime",
    download_url = "https://github.com/amaljithkuttamath/exectime/archive/0.4.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)