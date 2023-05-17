# A python program that takes two numbers and returns their absolute difference
# Chase Tramel aka Kasey Chase Littlepaws - https://github.com/ChaseLittlepaws

def absDifference(x, y):
    if (x == y):
        return 0
    else:
        nums = [x, y]
        diff = max(nums) - min(nums)
        return abs(diff)
    
print(absDifference(5, 10))
print(absDifference(10, 5))
print(absDifference(200, -200))