class User:
    def __init__(self, age, gender, child_gender=None, pregnant=False, breastfeeding=False):
        # Initialize user attributes
        self.age = age
        self.gender = gender.lower() if gender else None
        self.child_gender = child_gender
        self.pregnant = pregnant
        self.breastfeeding = breastfeeding

    def input_validation(self):
        # Validate user inputs
        if self.age < 0:
            raise ValueError("Age cannot be negative.")
        if self.gender == "female" and (self.pregnant or self.breastfeeding) and self.age < 19:
            raise ValueError("Pregnancy and breastfeeding are not valid for minors (age < 19).")
        if self.age <= 18 and self.child_gender not in ['boy', 'girl']:
            raise ValueError("For children under 18, you must specify whether the child is a boy or a girl.")
        if self.age > 18 and self.gender not in ["male", "female"]:
            raise ValueError("Gender must be 'male' or 'female'.")



class DietaryRecommendation:
    # Initialize with user and food group details
    def __init__(self, user):
        self.user = user
        self.recommendations = {}
        self.food_groups_details = {
            "VEGETABLES": [
                # Examples of a single serve of vegetables
                "A vegetables single serve is 75g (100-350kJ). Here are some examples:",
                "• 0.5 cup of cooked green or orange vegetables (like broccoli, spinach, carrots, or pumpkin)",
                "• 0.5 cup of cooked dried or canned beans, peas, or lentils",
                "• 1 cup of green leafy or raw salad vegetables",
                "• 0.5 cup of sweet corn",
                "• 0.5 of a medium potato or other starchy vegetables (such as sweet potato, taro, or cassava)",
                "• 1 medium tomato"
            ],
            "FRUITS": [
                # Examples of a single serve of fruits
                "A fruits single serve is 150g (350kJ). Examples:",
                "• 1 medium apple, banana, orange, or pear",
                "• 2 small apricots, kiwi fruits, or plums",
                "• 1 cup of diced or canned fruit (with no added sugar)"
            ],
            "GRAINS": [
                # Examples of a single serve of grains
                "A grains single serve is (500kJ). Examples:",
                "• 1 slice (40g) of bread",
                "• 0.5 medium (40g) roll or flat bread",
                "• 0.5 cup (75-120g) of cooked rice, pasta, noodles, barley, buckwheat, semolina, polenta, bulgur or quinoa",
                "• 0.5 cup (120g) of cooked porridge",
                "• 0.66 cup (30g) of wheat cereal flakes",
                "• 0.75 cup (30g) of muesli",
                "• 3 (35g) crispbreads",
                "• 1 (60g) crumpet",
                "• 1 small (35g) English muffin or scone"
            ],
            "MEAT": [
                # Examples of a single serve of meat and alternatives
                "A meat single serve is (500-600kJ). Examples:",
                "• 65g cooked lean red meats such as beef, lamb, veal, pork, goat, or kangaroo (about 90-100g raw)",
                "• 80g cooked lean poultry such as chicken or turkey (100g raw)",
                "• 100g cooked fish fillet (about 115g raw) or one small can of fish",
                "• 2 large (120g) eggs",
                "• 1 cup (150g) cooked or canned legumes/beans such as lentils, chickpeas, or split peas",
                "• 170g tofu",
                "• 30g nuts, seeds, peanut or almond butter, tahini, or other nut or seed paste"
            ],
            "DAIRY": [
                # Examples of a single serve of dairy
                "A single serve of dairy is (500-600kJ). Examples:",
                "• 1 cup (250ml) of fresh, UHT long life, reconstituted powdered milk or buttermilk",
                "• 0.5 cup (120ml) of evaporated milk",
                "• 2 slices (40g) or a 4 x 3 x 2 cm cube (40g) of hard cheese, such as cheddar",
                "• 0.5 cup (120g) of ricotta cheese",
                "• 0.25 cup (200g) of yoghurt",
                "• 1 cup (250ml) of soy, rice or other cereal drink with at least 100mg of added calcium per 100ml"
            ]
        }
        self.get_recommendations()

    def get_recommendations(self):
        # Calculate recommendations based on user data
        if self.user.age >= 19:
            if self.user.gender == "male":
                self.recommendations = {
                    'Vegetables': 6,
                    'Fruits': 2,
                    'Grains': 6,
                    'Meat': 3,
                    'Diary': 2.5,
                }
            if self.user.age > 50:
                self.recommendations['Vegetables'] = 5.5
                self.recommendations['Meat'] = 2.5
                if self.user.age > 70:
                    self.recommendations['Vegetables'] = 5
                    self.recommendations['Grains'] = 4.5
                    self.recommendations['Dairy'] = 3.5

            elif self.user.gender == "female":
                self.recommendations = {
                    'Vegetables': 5,
                    'Fruits': 2,
                    'Grains': 6,
                    'Meat': 2.5,
                    'Dairy': 2.5,
                }
                if self.user.age > 50:
                    self.recommendations['Grains'] = 4
                    self.recommendations['Meat'] = 2
                    self.recommendations['Dairy'] = 4
                    if self.user.age > 70:
                        self.recommendations['Grains'] = 3

                if self.user.pregnant:
                    self.recommendations['Grains'] = 8.5
                    self.recommendations['Meat'] = 3.5
                if self.user.breastfeeding:
                    self.recommendations['Vegetables'] = 7.5
                    self.recommendations['Grains'] = 9
        else:
            # Recommendations for children under 18
            if self.user.child_gender == 'boy':
                if self.user.age <= 3:
                    self.recommendations = {'Vegetables': 2.5, 'Fruits': 1, 'Grains': 4, 'Meat': 1, 'Dairy': 1.5}
                elif self.user.age <= 8:
                    self.recommendations = {'Vegetables': 4.5, 'Fruits': 1.5, 'Grains': 4, 'Meat': 1.5, 'Dairy': 2}
                elif self.user.age <= 11:
                    self.recommendations = {'Vegetables': 5, 'Fruits': 2, 'Grains': 5, 'Meat': 2.5, 'Dairy': 2.5}
                elif self.user.age <= 13:
                    self.recommendations = {'Vegetables': 5.5, 'Fruits': 2, 'Grains': 6, 'Meat': 2.5, 'Dairy': 3.5}
                else:
                    self.recommendations = {'Vegetables': 5.5, 'Fruits': 2, 'Grains': 7, 'Meat': 2.5, 'Dairy': 3.5}
            else:  # Girl
                if self.user.age <= 3:
                    self.recommendations = {'Vegetables': 2.5, 'Fruits': 1, 'Grains': 4, 'Meat': 1, 'Dairy': 1.5}
                elif self.user.age <= 8:
                    self.recommendations = {'Vegetables': 4.5, 'Fruits': 1.5, 'Grains': 4, 'Meat': 1.5, 'Dairy': 1.5}
                elif self.user.age <= 11:
                    self.recommendations = {'Vegetables': 5, 'Fruits': 2, 'Grains': 4, 'Meat': 2.5, 'Dairy': 3}
                elif self.user.age <= 13:
                    self.recommendations = {'Vegetables': 5, 'Fruits': 2, 'Grains': 5, 'Meat': 2.5, 'Dairy': 3.5}
                else:
                    self.recommendations = {'Vegetables': 5, 'Fruits': 2, 'Grains': 7, 'Meat': 2.5, 'Dairy': 3.5}

    def display_recommendations(self):
        # Print the calculated recommendations
        print("\nBased on your inputs, the minimum recommended servings are:")
        for food_group in self.recommendations:  # Loop through the food groups
            servings = self.recommendations[food_group]  # Get servings for the current food group
            print(f"{food_group}: {servings:.1f} servings per day")
        # Print detailed single-serve information
        print("\nAdditionally, each food category single serving recommendations are detailed as shown as follows:")
        for food_group in self.food_groups_details:  # Loop through food groups for details
            print(f"\n{food_group}")  # Print the food group name
            for detail in self.food_groups_details[food_group]:  # Loop through details for each food group
                print(f"  {detail}")  # Indent details for readability

    def export_recommendations(self, filename="DietaryRecommendations.txt"):
        # Export recommendations to a text file
        with open(filename, 'w') as file:
            file.write("Based on your inputs, the minimum recommended servings are:\n")
            for food_group in self.recommendations:  # Loop through the food groups
                servings = self.recommendations[food_group]  # Get servings for the current food group
                file.write(f"{food_group}: {servings} serves per day\n")

            file.write(
                "\nAdditionally, each food category single serving recommendations are detailed as shown as follows:\n")
            for food_group in self.food_groups_details:  # Loop through food groups for details
                file.write(f"\n{food_group}:\n")  # Write the food group name
                for detail in self.food_groups_details[food_group]:  # Loop through details for each food group
                    file.write(f"  {detail}\n")  # Indent details for readability

        print(f"Recommendations and serving sizes have been exported to  {filename}")


if __name__ == '__main__':
        try:
            # User input prompts
            age = int(input("Enter your age: "))
            gender = None
            child_gender = None
            pregnant = False
            breastfeeding = False

            if age <= 18:
                child_gender = input("Are you a boy or girl? ").lower()
            else:
                gender = input("Enter your gender (male/female): ").lower()
                if gender == 'female':
                    pregnant = input("Are you pregnant? (yes/no): ").lower() == 'yes'
                    breastfeeding = input("Are you breastfeeding? (yes/no): ").lower() == 'yes'

            # Create user and calculate recommendations
            user = User(age=age, gender=gender, child_gender=child_gender, pregnant=pregnant,
                        breastfeeding=breastfeeding)
            user.input_validation()
            diet = DietaryRecommendation(user)
            diet.display_recommendations()

            # Ask if user wants to export recommendations
            export = input("\nWould you like to export these recommendations to a text file? (yes/no): ").lower()
            if export == 'yes':
                filename = input("Enter a filename for the export (leave blank for 'DietaryRecommendations.txt'): ")
                if not filename:
                    filename = "DietaryRecommendations.txt"
                diet.export_recommendations(filename)

        except ValueError as ve:
            print(f"Input error: {ve}")
            print("Please check your input and try again. Ensure all inputs are valid, such as age being a number and gender being 'male' or 'female'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please restart the program or contact support if the issue persists.")
