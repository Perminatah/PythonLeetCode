
x = 101
def isPalindrome(x):
    xstr = str(x)
    # the below checks to see if the string is one number
    if len(xstr)==1:
         return True
    if len(xstr)%2==0:
        evenodd = True
    else: 
        evenodd = False
    if evenodd==True:
        # the below is a the halfway integer that splits a word in half
        half = int(len(xstr)/2)
        snip = xstr[half-1::-1]
        # snip is a variable which is half of xstr then reversed
        # check for equality of the two halves and then return result
        if snip==xstr[half:]:
            return True
        else: return False
    if evenodd==False:
            # create half variable which is halfway integer
            half = int((len(xstr))/2)
            # create snipped variable which is firsthalf excluding the middle number
            snip = xstr[half-1::-1]
            # checks if snip is the same as second half, excluding middle number, returns result
            if snip==xstr[half+1:]:
                 return True
            else: return False

print(isPalindrome(x))


