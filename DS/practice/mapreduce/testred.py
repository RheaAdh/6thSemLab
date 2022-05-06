import fileinput

prev_country = None
maxpop = 0

for line in fileinput.input():
	line = line.strip().split('\t')
	if len(line)==2:
		country,population = line
		population = int(population)
		if prev_country == None:
				prev_country = country
				maxpop = population
				continue
		if prev_country==country:
			if population>maxpop:
				maxpop=population
		else:
			print("{}\t{}".format(prev_country,maxpop))
			prev_country = country
			maxpop = population


print(prev_country,'\t',maxpop)