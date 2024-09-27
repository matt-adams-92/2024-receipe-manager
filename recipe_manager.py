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

# if __name__ == "__main__":                                                            # Example
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

# if __name__ == "__main__":                                                            # Example
#     egg = Ingredient("Egg", 100, 150, 10, 15, 1)
#     milk = Ingredient("Milk", 200, 120, 10, 5, 15)
    
#     omelette = Recipe("Omelette")
    
#     omelette.add_ingredient(egg)
#     omelette.add_ingredient(milk)
    
#     print(f"Nutritional information for '{omelette.name}': {omelette.calculate_nutrition()}")


def display_menu():                                                                         # This function shows the available options.
    print("\nRecipe Manager")
    print("1. Create a new recipe")
    print("2. Add ingredients to recipe")
    print("3. View recipe's nutritional info")
    print("4. Exit")

def create_recipe():                                                                        # takes user input for the recipe name and creates a Recipe object.
    recipe_name = input("Enter the name of the recipe: ")
    return Recipe(recipe_name)

def add_ingredients_to_recipe(recipe):                                                      # allows the user to input the ingredient details, then adds it to the recipe.
    name = input("Enter ingredient name: ")
    quantity = float(input(f"Enter {name} quantity (grams): "))
    calories = float(input(f"Enter the calories in {quantity}(grams) of {name}: "))
    protein = float(input(f"Enter the protein content (grams) of {name}: "))
    fats = float(input(f"Enter the fat content (grams) of {name}: "))
    carbs = float(input(f"Enter the carbohydrate content (grams) of {name}: "))
    
    ingredient = Ingredient(name, quantity, calories, protein, fats, carbs)
    recipe.add_ingredient(ingredient)

def view_nutritional_info(recipe):                                                          # This calculates and prints the total nutritional information for the recipe.
    nutrition = recipe.calculate_nutrition()
    print(f"\nNutritional Information for {recipe.name}:\n")
    print(f"Calories: {nutrition['calories']}")
    print(f"Protein: {nutrition['protein']}g")
    print(f"Fats: {nutrition['fats']}g")
    print(f"Carbs: {nutrition['carbs']}g")

if __name__ == "__main__":                                                                  # The program runs in a loop, allowing the user to interact until they choose to exit.
    current_recipe = None
    
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            current_recipe = create_recipe()
            print(f"Recipe '{current_recipe.name}' created successfully.")
        
        elif choice == '2':
            if current_recipe:
                add_ingredients_to_recipe(current_recipe)
                print(f"Ingredient added to '{current_recipe.name}'.")
            else:
                print("Please create a recipe first.")
        
        elif choice == '3':
            if current_recipe:
                view_nutritional_info(current_recipe)
            else:
                print("No recipe available. Please create a recipe first.")
        
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")