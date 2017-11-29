from datetime import datetime
import xlsxwriter
import os
workbook = xlsxwriter.Workbook('Database17.xlsx')
worksheet = workbook.add_worksheet()
f1 = workbook.add_format()
f1.set_text_wrap()
f1.set_bold()
f1.set_align('left')
f2 = workbook.add_format()
f2.set_num_format('dd/mm/yy')
f2.set_align('right')
worksheet.set_column('A:D', 15)
row=0
col=0
worksheet.write(row,col,"First Name",f1)
worksheet.write(row,col+1,"Last Name",f1)
worksheet.write(row,col+2,"Date of Birth",f1)
worksheet.write(row,col+3,"City",f1)


for i in range(1,11):
  Fname = input("First Nmae: ")
  Lname = input("Last name:")
  dob = input("Data of birth(dd/mm/yy): ")
  city = input("City: ")
  date_time = datetime.strptime(dob,'%d/%m/%Y')
  worksheet.write_string(row+i,col,Fname)
  worksheet.write_string(row+i,col+1,Lname)
  worksheet.write_datetime(row+i,col+2,date_time,f2)
  worksheet.write_string(row+i,col+3,city)
  os.system('cls')
workbook.close()
