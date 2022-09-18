
name = input("Enter your name:")
age = input("Enter your age:")
address = input("Enter your address:")

if name.isalpha() and age.isnumeric() and address.isalpha():
    print(f"Hello Mr/Ms {name} age {age} located in {address}.\n thanks for beening"
          f" one od our community,\t Enjoy")
else:
    print("Invalid name or age or address!")
