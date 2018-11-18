export const solve = (x, y) => {
  if (typeof x !== 'number' || typeof y !== 'number') return null;
  const dist = Math.sqrt((x * x) + (y * y));
  if (dist > 10) return 0;
  if (dist > 5) return 1;
  if (dist > 1) return 5;
  return 10;
};
