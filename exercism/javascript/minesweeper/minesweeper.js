const counter = grid => (x, y) => {
  if (grid[x][y] === '*') return '*';
  let mines = 0;
  if (grid[x - 1] && grid[x - 1][y] === '*') mines += 1;
  if (grid[x - 1] && grid[x - 1][y - 1] === '*') mines += 1;
  if (grid[x - 1] && grid[x - 1][y + 1] === '*') mines += 1;
  if (grid[x][y - 1] === '*') mines += 1;
  if (grid[x][y + 1] === '*') mines += 1;
  if (grid[x + 1] && grid[x + 1][y] === '*') mines += 1;
  if (grid[x + 1] && grid[x + 1][y - 1] === '*') mines += 1;
  if (grid[x + 1] && grid[x + 1][y + 1] === '*') mines += 1;
  return mines > 0 ? mines : ' ';
};

export default class Minesweeper {
  annotate(grid) {
    if (!grid.length || !grid[0]) return grid;
    const mygrid = grid.map((row) => {
      const ret = [];
      for (let i = 0; i < row.length; i += 1) {
        const char = row.charAt(i);
        ret.push(char === '*' ? char : 0);
      }
      return ret;
    });
    const f = counter(mygrid);
    for (let i = 0; i < mygrid.length; i += 1) {
      for (let j = 0; j < mygrid[0].length; j += 1) {
        mygrid[i][j] = f(i, j);
      }
    }
    return mygrid.map(row => row.join(''));
  }
}
