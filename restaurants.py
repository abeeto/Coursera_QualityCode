

FILENAME = "restaurants.txt"


def reccomend(file, price, cuisines_list):
    """ returns [rating%, restaurant name] based on the price and cuisine list"""
    name_to_rating, price_to_names, cuisines_to_names = read_restaurants(file)

    names_matching_price = price_to_names[price]


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


print(reccomend(FILENAME, "$", ["Mexican", "Malaysian", "Chinese", "Thai"]))
