const codes = {
    1: 'eggs',
    2: 'peanuts',
    4: 'shellfish',
    8: 'strawberries',
    16: 'tomatoes',
    32: 'chocolate',
    64: 'pollen',
    128: 'cats',
};

export default class Allergies {
  constructor(code) {
    this.allergies = [];
    Object.keys(codes).forEach((k) => {
      if (code & k) this.allergies.push(codes[k]);
    });
  }

  list() {
    return this.allergies;
  }

  allergicTo(food) {
    return this.allergies.includes(food);
  }
}
