var humanYearsCatYearsDogYears = function (humanYears) {
  return [
    humanYears,
    humanYears === 1
      ? 15
      : humanYears === 2
      ? 24
      : 15 + 9 + (humanYears - 2) * 4,
    humanYears === 1
      ? 15
      : humanYears === 2
      ? 24
      : 15 + 9 + (humanYears - 2) * 5,
  ];
};
