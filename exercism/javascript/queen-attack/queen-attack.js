const repeat = (fn, n) => Array(n).fill(0).map(fn);
const grid = n => repeat(() => repeat(() => '_', n), n);


export default class Queens {

  constructor(positioning = { white: [0, 3], black: [7, 3] }, boardSize = 8) {
    const { white, black } = positioning;
    if (white[0] === black[0] && white[1] === black[1]) {
        throw Error('Queens cannot share the same space');
    }
    this.white = white;
    this.black = black;
    this.boardSize = boardSize;
  }

  toString() {
      const board = grid(this.boardSize);
      const [ wx, wy ] = [...this.white];
      const [ bx, by ] = [...this.black];
      board[wx][wy] = 'W';
      board[bx][by] = 'B';
      return board.map(r => r.join(' ')).join('\n') + '\n';
  }

  canAttack() {
      const [ wx, wy ] = [...this.white];
      const [ bx, by ] = [...this.black];
      return (wx === bx || wy === by || Math.abs(wx - bx) === Math.abs(wy - by));
  }
}
