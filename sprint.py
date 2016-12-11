import sys
import csv
import string

contents = []
row2Group = {}
table_string = ""

with open('a2_input.csv') as input_file:

  for row in csv.reader(input_file):
        contents = contents + [row]


		print(contents[0][0])
		print("Cell at index 0,1:")
		print(contents[0][1])
		print("Cell at index 1,0:")
		print(contents[1][0])

	for row1, row2, numericalRow in csv.reader(input_file):
        row2Group.setdefault(row2.strip(), []).append(int(numericalRow.strip()))

	for row2, numericalGroup in sorted(row2Group.items()):
    	print ("{}: {}".format(row2, sorted(numericalGroup)[len(numericalGroup//2)] ))


    
    for row in reader:
        table_string += "<tr>" + \
                          "<td>" + \
                              string.join( row, "</td><td>" ) + \
                          "</td>" + \
                        "</tr>\n"
    
htmlfile = open('output.html','w')
htmlfile.write(table_string)
htmlfile.close()
