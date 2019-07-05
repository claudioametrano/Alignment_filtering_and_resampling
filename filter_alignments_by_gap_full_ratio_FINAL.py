print("********************************")
print("*Claudio G. Ametrano 2018 UNITS*")
print("********************************")
#USE: the script counts how many are the alignment columns composed more of nucleotides (A,C,T,G) than missing data (-), if these column are more 
# than a user defined value the alignment the alignment file is copied in the output path
import os 
import random
from Bio import SeqIO
import numpy as np
import shutil
from colorama import Fore
from colorama import Back
from colorama import Style
path = os.getcwd()
header_list = []
the_matrix = []

minimum_amount_of_column_with_less_than_50percent_missing_data = int(input('How many position with at least 50% of nucleotides should have the alignments?'))
output_path = input("In which path do I copy the files which meet the criterio? ")
for root, dirs, files in os.walk(path, topdown=True):
	for alignment_file in files:
		if alignment_file.endswith('.fas'):
			print(Fore.MAGENTA + Style.BRIGHT + '-----------------------------------------------------------------------------------------------' + Style.RESET_ALL)
			print('Sto elaborando il file ',alignment_file,'')
			header_list = []
			the_matrix = []
			for record in SeqIO.parse(alignment_file, "fasta"):
			#SeqInputOutput.parse reads the fatsa ("fasta" specifies the file format)	
				header_list.append(record.id)
			#"record.id" are the sequences headers (in SeqIO from Biopython), "record.seq" are the sequences	
			#print(header_list)	
			# creates a list appending one after the other the headers	
			number_of_sequences = len(header_list)
			# counts the elements in the list
			print(Fore.GREEN + "the number of sequences is " + Style.RESET_ALL ,number_of_sequences)
			sequences_length = len(record.seq)
			# counts characters in a sequence... senqeunce length should be all the same in an alignment!
			print(Fore.GREEN + "alignment length "+ Style.RESET_ALL ,sequences_length, Fore.GREEN + " bp" + Style.RESET_ALL)

			for record in SeqIO.parse(alignment_file, "fasta"):
				a = record.seq
				split_a = list(record.seq)
				the_matrix.append(split_a)
			# takes every sequence and creates a list made of the single nucletides which is then appeneded to the list "the_matrix"		
			#print("the list of lists with the sequences inside is:")
			#print(the_matrix)
			the_matrix_numpy = np.array(the_matrix)
			# takes the list of lists and make a two dimesion array 
			#print("the list as an array:") 
			#print(the_matrix_numpy)
			#print(the_matrix_numpy.dtype.name)
			count_fifty_percent_columns = 0
			for y in range(the_matrix_numpy.shape[1]):
			# iteration along the columns: .shape generates a list which has as elements the dimensions of the matrix (e.g. matrix 4x3: [4,3])  
			# [0] are the rows. [1] are the columns of the matrix 
				count = 0 
				countA = 0
				countT = 0
				countG = 0
				countC = 0
				count_missing_data = 0
				for n in range(the_matrix_numpy.shape[0]):
				# iteration on every element of the column, as [0] are the rows		
					if the_matrix_numpy[n,y] == "A" :
						countA = countA + 1
					elif the_matrix_numpy[n,y] == "T" :
						countT = countT + 1	
					elif the_matrix_numpy[n,y] == "C" :
						countC = countC + 1	
					elif the_matrix_numpy[n,y] == "G" :
						countG = countG + 1	
					elif the_matrix_numpy[n,y] == "a" :
						countA = countA + 1	
					elif the_matrix_numpy[n,y] == "t" :
						countT = countT + 1	
					elif the_matrix_numpy[n,y] == "c" :
						countC = countC + 1	
					elif the_matrix_numpy[n,y] == "g" :
						countG = countG + 1						
					else:
						count_missing_data = count_missing_data + 1	
					# if a charachter is a nucleotide count it
					# otherwise count it as a gap	
				count = countA + countC + countT + countG
				#print('the number of position of the column',y,' busy by nucleotides is: ',count)			
				#print('the number of gap is: ',count_missing_data)	
				if  count / n >= 0.5:
					count_fifty_percent_columns = count_fifty_percent_columns + 1  
				else:
					count_fifty_percent_columns = count_fifty_percent_columns
				# if the number of nucleotides divided by number of elements of the column is > than 0.5, then count the column		
			print('the number of columns with less than (or equal to) 50% of missing data is: ' + Fore.GREEN + Style.BRIGHT + '',count_fifty_percent_columns, '' + Style.RESET_ALL)
			if count_fifty_percent_columns >= minimum_amount_of_column_with_less_than_50percent_missing_data:
				print(Fore.RED + 'the file ', alignment_file,' has at least' + Style.RESET_ALL , minimum_amount_of_column_with_less_than_50percent_missing_data, Fore.RED +' columns with less than 50% of missing data' + Style.RESET_ALL) 	
				print(Fore.YELLOW + Style.BRIGHT + "Copying the file to the output folder..." + Style.RESET_ALL)
				shutil.copy(root + "/" + alignment_file, output_path)
			else:
				print(Fore.RED + 'the file ', alignment_file, Fore.RED  + Back.GREEN + ' has LESS than ' + Style.RESET_ALL , minimum_amount_of_column_with_less_than_50percent_missing_data, Fore.RED + ' columns with less than 50% of missing data' + Style.RESET_ALL) 					
				
#		/home/qiime2/Desktop/output		
				
