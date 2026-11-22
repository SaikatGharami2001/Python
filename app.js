// 1. Replace 5 with 3
// 2. Replace 3 with 10
// 3. Remove 5
// 4. Find 3
// 5. Find the largest number
// 6. Find the smallest number
// 7. Reverse the array
// 8. Count duplicates
// 9. Remove duplicates
// 10. Move all zeroes to the end

// const array = [100, 200, 730, 740, 50];

// let j = array.length - 1;

// for (let i = 0; i < array.length; i++) {
//   if (array[i] == 30) array[i] = array[j];
// }

// console.log(array);

// let j = 100;
// for (let i = 0; i < array.length; i++) {
//   if (array[i] == 30) array[i] = j;
// }

// console.log(array);

// let j = 50;
// for (let i = 0; i < array.length; i++) {
//   if (array[i] == j) array.pop();
// }

// console.log(array);

// for (let i = 0; i < array.length; i++) {
//   if (array[i] == 30) console.log("Found");
// }

// let smallest = array[0];

// for (let i = 0; i < array.length; i++) {
//   if (array[i] < smallest) {
//     smallest = array[i];
//   }
// }

// console.log(smallest);

// const array = [100, 200, 730, 740, 50];
// let i = 0;
// let j = array.length - 1;

// while (i < j) {
//   temp = array[i];
//   array[i] = array[j];
//   array[j] = temp;
//   i++;
//   j--;
// }

// console.log(array);

// 10. Move all zeroes to the end
const array = [1, 2, 0, 0, 3, 0, 4, 0, 5];

let j = array.length - 1;
let i = 0;

while (i < j) {
  if (array[i] !== 0) i++;
  else if (array[j] === 0) j--;
  else {
    let temp = array[i];
    array[i] = array[j];
    array[j] = temp;
    i++;
    j--;
  }
}

console.log(array);
