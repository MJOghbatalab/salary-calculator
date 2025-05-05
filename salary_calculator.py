with open("README.md",encoding="utf-8") as f:
    contents = f.read()
    print(contents)
    

from importlib.resources import contents


def calculate_salary(hours_worked, hourly_rate):
    return hours_worked * hourly_rate

if __name__ == "__main__":
    hours = float(input("How many hours did you work?"))
    rate = float(input("What is your hourly rate?"))
    salary = calculate_salary(hours, rate)
    print(f"Your salary this month is : {salary:,} Rials ...")

