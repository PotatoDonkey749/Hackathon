import numpy as np

def read_file(filename):
    matrices = {}
    ops = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        section = None
        matrix_name = None
        matrix_data = []
        
        for line in lines:
            line = line.strip()
            if line == "matrices":
                section = "matrices"
                continue
            elif line == "operations":
                section = "operations"
                if matrix_name and matrix_data:
                    matrices[matrix_name] = np.array(matrix_data)
                continue
            
            if section == "matrices":
                if not line:
                    continue
                elif line.isalpha():
                    if matrix_name and matrix_data:
                        matrices[matrix_name] = np.array(matrix_data)
                    matrix_name = line
                    matrix_data = []
                else:
                    row = list(map(int, line.split()))
                    matrix_data.append(row)
            
            elif section == "operations":
                if line:
                    ops.append(line)
                    
        if matrix_name and matrix_data:
            matrices[matrix_name] = np.array(matrix_data)
            
    return matrices, ops

def add_matrices(A, B):
    return A + B

def multiply_matrices(A, B):
    return np.dot(A, B)

def process_operations(matrices, operations):
    results = []
    for operation in operations:
        result = None
        terms = operation.split()
        i = 0
        while i < len(terms):
            if terms[i] in matrices:
                if result is None:
                    result = matrices[terms[i]]
                else:
                    if terms[i-1] == '+':
                        result = add_matrices(result, matrices[terms[i]])
                    elif terms[i-1] == '*':
                        result = multiply_matrices(result, matrices[terms[i]])
            i += 1
        results.append((operation, result))
    return results

def print_results(results):
    for operation, result in results:
        print(operation)
        for row in result:
            print(" ".join(map(str, row)))
        print("\n")

def main():
    filename = "./input.txt"
    matrices, operations = read_file(filename)
    results = process_operations(matrices, operations)
    print_results(results)

if __name__ == "__main__":
    main()
