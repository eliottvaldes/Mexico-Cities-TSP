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


def hybrid_algorithm(population: list = None, population_size: int = 50, size_individual: int = 11, start_city: int = 0, generations: int = 200, mutation_prob: float = 0.05) -> dict:
    if population is None:
        population = []
    
    # initialize the population only if it is the first time
    if not population:
        population = [generate_individual(size_individual, start_city) for i in range(population_size)]
        vof_initial_population = [calculate_route_distance(individual, distances) for individual in population]
    
    # execute the algorithm for a given number of generations
    for generation in range(generations):
        family = []
        
        # generate the family
        for i in range(int(len(population)/2)):
            p1 = numpy.random.randint(len(population))
            p2 = numpy.random.randint(len(population))
            child = create_child(population[p1], population[p2], size_individual, start_city)

            local_family_individuals = [population[p1], population[p2], child]
            local_family_vof = [vof_initial_population[p1], vof_initial_population[p2], calculate_route_distance(child, distances)]
            worst_individual_index = numpy.argmax(local_family_vof)

            # Add to the family all except the worst
            for j in range(3):
                if j != worst_individual_index:
                    family.append(local_family_individuals[j])
        
        # Mutation of the family
        for i, individual in enumerate(family):
            if numpy.random.rand() < mutation_prob:
                family[i] = generate_individual(size_individual, start_city)
        
        # Prepare the next generation
        population = family
        vof_initial_population = [calculate_route_distance(individual, distances) for individual in population]
    
    # Find the best individual at the end of all generations
    vof_family = [calculate_route_distance(individual, distances) for individual in family]
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
    