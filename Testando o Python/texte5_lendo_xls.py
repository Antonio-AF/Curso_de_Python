import xlrd
from datetime import datetime
from datetime import date

book = xlrd.open_workbook("envio_email.xlsx")

#print("Número de abas: ", book.nsheets)
#print("Nome da Planilhas: ", book.sheet_names())

now = datetime.now()
data_atual = date.today()
sh = book.sheet_by_index(0)

#print(sh.name, sh.nrows, sh.ncols)

#print("Valor da célula A2 é ", sh.cell_value(rowx=1, colx=0))

#print(f'{sh.cell_value(rowx=1, colx=4)}/{sh.cell_value(rowx=1, colx=5)}/'
      #f'{sh.cell_value(rowx=1, colx=6)}')

print(data_atual)
print(type(data_atual))
print(now.day)
print(sh.cell_value(rowx=1, colx=4))
print(data_atual == sh.cell_value(rowx=1, colx=4))
