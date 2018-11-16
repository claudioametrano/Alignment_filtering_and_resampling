print("********************************")
print("*Claudio G. Ametrano 2018 UNITS*")
print("********************************")
#USO: valuta quante sono le colonne della matrice (alignment) che hanno più caselle piene (a, g, t, c) che missing data "-" e se ce ne sono più di tot (deciso dall'utente) copia il file altrove
#  per dirla in altro modo cerca i file che hanno meno del 50% di missing data in almeno tot colonne dell'alignment!
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

minimum_amount_of_column_with_less_than_50percent_missing_data = int(input('Quante posizioni minimo con meno del 50% di missing data devono avere gli alignments? '))
output_path = input("In che path copio i file che soddisfano il criterio? ")
for root, dirs, files in os.walk(path, topdown=True):
	for alignment_file in files:
		if alignment_file.endswith('.fas'):
			print(Fore.MAGENTA + Style.BRIGHT + '-----------------------------------------------------------------------------------------------' + Style.RESET_ALL)
			print('Sto elaborando il file ',alignment_file,'')
			header_list = []
			the_matrix = []
			for record in SeqIO.parse(alignment_file, "fasta"):
			#SeqInputOutput.parse legge i dati del fasta (con "fasta" specifichi in che formato è il file con le sequenze)	
				header_list.append(record.id)
			#record.id sono gli header (nel pacchetto SeqIO di Biopython), record.seq sono invece le sequenze	
			#print(header_list)	
			# crea una lista appendendo uno dopo l'altro gli header delle sequenze	
			number_of_sequences = len(header_list)
			# conta gli elementi della lista creata
			print(Fore.GREEN + "il numero delle sequenze è " + Style.RESET_ALL ,number_of_sequences)
			sequences_length = len(record.seq)
			# conta i caratteri di una sequenza... si suppone le sequenze siano tutte lunghe uguali (dopo averle allineate e tagliate)
			print(Fore.GREEN + "l'alignment è lungo "+ Style.RESET_ALL ,sequences_length, Fore.GREEN + " nucleotidi" + Style.RESET_ALL)

			for record in SeqIO.parse(alignment_file, "fasta"):
				a = record.seq
				split_a = list(record.seq)
				the_matrix.append(split_a)
			# prendo le requenze una per una ricorsivamente e crea per ognuna una lista fatta dai singoli nucleotidi che appendo alla lista the_matrix		
			#print("la lista di liste contententi le sequenze è:")
			#print(the_matrix)
			the_matrix_numpy = np.array(the_matrix)
			# trasforma la lista di liste in un array a due dimensioni 
			#print("ecco la lista di lista trasformata in array:") 
			#print(the_matrix_numpy)
			#print(the_matrix_numpy.dtype.name)
			count_fifty_percent_columns = 0
			for y in range(the_matrix_numpy.shape[1]):
			# itero lungo le colonne: .shape genera una lista che ha per elementi le dimensioni della matrice es: matrice a 2 dimensioni 4 x 3  [4,3] 
			# [0] sono le righe. [1] le colonne in una matrice a due dimensioni 
				count = 0 
				countA = 0
				countT = 0
				countG = 0
				countC = 0
				count_missing_data = 0
				for n in range(the_matrix_numpy.shape[0]):
				# itero su ogni elemento della colonna, essendo [0] la righe	
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
					# se la casella della colonna contiene un nucleaotide contalo
					# se contine qualsiasi altra cosa contalo come gap	
				count = countA + countC + countT + countG
				#print('il numero di posizioni della colonna',y,' occupate da nucleotidi è: ',count)			
				#print('il numero di gap è: ',count_missing_data)	
				if  count / n >= 0.5:
					count_fifty_percent_columns = count_fifty_percent_columns + 1  
				else:
					count_fifty_percent_columns = count_fifty_percent_columns	
				# se il numero dei nucleotidi fratto il numero degli elementi della colonna è maggiore di 0.5 (ho più nucleotidi che gap) allora conta la colonna	
			print('il numero di colonne con missing data minore o uguale al 50% è: ' + Fore.GREEN + Style.BRIGHT + '',count_fifty_percent_columns, '' + Style.RESET_ALL)
			if count_fifty_percent_columns >= minimum_amount_of_column_with_less_than_50percent_missing_data:
				print(Fore.RED + 'il file ', alignment_file,' ha almeno' + Style.RESET_ALL , minimum_amount_of_column_with_less_than_50percent_missing_data, Fore.RED +' colonne con meno del 50% di missing data' + Style.RESET_ALL) 	
				print(Fore.YELLOW + Style.BRIGHT + "Sto copiando il file nella cartella di output..." + Style.RESET_ALL)
				shutil.copy(root + "/" + alignment_file, output_path)
			else:
				print(Fore.RED + 'il file ', alignment_file, Fore.RED  + Back.GREEN + ' ha MENO di ' + Style.RESET_ALL , minimum_amount_of_column_with_less_than_50percent_missing_data, Fore.RED + ' colonne con meno del 50% di missing data' + Style.RESET_ALL) 	
			# se le colonne che hanno più nucleotidi che missing data sono maggiori del numero prescelto copia il file nella cartella output se no avvisami che ha troppi missing data	
						
				
#		/home/qiime2/Desktop/output		
				
