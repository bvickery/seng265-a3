import sys
#unlss i can google or think of another way will have to keep a global list of all the column names excluding the key column name and compare against it each time we
#recursively call merge to make sure that there is not multiple columns of the same name in any of the files

key_value = []

#all other error cases can be handled in here or any helper functions for this function
def merge_tables(file_list, columns):
	if len(file_list) == 1:
		#print(file_list)
		return
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

			except EnvironmentError:
				print("couldnt open file")
				exit()
				
	except EnvironmentError:
		print("couldnt open file dun goof")
		exit()
#need to create new file here and then delete at zero insert new file then remove at 1
	file_list.pop(1)
	#print(file_list)
	merge_tables(file_list,columns)
	return

#need to catch the error of not enough arguments being given do this in main
if __name__ == "__main__":

	file_list = []
	length = len(sys.argv)
	if length < 2:
		print("Usage: python3 merge.py <key column name> <file 1> <file 2> <file 3> <file 4> ...")
		exit()
	for arg in sys.argv:
		file_list.append(arg)
	key_value = file_list[1].strip()
	file_list = file_list[2:]
	columns = set()
	merge_tables(file_list,columns)	