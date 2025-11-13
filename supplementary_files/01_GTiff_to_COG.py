import subprocess

# Path to GDAL executable
gdal_translate_exe = "path_to_gdal_translate" # On windows, if QGIS is installed, this is typically located in C:/Program Files/bin

# File paths
input_file = "input_file_path"
cog_file = "output_file_path"

# Convert to COG
subprocess.run([
    gdal_translate_exe,
    input_file,
    cog_file,
    "-of", "COG",
    "-co", "COMPRESS=LZW",
    "-co", "RESAMPLING=NEAREST",
    "-co", "TILING_SCHEME=GoogleMapsCompatible",
    "-co", "BLOCKSIZE=512",
], check=True)
