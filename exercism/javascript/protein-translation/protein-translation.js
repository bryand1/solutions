const protein = new Map([['AUG', 'Methionine'], ['UUU', 'Phenylalanine'], ['UUC', 'Phenylalanine'],
  ['UUA', 'Leucine'], ['UUG', 'Leucine'], ['UCU', 'Serine'], ['UCC', 'Serine'], ['UCA', 'Serine'],
  ['UCG', 'Serine'], ['UAU', 'Tyrosine'], ['UAC', 'Tyrosine'], ['UGU', 'Cysteine'], ['UGC', 'Cysteine'],
  ['UGG', 'Tryptophan'], ['UAA', 'STOP'], ['UAG', 'STOP'], ['UGA', 'STOP']]);

export default (rna) => {
  if (!rna) return [];
  const names = rna.match(/.{3}/g).map((codon) => {
    const name = protein.get(codon);
    if (name === undefined) throw new Error('Invalid codon');
    return name;
  });
  const stop = names.indexOf('STOP');
  return stop === -1 ? names : names.slice(0, stop);
};
