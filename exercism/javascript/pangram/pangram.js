const letters = 'abcdefghijklmnopqrstuvwxyz';

export const isPangram = (a) => {
  if (!a) return false;
  const b = new Set(Array.from(letters));
  Array.from(a.toLowerCase()).forEach(c => b.delete(c));
  return b.size === 0;
};
