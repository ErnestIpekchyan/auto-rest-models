import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="auto-rest-models",
    version="0.0.1",
    author="Ernest Ipekchyan",
    author_email="ghost199632@gmail.com",
    description="Provides automatic REST API for models in Django project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ErnestIpekchyan/auto-rest-models",
    packages=setuptools.find_packages(exclude=['tests*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
