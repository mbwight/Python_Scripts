__author__ = 'Mark'
print("Welcome to the payroll manager")

def payroll_calculator(name,hoursworked,payrate):
    salary = hoursworked * payrate
    overtime = 0
    overtimemoney = overtime * 1.5
    totalpay = overtime + overtimemoney + salary

    if hoursworked > 40:
        overtime = hoursworked - 40
        overtimemoney = overtime * 1.5
        totalpay = overtime + overtimemoney + salary
    print(name, "your total paycheck is", totalpay)

def main():
    payroll_calculator("bob",41,10)
    payroll_calculator("Carl", 10,10)
    payroll_calculator("Chuck", 50,12.50)
    payroll_calculator("Rachel", 40, 13)
    payroll_calculator("Gee", 20, 30)

main()
