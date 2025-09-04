x=input("enter a character:")
def func(x):
    if (x>='a' and x<='z') or (x>='A' and x<='Z'):#x.isdigit() x.isalpha()
        print(f"{x} is an alphabet")
    elif x>='0' and x<='9':
        print(f"{x} is a digit")
    else:
        print(f"{x} is a special character")
func(x)