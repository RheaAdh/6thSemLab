import fileinput
i=0
for line in fileinput.input():
	line = line.strip().split(',')
	if i!=0:
		if len(line)==6:
			country,continent,year,lifeExpectancy,population,gdpPerCapita = line
			print ("{}\t{}".format(country,population))
	i=i+1