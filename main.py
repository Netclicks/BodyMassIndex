def calculate_bmi(height_feet, height_inches, weight_pounds):
    # Convert height to inches
    total_height_inches = (height_feet * 12) + height_inches
    # Convert height to meters
    height_meters = total_height_inches * 0.0254
    # Convert weight to kilograms
    weight_kg = weight_pounds * 0.453592
    # Calculate BMI
    bmi = weight_kg / (height_meters ** 2)
    # Round to one decimal place
    bmi = round(bmi, 1)
    return bmi


def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("BMI Calculator")
    try:
        height_feet = int(input("Enter just your height in feet: "))
        height_inches = int(input("Enter additional height in inches: "))
        weight_pounds = float(input("Enter weight (pounds): "))

        bmi = calculate_bmi(height_feet, height_inches, weight_pounds)
        category = categorize_bmi(bmi)

        print(f"\nYour BMI is: {bmi}")
        print(f"Category: {category}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()

