class Node {
  constructor(value, left = null, right = null) {
    this.value = value;
    this.left = left;
    this.right = right;
  }

  toString() {
    return `Node(${this.value}${
      this.left ? `, ${typeof this.left.value}` : ""
    }${this.right ? `${typeof this.right.value}` : ""})`;
  }
}

root = new Node(10);
left = new Node(5);
right = new Node(15);
left_left = new Node(2);
left_right = new Node(7);
right_left = new Node(12);
right_right = new Node(17);

root.left = left;
root.right = right;

left.left = left_left;
left.right = left_right;

right.left = right_left;
right.right = right_right;

module.exports = { Node, root };
