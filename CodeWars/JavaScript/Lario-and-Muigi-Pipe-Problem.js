function pipeFix(numbers) {
  return Array.from(
    { length: Math.max(...numbers) + 1 - Math.min(...numbers) },
    (_, i) => i + Math.min(...numbers)
  );
}
