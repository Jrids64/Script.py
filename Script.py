destinations=['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']
test_traveler=['Erin Wilkes', 'Shanghai, China', 'historical site', 'art']
def get_destination_index(destination):
    destination_index=destinations.index(destination)
    return destination_index
print(get_destination_index('Paris, France'))

def get_traveler_location(traveler):
    traveler_destination=traveler[1]
    traveler_destination_index=get_destination_index(traveler_destination)
    return traveler_destination_index

test_destination_index=get_traveler_location(test_traveler)
print(test_destination_index)

attractions=[[] for i in range(len(destinations))]
print(attractions)

def add_attractions(destination,attraction):
    try:
        destination_index=get_destination_index(destination)
    except ValueError:
        return
    attractions_for_destination=attractions[destination_index]    
    attractions_for_destination.append(attraction)
    return

add_attractions('Los Angeles, USA',['Venice Beach', ['beach']])


add_attractions("Paris, France", ["the Louvre", ["art", "museum"]])
add_attractions("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attractions("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attractions("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attractions("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attractions("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attractions("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attractions("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attractions("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attractions("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
print(attractions)
