#03_strFunctions.py

name = "Avneesh"

# print(len(name))
print(name.endswith("esh"))
print(name.capitalize())
print(name.startswith("Av"))


# ==========================Escape Sequence Characters==========================
# Escape sequence characters are used to insert certain special characters in a string.

# Backslash
print("Backslash: \\")             # Output: \

# Single quote
print('Single quote: It\'s OK')    # Output: It's OK

# Double quote
print("Double quote: He said \"Hi\"")  # Output: He said "Hi"

# Newline
print("Newline:\nHello\nWorld")    # Output on separate lines

# Carriage Return
print("Carriage Return: Hello\rWorld") # Output: Worldo

# Tab
print("Tab:\tAvneesh")             # Output: Tab:    Avneesh

# Backspace
print("Backspace: Helloo\b")       # Output: Hello

# Form Feed (page break – rarely visible)
print("Form Feed: Hello\fWorld")

# Vertical Tab
print("Vertical Tab: Hello\vWorld")

# Bell / Alert sound (may not work on all systems)
print("Bell/Alert: \a")

# Unicode by name
print("Unicode by name: \N{Greek Capital Letter Omega}")  # Output: Ω

# Unicode (16-bit)
print("Unicode 16-bit: \u03A9")     # Output: Ω

# Unicode (32-bit)
print("Unicode 32-bit: \U0001F600") # Output: 😀

# Hexadecimal value
print("Hex value: \x41")            # Output: A

# Octal value
print("Octal value: \101")          # Output: A

# Null character
print("Null char: ABC\0DEF")        # Output: ABC DEF (null ignored)

# Raw string (ignores escape sequences)
print(r"Raw string: C:\newfolder")  # Output: C:\newfolder
