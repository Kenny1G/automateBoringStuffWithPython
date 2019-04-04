tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(list):
    colWidth = [0] * len(list)
    n = len(list)
    for t in range(n):
        i = 0
        j = list[t]
        for k in j:
            if i > len(k):
                continue
            else:
                i = len(k)
        colWidth[t] = i
    print(colWidth)
    for item in range(len(list[0])):
        for nosListInList in range(len(list)):
            print(list[nosListInList][item].rjust(colWidth[nosListInList]),end = ' ')

        print('\n')


printTable(tableData)
# lic    lic   lic
# 111    212   313
# 121    222   323
# 131    232   333
# 141    242   343
