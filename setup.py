import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pmacs',
    version='0.0.1',
    author='Barton L. Brown',
    author_email='bartonlbrown@gmail.com',
    license="License :: OSI Approved :: MIT License",
    description='Python editing MACroS',
    long_description_content_type="text/markdown",
    url='https://github.com/bartlbrown/pmacs',
    python_requires='==2.7',
    install_requires=[
        'PyQt4',
      ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
