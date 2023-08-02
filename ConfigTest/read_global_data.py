import xlrd
import openpyxl as xl
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
class Testdata:
    sfile = "C://Users//thipr//OneDrive - HARMAN\Documents//Testdata1.xls"
    sDriversheet = "Driver"
    workbook = xlrd.open_workbook(sfile)
    dsheet = workbook.sheet_by_name(sDriversheet)


    rowCount = dsheet.nrows
    # print(rowCount)
    ColCount =dsheet.ncols
    # print(ColCount)

    for cur_rows in range(1,rowCount):
        status =dsheet.cell_value(cur_rows,2)
        if status == "Yes":
            sheet_name = dsheet.cell_value(cur_rows, 1)
            # print(sheet_name)
            modulesheet = workbook.sheet_by_name(sheet_name)
            modulerowCount = modulesheet.nrows
            moduleColCount = modulesheet.ncols
            result_data = []

            # for curr_row in range(1, modulerowCount):
            # for curr_rows in range(1, modulerowCount):
            row_data = []
            for curr_col in range(0, moduleColCount):

                    data = modulesheet.cell_value(1, curr_col)
                    row_data.append(data)
            print(row_data)


            # result_data.append(row_data)
            # print(result_data[1])

            # print(row_data)
            # print(row_data[0])
            # print(row_data[1])
            # print(row_data[2])
            # print(row_data[3])

                # user_name = modulesheet.cell_value(curr_rows, 0)
                # pass_word = modulesheet.cell_value(curr_rows, 1)
                # url = modulesheet.cell_value(curr_rows, 2)
                # search = modulesheet.cell_value(curr_rows, 3)
                # row_data.append(data)

            # num_lists = int(input("How many lists do you want? "))
            # lists = []
            # for p in range(num_lists):
            #     lists.append(p)
            # print(lists)
            # print(lists[3])












