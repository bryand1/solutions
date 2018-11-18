export const encode = s => s.replace(/(.)\1+/g, ($0, $1) => $0.length + $1);
export const decode = s => s.replace(/(\d+)(.)/g, ($0, $1, $2) => $2.repeat($1));
