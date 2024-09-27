class Ingredient:
    def __init__(self, name, quantity, calories, protein, fats, carbs):                 # Store the name, quantity, and nutritional values for each ingredient.
        self.name = name
        self.quantity = quantity
        self.calories = calories
        self.protein = protein
        self.fats = fats
        self.carbs = carbs
    
    def get_nutritional_info(self):                                                     # Have a method to return nutritional information.
        return {
            "name": self.name,
            "quantity": self.quantity,
            "calories": self.calories,
            "protein": self.protein,
            "fats": self.fats,
            "carbs": self.carbs
        }

# # Example
# if __name__ == "__main__":
#     egg = Ingredient("Egg", 100, 150, 10, 15, 1)
#     print(egg.get_nutritional_info())



class Recipe:                                                                           # stores ingredients and calculates the total nutritional values for the recipe.
    def __init__(self, name):
        self.name = name
        self.ingredients = []
    
    def add_ingredient(self, ingredient):                                               # adds an ingredient to the recipe
        self.ingredients.append(ingredient)
    
    def calculate_nutrition(self):                                                      # this method sums up the calories, protein, fats, and carbs from all the ingredients.
        total_calories = sum([i.calories for i in self.ingredients])
        total_protein = sum([i.protein for i in self.ingredients])
        total_fats = sum([i.fats for i in self.ingredients])
        total_carbs = sum([i.carbs for i in self.ingredients])

        return {                                                                        
            "calories": total_calories,
            "protein": total_protein,
            "fats": total_fats,
            "carbs": total_carbs
        }
    
    def get_ingredients(self):                                                          # returns a list of ingredient names for easy reference.
        return [ingredient.name for ingredient in self.ingredients]

# Example
if __name__ == "__main__":
    egg = Ingredient("Egg", 100, 150, 10, 15, 1)
    milk = Ingredient("Milk", 200, 120, 10, 5, 15)
    
    omelette = Recipe("Omelette")
    
    omelette.add_ingredient(egg)
    omelette.add_ingredient(milk)
    
    print(f"Nutritional information for '{omelette.name}': {omelette.calculate_nutrition()}")