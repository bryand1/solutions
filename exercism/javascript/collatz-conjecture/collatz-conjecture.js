const collatz = (n, steps = 0) => {
  if (n === 1) return steps;
  if (n % 2 === 0) return collatz(n / 2, steps + 1);
  return collatz(3 * n + 1, steps + 1);
};

export const steps = (n) => {
  if (n <= 0) throw Error('Only positive numbers are allowed');
  return collatz(n);
};
