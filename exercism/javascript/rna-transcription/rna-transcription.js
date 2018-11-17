const m = new Map([
  ['', ''],
  ['G', 'C'],
  ['C', 'G'],
  ['T', 'A'],
  ['A', 'U'],
]);

export const toRna = (s) => {
  const t = s.split('').map((char) => {
    const value = m.get(char);
    if (value === undefined) throw new Error('Invalid input DNA.');
    return value;
  });
  return t.join('');
};
