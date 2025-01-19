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
    return(sum(numbers),max(numbers),min(numbers))

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
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
    common_elements=[]
    
    for item in list1:
        if(item in list2):
            common_elements.append(item)
            
    return(set(common_elements))

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