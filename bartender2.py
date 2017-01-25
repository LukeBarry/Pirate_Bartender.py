import random
questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

#function 1 asks what style of drink a customer likes
def function1 ():
    preferences = {}
    for flavor in questions:
        response = input(questions[flavor])
        if response == "y":
            preferences[flavor] = "true"
        else:
            preferences[flavor] = "false"
            
    return preferences
    
#function 2 constructs the drink
def function2 (preferences):
    drink = []
    for flavor in preferences:
        if preferences[flavor] == "true":
            drink.append(random.choice(ingredients[flavor]))
    return drink   

#function 3 is the main function
def main ():
    preferences = function1() 
    drink = function2(preferences)
    print("I am going too make you something delicious. Here are the ingredients.")
    print(drink)


if __name__ == '__main__': 
    main()

    


