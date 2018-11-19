export const convert = (seq, inputBase, outputBase) => {
  if (inputBase === undefined || inputBase < 2 || !Number.isInteger(inputBase)) throw Error('Wrong input base');
  if (outputBase === undefined || outputBase < 2 || !Number.isInteger(outputBase)) throw Error('Wrong output base');
  if (seq.length === 0 || (seq.length > 1 && seq[0] === 0)) throw Error('Input has wrong format');
  if (seq.filter(x => x < 0 || x >= inputBase).length) throw new Error('Input has wrong format');
  let length = seq.length - 1;
  const baseTen = seq.map((i) => {
    const x = i * (inputBase ** length);
    length -= 1;
    return x;
  }).reduce((a, b) => a + b);
  const baseTenSeq = baseTen.toString().split('').map(x => Number(x));
  length = baseTenSeq.length - 1;

};
