# EXERCISE:
# create a function that reads a csv_file into a python list of lists
# without using csv library

# Every inner list contains a full row of the csv file,
# The items inside each inner list correspond to the items on its
# corresponding line of the csv file

# ex. csv file w2day4car.csv (with ; as separator) should return
# list_out = [['car1','red','2000'],['car2','blue',300],['car3','black','5000]]
# if the file I want to read is in this same folder, I don't need to put all the path


def read_csv(csv_file_in,separator):
    list_out = []
    fh1 = open(csv_file_in,'r')
    csv_content = fh1.read()
    csv_content_rowsplit= csv_content.split('\n')
    for r in csv_content_rowsplit:
        csv_row_items = r.split(separator)
        list_out.append(csv_row_items)
    fh1.close()
    print ('list out is:', list_out)
