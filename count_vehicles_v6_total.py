import os
print(os.getcwd())
#os.chdir('runs/inference/exp/labels')
pwd=os.getcwd()
entries = os.listdir(pwd)
bicycle=0
car=0
motorcycle=0
bus=0
truck=0
cntveh=0
for entry in entries:
	#print('\n File ',entry,'\n')
	file = open(entry, "rt")
	data = file.read()
	words = data.split()

	
	n=words.count("1")
	if n>0:
		#print(n , 'bicycle')
		cntveh=cntveh+n
		bicycle=bicycle+n
	n=words.count("2")
	if n>0:
		#print(n , 'cars')
		cntveh=cntveh+n
		car=car+n
	n=words.count("3")
	if n>0:
		#print(n , 'Motorcycle')
		cntveh=cntveh+n
		motorcycle=motorcycle+n
	n=words.count("5")
	if n>0:
		#print(n , 'Bus')
		cntveh=cntveh+n
		bus=bus+n
	n=words.count("7")
	if n>0:
		#print(n , 'Truck')
		cntveh=cntveh + n
		truck=truck+n
print('Total vehicles :- ',cntveh,'\n')
print('bicycle :- ',bicycle)
print('car :- ',car)
print('motorcycle :- ',motorcycle)
print('bus :- ',bus)
print('truck :- ',truck)
