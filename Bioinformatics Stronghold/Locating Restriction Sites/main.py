from Utilities.InputFileTools import Fasta


my = Fasta.get_fasta_as_list(fasta_string='''>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT
TCAATGCATGCGGGTCTATATGCAT
''')

print(my)