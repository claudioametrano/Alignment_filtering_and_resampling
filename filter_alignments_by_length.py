print("********************************")
print("*Claudio G. Ametrano 2018 UNITS*")
print("********************************")
#USE: in una cartella se un file è .fas ed allineato (tutte le sequenze di egual lunghezza) ti dice quali alignment sono >= e quali < di una 
#certa lunghezza e manda a schermo una lista di quelli >= di tot bp  
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
length = input('quante baia di basi devono essere lunghi almeno gli aligment? ')
length = int(length)
for root, dirs, files in os.walk(path, topdown=True):
	for alignment_file in files:
		if alignment_file.endswith('.fas'):
			for record in SeqIO.parse(alignment_file, "fasta"):
			#SeqInputOutput.parse legge i dati del fasta (con "fasta" specifichi in che formato è il file con le sequenze)	
				header_list.append(record.id)
			#record.id sono gli header (nel pacchetto SeqIO di Biopython), record.seq sono invece le sequenze	
			#print(header_list)	
			# crea una lista appendendo uno dopo l'altro gli header delle sequenze	
			number_of_sequences = len(header_list)
			# conta gli elementi della lista creata
#			print("il numero delle sequenze è %s" %(number_of_sequences))
			sequences_length = len(record.seq)
			# conta i caratteri di una sequenza... si suppone le sequenze siano tutte lunghe uguali (dopo averle allineate e tagliate)
#			print("l'alignment è lungo %s nucleotidi" %(sequences_length))
			if sequences_length >= length:
				count = count + 1
				alignemtns_longer_than.append(alignment_file)
			else:
				count1 = count1 + 1
		else:
			count2 = count2 + 1
print('Gli alignment più lunghi o uguali a ',length,'bp sono: ', alignemtns_longer_than)			
print('Gli alignment più lunghi o uguali a 1000 bp sono ',count)
print('Gli alignment più corti di ',length,' bp sono ',count1)
print('Nelle cartelle ci sono ',count2,' file che non sono .fas')