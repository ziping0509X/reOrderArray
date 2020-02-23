
#剑指第13题
#输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
# 使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
# 并保证奇数和奇数，偶数和偶数之间的相对位置不变。

class Solution:
    def reOrderArray(self, array):
        # write code here
        row = len(array)
        array_1 = [1,2,3,7,5,6,8]
        j = 0
        for i in range(row):
            if not(array[i]%2 == 0.0):
                array_1[j] = array[i]
                j = j + 1
        k = j
        for i in range(row):
            if  array[i]%2 == 0.0:
                array_1[k] = array[i]
                k = k + 1
        return array_1

list_=[1,2,3,4,5,6,7]
solution=Solution()
list_=solution.reOrderArray(list_)
print(list_)

#调试成功！