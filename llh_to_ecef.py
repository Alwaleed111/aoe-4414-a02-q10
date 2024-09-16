# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km
#  Python Script that converts LLH to ECEF 
# Parameters:
#  Lat_deg: Latitude in Deg
#  Lon_deg: Longitude in Deg
#  hae_km: Height Above Ellipsoid in Kilometers 
# Output:
#  Code prints out the x,y, and z components in the ECEF frame
#
# Written by Alwaleed Alrashidi 
# Other contributors: Prof Brad Denby (Boilerplate and lecture slide refernce code)
#

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# "constants"
R_E_KM = 6378.1363
e_E = 0.081819221456

# helper functions
def calc_denom(ecc,lat_rad):
    return math.sqrt(1.0-ecc*ecc*math.pow(math.sin(lat_rad),2.0))

# initialize script arguments
lat_deg = float('nan') #Latitude in Degrees
lon_deg = float('nan') #Longitude in Degrees
hae_km = float('nan') #Height Above Ellipsoid in Kilometers

# parse script arguments
if len(sys.argv)==4:
  lat_deg = float(sys.argv[1])
  lon_deg = float(sys.argv[2])
  hae_km = float(sys.argv[3])
else:
  print(\
  'Usage: '\
  'python3 llh_to_ecef.py lat_deg long_deg hae_km'\
  )
  exit()


# write script below this line
lat_rad = lat_deg*(math.pi/180) #Converting from radians to degrees
long_rad = long_deg*(math.pi/180)#Converting from radians to degrees

denom = calc_denom(e_E,lat_rad)
C_E = R_E_KM/denom
S_E = (R_E_KM*(1-e_E*e_E))/denom

r_x_km = (C_E+hae_km)*math.cos(lat_rad)*math.cos(long_rad)
r_y_km = (C_E+hae_km)*math.cos(lat_rad)*math.sin(long_rad)
r_z_km = (S_E+hae_km)*math.sin(lat_rad)

# printing the output:
print(r_x_km)
print(r_y_km)
print(r_z_km)
