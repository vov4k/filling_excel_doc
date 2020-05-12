import openpyxl as opx
import shutil
file_with_data = "../"+input("Введите название файла с данными (без расширения) \n")+".xlsx"
template = "../"+input("Введите название файла с шаблоном (без расширения) \n")+".xlsx"

fio_wb = opx.load_workbook(file_with_data)
fio_sheet = fio_wb.worksheets[0]
n_row = 0
indexes = []
for row in fio_sheet.rows:
        data_one_row = []
        
        for d in row:
                data_one_row.append(str(d.value))
        if n_row == 0:
                n_row = 1
                for temp in data_one_row:
                        indexes.append(list(map(int, input("Введите (через пробел) строку и клетку начала поля для столбца "+temp + "\n").split())))
                print("Введите (через пробел) номера полей которые будут в названии файла")
                k = 1
                for temp in data_one_row:
                        print(k, "-", temp)
                        k+=1
                names = list(map(int, input("\n").split()))
                step = input("Введите шаг с которым идут клетки (по умолчанию 1) \n")
                if not step:
                        step = 1
                else:
                        step = int(step)
                continue
        
        file = "../res/"
        for h in names:
                if data_one_row[h-1]:
                        file+=data_one_row[h-1].strip()+" "
        print("Начал: "+file)
        file =file.strip() + ".xlsx"
        
        shutil.copy(template, file)
        
        data_wb = opx.load_workbook(file)
        sheet = data_wb.worksheets[0]
        j = 0
        for tmp in data_one_row:
                if tmp and tmp != 'None':
                        ji = 0
                        for i in range(len(tmp)):
                                ffff = sheet.cell(row=indexes[j][0], column=ji+indexes[j][1]).coordinate
                                sheet[ffff].value=tmp[i]
                                ji+=step
                j = j +1
        data_wb.save(file)
        print("Закончил: "+file)
                
    