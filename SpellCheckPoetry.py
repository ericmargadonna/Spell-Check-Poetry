import string

text = input("Enter a poem: ")

text = text.replace(" ", "")
for char in string.punctuation:
    text = text.replace(char, "")

text = list(text)

spacing = input("Enter the spacing, separated by spaces: ")
spacing = spacing.split()
spacing = [int(i) for i in spacing]

sp_num = 0
cursor = 1
while cursor <= len(text)-1:
    cursor += spacing[sp_num]
    text.insert(cursor-1, " ")
    cursor += 1
    if sp_num < len(spacing)-1: sp_num += 1 
    else: sp_num = 0

text = str(text)
print(text)