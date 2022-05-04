import fileinput
province_count = 0
confirm_total = 0
for line in fileinput.input():
data = line.strip().split("\t")
if len(data) != 2:
# Something has gone wrong. Skip this line.
 continue
current_key, current_value = data
if current_value == 'Confirmed':
 pass
else:
 province_count += 1
 confirm_total += float(current_value)
print (province_count, "\t", confirm_total)