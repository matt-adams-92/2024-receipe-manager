class Ingredient:
    def __init__(self, name, quantity, calories, protein, fats, carbs):
        self.name = name
        self.quantity = quantity
        self.calories = calories
        self.protein = protein
        self.fats = fats
        self.carbs = carbs
    
    def get_nutritional_info(self):
        return {
            "name": self.name,
            "quantity": self.quantity,
            "calories": self.calories,
            "protein": self.protein,
            "fats": self.fats,
            "carbs": self.carbs
        }


# Example
if __name__ == "__main__":
    egg = Ingredient("Egg", 100, 150, 10, 15, 1)
    print(egg.get_nutritional_info())