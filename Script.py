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

attractions=[[] for i in range(len(destinations))]

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

def find_attractions(destination,interests):
    destination_index=get_destination_index(destination)
    attractions_in_city=attractions[destination_index]
    attractions_with_interest=[]
    for i in attractions_in_city:
        possible_attraction=i
        attraction_tags=i[1]
        for i in interests:
            if attraction_tags.count(i)>0:
                attractions_with_interest.append(possible_attraction[0])
    return attractions_with_interest

la_arts=find_attractions('Los Angeles, USA',['art'])
print(la_arts)
