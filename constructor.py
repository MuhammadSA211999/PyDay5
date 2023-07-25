class Details:
    name=""
    roll=""
    university=""
    def __init__(self,name,roll,university):
        self.name=name
        self.roll=roll
        self.university=university
    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}, University: {self.university}")
msa=Details('MSA',23456,'NSTU')
print(msa.display())