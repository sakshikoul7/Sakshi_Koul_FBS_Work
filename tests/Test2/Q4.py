#To calculate the toatl cost of painting. The interior of building with four equal sized walls.
side = float(input("Enter the length of one side of the wall: "))
rate = float(input("Enter the interior painting rate per square meter: "))
total_walls = 4
area = side * side
total_area = total_walls * area
total_cost = total_area * rate
print("Total cost of painting the interior of the building is:", total_cost)