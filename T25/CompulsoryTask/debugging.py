# adding the * to the keys argument passed to the funtion so a variable number of arguments can be passed
def print_values_of(dictionary, *keys):
    for key in keys:
        print(dictionary[key])

# Wrapped the value d'oh in double quotes to include the single quote in the value of the key "homer"
simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": "d'oh", "maggie": " (Pacifier Suck)"}

print_values_of(simpson_catch_phrases, 'lisa', 'bart', 'homer')

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

