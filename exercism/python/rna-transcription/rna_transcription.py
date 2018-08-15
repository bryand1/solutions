dna_rna_map = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
}
dna_nucleotides = dna_rna_map.keys()

def to_rna(dna_strand):
    rna_strand = []
    for nucleotide in dna_strand:
        if nucleotide in dna_nucleotides:
            rna_strand.append(dna_rna_map[nucleotide])
        else:
            raise ValueError("{} nucleotide is invalid".format(nucleotide))
    return ''.join(rna_strand)
