import setuptools

with open('requirements.txt', 'r') as f:
    reqs = f.readlines()
reqs = list(map(lambda x: x.strip(), reqs))

pip_requirements = reqs

setuptools.setup(
    name="power-aligner",
    version="1.0.0",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=pip_requirements,
    include_package_data=True
)