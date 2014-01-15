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

import os
from evolver import *

def rerun():
    if len(sys.argv) < 2:
        print "Please specify experiment to restart"
        exit()
    
    PATHNAME = "results/"+str(sys.argv[1])
    filename = get_last_gen(PATHNAME)
    lastgen = int(filename.rstrip('.dat').lstrip('gen'))
    print "the last generation was:", lastgen
    parsed_pop = parse_pop(PATHNAME+'/'+filename)

    BNF_GRAMMAR = GRAMMAR.Grammar(GRAMMAR_FILE)
    INDIVIDUALS = reinitialise_pop(parsed_pop)
    LAST_POP = restart_search_loop(GENERATIONS, INDIVIDUALS, BNF_GRAMMAR, tournament_selection, FITNESS_FUNCTION, lastgen, PATHNAME)

def parse_pop(filename):
    population = []
    name = filename.rstrip('.dat')
    resultsfile = open(filename, 'r')
    for line in resultsfile:
        population.append(eval(line))
    return population

def reinitialise_pop(parsed_pop):
    newpop = []
    for indiv in parsed_pop:
        newpop.append(Individual(indiv['genome']))
    return newpop

def get_last_gen(pathname):
    files = os.listdir(pathname)
    datfiles =  [i for i in files if i.startswith('gen')]
    datfiles = sorted(datfiles)
    print "starting at", datfiles[-1], "in", pathname
    return datfiles[-1]

def restart_search_loop(max_gens, individuals, grammar, selection, fit_func, last_gen, pathname):
    """Loop over max generations"""
    #Evaluate initial population
    fronts = []
    evaluate_fitness(individuals, grammar, fit_func)
    best_ever = max(individuals)
    individuals.sort(reverse=True)
    print_stats(individuals,last_gen, pathname)
    
    for generation in xrange((last_gen + 1), (max_gens + 1)):
        individuals, fronts, best_ever = step(
            individuals, fronts, grammar, selection, fit_func, best_ever)
        print_stats(individuals, generation, pathname)
        save_pop(individuals, generation, pathname)
    return individuals

if __name__=='__main__':
    rerun()
