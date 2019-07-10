print("********************************")
print("*Claudio G. Ametrano 2018 UNITS*")
print("********************************")
#USE: it takes a fasta file, samples randomly without replacement n colunms and creates a new fasta with those sampled columns 
import os 
import random
from Bio import SeqIO
import numpy as np

path = os.getcwd()
header_list = []
the_matrix = []
resampled_matrix = []
count = 0
alignment_file = input("File name to be resampled:")
rasampling_repeats = input("How many alignments do you need?: ")
rasampling_repeats = int(rasampling_repeats)
for record in SeqIO.parse(alignment_file, "fasta"):
#SeqInputOutput.parse reads the fasta file	
	header_list.append(record.id)
#record.id are the headers (in SeqIO of Biopython), record.seq are the sequences	
#print(header_list)	
# creates a list of the headers	
number_of_sequences = len(header_list)
# counts the element of the list
print("il numero delle sequenze è %s" %(number_of_sequences))
sequences_length = len(record.seq)
# counts the nucleotides of the alignment
print(" the alignment is %s nucleotided" %(sequences_length))
columns_to_sample = int(input("How many alignment posotions do you want to sample?"))
# lo legger come un integer
        
for record in SeqIO.parse(alignment_file, "fasta"):
		a = record.seq
		split_a = list(record.seq)
		the_matrix.append(split_a)
#creates a list of the nucleotides for every sequence in the alignment and appends them to the list the_matrix		
#print("The list of lists is:")
#print(the_matrix)

#print("the same list represented as row and columns")
#for righe in the_matrix:
#	for oggetto in righe:
#		print (oggetto, end='')
#	print()
# it print the list in a nice, tidy up way

the_matrix_numpy = np.array(the_matrix) 
#the list of lists is converted in a two dimension array 
#print("Here is the array:") 
#print(the_matrix_numpy)

for k in range (rasampling_repeats):
	count = count + 1
	number_list = list(range(sequences_length))
	random_number_list = random.sample(number_list, columns_to_sample)   
	print("sampled position in the alignment",random_number_list)
	#creates a list of integer with the same length of the alignment, then samples randomply n numbers and put them in a list (without repetition)
	"""#If I want to sample with repetition...
	random_number_list = []
	#creates an empty list
	for i in range(0,5):
	#samples for instance 5 numbers	
		random_number_list.append(random.randrange(0,14))                       
	print(random_number_list)
	#appends to the list a certain number of random numbers between 0 and m (random.ranrange(0,m))
	#while random.randrange only creates random numbers using the range and then you have to append them to a list
	# the command random.sample samples from an alreay existing list of numbers and creates a list with the sampled numbers """
	
	resampled_matrix = the_matrix_numpy[:,random_number_list]
	print("the resampled alignment is: ")
	print(resampled_matrix)
	# the new matrix is composed by the columns wchich correspond the the random number generated in the "random_number_list"
	output_file = open("resampled_alignment", "w")
	percentage = int(columns_to_sample) / int(sequences_length)*100 
	percentage = round(percentage, 1)
	percentage = str(percentage) 
	count = str(count)
	#print(count)
	#print(percentage)
	os.rename(path +"/"+ "resampled_alignment", path +"/"+percentage + "%" + "resampled_alignment" + count + ".fas")
	count = int(count)
	for header, row in zip(header_list, resampled_matrix):
	# zip is useful when you have to run two for cycle in a paralle way
	#this for cycle writes in a parallel way the header and its sequence
		output_file.write(">" + header + "\n")	
		line= (''.join([str(elem) for elem in row]))	
	# the resampled sequence is a join, without spaces of the elements in a row	
		output_file.write(line + "\n")

	print("From the aligment file: ", alignment_file, "have been created ",count,"alignments, samplig", columns_to_sample, "alignment position without repetition, output have been saved to resampled_alignment.fas")
