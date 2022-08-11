/*
Given the root of a tree, return a list with every node by level, from left to right. 
Example: 
             10  <-- (root)
        5         15
    2      7   12     17  

Your code should return: [10, 5, 15, 2, 7, 12, 17]
Note: we do not care what data structure or algorithm you use, we only care about the output.
Moreover, the solution has to be strictly O(N) or better in time and space complexity where N = Nodes in the tree.
*/

const { Node: TreeNode, root } = require("./trees.js"); // brings in a pre-built tree representetd the given example

// to comply with the restrictions given, we must implement a custome queue since
// js does not have a package I can import
class Node {
  constructor(value, next = null, previous = null) {
    this.value = value;
    this.next = next;
    this.prev = previous;
  }
}

class Queue {
  constructor(items = []) {
    this.head = null;
    this.tail == null;

    items.forEach((item) => this.enqueue(item));
  }

  enqueue(value) {
    if (!this.tail) {
      this.head = new Node(value);
      this.tail = this.head;
      return;
    }

    this.tail.next = new Node(value, null, this.tail);
    this.tail = this.tail.next;
  }

  dequeue() {
    if (!this.head) return null;
    const { value } = this.head;
    if (this.head === this.tail) {
      this.head = null;
      this.tail = null;
      return value;
    }

    this.head = this.head.next;
    this.head.prev = null;
    return value;
  }

  isEmpty() {
    return this.head === null;
  }
}

/**
 * Takes the root of a tree and return a list with every node by level, from left to right.
 * @param {TreeNode} root of a tree
 * @returns {Array<Number>} list
 */
const bfs = (root) => {
  const queue = [root]; // FILO
  const output = [];
  while (queue.length > 0) {
    const { value, left, right } = queue.shift(); // destructing works out of the box
    output.push(value);

    if (left != null) {
      queue.push(left);
    }
    if (right != null) {
      queue.push(right);
    }
  }
  return output;
};

/**
 * Takes the root of a tree and return a list with every node by level, from left to right.
 * @param {TreeNode} root of a tree
 * @returns {Array<Number>} list
 */
const bfs_new_queue = (root) => {
  const queue = new Queue([root]);
  const output = [];
  while (!queue.isEmpty()) {
    const { value, left, right } = queue.dequeue(); // destructing works out of the box
    output.push(value);
    if (left != null) {
      queue.enqueue(left);
    }
    if (right != null) {
      queue.enqueue(right);
    }
  }
  return output;
};

console.log(bfs_new_queue(root));
