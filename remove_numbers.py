def remove_numbers(text):
    result = re.sub(r'\d+', '', text)
    return result
 
input_str = "There are 3 balls in this bag, and 12 in the other one."
remove_numbers(input_str)