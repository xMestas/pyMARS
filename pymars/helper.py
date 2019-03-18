
##############
# This function takes the conditions array and converts it into an array of simulation species_objects
#
# conditions array: array of initial conditions read in from the ic file
#  model: model to base the simulation off of
#
# simulation array: an array of unran simulation objects from simulation.py
##############

from simulation import Simulation
import numpy as np
import sys
def setup_simulations(conditions_array, model):
    sim_array = []
    i = 0
    while (i < len(conditions_array)): #For all conditions
        properties = {} #create properties dictionary
        properties['temperature'] = float(conditions_array[i].temperature)
        properties['pressure'] = float(conditions_array[i].pressure)
        properties['equivalence_ratio'] = float(conditions_array[i].equi)
        properties['fuel'] = conditions_array[i].fuel
        properties['oxidizer'] = conditions_array[i].oxid

        sim_array.append(Simulation(i,properties,model)) #create simulation object and add it to the array
        i = i + 1

    return sim_array


############
# This function takes a set up simulation array, simulates it, and processes the results.  It returns a numpy array of the ignition delays
#
# sim_array: An array of set up simulation objects.  Comes in unsimulated and comes out simulated with results processed.
#
# ignition_delay: np array of the ignition delays from the setup_simulations.
#############


def simulate(sim_array):
        tau = [] #Ignition delays
        sample_points = [] #Sample information
        for case in sim_array: #Run simulations for original model and process results
            tau.append(case.run_case())
            sample_points.append(case.process_results())

        ignition_delay = np.array(tau) #Turn tau array into a numpy array
        return ignition_delay


def target_error_check(graph, target_species):
    """
    check if target species are present in solution object before attempting to remove them, 
    if a target is absent from the graph the program will exit with error message

    Parameters
    ----------
    graph : obj
        networkx graph object of solution
    target_species : list
        List of target species to search from

    Returns
    -------
    void

    """
    for target in target_species:
        if(target not in graph):
            sys.exit('exiting with error target species ' + target + ' not found model')
    return


############
# Add oxidizers, fuels, and targets to retianed species.
#
# conditions array: array of initial conditions read in from the ic file
# target_species: array of target species names
# retained_species: array of species to retain
#############
def addRetained(conditions_array, target_species, retained_species):

    # Add the target species to the retained species if not already in
    for sp in target_species:
        if sp not in retained_species:
            retained_species.append(sp)

    # For each initial condition set
    for condition in conditions_array:
        # Extract species names from condition formatting
        # Replace , with :, split by :, and take every other element
        oxid_names = condition.oxid.replace(",",":").split(":")[::2]
        fuel_names = condition.fuel.replace(",",":").split(":")[::2]

        # Add the oxidzers to the retained species if not already in
        for sp in oxid_names:
            if sp not in retained_species:
                retained_species.append(sp)

        # Add the fuels to the retained species if not already in
        for sp in fuel_names:
            if sp not in retained_species:
                retained_species.append(sp)
    return retained_species


