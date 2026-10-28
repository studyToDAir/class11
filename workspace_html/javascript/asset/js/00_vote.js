
const names = ['규혁', '근욱', '영욱', '상우', '용준', '도영', '재성', '준석']

let idx = Math.floor(Math.random() * names.length)
console.log(names[idx])

result = {}
for (let i=0; i<100; i++){
    let idx = Math.floor(Math.random() * names.length)
    // console.log(names[idx])
    if (result[names[idx]] == undefined){
        result[names[idx]] = 1
    } else {
        // result[names[idx]] = result[names[idx]] + 1
        // result[names[idx]] += 1
        result[names[idx]]++
    }
}
console.log(result)

let max = -1
let name = null
for(obj in result) {
    // console.log(obj, result[obj])
    if(max < result[obj]){
        max = result[obj]
        name = obj
    }
}

console.log(name, max)
