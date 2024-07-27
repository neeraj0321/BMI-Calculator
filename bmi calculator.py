def calculate(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def get_weight():
    print("Please enter your weight in kilograms: ")
    weight = float(input())
    return weight

def get_height():
    print("Please enter your height in meters:")
    height = float(input())
    return height

def display_results(weight, height, bmi, category, Name):
    print("\nCalculating your BMI...\n")
    print(f"Your weight: {weight:.2f} kg")
    print(f"Your height: {height:.2f} meters")
    print(f"Your BMI is: {bmi:.2f}")
    print(f"{Name} you are classified as: {category}")

def entered_weight(weight):
    print(f"You have entered your weight as {weight:.2f} kg.")

def entered_height(height):
    print(f"You have entered your height as {height:.2f} meters.")

def main():
    
    weight = get_weight()
    entered_weight(weight)
    
    height = get_height()
    entered_height(height)
    
    bmi = calculate(weight, height)
    category = classify(bmi)
    print(bmi)
    display_results(weight, height, bmi, category, Name)

if __name__ == "__main__":
    while True:
        Name = input("Enter your name : ").strip()
        
        print("Hello ",Name,", Welcome to the BMI Calculator")
        
        main()
        print("\nWould you like to calculate another BMI? (yes/no)")
        restart = input().strip().lower()
        if restart == 'no':
            print("come back later!")
            break
