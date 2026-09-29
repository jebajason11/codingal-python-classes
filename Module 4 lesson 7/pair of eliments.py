class pair_elements:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i
value = int(input("Enter sum for which you want to make this search :"))
result = pair_elements(). twoSum((10,20,30,40,50,60,70),value)
if result is not None:
    print(f"index={result[0]},index2 = {result[1]}")
else:
    print("No pair found")