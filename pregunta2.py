
def encontrarNumero(input_list):

  sum_of_elements = sum(input_list)
 
  # falta el numero 2
  n = len(input_list) + 1
  actual_sum = (n * ( n + 1 ) ) / 2
 
  return int(actual_sum - sum_of_elements)
lista1 = [1,5,6,3,4]
print("Missing element in list_1: ",encontrarNumero(lista1))
