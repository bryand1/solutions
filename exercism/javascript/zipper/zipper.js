const copy = tree => JSON.parse(JSON.stringify(tree));

class Zipper {
  constructor(tree, parent) {
    this.tree = tree;
    this.parent = parent || null;
  }

  static fromTree(tree) {
    return new Zipper(tree);
  }

  toTree() {
    return this.parent ? this.parent.toTree() : this.tree;
  }

  left() {
    const tree = this.tree.left;
    return tree ? new Zipper(tree, this) : null;
  }

  right() {
    const tree = this.tree.right;
    return tree ? new Zipper(tree, this) : null;
  }

  value() {
    return this.tree.value;
  }

  up() {
    return this.parent;
  }

  setValue(value) {
    this.tree.value = value;
    return this;
  }

  setLeft(tree) {
    this.tree.left = copy(tree);
    return this;
  }

  setRight(tree) {
    this.tree.right = tree;
    return this;
  }
}

export default Zipper;
