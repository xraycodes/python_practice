

def creditCardNumber(CCnumber):
    lengthOfNumber = len(CCnumber)
    lastFourNumber = CCnumber[-4:]
    numberOfAsterisks = lengthOfNumber - 4
    print(f"{numberOfAsterisks * '*'}{lastFourNumber}")  
    

creditCardNumber('540512345')