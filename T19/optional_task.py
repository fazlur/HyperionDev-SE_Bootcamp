# Opening the file for reading, storing it as a string in a variable, closing the file once read
file = open('input.txt', 'r')
file_text = file.read()
file.close()

# Counting the lines in the file by counting the carriage returns, and storing in a counter already inititaed to 1
lines = 1
for char in file_text:
    if char == "\n":
        lines += 1

# Counting the number of characters using the len function
chars = len(file_text.strip())

# Couting the words using the len funtion based on the split count of the spaces
words = len(file_text.strip().split())

# Getting a count of each vowel and printing the total per vowel
a = file_text.lower().count("a")
e = file_text.lower().count("e")
i = file_text.lower().count("i")
o = file_text.lower().count("o")
u = file_text.lower().count("u")

print(f"""

==================
# Text From File #
==================

{file_text}

Word, Line and Char count
-------------------------
Word count: {words}
Line count: {lines}
Char count: {chars}

Vowel count
-----------
a count :   {a}
e count :   {e}
i count :   {i}
o count :   {o}
u count :   {u}

Vowels  :   {a + e + i + o + u} """)
