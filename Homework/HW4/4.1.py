def find_approximate_sum(nums:list[int,...], target:int) -> (list[int,...], int):
    nums.sort()
    closest_sum = float('inf')
    result = []

    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            left = j + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                current_diff = abs(target - current_sum)

                if current_diff == 0:
                    return [nums[i], nums[j], nums[left], nums[right]], current_sum
                elif current_diff < closest_sum:
                    closest_sum = current_diff
                    result = [nums[i], nums[j], nums[left], nums[right]]

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

    return result, sum(result)

if __name__ == '__main__':
    N = int(input('Enter the length of the array: '))
    numbers = []
    for index in range(N):
        numbers.append(int(input(f'Enter a number{index+1}: ')))
    C = int(input('Enter a result number: '))

    result, closest_sum = find_approximate_sum(numbers, C)
    print(result)
    print(closest_sum)
