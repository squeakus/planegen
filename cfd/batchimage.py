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

# run with command pvbatch --use-offscreen-rendering batchimage.py 

import sys
from paraview.simple import *
# Load the state


if len(sys.argv) < 2: 
    print "Error: please specify filename"
    exit()

print "saving image", sys.argv[1]

paraview.simple._DisableFirstRenderCameraReset()


servermanager.LoadState("pressure.pvsm")
view = GetRenderView()
SetActiveView(view)

#GetDisplayProperties().CubeAxesVisibility = 0

Render()
WriteImage(sys.argv[1]+".png")

