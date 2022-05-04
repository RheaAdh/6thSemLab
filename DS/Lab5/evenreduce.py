import fileinput
sum = 0
for line in fileinput.input():
    print('line',line)

    data = line.strip().split("-")
    print(data)
    current_key = data[0]
    current_value=data[1]
    sum += int(current_value)
print("Number of even numbers is:", sum)