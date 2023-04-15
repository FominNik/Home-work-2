from setuptools import setup, find_packages

setup(
    name="clean_folder_user_unique_package_2",
    version="0.1.0",
    description="Script sorts files in folders and removes empty folders",
    author="Nik",
    author_email="nekit4minfn@gmail.com",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=[],
    python_requires=">=3.5",
    entry_points={
        "console_scripts": [
            "clean-folder=clean_folder.clean:main",
        ],
    },
)
