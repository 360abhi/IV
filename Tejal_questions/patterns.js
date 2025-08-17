//# reverse strings in an array
let input_list_1 = ["Hello","World"]

function reverse(arr){
    return arr.map(ele => ele.split('').reverse().join(''))
}

// palindromes in a list
let input_list_2 = ["nan","cococ","notin"]

function palindrome(arr){
    return arr.filter(ele => ele === ele.split('').reverse().join(''))
}

// console.log(palindrome(input_list_2))

// capitlize first letter 
let input_list_3 = ['abhishek','none']

function capitalize(arr){
    return arr.map(ele=>ele.charAt(0).toUpperCase()+ele.slice(1))
}
// console.log(capitalize(input_list_3))

// Sort by string length then alphabetically

let input_list_4 = ["none","null","undefined","abc","bcd","ze"]

function sortarr(arr){
    return arr.sort((a,b)=>{
        return a.length - b.length || a.localeCompare(b)
    })
}

console.log(sortarr(input_list_4))
