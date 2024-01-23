'''check whether the number in the list
contains 009 in order or not
for example [0,2,43,0,0,9,5] here the number is in the list
[0,9,0,3,5,2,5,0,0,5,9] here the number is not in order'''

def intelligent_game(numList):
    i = 0
    for i in range(len(numList)):
        # if(numList[i]==0 and numList[i+1]==0 and numList[i+2]==9):
        if[0,0,9] == numList[i:i+3]:
            return True
    return False
     
print(intelligent_game([1,2,0,0,9,8]))
print(intelligent_game([1,0,1,0,9,9,5]))


def game(nums):
    code = [0, 0, 9, 'x']
    for num in nums:
        if num == code[0]:
            code.remove(num)
    
    return len(code) == 1
print(game([1,2,4,0,0,9,5]))
print(game([1,0,1,0,9,9,5])) #wrong

