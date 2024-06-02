from tsp import distances, city_names, hybrid_algorithm, result_analysis
from show_results_tsp import create_map

# ==============================================================
# ====================== CODE EXECUTION ========================
# ==============================================================    

# define global configuration variables
population_size = 200
mutation_prob = 0.05
generations = 250
size_individual = len(distances)
algorithm_executions = 10
start_city = 4

# define variables to use over the program
global_results = []    
# matrix of distances between cities

# print all the cities to ask the user to select the start city
print(f'{"*"*50}')
print(f"Select the start city for the TSP Problem")
# show all the city names to the user
for i, city in enumerate(city_names):
    print(f"{i}. {city_names[city]}")
print(f'{"*"*50}')
    
start_city_user = int(input("Select the start city: "))
if start_city_user >= 0 and start_city_user < len(city_names):
    start_city = start_city_user
    print(f"Start city selected: {city_names[start_city]}")
else:
    print(f"Invalid city selected. Using the default city: {city_names[start_city]}")
    
# print the configuration of the algorithm                      
print(f'{"*"*50}')
print(f"Running solution for the TSP Problem using a Hybrid Algorithm (Genetic Algorithm + Edge Recombination Algorithm)")
print(f"Configuration:")
print(f"- Population Size: {population_size}")
print(f"- Mutation Probability: {mutation_prob}")
print(f"- Generations: {generations}")
print(f"- Size of the Individual: {size_individual}")
print(f"- Algorithm Executions: {algorithm_executions}")
print(f"- Start City: {city_names[start_city]}")
print(f'{"*"*50}', end='\n\n')
# execute the algorithm n times
for i in range(algorithm_executions):
    print(f'\n{"-"*50}')
    print(f'Execution: {i+1}')
    result = hybrid_algorithm([], population_size, size_individual, start_city, generations, 1, mutation_prob)
    print(f'Best Route Found: {result.get("individual")} => VOF {result.get("vof")}')
    print(f"Cities: {' -> '.join([city_names[city] for city in result.get('individual')])}")
    global_results.append(result)
else:
    print(f'\n\n{"*"*50}')
    print(f'Getting statics analysis from all results ({algorithm_executions} executions)')
    print("*"*50, end='\n\n')
    # get the static analysis results
    best_route = result_analysis(global_results)    
    html_path = create_map(best_route)
    print(f"\n\nThe map has been saved in the following path: {html_path}")