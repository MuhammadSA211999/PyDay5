# class exploration in python 
class Student:
    name=""
    age=""
    gpa=""
    whichClass=""

msa=Student()
msa.age='24'
msa.name='MSA'
msa.gpa='3.44'
msa.whichClass=15
print(isinstance(msa,Student)) #true
print(f"Name: {msa.name}, Age: {msa.age}, GPA: {msa.gpa}, Class: {msa.whichClass}")

karim=Student()
karim.whichClass=15
karim.age=26
karim.gpa='3.99'
karim.name='Karim'
print(f"Name: {karim.name}, Age: {karim.age}, Class: {karim.whichClass}, GPA: {karim.gpa}")