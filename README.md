# Displaying Gridded Data on a Website
Example code on how to display (large) gridded data (TIFF files) on a website.

## TiTiler Setup
This section discusses how to setup titiler, the main python module used to allow for dynamic tiling.
### Localhost setup
#### 1. Install python modules
There are two python modules that need to be installed:
- [Uvicorn](https://pypi.org/project/uvicorn/0.20.0/) version **0.20.0**
	- ```	
	  pip install uvicorn==0.20.0
	  ```
- [TiTiler](https://pypi.org/project/titiler/0.22.1/) version **0.22.1**
	- ```
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

Python code found in supplementary_files.\
Notes:
- Requires at least gdal version 3.1
- Based off this gdal command: 
	```
	gdal_translate input_file cog_file -of COG -co COMPRESS=LZW -co RESAMPLING=NEAREST -co TILING_SCHEME=GoogleMapsCompatible -co BLOCKSIZE=512
	```
	- input_file is the input file as an absolute path.
	- output_file is the output file as an absolute path. It must be a new file, you cannoted override the input file.
	- -of COG converts it into a COG file.
	- -co COMPRESS=LZW decides the compression algorithm (LZW is desired).
	- -co RESAMPLING=NEAREST decides the resampling method.
		- NEAREST preserves values but may slightly shift pixels (unnoticable amount).
		- BILINEAR preserves pixel location but values will change due to the method taking averages of an area.
		- NEAREST is typically desired as preserving values is more valuable.
	- -co TILING_SCHEME=GoogleMapsCompatible puts the file in ESPG:3857 and tweaks other attributes as needed. This is desirable for web hosting.
	- -co BLOCKSIZE=512 sets the amount of pixels per block. 512 is desired for its speed.
	- For more information on gdaltranslate see documentation [here](https://gdal.org/en/stable/programs/gdal_translate.html).

#### 02. Converting COG to Coloured COG
Python code found in supplementary_files.\
Notes:
- Requires at least gdal version 3.1.
- Based off this gdal command:
	```
	gdaldem color-relief cog_file colour_txt_file colour_file -co COMPRESS=LZW -nearest_color_entry -alpha 
	```
	- color-relief generates a colour relief map.
	- cog_file is the file output from step 01. 
	- colour_txt_file is a .txt file that contains value and RGB infomation. An example file can be found in supplementary_files and more information found below. 
	- colour_file is the outputed coloured COG file. This is the file that will be displayed on the website. It must be a new file, you cannoted override the input file.
	- -co COMPRESS=LZW decides the compression algorithm (LZW is desired).
	- -nearest_color_entry interpolates the colour value to assign points based off the colour_txt_file.
		- -exact_color_entry picks the closest value provided and uses the colour directly corresponding to it. 
	- -alpha makes any NoData values transparent and uses the final column of the colour_txt_file as alpha values. More information below.
	- For more information on gdaldem color-relief see documentation [here](https://gdal.org/en/stable/programs/gdaldem.html#color-relief).
- Colour_txt_file information
	- For example: 
		- ```
		  -1 50 50 50 255
		  0 75 75 75 255
		  1 100 100 100 255
		  2 125 125 125 255
		  nv 0 0 0 0
		  ```
	- Each row in the text file represents "value red green blue [alpha]". The alpha column will have significance when -alpha is used during creation.
		- Where "red green blue [alpha]" are values between 0 and 255.
		- Value represents which values adopt the RGBA colours.
	- The final row "nv 0 0 0 0" indicates "no value" points should be transparent 
- *IMPORTANT:* In the new file this step creates, the values of all the pixels will represent their RGBA values and will lose their orignal value.

## Displaying On Website Using Leaflet
Examples of the html and javascript required to display the gridded datasets can be found in this repository. The html file simply called "index.html", and the javascript file found under "javascript/grid_webpage.js"

