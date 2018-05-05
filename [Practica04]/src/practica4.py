import sys

def lectura(archivo):
    'Lectura de un archivo'
    lista=[]
    archivo= open(archivo,"r")
    for linea in archivo:
        linea2=linea.split(" ")
        for elem in linea2:
            if(elem is not "\n"):
                entero=int(elem)
                lista.append(entero)
    return lista


# Python program for counting sort

# The main function that sort the given string arr[] in
# alphabetical order
def countSort(arr):

    # The output character array that will have sorted arr
    output = [0 for i in range(256)]

    # Create a count array to store count of inidividul
    # characters and initialize count array as 0
    count = [0 for i in range(256)]

    # For storing the resulting answer since the
    # string is immutable
    ans = ["" for _ in arr]

    # Store count of each character
    for i in arr:
        count[i] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(256):
        count[i] += count[i-1]

    # Build the output character array
    for i in range(len(arr)):
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1

    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans

# Python program for implementation of Radix Sort

# A function to do counting sort of arr[] according to
# the digit represented by exp.





def countingSort(arr, exp1):

    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i]/exp1)
        count[ (index)%10 ] += 1

    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1,10):
        count[i] += count[i-1]

    # Build the output array
    i = n-1
    while i>=0:
        index = (arr[i]/exp1)
        output[ count[ (index)%10 ] - 1] = arr[i]
        count[ (index)%10 ] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]
        return arr


# Method to do Radix Sort

def radixSort(arr):

    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1/exp > 0:
        countingSort(arr,exp)
        exp *= 10
    print("La lista ordenada:")
    return arr


def bucketsort( A ):
  # get hash codes
  code = hashing( A )
  buckets = [list() for _ in range( code[1] )]
  # distribute data into buckets: O(n)
  for i in A:
    x = re_hashing( i, code )
    buck = buckets[x]
    buck.append( i )

  # Sort each bucket: O(n).
  # I mentioned above that the worst case for bucket sort is counting
  # sort. That's because in the worst case, bucket sort may end up
  # with one bucket per key. In such case, sorting each bucket would
  # take 1^2 = O(1). Even after allowing for some probabilistic
  # variance, to sort each bucket would still take 2-1/n, which is
  # still a constant. Hence, sorting all the buckets takes O(n).

  for bucket in buckets:
    print countSort( bucket )

  ndx = 0
  # merge the buckets: O(n)
  for b in range( len( buckets ) ):
    for v in buckets[b]:
      A[ndx] = v
      ndx += 1
  print("La lista ordenanda es:")
  return A

import math

def hashing( A ):
  m = A[0]
  for i in range( 1, len( A ) ):
    if ( m < A[i] ):
      m = A[i]
  result = [m, int( math.sqrt( len( A ) ) )]
  return result


def re_hashing( i, code ):
  return int( i / code[0] * ( code[1] - 1 ) )

#Main
a=sys.argv
archivo= lectura(a[1])
algoritmo=a[2]

if(algoritmo=="counting"):
    print (countSort(archivo))
elif(algoritmo=="radix"):
    print (radixSort(archivo))
elif(algoritmo=="bucket"):
    print (bucketsort(archivo))
else:
    print("algoritmo invalida")
