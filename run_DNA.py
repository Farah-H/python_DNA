from DNA_class import DNA


while True:
    dna_string = input('Please insert your DNA string').upper()
    if len(dna_string) > 1000:
        continue    
    else: 
        dna_instance = DNA()
        dna_instance.count_DNA(dna_string)