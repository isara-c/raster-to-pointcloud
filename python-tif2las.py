import os
import pylas
import numpy as np
import pandas as pd

def pylas_xyz2las(src_path, dst_path):
    '''
    use pylas to convert .xyz to .las
    output data only x, y, z not include RGB
    output in type of pointcloud without nodata(-10000) in this case use gdal
    '''
    df_xyz = pd.read_csv(src_path, sep=' ', header=None)
    # filter out nodata in .xyz
    df_xyz_without_nodata = df_xyz[df_xyz[2] != -10000]
    x = df_xyz_without_nodata.values[:, 0]
    y = df_xyz_without_nodata.values[:, 1]
    z = df_xyz_without_nodata.values[:, 2]
    las = pylas.create()
    las.x = x
    las.y = y
    las.z = z
    las.write(dst_path)

def gdal_translate_tif2xyz(src_path, dst_path):
    '''
    use gdal in local to convert .tif to .xyz with commandline with python
    '''
    gdal_command = "gdal_translate -of XYZ '" + src_path + "' " +  dst_path
    os.system(gdal_command)

if __name__ == "__main__":
    # path
    tif_path = '/Users/isara/Downloads/F1_CamM_150m_80_75_dsm_gsd25cm.tif'
    xyz_path = tif_path.replace( '.tif', '.xyz')
    las_path = tif_path.replace( '.tif', '.las')

    # convert tif to xyz
    # gdal_translate_tif2xyz(tif_path, xyz_path)
    pylas_xyz2las(xyz_path, las_path)
