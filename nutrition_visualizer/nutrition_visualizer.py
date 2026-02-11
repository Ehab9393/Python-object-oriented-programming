import matplotlib.pyplot as plt

import numpy as np

# User Class
class User:
    def __init__(self, age, gender, weight, height):
        # Represents a user with basic attributes such as age, gender, weight, and height
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        """
        calculate BMI = weight(kg) / ((height (m))^ 2)
        """
        return round(self.weight / (self.height / 100) ** 2, 2)

# Food Intake Class
class FoodIntake:
    # Stores user's food intake and recommended servings for each food category
    RECOMMENDATION = {
        "vegetables": 6,
        "fruits": 2,
        "grains": 6,
        "meats": 3,
        "dairy": 2.5,
    }

    def __init__(self, vegetables, fruits, grains, meats, dairy):
        self.vegetables = vegetables
        self.fruits = fruits
        self.grains = grains
        self.meats = meats
        self.dairy = dairy

# Strategy Interface
class ChartStrategy:
    # Abstract base class for chart strategies
    def create_chart(self, *args):
        pass


class BMIChartStrategy(ChartStrategy):
    # Strategy for creating a BMI visualization chart
    def create_chart(self, bmi):
        categories = [
            "Very Underweight",
            "Underweight",
            "Healthy Weight",
            "Overweight",
            "Obese",
        ]
        thresholds = [15, 18.5, 24.9, 29.9, 35]
        y_positions = range(len(categories))

        plt.figure(figsize=(8, 6))
        plt.hlines(y=y_positions, xmin=0, xmax=thresholds, colors="black", linewidth=2)
        plt.axvline(x=bmi, color="red", linewidth=2)

        # Display the user's BMI on the chart
        plt.text(
            bmi,
            len(categories),
            f"Your BMI: {bmi:.2f}",
            color="red",
            fontsize=10,
            fontweight="bold",
            ha="center",
        )

        plt.gca().invert_yaxis()

        # Add labels and title
        plt.yticks(y_positions, categories)
        plt.xticks(range(0, 40, 5))
        plt.xlabel("BMI")
        plt.ylabel("Weight Category")
        plt.title("BMI Chart for Adults")

        plt.tight_layout()
        plt.savefig("bmi_chart_updated.jpg")
        plt.show()


class BarChartStrategy(ChartStrategy):
    # Strategy for creating a bar chart comparing actual and recommended food intake
    def create_chart(self, actual, recommended):
        categories = list(actual.keys())
        actual_values = list(actual.values())
        recommended_values = list(recommended.values())

        # Set up positions for the bars
        x = np.arange(len(categories))  # The label locations
        width = 0.35  # The width of the bars

        # Create the figure and the axes
        plt.figure(figsize=(10, 5))

        # Plot bars for recommended and actual values
        plt.bar(
            x - width / 2, recommended_values, width, label="Recommended", color="blue"
        )
        plt.bar(x + width / 2, actual_values, width, label="Actual", color="orange")

        # Add labels, title, and legend
        plt.xlabel("Food Group")
        plt.ylabel("Servings")
        plt.title("Recommended vs Actual Intake")
        plt.xticks(
            ticks=x, labels=categories
        )  # Set the tick labels to the food group names
        plt.legend()

        # Save and display the chart
        plt.tight_layout()
        plt.savefig("grouped_bar_chart.jpg")
        plt.show()


class LineChartStrategy(ChartStrategy):
    # Strategy for creating a line chart comparing actual and recommended food intake
    def create_chart(self, actual, recommended):
        categories = list(actual.keys())  # Food categories
        actual_values = list(actual.values())  # Actual intake values
        recommended_values = list(recommended.values())  # Recommended intake values

        # Create line chart
        plt.plot(categories, actual_values, marker="o", label="Actual", linestyle="-")
        plt.plot(
            categories,
            recommended_values,
            marker="x",
            label="Recommended",
            linestyle="--",
        )
        plt.xlabel("Food Categories")
        plt.ylabel("Servings")
        plt.title("Line Chart: Food Intake vs Recommendations")
        plt.legend()
        plt.savefig("line_chart.jpg")  # Save as .jpg
        plt.show()


class PieChartStrategy(ChartStrategy):
    # Strategy for creating a pie chart to visualize actual and recommended intake
    def create_chart(self, actual):
        categories = actual.keys()  # Food categories
        actual_values = actual.values()  # Actual intake value
        recommended_values = recommended.values()
        # Create subplots for side-by-side pie charts
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))

        # Create pie chart
        # User Intake Pie Chart
        axes[0].pie(actual_values, labels=categories, autopct="%1.1f%%", startangle=90)
        axes[0].set_title("User Intake")
        # Recommended Intake Pie Chart
        axes[1].pie(
            recommended_values, labels=categories, autopct="%1.1f%%", startangle=90
        )
        axes[1].set_title("Recommended Intake")
        # Overall Title
        fig.suptitle("Daily Serving Intake")

        plt.savefig("pie_chart.jpg")  # Save as .jpg
        plt.show()


class Visualiser:
    # Uses a strategy to create different types of charts
    def __init__(self, strategy: ChartStrategy):
        self.strategy = strategy

    def create_chart(self, *args):
        self.strategy.create_chart(*args)


class DataProcessor:
    @staticmethod
    def save_data(user, food_intake):
        # Saves user details and food intake to a file
        with open("user_info.txt", "w") as f:
            f.write(f"Age: {user.age} years\n")
            f.write(f"Gender: {user.gender}\n")
            f.write(f"Weight: {user.weight} kg\n")
            f.write(f"Height: {user.height} cm\n")
            f.write("Daily Serving Intake:\n")

            # Write food intake details
            f.write(f"Vegetables: {food_intake.vegetables} servings\n")
            f.write(f"Fruits: {food_intake.fruits} servings\n")
            f.write(f"Grains: {food_intake.grains} servings\n")
            f.write(f"Meats: {food_intake.meats} servings\n")
            f.write(f"Dairy: {food_intake.dairy} servings\n")


if __name__ == "__main__":
    # Input user details and food intake
    age = int(input("Enter your age (in years): "))
    gender = input("Enter your gender (male or female): ")
    weight = float(input("Enter your weight (in kg): "))
    height = float(input("Enter your height (in cm): "))
    vegetables = float(input("Enter your daily intake of Vegetables (in servings): "))
    fruits = float(input("Enter your daily intake of Fruits (in servings): "))
    grains = float(input("Enter your daily intake of Grains (in servings): "))
    meats = float(input("Enter your daily intake of Meats (in servings): "))
    dairy = float(input("Enter your daily intake of Dairy (in servings): "))

    user = User(age, gender, weight, height)
    food_intake = FoodIntake(vegetables, fruits, grains, meats, dairy)

    # Calculate and display BMI
    bmi = user.calculate_bmi()
    print(f"Your BMI is: {bmi}")

    # Save BMI Chart
    save_bmi = input("Would you like to save the BMI chart? (yes/no): ").lower()
    if save_bmi == "yes":
        visualiser = Visualiser(BMIChartStrategy())
        visualiser.create_chart(bmi)
        print("Visualize BMI saved as visualize_bmi_chart.jpg")

    # Prepare data for visualisation
    actual = {
        "vegetables": food_intake.vegetables,
        "fruits": food_intake.fruits,
        "grains": food_intake.grains,
        "meats": food_intake.meats,
        "dairy": food_intake.dairy,
    }
    recommended = FoodIntake.RECOMMENDATION

    # Ask to save other charts
    save_charts = input("Would you like to save the charts? (yes/no): ").lower()
    if save_charts == "yes":
        visualiser = Visualiser(BMIChartStrategy())
        visualiser.create_chart(bmi)
        print("Visualize BMI saved as visualize_bmi_chart.jpg")
        visualiser = Visualiser(BarChartStrategy())
        visualiser.create_chart(actual, recommended)
        print("Visualize Bar Chart saved as visualize_bar_chart_chart.jpg")

        visualiser = Visualiser(LineChartStrategy())
        visualiser.create_chart(actual, recommended)
        print("Visualize Line Chart saved as visualize_line_chart_chart.jpg")

        visualiser = Visualiser(PieChartStrategy())
        visualiser.create_chart(actual)
        print("Visualize Pie Chart saved as visualize_pie_charts_chart.jpg")

    # Optionally export user data
    export_data = input("Do you also want to export your data? (yes/no): ").lower()
    if export_data == "yes":
        DataProcessor.save_data(user, food_intake)
        print("Data has been exported to user_info.txt")
