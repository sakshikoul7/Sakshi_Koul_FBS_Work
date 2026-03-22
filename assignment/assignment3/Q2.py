#to checj whether the alphabet is a vowel or consonant
alphabet=input("Enter an alphabet: ").lower()

if alphabet in ['a', 'e', 'i', 'o', 'u']:
    print(f'{alphabet} is a vowel.')
else:
    print(f'{alphabet} is a consonant.')
    