#task 2: preparing data

#requirements
#1 filter products to only include Pink Morsels;
#2 tranform sales: sales = price * quantity;
#3 include date as-is;
#4 include region as-is;

#flow
#1 define 
#2 transform
#3 transfer

#active code
import csv

#input info
in_1 = str("daily_sales_data_")

#output info
name = str("ouput.csv")
fields = ["Sales", "Date", "Region"]

#buffers
p_temp_list = []
i_list = []
d_list = []
r_list = []
q_list = []
p_list = []
s_list = []
row =[]

#input processing
def prep(l: int, u: int, source: str):
   
   for c in range(l, u+1):
      input = source
      input += str(c)
      input += str(".csv")

      with open(input, 'r') as input:
         read = csv.reader(input)
         next(read, None)

         for col in read:
            p_temp_list.append(col[1])
            q_list.append(col[2])
            i_list.append(col[0])
            d_list.append(col[3])
            r_list.append(col[4])            

def collate():

   global p_list
   global s_list
   global row
   n = len(p_temp_list)
   p_list = ["null"]*(n)
   s_list = ["null"]*(n)
   row = ["null"]*(n)

   for i in range(0, n):
      p_list[i] = p_temp_list[i].strip("$")
      s_list[i] = int(q_list[i])*float(p_list[i])
      row[i] = [s_list[i], d_list[i], r_list[i]]

#output processing
def csv_out(filename: str, entry: list, fields, filter: list, criteria: str):

   with open(filename, 'w') as output:

      write = csv.writer(output, lineterminator="\n")
      write.writerow(fields)
      n = len(entry)

      for i in range (1, n):
         if filter[i] == criteria:
            write.writerow(entry[i])

#final activity
prep(0, 2, in_1)
collate()
csv_out(name, row, fields, i_list, "pink morsel")

   
