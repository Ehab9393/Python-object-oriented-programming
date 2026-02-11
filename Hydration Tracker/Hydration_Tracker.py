import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# User Class
# -----------------------------
class User:
    def __init__(self, name, weight, activity_level):
        """
        Initialize user attributes.
        :param name: User's name
        :param weight: User's weight in kg
        :param activity_level: Daily activity level ('low', 'medium', 'high')
        """
        self.name = name
        self.weight = weight
        self.activity_level = activity_level.lower()

    def recommended_water_intake(self):
        """
        Calculate recommended daily water intake in liters.
        Base: 35 ml per kg of body weight, plus activity adjustment:
        - Low: no extra
        - Medium: +0.5 L
        - High: +1 L
        """
        base_intake = self.weight * 0.035  # in liters
        if self.activity_level == 'medium':
            base_intake += 0.5
        elif self.activity_level == 'high':
            base_intake += 1.0
        return round(base_intake, 2)

# -----------------------------
# Water Intake Class
# -----------------------------
class WaterIntake:
    def __init__(self, daily_intake_list):
        """
        Track daily water intake.
        :param daily_intake_list: List of water consumed each day in liters
        """
        self.daily_intake = daily_intake_list

    def total_intake(self):
        return round(sum(self.daily_intake), 2)

    def average_intake(self):
        if len(self.daily_intake) == 0:
            return 0
        return round(sum(self.daily_intake) / len(self.daily_intake), 2)

# -----------------------------
# Chart Strategy Pattern
# -----------------------------
class ChartStrategy:
    def create_chart(self, *args):
        pass

class BarChartStrategy(ChartStrategy):
    def create_chart(self, daily_intake, recommended):
        """
        Bar chart comparing daily water intake with recommended intake
        """
        days = [f"Day {i+1}" for i in range(len(daily_intake))]
        x = np.arange(len(days))
        width = 0.4

        plt.figure(figsize=(10, 5))
        plt.bar(x - width/2, daily_intake, width, label="Actual Intake", color="skyblue")
        plt.bar(x + width/2, [recommended]*len(days), width, label="Recommended", color="lightgreen")
        plt.xticks(x, days)
        plt.ylabel("Water Intake (L)")
        plt.title("Daily Water Intake vs Recommended")
        plt.legend()
        plt.tight_layout()
        plt.savefig("water_intake_bar_chart.jpg")
        plt.show()

class LineChartStrategy(ChartStrategy):
    def create_chart(self, daily_intake, recommended):
        """
        Line chart showing daily water intake trends
        """
        days = [f"Day {i+1}" for i in range(len(daily_intake))]
        plt.figure(figsize=(10, 5))
        plt.plot(days, daily_intake, marker='o', label="Actual Intake", linestyle='-')
        plt.plot(days, [recommended]*len(daily_intake), marker='x', label="Recommended", linestyle='--')
        plt.ylabel("Water Intake (L)")
        plt.title("Daily Water Intake Trend")
        plt.legend()
        plt.tight_layout()
        plt.savefig("water_intake_line_chart.jpg")
        plt.show()

class Visualiser:
    """
    Visualiser uses a chart strategy to generate charts
    """
    def __init__(self, strategy: ChartStrategy):
        self.strategy = strategy

    def create_chart(self, *args):
        self.strategy.create_chart(*args)

# -----------------------------
# Data Processor
# -----------------------------
class DataProcessor:
    @staticmethod
    def export_data(user, water_intake):
        """
        Export user details and water intake data to a text file
        """
        filename = f"{user.name}_water_log.txt"
        with open(filename, "w") as f:
            f.write(f"User: {user.name}\n")
            f.write(f"Weight: {user.weight} kg\n")
            f.write(f"Activity Level: {user.activity_level.capitalize()}\n")
            f.write(f"Recommended Daily Intake: {user.recommended_water_intake()} L\n")
            f.write("\nDaily Water Intake:\n")
            for i, intake in enumerate(water_intake.daily_intake):
                f.write(f"Day {i+1}: {intake} L\n")
            f.write(f"\nTotal Intake: {water_intake.total_intake()} L\n")
            f.write(f"Average Intake: {water_intake.average_intake()} L\n")
        print(f"Data exported to {filename}")

# -----------------------------
# Main Program
# -----------------------------
if __name__ == "__main__":
    try:
        # User Input
        name = input("Enter your name: ")
        weight = float(input("Enter your weight (kg): "))
        activity_level = input("Enter your activity level (low, medium, high): ").lower()
        days = int(input("Enter number of days to track: "))

        # Initialize user
        user = User(name, weight, activity_level)
        recommended = user.recommended_water_intake()

        # Collect daily intake
        daily_intake = []
        for i in range(days):
            intake = float(input(f"Enter water intake for Day {i+1} (in liters): "))
            daily_intake.append(intake)

        # Initialize WaterIntake object
        water_log = WaterIntake(daily_intake)

        # Display summary
        print(f"\nRecommended Daily Intake: {recommended} L")
        print(f"Total Intake: {water_log.total_intake()} L")
        print(f"Average Intake: {water_log.average_intake()} L")

        # Ask user for chart visualization
        save_charts = input("Would you like to generate charts? (yes/no): ").lower()
        if save_charts == "yes":
            visualiser = Visualiser(BarChartStrategy())
            visualiser.create_chart(daily_intake, recommended)
            visualiser = Visualiser(LineChartStrategy())
            visualiser.create_chart(daily_intake, recommended)

        # Ask user to export data
        export = input("Would you like to export your water intake data? (yes/no): ").lower()
        if export == "yes":
            DataProcessor.export_data(user, water_log)

    except ValueError as ve:
        print(f"Input error: {ve}. Please enter valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
