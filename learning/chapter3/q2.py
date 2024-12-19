# Write a program to fill in a letter template given below with name and date.

name = "om"

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter.replace('<|Name|>','Om').replace('<|Date|>','15 december 2024'))