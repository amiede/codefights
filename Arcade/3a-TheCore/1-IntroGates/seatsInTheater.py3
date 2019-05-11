# https://app.codesignal.com/arcade/code-arcade/intro-gates/bszFiQAog96G9CXKg
def seatsInTheater(nCols, nRows, col, row):
    
    # Person behind me gets blocked (+1), person left of me...not
    return (nCols - col + 1) * (nRows - row)
