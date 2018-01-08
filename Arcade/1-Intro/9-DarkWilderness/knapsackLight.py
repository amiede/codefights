# https://codefights.com/arcade/intro/level-9/r9azLYp2BDZPyzaG2/
# Nice solution by virgile_f
def knapsackLight(value1, weight1, value2, weight2, maxW):
    return max( int(weight1<=maxW)*value1, 
                int(weight2<=maxW)*value2, 
                int(weight1+weight2<=maxW)*(value1+value2) 
              )
