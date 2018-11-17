export default class Triangle {
  constructor(...args) {
    this.sides = [...args].sort((a, b) => a - b);
  }

  kind() {
    if (this.sides.filter(i => i <= 0).length) throw Error;
    if (this.sides.slice(0, 2).reduce((a, b) => a + b) <= this.sides[2]) throw Error;
    switch (new Set(this.sides).size) {
      case 1: return 'equilateral';
      case 2: return 'isosceles';
      default: return 'scalene';
    }
  }
}
