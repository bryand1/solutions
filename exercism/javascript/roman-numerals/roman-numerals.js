const roman = new Map([
  ['M', 1000],
  ['CM', 900],
  ['D', 500],
  ['CD', 400],
  ['C', 100],
  ['XC', 90],
  ['L', 50],
  ['XL', 40],
  ['X', 10],
  ['IX', 9],
  ['V', 5],
  ['IV', 4],
  ['I', 1],
]);

export default (digits) => {
  let n = digits;
  const out = [];
  roman.forEach((value, key) => {
    out.push(key.repeat(Math.floor(n / value)));
    n %= value;
  });
  return out.join('');
};
