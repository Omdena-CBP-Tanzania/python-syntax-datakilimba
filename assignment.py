def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return f"My name is {name} and I am {age} years old"
    

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    # Check if the argument is of type int
    if not isinstance(number, int):
       raise TypeError(f"Expected an integer, but got {type(number).__name__}")
   
    if(number > 10):
        return "Greater"
    
    if(number < 10):
        return "Lesser"
        
    if(number==10):
        return "Equal"
    
        

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    # Check if the argument is of type int
    if not isinstance(n, int):
        raise TypeError(f"Expected an integer, but got {type(n).__name__}")
   
    i=1
    summation=0
    while(i<=n):
        summation=summation+i
        i=i+1
    
    return(summation)
    

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    # Check if the input is a list
    if not isinstance(numbers, list):
        raise TypeError(f"Expected a list, but got {type(numbers).__name__}")

    # Check if all elements in the list are numbers (int or float)
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements in the list must be integers or floats")

    return(sum(numbers),max(numbers),min(numbers))

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    # Check if the input is a dictionary
    if not isinstance(students_dict, dict):
        raise TypeError(f"Expected a dictionary, but got {type(students_dict).__name__}")

    # Check if all values in the dictionary are numeric
    if not all(isinstance(score, (int, float)) for score in students_dict.values()):
        raise TypeError("All scores in the dictionary must be integers or floats")

    names=[]
    for student, score in students_dict.items():
        if score > 80:
            names.append(student)  # Add the student's name to the list
    
    return names
    

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    # Check if both inputs are lists
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both inputs must be lists")

    # Use set intersection to find common elements
    return set(list1) & set(list2)

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    operation_results={}
    operation_results["sum"]=a+b
    operation_results["difference"]=a-b
    operation_results["product"]=a*b
    operation_results["quotient"]=a/b
    return(operation_results)
    

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    logical_results={}
    logical_results["and"]=x and y
    logical_results["or"]=x or y
    logical_results["not_x"]=not x
    return(logical_results)

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    return {
        "and": a & b,        # Bitwise AND
        "or": a | b,         # Bitwise OR
        "xor": a ^ b,        # Bitwise XOR
        
    }