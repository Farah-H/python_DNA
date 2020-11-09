# Python OOP Task - DNA Parsing

## Task 
__Given:__ A DNA string s of length at most 1000 nt.

__Return:__ Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Sample Dataset:

AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output:

20 12 17 21

__NOTE: Must be in class and method format__

## Pre-Requisites
__Necessary:__ You must have python installed.  
__Optional:__ It is easier to complete this task when using a code editor, such as Visual Studio Code or PyCharm. You can learn how to [install VSC](https://docs.microsoft.com/en-us/visualstudio/install/install-visual-studio?view=vs-2019) or [install PyCharm](https://www.jetbrains.com/help/pycharm/quick-start-guide.html) using these hyperlinks. 

## Syntax 
### Step 1: Create a DNA class
```python
class DNA:
    
    # Initialising the class, defining a,c,g,t
    def __init__(self):
        self.a = 'A'
        self.c = 'C'
        self.g = 'G'
        self.t = 'T'
```

### Step 2: Create a Function to Count and Print the Number of Times Each Symbol Comes Up
```python
    def count_DNA(self, string_input):
        count_a = string_input.count(self.a)
        count_c = string_input.count(self.c)
        count_g = string_input.count(self.g)
        count_t = string_input.count(self.t)

        print(f'{self.a} {self.c} {self.g} {self.t}')
        print(f'{count_a} {count_c} {count_g} {count_t}')
```
### Step 3: In a Seperate File, Import your DNA Class 
```python
# importing DNA class
from DNA_class import DNA
```
### Step 4: Run the DNA Parsing Function by Instantiating the Class
Now is a good opportunity to test for the length of the DNA string being less than 1000, recalling that this was one of the requirements. `upper()` was used to capitalise the string, making sure that the letters are as defined in the class' `__init__` function, to avoid any issues with case-sensitivity

```python
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
```