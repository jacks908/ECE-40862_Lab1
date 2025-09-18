class TwoSum:
    def find(self, nums, target):
        seen = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return seen[need], i
            seen[x] = i
        return None

if __name__ == "__main__":
    arr = [10, 20, 10, 40, 50, 60, 70]
    target = int(input("What is your target number? "))
    ans = TwoSum().find(arr, target)
    if ans:
        i, j = ans
        print(f"index1={i}, index2={j}")
    else:
        print("No solution.")