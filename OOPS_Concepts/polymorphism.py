class python:
    def __init__(self, lang):
        self.lang=lang

    def get_writer(self):
        return f"{self.lang} is introduced by Guido van Rossum"
    
    def type_language(self):
        return f"{self.lang} is a interpreted language"

class java:
    def __init__(self, lang):
        self.lang=lang

    def get_writer(self):
        return f"{self.lang} is introduced by James Gosling"
    
    def type_language(self):
        return f"{self.lang} is a compiled language"
    
def main():
    for each in [python("python"), java("java")]:
        print(each.get_writer())
        print(each.type_language())

if __name__ == "__main__":
    main()

"""
Output:
python is introduced by Guido van Rossum
python is a interpreted language   
java is introduced by James Gosling
java is a compiled language 
"""


