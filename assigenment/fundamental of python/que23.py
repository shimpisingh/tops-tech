#Write a Python function to insert a string in the middle of a string

def insert_string_middle(original_string, string_to_insert):
    midpoint = len(original_string) // 2
    first_half = original_string[:midpoint]
    second_half = original_string[midpoint:]
    final_string = first_half + string_to_insert + second_half
    return final_string

print(insert_string_middle("Hello", "world"))  
print(insert_string_middle("Python is awesome", "very ")) 
