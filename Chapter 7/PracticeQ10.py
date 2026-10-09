# Write a function that takes a string and returns the count of vowels and 
# consonants separately.

def countVowCons(usrInput):
    vowels = "aeiouAEIOU"
    countVowels = 0
    countCosonants = 0
    for eachChar in usrInput:
        if eachChar.isalpha():
            if eachChar in vowels:
                countVowels +=1
            else:
                countCosonants +=1
    return countVowels, countCosonants

totalVowels, totalConsonants = countVowCons("Harshit Singh")
print("Total Vowels are:", totalVowels)
print("Total Consonants are:", totalConsonants)