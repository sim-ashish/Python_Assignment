# this program will generate vaild parenthesis for the input number
# input - 3
# output - ['()()()','((()))','()(())','(())()']



def parenthesis_generator(n: int, combo_result='', openBr=0, closeBr=0, result=None) -> list :
    if result is None:
        result = []

    if openBr == closeBr == n:
        result.append(combo_result)
        return
    
    if openBr < n:
        parenthesis_generator(n, combo_result + '(', openBr + 1, closeBr, result)
    
    if closeBr < openBr:
        parenthesis_generator(n, combo_result + ')', openBr, closeBr + 1, result)
    
    return result

if __name__ == '__main__':

    number = int(input("Enter the number for which you want combination : "))
    if (number <= 0):
        print('[]')
    elif (number == 1):
        print("['()']")
    else:
        generated = parenthesis_generator(number)
        print(generated)
