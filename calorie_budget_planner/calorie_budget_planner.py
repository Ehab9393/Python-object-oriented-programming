# -----------------------------
# User Class
# -----------------------------
class User:
    def __init__(self, name, daily_calorie_goal):
        """
        Initialize user with a daily calorie goal
        """
        self.name = name
        self.daily_goal = daily_calorie_goal

# -----------------------------
# Food Item Class
# -----------------------------
class FoodItem:
    def __init__(self, name, calories, protein, carbs, fats):
        """
        Represents a single food item
        :param name: Food name
        :param calories: Calories in kcal
        :param protein: Protein in grams
        :param carbs: Carbs in grams
        :param fats: Fats in grams
        """
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fats = fats

# -----------------------------
# Meal Tracker Class
# -----------------------------
class MealTracker:
    def __init__(self):
        """
        Store all food items for the day
        """
        self.food_items = []

    def add_food(self, food_item):
        self.food_items.append(food_item)

    def total_calories(self):
        return sum(item.calories for item in self.food_items)

    def total_macros(self):
        protein = sum(item.protein for item in self.food_items)
        carbs = sum(item.carbs for item in self.food_items)
        fats = sum(item.fats for item in self.food_items)
        return protein, carbs, fats

    def summary(self):
        print("\n--- Daily Meal Summary ---")
        for item in self.food_items:
            print(f"{item.name}: {item.calories} kcal | P: {item.protein}g, C: {item.carbs}g, F: {item.fats}g")
        total_cal = self.total_calories()
        protein, carbs, fats = self.total_macros()
        print(f"\nTotal Calories: {total_cal} kcal")
        print(f"Total Macros: Protein: {protein}g, Carbs: {carbs}g, Fats: {fats}g")

        return total_cal

# -----------------------------
# Data Processor
# -----------------------------
class DataProcessor:
    @staticmethod
    def export_data(user, meal_tracker):
        filename = f"{user.name}_calorie_log.txt"
        with open(filename, "w") as f:
            f.write(f"User: {user.name}\n")
            f.write(f"Daily Calorie Goal: {user.daily_goal} kcal\n\n")
            f.write("--- Daily Meal Summary ---\n")
            for item in meal_tracker.food_items:
                f.write(f"{item.name}: {item.calories} kcal | P: {item.protein}g, C: {item.carbs}g, F: {item.fats}g\n")
            total_cal = meal_tracker.total_calories()
            protein, carbs, fats = meal_tracker.total_macros()
            f.write(f"\nTotal Calories: {total_cal} kcal\n")
            f.write(f"Total Macros: Protein: {protein}g, Carbs: {carbs}g, Fats: {fats}g\n")
        print(f"Data exported to {filename}")

# -----------------------------
# Main Program
# -----------------------------
if __name__ == "__main__":
    try:
        # User input
        name = input("Enter your name: ")
        daily_goal = float(input("Enter your daily calorie goal (kcal): "))

        user = User(name, daily_goal)
        meal_tracker = MealTracker()

        print("\nEnter your meals. Type 'done' when finished.")
        while True:
            food_name = input("\nFood name: ")
            if food_name.lower() == "done":
                break
            calories = float(input("Calories (kcal): "))
            protein = float(input("Protein (g): "))
            carbs = float(input("Carbs (g): "))
            fats = float(input("Fats (g): "))

            food_item = FoodItem(food_name, calories, protein, carbs, fats)
            meal_tracker.add_food(food_item)

        # Summary
        total_cal = meal_tracker.summary()
        if total_cal > user.daily_goal:
            print(f"\n⚠️ You exceeded your daily goal by {total_cal - user.daily_goal} kcal.")
        else:
            print(f"\n✅ You are within your daily goal. Remaining: {user.daily_goal - total_cal} kcal.")

        # Export option
        export = input("\nDo you want to export your meal log? (yes/no): ").lower()
        if export == "yes":
            DataProcessor.export_data(user, meal_tracker)

    except ValueError as ve:
        print(f"Input error: {ve}. Please enter valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
