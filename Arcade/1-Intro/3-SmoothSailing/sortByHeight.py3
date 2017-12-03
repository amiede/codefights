# https://codefights.com/arcade/intro/level-3/D6qmdBL2NYz49XHwM
def sortByHeight(a):

      # Selection sort
      for i in range(len(a)-1, 0 , -1):
           
            if a[i] != -1:
                  maximum = 0
            else: continue
            
            for j in range(1,i+1):
                  if a[j] != -1:
                        if a[j] > a[maximum]:
                              maximum = j
                        a[i], a[maximum] = a[maximum], a[i]
                        #print(a[i], a[j], a[maximum])
            
      return a