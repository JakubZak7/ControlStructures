driving_mode = input("Enter driving mode (A/M/E): ")
distance = int(input("Enter distance: "))


if driving_mode == "A":
    fuel_consuption = 7
elif driving_mode == "M":
    fuel_consuption = 9
elif driving_mode == "E":
    fuel_consuption = 6
else:
    fuel_consuption = 0


if distance == 100:
    total_consumption = fuel_consuption
else:
    total_consumption = fuel_consuption * (distance/100)


print(total_consumption)
