area = float(input("Enter area of one wall:"))
interior_rate= float(input("Enter interior rate: "))
exterior_rate= float(input("Enter exterior rate: "))

total_walls = 8
shared_walls = 2

interior_area = total_walls *area
exterior_area = (total_walls - shared_walls) * area

interior_cost = interior_area * interior_rate
exterior_cost = exterior_area * exterior_rate

total_cost = interior_cost + exterior_cost
print("Interior cost:", interior_cost)
print("Exterior cost:", exterior_cost)
print("Total cost:", total_cost)