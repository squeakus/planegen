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
outfile = open('plane2.stl','w')
vertcount = 0
for line in stlfile:
    tmpline = line.strip()
    
    if tmpline.startswith(vertsymbol):
        vertcount += 1
        info = tmpline.split(' ')
        z = float(info[3])
	z += 3
        newline = str(info[0]) + " " + str(info[1]) + " " + str(info[2]) + " " + str(z) + "\n"
        outfile.write(newline)
        print "*****************"
        print "before", line
        print "after", newline
    else:
	outfile.write(line)
outfile.close()
    
print vertcount, "vertices"
