export default function updateUniqueItems(arg) {
  if (typeof arg !== 'object') {
    throw new Error('Cannot process');
  }
  for (const items of arg) {
    if (items[1] === 1) {
      arg.set(items[0], 100);
    }
  }
}
