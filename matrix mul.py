# it doenst work for now
def is2DList(matrix_list):
  if isinstance(matrix_list[0], list):
    return True
  else:
    return False

def mulArray(oneDArray , nDArray):
    if  not is2DList(nDArray):
        res = 0
        for index , value in enumerate(oneDArray):
           res = res + oneDArray[index] + nDArray[index]
        return res
    else:
        if (len(nDArray[0]) == len(oneDArray)):
            res = 0
            for index , value in enumerate(oneDArray):
                for index2 , value2 in enumerate(nDArray[index]):
                    res = res + value + value2
            return res

l1 = [[1,2,3],[1,2,3]]
l2 = [1,2,3,4,5]
l3 = [1,2,3,4,5]
print(mulArray(l2,l3))
