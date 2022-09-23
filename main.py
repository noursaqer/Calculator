
value1 = float(input("Value1="))
print("choose an operation")

print("For plus enter 1 or +")
print("For minus enter 2 or -")
print("For multiply enter 3 or *")
print("For divide enter 4 or / ")
print("For power enter 5 or ^")
print("For modulus enter 6 or %")
process = input("operation:")
value2 = float(input("Value2= "))


result_of_division = value1 / value2
result_of_multiplication = value1 * value2
result_of_addition = value1 + value2
result_of_subtraction = value1 - value2
result_of_power = value1 ** value2
result_of_modulus = value1 % value2

if process == "1" or process == "+":
    print("The result is " + str(value1+value2))
    print("you have other options; round, floor, and ceil")
    other = input("option picked: ")
    if other == "round":
        print("The round result is " + str(round(value1 + value2)))
    if other == "floor":
        print("The floored result is "+ str(result_of_addition.__floor__()))
    if other == "ceil":
      print("The ceiled result is "+ str(result_of_addition.__ceil__()))


elif process == "2" or process == "-":
    print("The result is " + str(value1-value2))
    print("you have other options; round, floor, and ceil")
    other = input("option picked: ")
    if other == "round":
        print("The round result is " + str(round(value1 - value2)))
    if other == "floor":
        print("The floored result is "+ str(result_of_subtraction.__floor__()))
    if other == "ceil":
      print("The ceiled result is "+ str(result_of_subtraction.__ceil__()))


elif process == "3" or process == "*":
    print("The result is " + str(value1*value2))
    print("you have other options; round, floor, and ceil")
    other = input("option picked: ")
    if other == "round":
        print("The round result is " + str(round(value1 * value2)))
    if other == "floor":
        print("The floored result is "+ str(result_of_multiplication.__floor__()))
    if other == "ceil":
      print("The ceiled result is "+ str(result_of_multiplication.__ceil__()))


elif process == "4" or process == "/":
    print("The result is " + str(value1/value2))
    print("you have other options; round, floor, and ceil")
    other = input("option picked: ")
    if other == "round":
        print("The round result is " + str(round(value1 / value2)))
    if other == "floor":
        print("The floored result is "+ str(result_of_division.__floor__()))
    if other == "ceil":
      print("The ceiled result is "+ str(result_of_division.__ceil__()))

elif process == "5" or process == "^":
    print("The result is " + str(value1**value2))
    print("you have other options; round, floor, and ceil")
    other = input("option picked: ")
    if other == "round":
        print("The round result is " + str(round(value1 ** value2)))
    if other == "floor":
        print("The floored result is "+ str(result_of_power.__floor__()))
    if other == "ceil":
      print("The ceiled result is "+ str(result_of_power.__ceil__()))


elif process == "6" or process == "%":
    print("The result is " + str(value1%value2))
    print("you have other options; round, floor, and ceil")
    other = input("option picked: ")
    if other == "round":
        print("The round result is " + str(round(value1 % value2)))
    if other == "floor":
        print("The floored result is "+ str(result_of_modulus.__floor__()))
    if other == "ceil":
      print("The ceiled result is "+ str(result_of_modulus.__ceil__()))

else:
    print("Please, choose a valid operation")











