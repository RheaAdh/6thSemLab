import fileinput
transactions_count = 0
sales_total = 0
for line in fileinput.input():
    data = line.strip().split("\t")
    print(data)
    if len(data) != 2:
        continue
    current_key, current_value = data
    transactions_count += 1
    sales_total += float(current_value)
    print('Transaction #',transactions_count)
    print(current_key,'->',current_value)

print ('Total sales->', "\t", sales_total)