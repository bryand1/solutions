export default (legacy) => {
  const shiny = {};
  for (let point in legacy) {
      legacy[point].forEach(letter => shiny[letter.toLowerCase()] = +point);
  }
  return shiny;
};
