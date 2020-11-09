class DNA:
    
    # Initialising the class, defining a,c,g,t
    def __init__(self):
        self.a = 'A'
        self.c = 'C'
        self.g = 'G'
        self.t = 'T'

    # this function counts the number of times each of the symbols appears in a string
    def count_DNA(self, string_input):
        count_a = string_input.count(self.a)
        count_c = string_input.count(self.c)
        count_g = string_input.count(self.g)
        count_t = string_input.count(self.t)

        # returning an f-string showing the number of times each symbol was counted
        print(f'{self.a} {self.c} {self.g} {self.t}')
        print(f'{count_a} {count_c} {count_g} {count_t}')