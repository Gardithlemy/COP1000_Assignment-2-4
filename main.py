# input statements
salary = float(input())
numDependents = float(input())

# calculate taxes here
stateTax = salary * 6.5/100
federalTax = salary* 28/100
dependentDeduction = salary*2.5* numDependents/100
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding
# output statements
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: $" + str(dependentDeduction))


print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
