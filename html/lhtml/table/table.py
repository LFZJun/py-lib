# !/bin/python3
# coding: utf-8
from bs4 import BeautifulSoup


class Element(object):
    def __init__(self, row, col, text, rowspan=1, colspan=1):
        self.row = row
        self.col = col
        self.text = text
        self.rowspan = rowspan
        self.colspan = colspan

    def __repr__(self):
        return f'''{{"row": {self.row}, "col":  {self.col}, "text": {self.text}, "rowspan": {self.rowspan}, "colspan": {self.colspan}}}'''

    def isRowspan(self):
        return self.rowspan > 1

    def isColspan(self):
        return self.colspan > 1


def parse(h) -> [[]]:
    doc = BeautifulSoup(h, 'html.parser')

    trs = doc.select('tr')

    m = []

    for row, tr in enumerate(trs):  # collect Node, rowspan node, colspan node
        it = []
        ts = tr.find_all(['th', 'td'])
        for col, tx in enumerate(ts):
            element = Element(row, col, tx.text.strip())
            if tx.has_attr('rowspan'):
                element.rowspan = int(tx['rowspan'])
            if tx.has_attr('colspan'):
                element.colspan = int(tx['colspan'])
            it.append(element)
        m.append(it)

    def solveColspan(ele):
        row, col, text, rowspan, colspan = ele.row, ele.col, ele.text, ele.rowspan, ele.colspan
        m[row].insert(col + 1, Element(row, col, text, rowspan, colspan - 1))
        for column in range(col + 1, len(m[row])):
            m[row][column].col += 1

    def solveRowspan(ele):
        row, col, text, rowspan, colspan = ele.row, ele.col, ele.text, ele.rowspan, ele.colspan
        offset = row + 1
        m[offset].insert(col, Element(offset, col, text, rowspan - 1, 1))
        for column in range(col + 1, len(m[offset])):
            m[offset][column].col += 1

    for row in m:
        for ele in row:
            if ele.isColspan():
                solveColspan(ele)
            if ele.isRowspan():
                solveRowspan(ele)
    return m


def prettyPrint(m):
    for i in m:
        it = [f'{len(i)}']
        for index, j in enumerate(i):
            if j.text != '':
                it.append(f'{index:2} {j.text[:4]:4}')
        print(' --- '.join(it))
