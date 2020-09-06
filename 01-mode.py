def Mode(List): 
	counter = 0
	num = List[0] 
	
	for i in List: 
		curr_frequency = List.count(i) 
		if(curr_frequency> counter): 
			counter = curr_frequency 
			num = i 

	return num 

numbers = [1,2,3,4,5,6,6,8,8,6,9]
grades = [87.5, 88.5, 60.5, 90.5, 88.5]

print(Mode(numbers))
print(Mode(grades))