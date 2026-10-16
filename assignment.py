below_range = 0
in_range = 0
above_range = 0
total_width = 0 

def classify(value):
    if value < 98:
        return "Below range"
    elif 98 <= value <= 102:
        return "In range"
    else:
        return "Above range"   

def calculate_average(total, count):
    return total / count

tiles = int(input("Enter the number of tiles: "))

for i in range(tiles):
    width = int(input("Enter the width for tile : "))
    total_width += width
    

    category = classify(width)
    print(category)
  
    if category == "Below range":
        below_range += 1
    elif category == "In range":
        in_range += 1
    elif category == "Above range":
        above_range += 1

average_width = total_width / tiles

print(f"Total width: {total_width} g")
print(f"Average width: {average_width} g ")

print(f"Below range: {below_range}")
print(f"In range: {in_range}")
print(f"Above range: {above_range}")