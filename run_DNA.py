# importing DNA class
from DNA_class import DNA


# If the string is longer than 1000 characters
# the user will be prompted to enter a string again
while True:
    dna_string = input('Please insert your DNA string. Note: your string cannot be longer than 1000 characters').upper()
    if len(dna_string) > 1000:
        continue   
    else: 
        # instantiating the class so we can use the method
        dna_instance = DNA()
        dna_instance.count_DNA(dna_string)
        break 