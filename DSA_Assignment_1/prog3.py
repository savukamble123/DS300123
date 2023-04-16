#Q3. Write a program to check if two strings are a rotation of each other?
def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    s1s1 = s1 + s1

    return s2 in s1s1

s1 = "hello"
s2 = "lohel"
print(is_rotation(s1, s2))
s3 = "world"
s4 = "drowl"
print(is_rotation(s3, s4))