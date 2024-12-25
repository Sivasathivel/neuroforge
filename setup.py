from setuptools import setup, find_packages

setup(
    name="neuroforge",  # Framework name
    version="0.1.0",  # Initial version
    author="Sivasathivel",
    author_email="sivasathivel@yahoo.com",  # Your email
    description="Modular AI Framework for Community and Enterprise",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Sivasathivel/neuroforge",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.19.2",
        "pytest>=6.2.4",
        # Add other dependencies here
    ],
    extras_require={
        "enterprise": [
            "torch>=1.9.0",  # Example dependency for Enterprise features
            "tensorflow>=2.4.0",
        ]
    },
    include_package_data=True,
    license="NeuroForge Non-Commercial License (NNCL)",  # License type
    project_urls={
        "Documentation": "https://github.com/Sivasathivel/neuroforge/docs",
        "Source Code": "https://github.com/Sivasathivel/neuroforge",
        "Bug Tracker": "https://github.com/Sivasathivel/neuroforge/issues",
        "License": "https://github.com/Sivasathivel/neuroforge/blob/main/LICENSE",
    },
)
