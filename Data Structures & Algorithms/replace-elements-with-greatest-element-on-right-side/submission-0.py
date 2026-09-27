class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr2=[]
        for i in range(len(arr) - 1):
            max_num=max(arr[i+1:])
            arr2.append(max_num)
        arr2.append(-1)
        arr=arr2
        return arr
