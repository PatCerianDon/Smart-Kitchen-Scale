import sqlite3
from recipe_scrapers import scrape_me

conn = sqlite3.connect('recipes.db')

cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS database_recipes (
        recipe_name TEXT,
        recipe_ingredients TEXT,
        recipe_instructions TEXT
    )
""")

scraper = scrape_me("https://www.simplyrecipes.com/nilagang-baka-filipino-beef-stew-recipe-8286046")

recipeName = scraper.title()
recipeIngredients = scraper.ingredients()
recipeInstructions = scraper.instructions()

cursor.execute(""" 
    INSERT INTO database_recipes (recipe_name, recipe_ingredients, recipe_instructions) VALUES (?,?,?)
""", (str(recipeName), str(recipeIngredients), str(recipeInstructions)))

conn.commit()
conn.close()
