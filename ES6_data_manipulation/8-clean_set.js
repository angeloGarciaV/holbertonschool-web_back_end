export default function cleanSet(set, startString) {
  const arr = [];

  set.forEach((element) => {
    if (element.startsWith(startString)) {
      arr.push(element.slice(startString.length));
    }
  });

  return arr.join('-');
}
