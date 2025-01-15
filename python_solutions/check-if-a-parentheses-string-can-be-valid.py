class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # odd length strings can never be balanced
        if len(s) % 2 == 1:
            return False
        # if first paranthesis is ")" and locked, string is invalid
        if s[0] == ")" and locked[0] == "1":
            return False
        # if last paranthesis "(" and locked, string is invalid
        if s[-1] == "(" and locked[-1] == "1":
            return False
        # check locked string
        count_ol = 0
        count_u = 0
        for (p, l) in zip(s, locked):
            if l == "0":
                count_u += 1
            if l == "1" and p == "(":
                count_ol += 1
            elif l == "1" and p == ")":
                if count_ol > 0:
                    count_ol -= 1
                else:
                    if count_u == 0:
                        return False
                    else:
                        count_u -= 1
        # if no locked and unlocked are even, valid string
        if count_ol == 0 and count_u % 2 == 0:
            return True
        # Scan string rom right to balance out open locked parantheses
        countright_ol_bal = 0
        for i in range(len(s)-1, -1, -1):
            if locked[i] == "0":
                countright_ol_bal -= 1
                count_u -= 1
            elif s[i] == "(":
                countright_ol_bal += 1
                count_ol -= 1
            elif s[i] == ")":
                countright_ol_bal -= 1
            if countright_ol_bal > 0:
                return False
            if count_u == 0 and count_ol == 0:
                break
        # If we still have open locked parantheses, invalid string
        if count_ol > 0:
            return False
        else:
            return True
