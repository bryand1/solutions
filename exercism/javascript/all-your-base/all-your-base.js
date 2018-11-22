const validInputBase = n => Number.isInteger(n) && n > 1;
const validOutputBase = n => Number.isInteger(n) && n > 1;
const validSequence = (seq, inputBase) => {
  const noLeadingZero = seq.length === 1 || (seq.length > 1 && seq[0] !== 0);
  const outOfRange = seq.filter(x => x < 0 || x >= inputBase).length;
  return noLeadingZero && outOfRange === 0;
}

export const convert = (seq, inputBase, outputBase) => {
  // Validate arguments
  if (!validInputBase(inputBase)) throw Error('Wrong input base');
  if (!validOutputBase(outputBase)) throw Error('Wrong output base');
  if (!validSequence(seq, inputBase)) throw Error('Input has wrong format');

  // Convert input sequence to base 10 integer
  let length = seq.length - 1;
  let baseTen = seq.map((i) => {
    const x = i * (inputBase ** length);
    length -= 1;
    return x;
  }).reduce((a, b) => a + b);

  // Convert base 10 integer to sequence of `outputBase` integer(s)
  const out = [];
  do {
    out.unshift(baseTen % outputBase);
    baseTen = Math.floor(baseTen / outputBase);
  } while (baseTen);
  return out;
};
