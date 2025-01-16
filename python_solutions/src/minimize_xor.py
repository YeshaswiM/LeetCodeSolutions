class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Convert to binary
        num1_b = f'{num1:b}'
        num2_b = f'{num2:b}'
        # Number of setbits in num2
        count_set = num2_b.count('1')
        len1 = len(num1_b)
        len2 = len(num2_b)
        # Pad "0"s tp num1 to match len of num2 for XOR
        if len1 < len2:
            num1_b = "0" * (len2 - len1) + num1_b
            len1 = len(num1_b)
        # Initialize x to be of same len
        x = ["0"] * len1
        for i in range(len1):
            if count_set > 0:
                if num1_b[i] == "1":
                    x[i] = "1"
                    count_set -= 1
                else: 
                    x[i] = "0"
            else: 
                x[i] = "0"
        # If x has same setbit count, return
        if count_set == 0:
            int_x = int("".join(x), 2)
        # Else, ensure least significant digit is set
        else:
            for i in range(len1-1, -1, -1):
                if count_set == 0:
                    break
                if x[i] == "0":
                    x[i] = "1"
                    count_set -= 1
            int_x = int("".join(x), 2)
        return int_x
