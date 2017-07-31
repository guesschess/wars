
def validBraces(string):
    braces = ["(",")","{","}","[","]"]
    labels = [0,1,3,4,7,8]
    dic = dict(zip(braces, labels))
    valid = True
    for key, value in dic.iteritems():
        string = string.replace(key, str(value))
    nums = [int(i) for i in string]
    n = len(nums)# the length of the string
    for i in range(n-1):
        if nums[i]+1 == nums[i+1]:
            nums[i] = nums[i+1] = -2
    stack = list(filter(lambda x: x >= 0, nums))
    if len(stack) > 0:
        valid = all(stack[i]+1 == stack[-i-1] for i in range(len(stack)/2))
    return valid
