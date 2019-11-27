// // for loop 활용
// var students = [
//   { name: '서혁진', type: 'male'},
//   { name: '공선아', type: 'female'},
//   { name: '남찬우', type: 'male'},
//   { name: '이도현', type: 'female'},
// ]
// var strongStdudents = []
// // students라는 배열의 객체들 중 tpye이 female인 요소들만 뽑기!
// // studnets 원본 배열 자체를 바꾸고 싶은게 아니라,
// // 원하는 조건에 맞는 데이터들만 골라서 새로운 배열 만들기
// for (var i = 0; i < students.length; i++){
//   if(students[i].type == 'female'){
//     strongStdudents.push(students[i])
//   }
// }
// console.log(students)            // 원본 유지
// console.log(strongStdudents)     // 새로운 배열
// console.log(students[1].name)    // 객체 내 속성 접근하기

// // filter Helper 활용
// const STUDENTS = [
//   { name: '서혁진', type: 'male'},
//   { name: '공선아', type: 'female'},
//   { name: '남찬우', type: 'male'},
//   { name: '이도현', type: 'female'},
// ]
// // const STRONG_STUDENTS = STUDENTS.filter(function(studnet) {
// //   return students.type == 'female'
// // })

// const STRONG_STUDENTS = STUDENTS.filter( student => students.type == 'female')

// console.log(STRONG_STUDENTS)  // 새로운 배열
// console.log(STUDENTS)         // 원본 유지

// filter Helper를 사용해서 numbers 배열중 50보다 큰 값만 필터링해서 새로운 배열 저장하기

const numbers = [15, 35, 13, 36, 69, 3, 61, 55, 99, 5]
// const newNumbers = numbers.filter(function(num){
//   return num > 50
// })
const newNumbers = numbers.filter(num => num > 50)


console.log(numbers)
console.log(newNumbers)