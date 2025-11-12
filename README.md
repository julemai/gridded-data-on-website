# Displaying Gridded Data on a Website
Example code on how to display (large) gridded data on a website

## TiTiler Setup
This section discusses how to setup titiler, the main python module used to allow for dynamic tiling
### Localhost setup
#### 1. Install python modules
There are two python modules that need to be installed:
- [Uvicorn](https://pypi.org/project/uvicorn/0.20.0/) version 0.20.0
```
pip install uvicorn==0.20.0
```
- [TiTiler](https://pypi.org/project/titiler/0.22.1/) version 0.22.1
```
pip install titiler==0.22.1
```
#### 2. Set up main.py file
In the same file location as the html file which will display the grid dataset, create a main.py file that contains the following code:
```
from titiler.application.main import app
```
#### 3. Run uvicorn
In a python command prompt, run the following while in the same directory as the html file which will display the grid dataset: 
```
uvicorn titiler.application.main:app --host 0.0.0.0 --port 8000 --reload --proxy-headers --header "Access-Control-Allow-Origin:*"
```
To see if it is working, go to http://127.0.0.1:8000/. It should display the TiTiler home page. 
#### 4. Run localhost
In a python command prompt, run the following while in the same directory as the html file which will display the grid dataset: 
```
http.server 8080
```
Go to http://localhost:8080/index.html to see your website.

### Public server setup
Coming soon

## Geotiff to Cloud Optimized Geotiff
There are three main steps for getting from a typical Geotiff file to a coloured Cloud Optimized Geotiff (COG) file. 
#### 1. Setting nodata values and/or statistics
Notes:
- The nodata value only needs to be set one time. 
	- If it has previously been set for the geotiff files being used it is not necessary. 
- Calculating and setting statistics values are also optional.
	- It has no effect on creating COG files

