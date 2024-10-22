#!/usr/bin/python3
my_dna="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
print(my_dna)
number_A=my_dna.count('A')
number_T=my_dna.count('T')
length=len(my_dna)
AT_content=(int(number_A)+int(number_T)/int(length))
print("The A+T content of this sequence is:" + str(float(AT_content)))
complement_dna=my_dna.replace("A","T")
complement_dna=complement_dna.replace("T","A")
complement_dna=complement_dna.replace("C","G")
complement_dna=complement_dna.replace("G","C")
print("The complement of this sequence is: "+ complement_dna)

my_dna2="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
str="GAATTC"
position=my_dna2.find(str)
print(position)
first_length=len(my_dna2[0:int(position)+1])
second_length=len(my_dna2[int(position)+1:])
print("The restriction fragment are ", first_length, second_length)

my_dna3="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
first_exon=my_dna3[0:63]
second_exon=my_dna3[90:]
coding_sequence=first_exon + second_exon
print("The coding sequence is", coding_sequence)
percentage_DNA=int(len(coding_sequence))/int(len(my_dna3))*100
del str
print(str(int(percentage_DNA)) + " of the DNA3 sequence is coding")
intron=my_dna3[64:90]
sequence=first_exon + intron.lower() + second_exon
print("###exon intron exon###\n" + sequence)
