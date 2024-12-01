"""

  Distributes the ''Elements'' used, in the modules

""" 

from time import sleep
from json import dump, load
from os import getenv, path, remove as rm, mkdir, makedirs, rename

dsktp_regkey = r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
font_details = [('Noto Sans',8,'normal'), ('Segoe UI',10,'normal')] 
config_dir = getenv('APPDATA')+'\\mcskymaker\\settings.json' 
tempdir = getenv('TEMP')+'\\cspr\\'
image_details = []
rel = 'flat'

# color scheme
db, b, b2, f, ab = [ "#283149","#404b69", "#333e5f", "#dbedf3", "#00818a" ]
# place coords
yp, x, y , yb = [ 225, 15, 3, 2 ]

# output configuration 
ext, blend_width, curve_radius = [".png", 42, 2]

# current config's
def readconfig():
  with open(config_dir, 'r') as readconfig:
    readusingjson = load(readconfig)
    img_res = readusingjson['Image_Size']
    out_path = readusingjson['Outputfolder_Path']
    zip_pack_ch = readusingjson['Convert_To_Zip']
    mc_pack_ch = readusingjson['Convert_To_Mcpack']
  return [img_res, out_path, zip_pack_ch, mc_pack_ch]

# default configuration
config_dict = {"image_res": 256, "mc_convert": False, "jv_convert": False}