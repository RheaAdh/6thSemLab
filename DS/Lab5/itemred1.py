import fileinput
sex_count = 0
chol_total = 0
for line in fileinput.input():
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    current_key, current_value = data
    if current_value == 'chol':
        pass
    else:
        sex_count += 1
        chol_total += float(current_value)
chol_avg = chol_total/sex_count
print (sex_count, "\t", chol_avg)