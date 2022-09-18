from parsing_website import Parser
from write_xls import ExcelWriter


def main():
    parser = Parser()
    list_of_advs = parser.parse_list_of_advs()
    excel_writer = ExcelWriter(list_of_advs)
    excel_writer.write_data()


if __name__ == "__main__":
    main()
