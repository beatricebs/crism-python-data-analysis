import rasterio
from affine import Affine


def save_rgb_geotiff(
    RGB,
    output_path='visual/rgb.tif',
    px_x=None,
    px_y=None,
    x_ul=None,
    y_ul=None,
    crs_wkt=None
):
    # dimensions
    height, width = RGB.shape[:2]

    # transform
    transform = Affine(px_x, 0, x_ul, 0, -px_y, y_ul)

    # rasterio format: (H,W,3) -> (3,H,W)
    RGB_rio = RGB.transpose(2, 0, 1)

    # save file
    with rasterio.open(
        output_path,
        'w',
        driver='GTiff',
        height=height,
        width=width,
        count=3,
        dtype='uint8',
        crs=crs_wkt,
        transform=transform,
        compress='lzw'
    ) as dst:
        dst.write(RGB_rio)