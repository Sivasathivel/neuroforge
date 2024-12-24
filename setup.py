from setuptools import setup, find_packages

setup(
    name="neuroforge",
    version="0.1.0",
    author="Sivasathivel",
    description="Modular AI Framework for Community and Enterprise",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/neuroforge",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        # Add required dependencies here
    ],
)
