import numpy as np

def calculate_dot_product(vector1, vector2):
    return np.dot(vector1, vector2)

if __name__ == "__main__":
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    
    result = calculate_dot_product(v1, v2)
    print(f"The dot product is: {result}").