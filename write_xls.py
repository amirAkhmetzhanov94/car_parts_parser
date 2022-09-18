import xlsxwriter


class ExcelWriter:
    def __init__(self, list_of_data):
        self.list_of_data = list_of_data
        self.workbook = xlsxwriter.Workbook('database.xlsx')
        self.worksheet = self.workbook.add_worksheet()

    def setup_columns(self):
        bold = self.workbook.add_format({'bold': True})
        self.worksheet.write('A1', 'Ссылка', bold)
        self.worksheet.write('B1', 'Название компании', bold)
        self.worksheet.write('C1', 'Номер телефона', bold)

    def write_data(self):
        self.setup_columns()
        self.worksheet.set_column(0, 2, 100)
        for index, item in enumerate(self.list_of_data, 1):
            self.worksheet.write(index, 0, item.get("link", "ссылки нет"))
            self.worksheet.write(index, 1,
                                 item.get("name", "название отсутствует"))
            self.worksheet.write(index, 2, item.get("number", 0))
        self.workbook.close()
