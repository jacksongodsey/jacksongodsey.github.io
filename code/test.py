def employee():
    list = []
    employee_name = input()
    employee_pay_rate = float(input())
    employee_hours_worked = float(input())
    list.append(employee_name, employee_pay_rate, employee_hours_worked)
    return list

employee_one = employee()
employee_two = employee()
employee_thre = employee()

def initial_pay(hours, rate):
    if hours <= 40:
        return hours * rate
    else:
        othours = hours - 40
        return othours * 1.5 * rate + 40 * rate

def employerexp(gross):
    empsocsec = gross * 0.0615
    workman = gross * 0.0085
    futa = gross * 0.0038
    suta = gross * 0.0042
    insurance = 168.50
    return empsocsec + workman + futa + suta + insurance

def employeeexp(gross):
    workersocsec = gross * 0.0615
    medical = 30.00
    fedtax = gross * 0.0612
    return workersocsec + medical + fedtax


employee_one_initial = initial_pay(employee_one[1], employee_one[2])
employee_two_initial = initial_pay(employee_two[1], employee_two[2])
employee_three_initial = initial_pay(employee_three[1], employee_three[2])

employee_one_expenses = employerexp(employee_one_initial)
employee_two_expenses = employerexp(employee_two_initial)
employee_three_expenses = employerexp(employee_three_initial)
