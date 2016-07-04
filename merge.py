
import sys
#unlss i can google or think of another way will have to keep a global list of all the column names excluding the key column name and compare against it each time we
#recursively call merge to make sure that there is not multiple columns of the same name in any of the files



#all other error cases can be handled in here or any helper functions for this function
def merge_tables(file_list):
	key_value = file_list[1]
	tables = file_list[2:]
	#print(tables)
	for table in tables:
		with open(table) as t:
			#we now need to iterate through the first row which has the column names and make sure that the key_value is actually in the table
			#then once it is established that it is in there need to move on to the remaining rows and start to read in their first values seperated by the commas
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

	merge_tables(file_list)