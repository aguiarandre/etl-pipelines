# USAGE:

## Install cookiecutter if you don't have it.

> `pip install cookiecutter`

## To start a new project run:

> `cookiecutter https://github.com/aguiarandre/etl-pipelines`

for unix users or 

> `cookiecutter.exe https://github.com/aguiarandre/etl-pipelines`

for windows users.


This will create a file organization in the following structure:

Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── intermediate   <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        ├── client.py      <- Any external connection (via API for example) should be written here    
        ├── params.py      <- All parameters of the execution
        ├── pipeline.py    <- The ETL (extract-transform-load) pipeline itself containing the sequence of nodes
        │
        └── nodes          <- Scripts to containing each step of the ETL process.
             ├── data_preparation.py
             ├── data_gathering.py
             ├── data_transform.py
             ├── data_sotrage.py
             └── data_visualization.py
         
--------

## General Structure

The general idea is to centralize all steps of the pipeline in the nodes directory (submodule), the parameters in the `params.py` file, the connection in the `client.py` file and the pipeline itself on the `pipeline.py` file. 
Always specify (in `params.py`) files to be downloaded, uploaded or cached in the `data` folder. 

## Documentation

The initial documentation is also already updated. One can create the documentation by entering docs and typing: 
> `./make.bat`
for windows users and 
> `./make` 
for unix users. 

Also, to run the documentation as is, you'll have to install a requirement. To do that, just type 

> `pip install -r requirements.txt`
