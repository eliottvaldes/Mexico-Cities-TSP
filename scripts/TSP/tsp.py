import numpy
from edge_recombination_algorithm import create_child
from data_cities import distances, city_names
# ==============================================================
# ================== FUNCTIONS DEFINITION ======================
# ==============================================================

# ---------------FUNCTIONS FOR GENETIC ALGORITHM ----------------
def generate_individual(size_individual: int, start_city: int = 0) -> list:
    # generate a random permutation of the cities
    cities = list(range(size_individual))
    # remove the start city from the list of cities
    cities.remove(start_city)
    # shuffle the cities
    cities = [start_city] + list(numpy.random.permutation(cities))
    # return the individual
    return cities


def hybrid_algorithm(population: list = [], population_size: int = 50, size_individual: int = 11, start_city: int = 0, generations: int = 200, generations_iter: int = 0, mutation_prob: float = 0.05) -> list:
    
    if(generations_iter == 1):
        # generate initial population using 50 individuals
        population = [generate_individual(size_individual, start_city) for i in range(population_size)]
        
    # evaluate each individual using the route distance
    vof_initial_population = [(calculate_route_distance(individual, distances)) for individual in population]
    
    # =========== GENERATE THE FAMILY ===========
    # define a variable to store the child
    family = []
    # get the children from the parents using edge recombination algorithm
    for i in range(int(len(population)/2)):
        # ----  SELECTION ----
        p1 = numpy.random.randint(len(population))
        p2 = numpy.random.randint(len(population))
        
        # ---- ER Algorithm ----
        # get the children from the parents using edge recombination algorithm
        child = create_child(population[p1], population[p2], size_individual, start_city)
                
        # ---- EVALUATION ----
        # define the family
        local_family_individuals = [population[p1], population[p2], child]
        # define a list of the vof of the family
        local_family_vof = [vof_initial_population[p1], vof_initial_population[p2], calculate_route_distance(child, distances)]
        # get the index of the worst element
        worst_individual_index = numpy.argmax(local_family_vof)
        
        # push each individual to the family list except the worst one
        for j in range(3):
            if j != worst_individual_index:
                family.append(local_family_individuals[j])

    # =========== MUTATION ===========
    for i, individual in enumerate(family):
        if numpy.random.rand() < mutation_prob:
            # replace the family individual with the new one
            family[i] = generate_individual(size_individual, start_city)
    
    ## repeat using recursion. valdidate the stop condition is the same as the number of generations
    if generations_iter < generations:
        return hybrid_algorithm(family, population_size, size_individual, start_city, generations, generations_iter + 1, mutation_prob)
    else:
        # get the vof of the family to return the best individual
        vof_family = [(calculate_route_distance(individual, distances)) for individual in family]
        # get the best individual index
        best_individual_index = numpy.argmin(vof_family)
        
        return {
            'individual': family[best_individual_index],
            'vof': vof_family[best_individual_index]
        }
        
    
# ---------------FUNCTIONS FOR ROUTE CALCULATION ----------------
# function to calculate the total distance of a specific route, including the return to the starting point
def calculate_route_distance(route, distances):
    if len(route) < 2:  # Si hay menos de dos ciudades, la distancia es 0
        return 0

    total_distance = 0
    # Calculate the distance for the main part of the route
    for i in range(len(route) - 1):
        total_distance += distances[route[i]][route[i + 1]]

    # Add distance from the last city back to the first city
    total_distance += distances[route[-1]][route[0]]
    
    return total_distance       
    
    
    
# ---------------FUNCTIONS FOR FOR STATIC ANALYSIS ----------------
def result_analysis(best_results_individual: list[int])-> None :
    
    # get the array of best results
    best_results = [result['vof'] for result in best_results_individual]
    # get the best result
    best_result_index = numpy.argmin(best_results)
    # get the average of the results
    average_result = numpy.mean(best_results)
    # get the worst result
    worst_result_index = numpy.argmax(best_results)
    # get the standard deviation of the results
    std_result = numpy.std(best_results)
    
    # show results in a table format
    print("="*50)
    print(f'Best Result:\t\t {best_results[best_result_index]}')
    print(f'Average Result:\t\t {average_result}')
    print(f'Worst Result:\t\t {best_results[worst_result_index]}')
    print(f'Standard Deviation:\t {std_result}')
    print(f'Best Result Route:\t {(best_results_individual[best_result_index]).get("individual")}')    
    print(f'Worst Result Route:\t {(best_results_individual[worst_result_index]).get("individual")}')
    # show the cities of the best result
    print(f"Best result cities: \n{' -> '.join([city_names[city] for city in (best_results_individual[best_result_index]).get('individual')])}")    
    print("="*50)
    
    return (best_results_individual[best_result_index]).get("individual")
    