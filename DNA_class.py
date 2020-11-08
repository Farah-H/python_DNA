class DNA:
    
    def __init__(self):
        self.a = 'A'
        self.c = 'C'
        self.g = 'G'
        self.t = 'T'

    def count_DNA(self, string_input):
        count_a = string_input.count(self.a)
        count_c = string_input.count(self.c)
        count_g = string_input.count(self.g)
        count_t = string_input.count(self.t)

        print(f'{self.a} {self.c} {self.g} {self.t}')
        print(f'{count_a} {count_c} {count_g} {count_t}')