#14.
import math
def test14():    
    print("**********Question 14**********")
    while True:
        try:
            number = int(input("Enter an integer: "))
            break  
        except ValueError:
            print("That's not an integer! Please try again.")

    cube_root = math.pow(number, 1/3)
    if cube_root.is_integer():
        print(f"{cube_root} : Yes")
        print("**************End**************")
    else:
        print(f"{cube_root} : No")
        print("**************End**************")

#15.
def test15():
    print("**********Question 14**********")
    arr = [1, 2, 3, 4, 5, 8, 8, 2]

    duplicates = [x for x in arr if arr.count(x) > 1]

    unique_duplicates = list(set(duplicates))

    print(unique_duplicates)
    print("**************End**************")

#16.

test14()
test15()

