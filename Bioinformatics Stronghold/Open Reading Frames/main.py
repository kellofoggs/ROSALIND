import sys
import re
from Utilities.DNA import DNAStringTools
from Utilities.InputFileTools import Fasta


forward_strand = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"

reverse_complement = DNAStringTools.reverse_complement_dna(forward_strand)



def get_open_reading_frames(dna_strand:str):
    dna_string_len = len(dna_strand)
    start_codons = DNAStringTools.start_codons
    stop_codons = DNAStringTools.stop_codons
    reading_frames = []
    start_codon_indices = set()
    stop_codon_indices = []
    reading_frames = []
    last_reading_frame_len = 0

    for i in range(2, dna_string_len):
        curr_codon = dna_strand[i-2:i+1]
        if curr_codon in start_codons:

            start_codon_indices.add(i-2)
        if curr_codon in stop_codons and len(start_codon_indices) > 0:

            st_co = set(start_codon_indices)
            for index in st_co:
                if (i+1 - index) % 3 == 0:

                    reading_frames.append(dna_strand[index:i+1])
                    pass
                    start_codon_indices.remove(index)

    # print(reading_frames)
    return reading_frames


def main(dna_string:str):
    forward_strand = dna_string

    reverse_complement = DNAStringTools.reverse_complement_dna(dna_string)
    open_reading_frames = []
    open_reading_frames.extend(map(DNAStringTools.translate_dna_to_amino_acid, get_open_reading_frames(forward_strand)))
    open_reading_frames.extend(map(DNAStringTools.translate_dna_to_amino_acid, get_open_reading_frames(reverse_complement)))


    for frame in set(open_reading_frames):
        print((frame))
fasta_file_name = sys.argv[1]
dna_string = Fasta.get_fasta_as_list(fasta_file=fasta_file_name)[0]


main(dna_string)