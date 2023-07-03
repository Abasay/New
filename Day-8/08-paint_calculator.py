def paint_calculator():
    #number of cans = (width * height) / coverage per can
    #coverage per can = 5

    coveragePerCan = 5
    #input the wall height and width
    wall_height = int(input("Input the wall height: "))
    wall_width = int(input("Input the wall width: "))

    #calculate the number of cans needed

    numberOfCans = round((wall_height * wall_width) / coveragePerCan)

    return f"You will need {numberOfCans} number of cans"

def prime_numbers(n):
    """
    Function to print prime numbers from 1 to n
    """
    #we will need 2 for loops
         #First will accout for counting the number from 1 till n
         #Second will check for every value of 1 to n if it is divisible by any number
         #If divisible then a pprime number it is, else it is not a prime number
    #We print the prime numbers as the output
    if n >= 1:
        print(1, end=', ')
        isPrime = False
        #print(chr(ord('a') + 3))
        for i in range(2, n+1):
            
            for j in range(2, i + 1):
                if i % j == 0 and i > j:
                    isPrime = False
                    break
                    
                else:
                    isPrime = True
                    
            if (isPrime):
                print(i, end=', ')
                    
                
                
if __name__ == "__main__":
    #print(paint_calculator())
    prime_numbers(101)