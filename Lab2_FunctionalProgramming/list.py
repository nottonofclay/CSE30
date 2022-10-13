def list_comprehension(input_list):
    return [input_list[i] + input_list[i-1] for i in range(1, len(input_list), 2)]      # adds every consecutive nums & adds to list

A = [1]

print(list_comprehension(A))