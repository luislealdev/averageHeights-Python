heights = input("Enter the height separated by commas ex. (170, 175...)").split(',')
for n in range(0,len(heights)):
    heights[n] = int(heights[n])

#Calculate average
total = 0
for height in heights:
    total += height
average = round(total/len(heights))
print(f'The average is {average}')