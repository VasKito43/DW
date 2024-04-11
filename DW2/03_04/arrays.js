// criar um array

let v1 = [1, 2,  3]
let v2 = new Array(1, 2, 3)
let v3 = new Array(3)
let v4 = Array.from("abcd")
let v5 = Array.from({length:5})

//inserção

v1.push(4)
v1.unshift(0)
v1[10] = 5

// remoção

v1.shift()
v1.pop()

delete v1[1]
v1.splice(2, 1)


// let copia1 = v2
// copia[0] = 100
let copia1 = [...v2]
copia[0] = 100