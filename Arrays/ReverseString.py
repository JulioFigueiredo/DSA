
def ReverseStringFuncaoPronta(string):
    return string[::-1]

# print(ReverseStringFuncaoPronta('Revertaaaa'))

def ReverseStringTwoPointers(string):
    chars = list(string)
    left = 0
    right = len(chars) - 1

    while left < right:
        # chars[left], chars[right] = chars[right], chars[left]
        temp = chars[left]
        chars[left]=chars[right]
        chars[right]=temp

        left+=1
        right-=1

    return "".join(chars)

print(ReverseStringTwoPointers('Reverter a String'))
