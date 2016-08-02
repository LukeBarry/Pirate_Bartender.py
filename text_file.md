start with these 2 dictionaries

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

function 1 asks what style of drink a customer likes
    ask each of the questions in the questions dictionary
    for every question that the user answers yes too, store the key as true in a new dictionary
    return the new dictionary
    
function 2 constructs the drink
    take the preferences dictionary created in function 1 as a parameter
    create an empty list to represent the drink
    for each value of true from the new dictionary append a random.choice ingredient from the ingredients dictionary to the empty list
    
function 3 is the main function
    call function 1
    call function 2
    print out the contents of the drink


Use if __name__ == '__main__': to run the function from the command line.  This appears at the bottom of the code



    


