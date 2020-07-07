import openpyxl as opx
import shutil
settings_file = "../"+input("Введите название файла с настройками шаблона (без расширения) \n")+".template"
file_with_data = "../"+input("Введите название файла с данными (без расширения) \n")+".xlsx"
template = "../"+input("Введите название файла с шаблоном (без расширения) \n")+".xlsx"
fio_wb = opx.load_workbook(file_with_data)
fio_sheet = fio_wb.worksheets[0]
n_row = 0

with open(settings_file) as file:
    indexes = list()
    for line in file.readlines(): 
        indexes.append(line.rstrip().split(';')) # Обрезаем каретку переноса строки и делим по пробелу

print("Введите (через пробел) номера полей которые будут в названии файла")
k = 1
for temp in indexes:
        print(k, "-", temp[0])
        k+=1
names = list(map(int, input("\n").split()))

for row in fio_sheet.rows:
        data_one_row = []
        
        for d in row:
                data_one_row.append(str(d.value))
        if n_row == 0:
                n_row = 1
                headers=list(data_one_row)
                print(headers)
                continue


        file = "../res/"
        for h in names:
                if data_one_row[h-1]:
                        file+=data_one_row[h-1].strip()+" "
        
        file =file.strip() + ".xlsx"
        print("Начал: "+file)
        shutil.copy(template, file)
        
        data_wb = opx.load_workbook(file)
        sheet = data_wb.worksheets[0]
        j = 0

        lll=0
        for tmp in indexes:
         
            for header in headers:
                if header == tmp[0]:
                    one_data=data_one_row[lll]
                    if one_data and one_data != 'None':
                        ji = 0
                        for i in range(len(one_data)):
                                ffff = sheet.cell(row=int(indexes[j][1]), column=ji+int(indexes[j][2])).coordinate
                                sheet[ffff].value=one_data[i]
                                ji+=int(indexes[j][3])
                    j = j +1
                    lll+=1
                    break
        data_wb.save(file)
        print("Закончил: "+file)

