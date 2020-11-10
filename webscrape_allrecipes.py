from recipe_scrapers import scrape_me
import numpy as np
import pymongo
import pandas as pd
import csv  
    
# give the url as a string, it can be url from any site listed below
#scraper = scrape_me('https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/')
# Q: What if the recipe site I want to extract information from is not listed below?
# A: You can give it a try with the wild_mode option! If there is Schema/Recipe available it will work just fine.
#scraper = scrape_me('https://www.feastingathome.com/tomato-risotto/', wild_mode=True)
recipes = []
rows = []
for i in range(90000,90200):
    scraper = scrape_me('https://www.allrecipes.com/recipe/'+str(i)+'/')      
    if scraper.image() != "" and scraper.image() != 'https://images.media-allrecipes.com/images/79591.png':
        recipes.append([scraper.title(), scraper.image()])
        rows.append([str(i)])
        print(i)
    if i % 100 == 0:
        print(i)

# field names  
fields = ['Good Indices']  
# name of csv file  
recipe_numbers = "recipe_numbers_with_images.csv"
    
# writing to csv file  
with open(recipe_numbers, 'w') as csvfile:  
    csvwriter = csv.writer(csvfile)  
    csvwriter.writerow(fields)  
    csvwriter.writerows(rows) 

df=pd.DataFrame(recipes,columns=['Titles','Images'])
csv_data = df.to_csv('bare_minimum.csv', index = True) 
#scraper.title()
#scraper.total_time()
#scraper.yields()
#scraper.ingredients()
#scraper.instructions()
#scraper.image()
#scraper.host()
#scraper.links()