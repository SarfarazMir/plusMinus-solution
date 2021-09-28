def plusMinus(n, arr):
    postives, negatives, zeros = 0, 0, 0
    for i in range(n):
        if (arr[i] > 0):
            postives += 1
        elif (arr[i] < 0):
            negatives += 1
        elif(arr[i] == 0):
            zeros += 1
    
    # proportion of postive values
    print('%.6f'%(postives/n))
     # proportion of negative values
    print('%.6f'%(negatives/n))
      # proportion of zero values
    print('%.6f'%(zeros/n))

plusMinus(6, [-4, 3, -9, 0, 4, 1])
