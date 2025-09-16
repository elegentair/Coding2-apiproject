# Nation API
import requests
name = input("What country would you like to view information for? Please spell it correctly: ")
c2 = int(input("Would you like to \n1: View the capitol of the nation\n2: View the language\n3: View the region it is in \n4: View the population of said nation: "))
api = "https://restcountries.com/v3.1/name/" + name
print(api)
nation = requests.get(api)
data = nation.json()
#print(data)
if c2 == 1:
    capital = data[0]['capital'][0]
    print(f"The capital is: " + capital)
if c2 == 2:
    langd = data[0]['languages']
    #Makes an iterator (like a list, but you can step through it) and goes to the next (in this case first and only item)
    langi = next(iter(langd))
    lang = data[0]['languages'][langi]
    print("The language is: " + lang)
if c2 == 3:
    region = data[0]['subregion']
    print("The region is: " + region)
if c2 == 4:
    pop = str(data[0]['population'])
    print("The population is: " + pop)
