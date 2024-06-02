import random

# function to get the neighbours of each element in the individual
def get_neighbours(individual):
    return {city: [individual[i - 1], individual[(i + 1) % len(individual)]] for i, city in enumerate(individual)}
        
# funciton to merge 2 dictionaries using the keys to get unique values        
def merge_neighbours(neighbours_1, neighbours_2):
    merged_neighbours = {key: sorted(set(neighbours_1.get(key, []) + neighbours_2.get(key, []))) for key in set(neighbours_1) | set(neighbours_2)}
    return merged_neighbours

# function to remove an item from the neighbours dict
def remove_item(neigbours: dict, item: int) -> dict:
    for key in neigbours:
        if item in neigbours[key]:
            neigbours[key].remove(item)
    return neigbours

# this function is used to select a city based on how many neighbours it has. The city with the least neighbours will be selected
def select_new_city(cities: list, neighbours: dict) -> int:
    size_cities = []
    for city in cities:
        # validate city key exists in the neighbours dict
        if city  in neighbours:            
            # access to the neighbours of the city and get the length of the list
            size_cities.append(len(neighbours[city]))
    # get the index of the city with the least neighbours. in case of a tie, select randomly one of the cities with the least neighbours
    index = [i for i, x in enumerate(size_cities) if x == min(size_cities)]
    if len(index) == 0:        
        return index[0]     
    else:                
        return random.choice(index)   
                   

# =============================================================================
# ======================= MAIN FUNCTION FOR EDGE RECOMBINATION ================
# =============================================================================
def create_child(individual_1: list, individual_2: list, size_individual: int, start_city: int) -> list:
    # start the child route with the start city
    child = [start_city]
    # merge the neighbours of both parents to guide the construction of the child route
    neighbours = merge_neighbours(get_neighbours(individual_1), get_neighbours(individual_2))
    # strart the construction of the route from the start city
    current_city = start_city
    # loop over all the elements in the individual to get the child
    for i in range(1, size_individual):
        # remove the current city from the neighbours to avoid visiting it again
        neighbours = remove_item(neighbours, current_city)
        # if the current city has neighbours, select the next city based on the neighbours
        if len(neighbours[current_city]) > 0:
            current_neighbours = neighbours[current_city]
            new_current_city_index = select_new_city(current_neighbours, neighbours)
            current_city = current_neighbours[new_current_city_index]
            child.append(current_city)
        else:
            # if there are no valid neighbours, choose randomly from the non-visited cities
            non_visited_cities = [city for city in individual_1 if city not in child]
            current_city = random.choice(non_visited_cities)
            child.append(current_city)
    
    return child