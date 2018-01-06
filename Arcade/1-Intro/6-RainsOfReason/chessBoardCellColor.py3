# https://codefights.com/arcade/intro/level-6/t97bpjfrMDZH8GJhi
def chessBoardCellColor(cell1, cell2):

    darkCells = r'[ACEG][1357]|[BDFH][2468]'
    lightCells = r'[ACEG][2468]|[BDFH][1357]'

    if (re.search(darkCells, cell1) and re.search(darkCells, cell2)):
        return True
    elif (re.search(lightCells, cell1) and re.search(lightCells, cell2)):
        return True
    else:
        return False