// class Kata {
//     static disemvowel(str) {
//       let vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
//       let newStr = '';
//       for (let i = 0; i < str.length; i++) {
//         if (vowels.includes(str[i])) {
//           continue;
//         }
//         newStr += str[i];
//       }
//       return newStr;
//     }
//   }

//   console.log(Kata.disemvowel("This website is for losers LOL!"));

// function pat(n){
//   let str=''
//   for (let i=0;i<=n;i++){
//     for (let j=0; j < i;j++){
//       str +='*'
//     }
//     str +='\n'
//   }
//   return str
// }
// console.log(pat(6))

// function pat(n){
//   let str=''
//   for (let i=0;i<=n;i++){
//     for (let k=0;k< n-i;k++){
//       str +=' '
//     }
//     for (let j=0; j < i;j++){
//       str +='*'
//     }
//     str +='\n'
//   }
//   return str
// }
// console.log(pat(6))

// function pat(n){
//   let str=''
//   for (let i=0;i<=n;i++){
//     for (let k=0;k<i;k++){
//       str +=' '
//     }
//     for (let j=0; j < n-i;j++){
//       str +='*'
//     }
//     str +='\n'
//   }
//   return str
// }
// console.log(pat(6))

// const encryptThis = (str)=> {
//     const fun = (word) => {
//       console.log("Word:", word);
      
//       // Check if the word is empty
//       if (word === "") {
//         return "";
//       }
  
//       const char = word.split("");
  
//       console.log("Characters:", char);
  
//       // Convert the first character to its ASCII code
//       char[0] = word.charCodeAt(0).toString();
      
//       console.log("After converting to ASCII:", char[0]);
  
//       // Swap the second and last characters if the word has more than one character
//       if (char.length > 1) {
//         const temp = char[1];
//         char[1] = char[char.length - 1];
//         char[char.length - 1] = temp;
//       }
  
//       console.log("After swapping:", char.join(""));
  
//       return char.join("");
//     };
  
//     return str.split(" ").map(fun).join(" ");
//   };
  
// console.log(encryptThis("A wise old owl lived in an oak"));



// function meeting(s){
//     const met= s.toUpperCase().split(';')
//      .map((el)=>{
//          const temp= el.split(':')
//          console.log(temp)
//          const formitted= `(${temp[1]}, ${temp[0]})`
//          console.log('for',formitted)
//          return formitted
//      })
//      console.log('mrt',met)
//  met.sort((a,b)=>{
//      if(a>b){
//          return 1
//      }
//      else if(a<b){
//          return -1
//      }else{
//          return 0
//      }
 
//  })
//  return met.join('')
//  }


// // Example usage
// const meetingsString = "john:15;mary:10;peter:5";
// console.log("Result:", meeting(meetingsString));
