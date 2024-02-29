def largest_sum(nums):
    max_sum = float('-inf')  # Initialize max_sum with negative infinity

    for i in range(len(nums) - 1):
        current_sum = float(nums[i]) + float(nums[i+1])  # Convert strings to floats before adding
        max_sum = max(max_sum, current_sum)

    return max_sum

if __name__ == "__main__":
  greater = input("Ingrese los números separados por comas: ")
  greater = greater.split(",")

  print(greater)
  print(largest_sum(greater))