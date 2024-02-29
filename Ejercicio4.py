def largest_sum(nums):
    max_sum = float('-inf')

    for i in range(len(nums) - 1):
        current_sum = float(nums[i]) + float(nums[i+1])  # Convierte entradas de strings a float
        max_sum = max(max_sum, current_sum)       

    return max_sum                                       # Aquí el ciclo retorna la mayor suma de los elementos

if __name__ == "__main__":
  greater = input("Ingrese los números separados por comas: ")
  greater = greater.split(",")
  print(largest_sum(greater))
