"""
You are going to write a program that adds to a 'travel_log'.
You can see a travel_log which is a List that contains 2 Dictionaries.

Write a function that will work with the following line of code on line 21
to add the entry for Russia to the 'travel_log'.

function => add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"]);
         => you visited Russia 2 times
         => You've been Moscow and Saint Petersburg.
DO NOT modify the 'travel_log' 
"""
from typing import List


travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

# TODO - 1 - write the function that will allow new countries to be added
#            to the travel_log.
def add_new_country(visitCountry:str, visitTotal:int, visitCities:List):
    newTravelLog = {
        "country": visitCountry, 
        "visits": visitTotal,
        "cities": visitCities
    };

    travel_log.append(newTravelLog);

def main():
    add_new_country("Rusia", 2, ["Moscow", "Saint Petersburg"]);
    print(travel_log);

if __name__ == "__main__":
    main();