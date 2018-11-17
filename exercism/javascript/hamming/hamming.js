export const compute = (a, b) => {
  if (a.length !== b.length) throw Error('left and right strands must be of equal length');
  let hamming = 0;
  for (let i = 0; i < a.length; i += 1) {
    if (a[i] !== b[i]) hamming += 1;
  }
  return hamming;
};
