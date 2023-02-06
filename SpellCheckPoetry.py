import string

text = input("Enter a poem: ")

for char in string.punctuation:
    text = text.replace(char, "")

spacing = input("Enter the spacing, separated by spaces: ")
spacing = spacing.split()
spacing = [int(i) for i in spacing]

sp_count = 0
cursor = 0
for letter in text:
    if cursor == spacing[sp_count]:
        pass
    cursor += 1