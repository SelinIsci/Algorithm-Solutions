function addLength(str) {
  let words = str.split(' ');
  let result = [];
  for (let i = 0; i < words.length; i++) {
    result.push(words[i] + ' ' + words[i].length);
  }
  return result;
}
