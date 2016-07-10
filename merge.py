import sys
#unlss i can google or think of another way will have to keep a global list of all the column names excluding the key column name and compare against it each time we
#recursively call merge to make sure that there is not multiple columns of the same name in any of the files

key_value = []

#all other error cases can be handled in here or any helper functions for this function


#problem there is no guarentee where exactly the key column will be in a given csv file so somehow we are going to have to find what position it is at
#in both the lists, i think using a for loop that looks through till it finds the key column and using a counter to find the index
def merge_tables(file_list, columns):

	#this is base case for recusion
	if len(file_list) == 1:
		#print(file_list)
		return file_list
	tables = file_list[0:2]
	#print(tables)
	#we now need to iterate through the first row which has the column names and make sure that the key_value is actually in the table
	#then once it is established that it is in there need to move on to the remaining rows and start to read in their first values seperated by the commas
	try:
#file 1
		with open(tables[0]) as M:
			
			col1 = M.readline().split(',')
			col1 = [line.strip() for line in col1]
			if any(name in col1 for name in columns):
				print("file contains a duplicate column name") #need to print name as well as file
				exit()
			for value in col1:
				columns.add(value)
				
			try:
				columns.remove(key_value)
			except KeyError:
				print("file does not contain the key column")
				exit()
				
			L_M = []
			length = len(col1)
			for read in M:
				temp = read.split(',')
				if len(temp) != length:
					print("incorrect number of columns in M")
					exit()
				temp = [read.strip() for read in temp]
				L_M.append(temp)
			#print(L_M)
#file 2
			try:
				with open(tables[1]) as T:
				
					col2 = T.readline().split(',')
					col2 = [line.strip() for line in col2]
					if any(name in col2 for name in columns):
						print("file contains a duplicate column name") #need to print name as well as file
						exit()
					for value in col2:
						columns.add(value)
						
					try:
						columns.remove(key_value)
					except KeyError:
						print("file does not contain the key column")
						exit()
						
					L_T = []
					length = len(col1) 
					for read in T:
						temp = read.split(',')

						if len(temp) != length:
							print("incorrect number of columns in T")
							exit()
						temp = [read.strip() for read in temp]
						L_T.append(temp)
					#print(L_T)
#at this point have all the info from the files into 2 lists for the column names (keys) and 2 lists for all the rest of the info
			except EnvironmentError:
				print("couldnt open file")
				exit()
				
	except EnvironmentError:
		print("couldnt open file dun goof")
		exit()

#create a dictonary now that contains each column as a list
#now to avoid the conundrum of having the key column being in different columns in each file and not knowing where it will be, we can make a dictonary for each file and then just join both of those dictonaries
#all the column names are different except the key, so we may not have to actually make 2 dictonaries just reorganize each list
	
#gets the positions of the key column in  each file, i is for the master file and j is for the file being merged with it
	i = 0
	for element in col1:
		if element == key_value:
			break
		i = i + 1

	j = 0
	for element in col2:
		if element == key_value:
			break
		j = j + 1

#need to somehow turn the rows into columns, there may be some matrix algebra i can do here, wait i think that there actually is. Thats it its the tranpose we want the tranpose of this 2D array now there may have been something in 212 like one of the matrix groups that allowed for this or can also check and see about 211 or you know can just google it. well lets think for doing the tranpose we are really just flipping everything along the diagonal so (a,a) -> (a,a) but (a,b) -> (b,a) awwww shite can just do that mother fucker, hells yeah we don figured it out now how does the actual indexing into lists of lists work and how can this actually be done. That my friend is a whole nother problem that i dont really know how to solve, so to google for that one.
#Conversely to that whole great big paragraph on matrix transposes can just see what ryan did and do that but want to do this shit yourself, to prove you can.
#need to create new file here and then delete at zero insert new file then remove at 1
	#print(L_M)
	tups = zip(*L_M)
	del L_M[:]
	for t in tups:
		L_M.append(t)
	
	#print(L_M)
	
	tups = zip(*L_T)
	del L_T[:]
	for t in tups:
		L_T.append(t)
	
	#print(L_T)
	D_M = dict(zip(col1, L_M))
	D_T = dict(zip(col2, L_T))
	#print(D_M)
	#print(D_T)
	D_T[key_value] += D_M[key_value]
	D_M.update(D_T)
	print(D_M)
	
	
	
	file_list.pop(1)
	#print(file_list)
	
	file_list = merge_tables(file_list,columns)
	#can just move the key column to the front here after all the recursion is done
	return file_list
	

if __name__ == "__main__":

	file_list = []
	length = len(sys.argv)
	if length < 3:
		print("Usage: python3 merge.py <key column name> <file 1> <file 2> <file 3> <file 4> ...")
		exit()
	for arg in sys.argv:
		file_list.append(arg)
	key_value = file_list[1].strip()
	file_list = file_list[2:]
	columns = set()
	file_list = merge_tables(file_list,columns)