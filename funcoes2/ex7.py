def deivis_sequence(n):

    if n == 1:
        return 1
    if n == 2:
        return 2
    
    return deivis_sequence(n-1) + deivis_sequence(n-2) - 1

        
print(deivis_sequence(2))
print(deivis_sequence(5))
print(deivis_sequence(10))