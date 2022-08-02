from operator import itemgetter
from typing import final


FILENAME = "restaurants.txt"


def reccomend(file, price, cuisines_list):
    """ returns [rating%, restaurant name] based on the price and cuisine list"""
    name_to_rating, price_to_names, cuisines_to_names = read_restaurants(file)

    names_matching_price = price_to_names[price]
    names_matching_cuisines = []
    for cuisine in cuisines_list:
        if len(names_matching_cuisines) > 0:
            names_matching_cuisines += cuisines_to_names[cuisine]
        else:
            names_matching_cuisines = cuisines_to_names[cuisine]
    names_matching_cuisines = list(dict.fromkeys(names_matching_cuisines))
    names_final = filter_by_cuisine(
        names_matching_price, cuisines_to_names, cuisines_list)

    rating_matching_names = sortByRatings(names_final, name_to_rating)
    return rating_matching_names


def sortByRatings(names_final, name_to_rating):
    finalList = []
    for name in names_final:
        rating = int(name_to_rating[name].strip("%"))
        finalList += [[rating, name]]
    return sorted(finalList, key=itemgetter(0), reverse=True)


def filter_by_cuisine(names_matching_price, cuisines_to_names, cuisines_list):
    toReturn = []
    for cuisine in cuisines_list:
        for name in cuisines_to_names[cuisine]:
            if name in names_matching_price:
                toReturn = list(dict.fromkeys(
                    toReturn + cuisines_to_names[cuisine]))
    return toReturn


def read_restaurants(file):
    # extract paragraphs
    with open(file, "r") as f:
        lines = f.readlines()
        lines = [line.strip('\n').strip()
                 for line in lines if line.strip('\n').strip() != ""]
        # 1st dictionary: {restaurant name: rating}
        restaurant_ratings = {}
        restaurant_price = {"$": [], "$$": [], "$$$": [], "$$$$": []}
        restaurant_cuisine = {}
        for i in range(0, len(lines), 4):
            restaurant_ratings[lines[i]] = lines[i+1]
            restaurant_price[lines[i+2]] += [lines[i]]
            cuisinesForRestaurant = lines[i+3].split(",")
            for cuisine in cuisinesForRestaurant:
                cuisine = cuisine.strip()
                if cuisine not in restaurant_cuisine:
                    restaurant_cuisine[cuisine] = [lines[i]]
                else:
                    restaurant_cuisine[cuisine] += [lines[i]]
        return restaurant_ratings, restaurant_price, restaurant_cuisine


print(reccomend(FILENAME, "$", ["Malaysian", "Chinese"]))
