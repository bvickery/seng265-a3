import sys

def merge_tables(file_list, key_value):
	
	L = []
	columns = set()

	for file in file_list:
#this try and except might be fine but will just have to add the finding of the key_column index into here, then use bills table_to_dict and join grades program tp finish solving this, because it looks like if i try to continue doing this the way i currently am will basically have to redo a lot of stuff because it was lost when making it into a dict of lists
		try:
			
			with open(file) as M:
			
				for line in M:
					if len(line.strip()) == 0:
						continue
					else:
						col1 = line.split(',')
						break

				col1 = [line.strip() for line in col1]
				name = []
				if any(name in col1 for name in columns):
					print("file: %s contains a duplicate column name: %s"%(file,name)) #need to print name as well as file
					exit()
				for value in col1:
					columns.add(value)
					
				try:
					columns.remove(key_value)
				except KeyError:
					print("file: %s does not contain the key column: %s"%(file,key_value))
					exit()
					
				L_M = [col1]
				length = len(col1)
				for read in M:
					if len(read.strip()) == 0:
						continue
					else:
						temp = read.split(',')
						if len(temp) != length:
							print("incorrect number of columns in: %"%(file))
							exit()
						temp = [read.strip() for read in temp]
						L_M.append(temp)
						
		except EnvironmentError:
			print("couldnt open file: %s"%(file))
			exit()

		i = 0
		for element in col1:
			if element == key_value:
				break
			i = i + 1
		
		L.append(table_to_dict(L_M,i))

	for x in L:

		dict1 = L[0]
		
		dict2 = L[1]
		columns1 = len(dict1[key_value])
		columns2 = len(dict2[key_value])
		L.pop(1)
		L.pop(0)

		all_student_ids = set()
		for student_id in dict1:
			all_student_ids.add(student_id)
		for student_id in dict2:
			all_student_ids.add(student_id)

		joined_table = []
		for student_id in all_student_ids:
			if student_id not in dict1:

				entry1 = ['']*columns1
	
			else:
				entry1 = dict1[student_id]

			if student_id not in dict2:

				entry2 = ['']*columns2
	
			else:
				entry2 = dict2[student_id]

			result_row = [student_id] + list(entry1) + list(entry2)
			joined_table.append(result_row)
		
		dict_T = table_to_dict(joined_table,0)
		L.insert(0,dict_T)

	print(L)
	return file_list

	
def table_to_dict(T, key_column_index):
	output_dict = {}
	for row in T:
		key = row[key_column_index]
		rest_of_row = row[0:key_column_index] + row[key_column_index+1:]
		if key in output_dict:
			raise DuplicateKeyError(key)
		output_dict[key] = rest_of_row
	return output_dict
	

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

	file_list = merge_tables(file_list,key_value)