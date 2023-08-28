# Setup

## Host Environment

* [Node >= 16](https://nodejs.org/en)
* [Python >= 3.11](https://www.python.org/downloads/)
* [Git](https://gitforwindows.org/)

### Install

Follow the installation procedure for NodeJS, Python & Git depending on your operating system.

Create a directory for your project. Assuming **C:\Users\MyUser\Workspace\IlotDeChaleur\\**

### Clone the repository

open a terminal in the Projects folder

```bash
cd C:\Users\MyUser\Workspace\
```

clone the repository

```bash
git clone git@github.com:rtbfinfo/ilots-de-chaleur.git
```

or 

```bash
git clone https://github.com/rtbfinfo/ilots-de-chaleur.git
```
### Create the virual env

Go into the **ilot-de-chaleur** folder.

You should be in **C:\Users\MyUser\Workspace\ilot-de-chaleur** folder.


```bash
py -m venv .
```
*on windows*

```bash
python3 -m venv .
```
*on mac or linux*

**Activate the virtual env**

```bash
Scripts\activate.bat
```
*on widnows*

```bash
source bin/activate
```
*on mac or linux*

### Install all needed libraries

```bash
py -m pip install notebook rasterio pandas geopandas matplotlib
```
*on windows*

```bash
python3 -m pip install notebook rasterio pandas geopandas matplotlib
```
*on mac or linux*

## Running the environment

```bash
jupyter notebook
```

Then you can navigate to th "récolte-data" folder and run the notebook: http://localhost:8888/notebooks/r%C3%A9colte-data/2-centroid-temperature.ipynb.ipynb

### Python Notebook

### Web Server

