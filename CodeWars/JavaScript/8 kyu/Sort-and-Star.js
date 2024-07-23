function twoSort(s) {
  s.sort();
  const firstValue = s[0];
  const formattedString = firstValue.split('').join('***');
  return formattedString;
}
