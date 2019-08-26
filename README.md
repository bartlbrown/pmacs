# Pmacs

## Installation

1. Install Anaconda [(https://www.anaconda.com/distribution/)](https://www.anaconda.com/distribution/)
2. Create a new environment
```
conda create -n pmacs python=2.7
```
3. Activate the environment
```
conda activate pmacs
```
2. Install PyQt4 from the anaconda channel
```
conda install -c anaconda pyqt=4
```
3. pmacs is available from the Python Package Index [(https://pypi.org/project/pmacs/)](https://pypi.org/project/pmacs/). Install it using pip
```
pip install pmacs --user
```
4. Run pmacs
```
python -m pmacs
```
## Development

1. Install Anaconda [(https://www.anaconda.com/distribution/)](https://www.anaconda.com/distribution/).

2. Navigate to a convenent location and clone into pmacs by typing
```
git clone https://github.com/bartlbrown/pmacs.git
```
3. Create a conda environment using the conda environment file by running
```
conda create --name pmacs --file conda_environment.yml
```
4. Activate the environment
```
conda activate pmacs
```
5. Make sure you can run pmacs successfully
```
cd pmacs/pmacs
python __main__.py
```

## License

pmacs is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).