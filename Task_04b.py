#Task 4b King Letter
'''
Task 4b King Letter (2marks)

Add to the code from part 1 to change the output when a number is 
greater than 100 to show for example:

=========================
How old are you? 111
You already got your letter 11 years ago
========================= 

'''
def main():
    x="Task4b"
    #===============================
    # Write your code here
    var1 = int(input('How old are you? '))
    var  = 100 - var1
    if var1 <= 100:
        print(f'Years until your letter...\n{var}')
    else:
        var2 = var1 - 100
        print(f'You already got your letter {var2} years ago')
    # End of your code here
    #===============================

if __name__ == '__main__':
    main()
