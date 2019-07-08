print("********************************")
print("*Claudio G. Ametrano 2018 UNITS*")
print("********************************")
#USE: if the file ends in .fas (must be an alignment: all sequences of the same length) the script gives you back which alignments are >= 
# of a ceartain length and prints them to screen
import os 
import random
from Bio import SeqIO
import numpy as np

path = os.getcwd()
header_list = []
alignemtns_longer_than=[]
count = 0
count1 = 0
count2 = 0
length = input('minimum alignment length? ')
length = int(length)
for root, dirs, files in os.walk(path, topdown=True):
	for alignment_file in files:
		if alignment_file.endswith('.fas'):
			for record in SeqIO.parse(alignment_file, "fasta"):
			#SeqInputOutput.parse reads the fasta file	
				header_list.append(record.id)
			#record.id are the headers (in Biopython SeqIO), record.seq are the sequences	
			#print(header_list)		
			# it creates a list of the headers
			number_of_sequences = len(header_list)
			# counts the elements of the list
			#print("the number of sequence is %s" %(number_of_sequences))
			sequences_length = len(record.seq)
			# it counts the sequences length
			#print("the alignment is %s nucleotides" %(sequences_length))
			if sequences_length >= length:
				count = count + 1
				alignemtns_longer_than.append(alignment_file)
			else:
				count1 = count1 + 1
		else:
			count2 = count2 + 1
print('The alignments longer than or equal to ',length,'bp are: ', alignemtns_longer_than)			
print('The alignemnts shorter than ',length,' bp are ',count1)
print('There are ',count2,' file which are not .fas')
