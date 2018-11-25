const abc = 'abcdefghijklmnopqrstuvwxyz';

export const encode = (s) => (
  s.match(/\w/g).reduce((acc, cur, idx) => {
    const space = (idx % 5 === 0 && idx > 0 ? ' ' : '')
    const char = !isNaN(cur) ? cur : abc.slice(~abc.indexOf(cur.toLowerCase())).charAt(0);
    return acc + space + char;
  }, '')
);
