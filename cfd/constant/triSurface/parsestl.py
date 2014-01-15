# This file is part of Plane Generator.
# Plane Generator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# Plane Generator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License 
# along with Plane Generator.  If not, see <http://www.gnu.org/licenses/>.
# Author Jonathan Byrne 2014

import sys

if sys.argv[1] == None:
    print "pass in either an .stl or .obj file"
filename = sys.argv[1]

if sys.argv[1].endswith('.stl'):
    vertsymbol = 'vertex'
elif sys.argv[1].endswith('.obj'):
    vertsymbol = 'v'
else:
    print "not a valid file extension"
    exit()

    
stlfile = open(filename,'r')
maxx, maxy, maxz = -1000, -1000, -1000
minx, miny, minz = 1000, 1000, 1000
vertcount = 0
for line in stlfile:
    line = line.strip()
    
    if line.startswith(vertsymbol):
        vertcount += 1
        info = line.split(' ')
        x = float(info[1])
        y = float(info[2])
        z = float(info[3])

        if x > maxx: maxx = x
        if x < minx: minx = x

        if y > maxy: maxy = y
        if y < miny: miny = y

        if z > maxz: maxz = z
        if z < minz: minz = z

print vertcount, "vertices"
print 'max x:', maxx, 'y:', maxy, 'z:', maxz
print 'min x:', minx, 'y:', miny, 'z:', minz
