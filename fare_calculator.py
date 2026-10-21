# Travel Fare Calculator
FARE_RATE = 14

while True:
    name = input("Enter passenger name: ")
    if name.strip():
        break
    else:
        print("Invalid name. Name cannot be empty. ")
        
    
while True:
    d = float(input("Enter distance (km): "))
    if d >= 0:
        break
    else:
        print("Invalid distance, enter a number greater than 0.")
        
    
while True:
    passengers = int(input("Enter number of passengers: "))
    if passengers >= 0:
        break
    else:
        print("Invalid passengers, enter a positive whole number")
        
total_fare = d * FARE_RATE * passengers

print(passengers, "passengers and", name)
print("Total fare: PHP", round(total_fare, 2))
