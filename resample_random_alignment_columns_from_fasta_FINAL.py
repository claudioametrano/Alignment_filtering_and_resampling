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
alignment_file = input("Inserire il nome del file fasta da ricampionare:")
rasampling_repeats = input("Quanti alignment ricampionati vuoi?: ")
rasampling_repeats = int(rasampling_repeats)
for record in SeqIO.parse(alignment_file, "fasta"):
#SeqInputOutput.parse legge i dati del fasta (con "fasta" specifichi in che formato è il file con le sequenze)	
	header_list.append(record.id)
#record.id sono gli header (nel pacchetto SeqIO di Biopython), record.seq sono invece le sequenze	
#print(header_list)	
# crea una lista appendendo uno dopo l'altro gli header delle sequenze	
number_of_sequences = len(header_list)
# conta gli elementi della lista creata
print("il numero delle sequenze è %s" %(number_of_sequences))
sequences_length = len(record.seq)
# conta i caratteri di una sequenza... si suppone le sequenze siano tutte lunghe uguali (dopo averle allineate e tagliate)
print("l'alignment è lungo %s nucleotidi" %(sequences_length))
columns_to_sample = int(input("Quante posizioni vuoi campionare?"))
# lo legger come un integer
        
for record in SeqIO.parse(alignment_file, "fasta"):
		a = record.seq
		split_a = list(record.seq)
		the_matrix.append(split_a)
#prendo le requenze una per una ricorsivamente e crea per ognuna una lista fatta dai singoli nucleotidi che appendo alla lista the_matrix		
#print("la lista di liste contententi le sequenze è:")
#print(the_matrix)

#print("eccola rappresentata come righe e colonne")
#for righe in the_matrix:
#	for oggetto in righe:
#		print (oggetto, end='')
#	print()
# stampa la lista bella ordinata :D

the_matrix_numpy = np.array(the_matrix) 
#trasforma la lista di liste in un array a due dimensioni 
#print("ecco la lista di lista trasformata in array:") 
#print(the_matrix_numpy)

for k in range (rasampling_repeats):
	count = count + 1
	number_list = list(range(sequences_length))
	random_number_list = random.sample(number_list, columns_to_sample)   
	print("posizioni campionate nell'alignment",random_number_list)
	#crea lista di integer lunga come l'alignment, campiona a caso da questa n numeri e li mette in una lista (senza ripetizione)
	
	"""#SE VOGLIO CAMPIONARE MA CON RIPETIZIONE...
	random_number_list = []
	#creo un lista vuota
	for i in range(0,5):
	#campioni 5 numeri	
		random_number_list.append(random.randrange(0,14))                       
	print(random_number_list)
	#appendere alla lista un certo numero n (range(0,n)) di numeri random tra 0 e m (random.ranrange(0,m))
	#mentra random.randrange crea solo i numeri casuali col range che gli indichi e poi li devi appendere tu ad una lista
	#il comando random.sample campiona da una lista già riempita di numeri e crea una lista coi numeri campionati random"""

	resampled_matrix = the_matrix_numpy[:,random_number_list]
	print("la matrice che rappresenta l'alignment ricampionato è")
	print(resampled_matrix)
	# la nuova matrice sarà composta dalle colonne identificate dai numeri casuali generati nella "random_number_list"
	
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
	# zip is useful to run two different for cycle in a parallel way!:)	
	# questo ciclo for scrive in modo alternato l'headr e la sua sequenza
		output_file.write(">" + header + "\n")	
		line= (''.join([str(elem) for elem in row]))	
	# the resampled sequence is a join, without spaces of the elements in a row	
		output_file.write(line + "\n")

	print("A partire dall'alignment file ", alignment_file, "sono stati creati ",count,"alignment campionando", columns_to_sample, "posizioni senza ripetizione, gli output sono salvati nei file resampled_alignment.fas")
