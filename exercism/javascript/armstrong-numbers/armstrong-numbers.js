export const validate = (n) => {
  const s = n.toString();
  return n === s.split('').map(i => parseInt(i, 10) ** s.length).reduce((a, b) => a + b);
};
