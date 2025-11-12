import rasterio

input_file = "path_to_input_geotiff_file"
with rasterio.open(input_file, 'r+') as src:
    band = 1
    data = src.read(band).astype(float)

    # Replace invalid NoData values if necessary
    data[data == -3.4e+38] = np.nan  # or whatever NoData value you want
	
    # Set NoData value
    src.nodata = -3.4e+38

    # Compute statistics
    min_val = np.nanmin(data)
    max_val = np.nanmax(data)
    mean_val = np.nanmean(data)
    std_val = np.nanstd(data)

    # Set band description
    src.set_band_description(band, "layer")

    # Set statistics metadata
    src.update_tags(
        band,
        STATISTICS_MINIMUM=float(min_val),
        STATISTICS_MAXIMUM=float(max_val),
        STATISTICS_MEAN=float(mean_val),
        STATISTICS_STDDEV=float(std_val)
    )
    data_to_write = np.where(np.isnan(data), -3.4e+38, data)
    src.write(data_to_write, band)

