export default function cleanSet(set, startString) {
  if (
    typeof set !== 'object' || typeof startString !== 'string' || startString.length === 0) {
    return '';
  }

  const arr = [];

  set.forEach((element) => {
    if (element.startsWith(startString)) {
      arr.push(element.slice(startString.length));
    }
  });

  return arr.join('-');
}
