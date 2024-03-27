weight = input("Weight: ")
unit = input("Lbs or Kgs ")

if unit == 'lbs':
    mass = weight * int(0.45)
    print(mass)
else:
    mass = weight * int(2.2)
    print(mass)
