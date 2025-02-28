# Program to find the gcd of two numbers
# Input -- ten twentytwo
# Output -- two

import re
from functools import reduce
# import pdb


class GCD:

    '''Class to Create objects of gcd instances, which includes gcd and word_to_number'''

    __wordDictionary = {"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    __revWordDictionary = {v: k for k, v in __wordDictionary.items()}

    def __init__(self: object, num1: str, num2: str) -> None:

        '''Initialize variables on the object creation time'''

        self.num_one = self.Convert(num1, GCD.__wordDictionary, "integer")
        self.num_two = self.Convert(num2, GCD.__wordDictionary, "integer")
        self.gcd_result = self.Convert((self.gcd(self.num_one, self.num_two) if self.num_one > self.num_two else self.gcd(self.num_two, self.num_one)), GCD.__revWordDictionary, "string")

    def gcd(self: object,num1: int, num2: int) -> int:

        '''Function to return the gcd of two numbers'''

        if num2 == 0:
            return num1
        else:
            return self.gcd(num2, num1 % num2)
        

    def Convert(self: object, word: object, word_dict: dict, output) -> int:
        '''Function to convert the string into number or vice versa according to output argument'''

        pattern = ''
        
        if output == "integer":
            pattern = "|".join(word_dict.keys()) 
        else:
            pattern = '[0-9]'
        
        temp_result = re.findall(pattern, str(word))          # re.findall(pattern, word)

        result = reduce(lambda initial, x: initial + word_dict[x], temp_result, "")

        try:

            if output == "integer":
                return int(result)

            return str(result)
        except:
            # print("Invalid Input: ", word)
            print(f'Invalid Input : \033[91;1;4m{word}\033[0m')
            exit()
    

if __name__ == '__main__':
    print("\033[35mInput Format : twoone, fivethree\033[0m")
    var1 = input("Enter First Number in word : ").lower()
    var2 = input("Enter Second Number in word : ").lower()

    # pdb.set_trace()

    gcd_object = GCD(var1, var2)

    print(f'GCD of given numbers is : \033[92;4m {gcd_object.gcd_result} \033[0m')    # these numbers are just for color output
