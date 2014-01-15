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

import sys, os

def parse_pop(filename):
    totaltime = 0
    resultsfile = open(filename, 'r')
    for line in resultsfile:
        info = eval(line)
        totaltime += info['time']
    print filename, totaltime, "seconds", totaltime/ 60,"minutes",totaltime/3600.0, "hours"
    return totaltime

def reinitialise_pop(parsed_pop):
    newpop = []
    for indiv in parsed_pop:
        newpop.append(Individual(indiv['genome']))
    return newpop

def get_run(pathname):
    files = os.listdir(pathname)
    datfiles =  [pathname + '/' + i for i in files if i.startswith('gen')]
    datfiles = sorted(datfiles)
    return datfiles

def main():
    if len(sys.argv) < 2:
        print "you must specify a run!"
        exit()
    folder = sys.argv[1]
    files = get_run(folder)
    for gen in files:
        parse_pop(gen)
    

if __name__=='__main__':
    main()
