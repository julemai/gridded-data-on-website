# Displaying Gridded Data on a Website
Example code on how to display (large) gridded data on a website.

## TiTiler Setup
This section discusses how to setup titiler, the main python module used to allow for dynamic tiling.
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
Coming soon.

## Geotiff to Cloud Optimized Geotiff
There are two main steps for getting from a typical Geotiff file to a coloured Cloud Optimized Geotiff (COG) file, and one optional step. 
#### 00. Setting nodata values and/or statistics
Code found in supplementary_files\
Notes:
- The nodata value only needs to be set one time. 
	- If it has previously been set for the geotiff files being used it is not necessary. 
- Calculating and setting statistics values are also optional.
	- It has no effect on creating COG files.
- This step is where any processing with the values of the data should be performed (i.e. calculating deciles).

#### 01. Converting Geotiff to COG

Code found in supplementary_files\
Notes:
- Requires at least gdal version 3.1
- Based off this gdal command: 
	```
	gdal_translate input_file cog_file -of COG -co COMPRESS=LZW -co RESAMPLING=NEAREST -co TILING_SCHEME=GoogleMapsCompatible -co BLOCKSIZE=512
	```
	- input_file is the input file as an absolute path
	- output_file is the output file as an absolute path
	- -of COG converts it into a COG file
	- -co COMPRESS=LZW decides the compression algorithm (LZW is desired)
	- -co RESAMPLING=NEAREST decides the resampling method
		- NEAREST preserves values but may slightly shift pixels (unnoticable amount)
		- BILINEAR preserves pixel location but values will change due to the method taking averages of an area
		- NEAREST is typically desired as preserving values is more valuable
	- -co TILING_SCHEME=GoogleMapsCompatible puts the file in ESPG:3857 and tweaks other attributes as needed. This is desirable for web hosting.
	- -co BLOCKSIZE=512 sets the amount of pixels per block. 512 is desired for its speed
