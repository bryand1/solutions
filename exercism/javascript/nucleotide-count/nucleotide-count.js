export default class NucleotideCounts {
  static parse(seq) {
    const counts = new Map([['A', 0], ['C', 0], ['G', 0], ['T', 0]]);
    seq.split('').forEach((nucleotide) => {
        if (counts.has(nucleotide)) {
            counts.set(nucleotide, counts.get(nucleotide) + 1);
        } else {
            throw new Error('Invalid nucleotide in strand');
        }
    });
    return [...counts.values()].join(' ');
  }
};
