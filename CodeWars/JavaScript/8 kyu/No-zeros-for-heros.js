function noBoringZeros(n) {
  return n.toString().replace(/0+$/, '') * 1;
}
