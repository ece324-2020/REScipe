from recipe_scrapers import scrape_me
from threading import Thread
from multiprocessing import Process
import numpy as np
import pandas as pd
import csv  
import time
    
# give the url as a string, it can be url from any site listed below
#scraper = scrape_me('https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/')
#scraper.total_time()
#scraper.yields()
#scraper.ingredients()
#scraper.instructions()
#scraper.host()
#scraper.links()
def check_recipes(start,end,filename):
    recipes = []

    for i in range(start,end): 
        scraper = scrape_me('https://www.allrecipes.com/recipe/'+str(i)+'/')      
        if scraper.image() != "" and scraper.image() != 'https://images.media-allrecipes.com/images/79591.png':
            recipes.append([scraper.title(), scraper.image(), scraper.total_time(), scraper.yields(), scraper.ingredients(), scraper.instructions(), str(i)])
            print(i)
        if i % 100 == 0:
            print(i)

            # Write Recipe info to csv file
            df=pd.DataFrame(recipes,columns=['Title','Image', 'Total Time', 'Yields', 'Ingredients', 'Instructions', 'URL'])
            csv_data = df.to_csv(filename, index = True, mode='a', header=False)
            recipes = []


if __name__ == '__main__':

    Thread(target=check_recipes,args=(70000,80000,'recipes1.csv')).start()
    time.sleep(3)
    Thread(target=check_recipes,args=(80000,90000,'recipes2.csv')).start()
    time.sleep(3)
    Thread(target=check_recipes,args=(90000,100000,'recipes3.csv')).start()
    time.sleep(3)
    Thread(target=check_recipes,args=(100000,110000,'recipes4.csv')).start()
    time.sleep(3)
    
