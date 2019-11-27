const tests = [90, 85, 77, 13, 58]

// const sum = tests.reduce(function(total, socre){
//   return total += socre
// })

const sum = tests.reduce((total, socre) => total += socre)

console.log(sum)