import subprocess

# Path to GDAL executable
gdaldem_exe = "path_to_gdaldem_executable" # On windows, if QGIS is installed, this is typically located in C:/Program Files/bin

# File paths
cog_file = "file_path_to_cog_file_from_step_01"
colour_txt_file = "file_path_to_text_file_with_colour_information" # See 02a_colours.txt for an example
colour_file = "file_path_to_coloured_cog_file_from_output"

# Convert
subprocess.run([
    gdaldem_exe,
    "color-relief",
    cog_file,
    color_txt_file,
    color_file,
    "-co", "COMPRESS=LZW",
    "-alpha",
    "-nearest_color_entry"
    # "-exact_color_entry"
], check=True)
