myFunction = (array) => {return array.length<3 ? [] : array.slice(3, (array.length))}

console.log(myFunction([1, 2, 3, 4, 5]));
console.log(myFunction([5, 4, 3, 2, 1, 0]));
console.log(myFunction([10, 20, 30]));
console.log(myFunction([99, 100]));

