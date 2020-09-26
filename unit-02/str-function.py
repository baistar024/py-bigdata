str1 = """
the impression that a person, an organization or a product, etc. gives to the public.
His public image is very different from the real person.
The Prime Minister knows that his personal image is his greatest political asset.
"""

print(str1.title())
lines = (str1.split(sep="."))
for line in lines:
    print(line)

print(str1.replace("His", "Her").replace("his", "her"))

print(str1.lower())
print(str1.upper())
str2 = "      this       "
print(str2.strip())
print(str2.lstrip())
print(str2.rstrip())