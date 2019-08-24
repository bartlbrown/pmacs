# Pmacs

## Installation

pmacs is available from the [pypi](https://pypi.org/project/pmacs/), use
```
pip install pmacs --user
```
to install/update.


## Development

1. Install [Anaconda](https://docs.conda.io/en/latest/) for your OS.
2. Clone pmacs
```
git clone https://github.com/bartlbrown/pmacs.git
```
3. Create a conda environment using the requirements file by running
```
conda create --name pmacs --file conda_environment.yml
```
4. Activate the environment
```
conda activate pmacs
```
5. Make sure you can run pmacs succesfully
```
cd pmacs/pmacs
python __main__.py
```