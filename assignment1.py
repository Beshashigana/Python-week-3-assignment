input_txt = '''
This is my first line 
This is my second line
I love programming
I need alot of practice
I am also learning python'''

with open("input.txt", "w") as file:
    file.write(input_txt)

with open("input.txt", "r") as file:
    content = file.read()

word_count = len(content.split())

upper_content = content.upper()

with open ("output.txt", "w") as file:
    file.write(f"Word count: {word_count}\n\n")
    file.write(upper_content)
print("The new file 'output.txt; has been created successfully.")


