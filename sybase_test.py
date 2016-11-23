#!/usr/bin/python

import Sybase
import xlwt
import types

if __name__ == '__main__':
    o = Sybase.connect('DBSVR', 'sa', '111111')
    c = o.cursor()
    c.execute('set chained off')
    c.callproc('imaptmdb..my_Test')
    result = c.fetchall()
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Alarm')
    rowNum = 1 
    for row in result:
        colNum = 0
        #print rowNum
        for col in row:
            if type(col) != types.StringTypes:
                #print rowNum, colNum, col
                ws.write(rowNum, colNum, str(col))
            else:
                ws.write(rowNum, colNum, col)
            colNum = colNum + 1
        rowNum = rowNum + 1
    c.close()
    o.close()
    wb.save('emily.xls')
    print '----hello tiky'
