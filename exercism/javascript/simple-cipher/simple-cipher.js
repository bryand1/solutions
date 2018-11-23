const alphabet = 'abcdefghijklmnopqrstuvwxyz';
const length = alphabet.length;
const charAt = (i) => alphabet.charAt(i);
const indexOf = (char) => alphabet.indexOf(char);
const rand = () => charAt(Math.floor(Math.random() * length));

export class Cipher {
  constructor(key) {
    if (key !== undefined) {
      if (key.match(/^[a-z]+$/) === null) throw new Error('Bad key');
      this.key = key
    } else {
      let s = '';
      for (let i = 0; i < 100; i++) s += rand();
      this.key = s;
    }
  }

  encode(text) {
    let s = '';
    for (let i = 0; i < text.length; i++) {
      s += charAt((indexOf(this.key[i % this.key.length]) + indexOf(text[i])) % length);
    }
    return s;
  }

  decode(text) {
    let s = '';
    for (let i = 0; i < text.length; i++) {
      let charIndex = (indexOf(text[i]) - indexOf(this.key[i % this.key.length]) + length) % length;
      s += charAt(charIndex);
    }
    return s;
  }
};
