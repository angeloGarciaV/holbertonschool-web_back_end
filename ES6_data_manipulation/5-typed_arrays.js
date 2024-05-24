export default function createInt8TypedArray(length = 0, position = 0, value = 0) {
  if (position > length - 1) {
    throw new Error('Position outside range');
  }
  const buffer = new ArrayBuffer(8);
  const view = new DataView(buffer);
  view.setInt8(position, value);

  return view;
}
