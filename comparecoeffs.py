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

def parsefile(filename):
    datfile = open(filename, 'r')

    attribs = ['time','moment','drag','lift','liftfront','liftrear']
    forcelist = []
    for line in datfile:
        if not line.startswith('#'):
            line = line.rstrip('\n')
            line = line.split()
            forces = [float(elem) for elem in line]  
            print forces
            forcelist.append(forces)

    print "differences"
    for i in range(len(forcelist)-1):
        difference = [a - b for a, b in zip(forcelist[i], forcelist[i+1])]
        print difference
    return forcelist

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        parsefile(filename)
    elif len(sys.argv) == 3:
        datfile1 = sys.argv[1]
        datfile2 = sys.argv[2]
        data1 = parsefile(datfile1)
        data2 = parsefile(datfile2)
        force1 = data1[-1]
        force2 = data2[-1]
        print datfile1 + ':\n' + str(force1)
        print datfile2 + ':\n' + str(force2)

        print "final diff:"
        difference = [a - b for a, b in zip(force1, force2)]
        print difference
    else:
        "pass args!"

if __name__=='__main__':
    main()
