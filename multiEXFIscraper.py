import os
import sys
import time
import colorama
from colorama import Fore
import csv
from PIL import Image
from PIL.ExifTags import GPSTAGS, TAGS

def gmaps(gps_coords):
     dec_lat = convert_deci(float(gps_coords["lat"][0]),  float(gps_coords["lat"][1]), float(gps_coords["lat"][2]), gps_coords["lat_ref"])
     dec_lon = convert_deci(float(gps_coords["lon"][0]),  float(gps_coords["lon"][1]), float(gps_coords["lon"][2]), gps_coords["lon_ref"])
     return f"https://maps.google.com/?q={dec_lat},{dec_lon}"

def convert_deci(degree, minutes, seconds, direction):
    decimal_degrees = degree + minutes / 60 + seconds / 3600
    if direction == "S" or direction == "W":
        decimal_degrees *= -1
    return decimal_degrees
    
def load_anim():
    blah = "..........."
    for l in blah:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.2)

print( Fore.GREEN + """
      
███╗░░░███╗██╗░░░██╗██╗░░░░░████████╗██╗  ███████╗██╗░░██╗██╗███████╗
████╗░████║██║░░░██║██║░░░░░╚══██╔══╝██║  ██╔════╝╚██╗██╔╝██║██╔════╝
██╔████╔██║██║░░░██║██║░░░░░░░░██║░░░██║  █████╗░░░╚███╔╝░██║█████╗░░
██║╚██╔╝██║██║░░░██║██║░░░░░░░░██║░░░██║  ██╔══╝░░░██╔██╗░██║██╔══╝░░
██║░╚═╝░██║╚██████╔╝███████╗░░░██║░░░██║  ███████╗██╔╝╚██╗██║██║░░░░░
╚═╝░░░░░╚═╝░╚═════╝░╚══════╝░░░╚═╝░░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░░░░

░██████╗░█████╗░██████╗░░█████╗░██████╗░███████╗██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
╚█████╗░██║░░╚═╝██████╔╝███████║██████╔╝█████╗░░██████╔╝
░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
██████╔╝╚█████╔╝██║░░██║██║░░██║██║░░░░░███████╗██║░░██║
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝
        """  )
time.sleep(0.5)
def message(string):
   
    for i in string:
       
        # printing each character of the message
        print(i, end="")
         
        # adding time delay of half second
        time.sleep(0.5)

cwd = os.getcwd()
os.chdir(os.path.join(cwd, "images"))
files = os.listdir()


if len(files) == 0:
    print("Add files to the ./images folder")
    exit()

for file in files:
    try:
        
        image = Image.open(file)
        print(Fore.CYAN + f"[+] Scrapping File - {file}")
        load_anim()
        print("\n")
        
        
        gps_coords = {}
         
        if image._getexif() == None:
            print(Fore.RED +"[+] ERR ->   {file} contains no exif data." )
        
        else:
            for tag, value in image._getexif().items():
                
                tag_name = TAGS.get(tag)
                if tag_name == "GPSInfo":
                    for key, val in value.items():
                        print(f"{GPSTAGS.get(key)} - {val}")
                        
                        if GPSTAGS.get(key) == "GPSLatitude":
                            gps_coords["lat"] = val
                        
                        elif GPSTAGS.get(key) == "GPSLongitude":
                            gps_coords["lon"] = val
                        
                        elif GPSTAGS.get(key) == "GPSLatitudeRef":
                            gps_coords["lat_ref"] = val
                        
                        elif GPSTAGS.get(key) == "GPSLongitudeRef":
                            gps_coords["lon_ref"] = val   
                else:
                    
                    print(Fore.WHITE +  f"{tag_name} - {value}")
            
            if gps_coords:
                print(Fore.RED  + "\n" + gmaps(gps_coords)+ Fore.WHITE)
            
    except IOError:
        print( "[+] Invalid File format!! ")



sys.stdout.close()
os.chdir(cwd)


