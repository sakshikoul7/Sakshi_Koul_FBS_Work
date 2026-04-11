length= int(input('Enter the length: '))
breadth = int(input('Enter the breadth: '))
radius = int(input('Enter the radius: '))
pi=3.14

area = (length*breadth) + (pi*radius*radius)/2
perimeter= (2*length) + breadth + (pi*radius)

print(f'Area of the shape is {area}')
print(f'Perimeter of the shape is {perimeter}')