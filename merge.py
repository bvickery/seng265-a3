''' merge.py
	Seng 265 Summer 2016
	Brandon Vickery
	07/11/16
'''
# *CITATION* USED BOTH OF THE FUNCTIONS FROM JOIN_GRADES.PY WRITTEN BY BILL BIRD, IT IS NOTED WHERE THEY ARE USED
import sys

def merge_tables(file_list, key_value):

	L = []
	columns = set()

	for file in file_list:
		
		try:
		#check if the file has no data i.e. is empty
			flag = True
			with open(file) as empty_check:
				for line in empty_check:
					if len(line.strip()) == 0:
						continue
					else:
						flag = False
						break
				
				if flag:
					sys.stderr.write("Error: file %s contains no data"%(file))
					exit()
		
		
		except EnvironmentError:
			sys.stderr.write("Error: Unable to open %s"%(file))
			exit()

		try:
			
			with open(file) as M:
			
				for line in M:
					if len(line.strip()) == 0:
						continue
					else:
						col1 = line.split(',')
						break

				col1 = [line.strip() for line in col1]

				#checks for duplicate column names in the current file
				temp_set = set()
				for header in col1:
					if header in temp_set:
						sys.stderr.write("file: %s contains a duplicate column name: %s"%(file,header))
						exit()
						
					temp_set.add(header)
				
				#duplicate column names over different files
				for name in col1:
					if name in columns:
						sys.stderr.write("file: %s contains a duplicate column name: %s"%(file,name))
						exit()

				for value in col1:
					columns.add(value)
					
				try:
					columns.remove(key_value)
				except KeyError:
				#file does not contain the key column
					sys.stderr.write('Error: File %s No column called "%s"'%(file,key_value))
					exit()
					
				L_M = [col1]
				length = len(col1)
				for read in M:
					if len(read.strip()) == 0:
						continue
					else:
						temp = read.split(',')
						if len(temp) != length:
						
							sys.stderr.write("incorrect number of columns in: %s"%(file))
							exit()
						temp = [read.strip() for read in temp]
						L_M.append(temp)
						
		except EnvironmentError:
			sys.stderr.write("Error: Unable to open %s"%(file))
			exit()

		i = 0
		for element in col1:
			if element == key_value:
				break
			i = i + 1
		
		L.append(table_to_dict(L_M,i,file))

#only one file case
	if len(L) == 1:
		D = L[0]
		keys = list(D.keys())
		keys.remove(key_value)
		keys.sort()
		D[key_value].insert(0,key_value)
		print(",".join(D[key_value]))
		for i in keys:
			print("%s,"%(i) + ",".join(D[i]))
		return

#multiple files case
#got this from bill bird join_grades made a few modifications so that it worked with my code
	for x in range(len(L)-1):

		dict1 = L[0]

		dict2 = L[1]

		columns1 = len(dict1[key_value])
		columns2 = len(dict2[key_value])

		L.remove(dict1)
		L.remove(dict2)

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

		dict_T = table_to_dict(joined_table,0,file)

		L.insert(0,dict_T)

	D = L[0]
	keys = list(D.keys())
	keys.remove(key_value)
	keys.sort()
	D[key_value].insert(0,key_value)
	print(",".join(D[key_value]))
	for i in keys:
		print("%s,"%(i) + ",".join(D[i]))
	
	return

#taken from bill bird from join_grades not changed at all
def table_to_dict(T, key_column_index,file):
	output_dict = {}
	for row in T:
		key = row[key_column_index]
		rest_of_row = row[0:key_column_index] + row[key_column_index+1:]
		if key in output_dict:
			sys.stderr.write("duplicate key: %s in file: %s"%(key,file))
			exit()
		output_dict[key] = rest_of_row
	return output_dict
	

if __name__ == "__main__":

	file_list = []
	length = len(sys.argv)
	if length < 3:
		
		sys.stderr.write("Usage: python3 merge.py <key column name> <file 1> <file 2> <file 3> <file 4> ...")
		exit()
	for arg in sys.argv:
		file_list.append(arg)
	key_value = file_list[1].strip()
	file_list = file_list[2:]

	merge_tables(file_list,key_value)