"""
操作excel文件
"""
import xlrd
from xlutils.copy import copy

class ExcelUtil:
    def __init__(self, excel_path=None, index=None):
        if excel_path == None:
            excel_path = "F:\Projects\Projects\Mooc_TestProject\config\cesedata.xls"
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheets()[index]
        # # 行数
        # self.rows = self.table.nrows
        # [[],[]]

    # 获取excel数据，按照每行一个list,添加到一个大的list里面
    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows != None:
            for i in range(rows):
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None

    # 获取excel行数
    def get_lines(self):
        # 行数
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return None

    # 获取单元格的数据
    def get_col_value(self, row, col):
        if self.get_lines() > row:
            data = self.table.cell(4, 4).value
            return data

    # 判断行数
    def has_next(self):

    # 写入数据
     def write_value(self, row, value):
        read_value = self.data
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row, 7, value)
        write_data.save("F:\Projects\Projects\Mooc_TestProject\config\keyword2.xls")


if __name__ == "__main__":
    ex = ExcelUtil("F:\Projects\Projects\Mooc_TestProject\config\keyword2.xls")
    print(ex.get_col_value(10, 10))
