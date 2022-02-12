# Program to display the Fibonacci sequence 
def fibonnacci():
            num = int(input("Enter a number? "))

            # first two terms
            n1, n2 = 0, 1
            count = 0

            # check if the number  is valid
            if num <= 0:
                print("Please enter a positive integer")
            # if there is only one number, return n1
            elif num == 1:
                
                print(n1)
            # generate fibonacci sequence
            
            else:
                print("Fibonacci sequence:")
                while count < num:
                    print(n1)
                    nth = n1 + n2
                    # update the fibonaccci values
                    n1 = n2
                    n2 = nth
                    count += 1

fibonnacci()
