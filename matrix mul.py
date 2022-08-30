from collections.abc import Sequence


def get_shape(lst, shape=()):
    if not isinstance(lst, Sequence):
        # base case
        return shape

    # peek ahead and assure all lists in the next depth
    # have the same length
    if isinstance(lst[0], Sequence):
        l = len(lst[0])
        if not all(len(item) == l for item in lst):
            msg = 'not all lists have the same length'
            raise ValueError(msg)

    shape += (len(lst), )
    
    # recurse
    shape = get_shape(lst[0], shape)

    return shape

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
           res = res + oneDArray[index] * nDArray[index]
        return res
    else:
        if (len(nDArray[0]) == len(oneDArray)):
            res = 0
            for index , value in enumerate(oneDArray):
                for index2 , value2 in enumerate(nDArray[index]):
                    res = res + value * value2
            return res

l1 = [[1,2,3],[1,2,3]]
l2 = [1,2,3,4,5]
l3 = [1,2,3,4,5]
print(mulArray(l2,l3))
