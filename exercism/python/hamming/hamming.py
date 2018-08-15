def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands have different lengths")
    return sum(int(a != b) for a, b in zip(strand_a, strand_b))
