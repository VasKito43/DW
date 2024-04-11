let v1 = [1,2,3,4]
v1.fill(0)
v1.reverse()

let copia = []
for (let i = 0; i<v2.length; i++) {
    copia[1] = v2[i] * 2
}

let copia2 = v2.map(elemento => elemento - 1)

// let copia3 = []
// for (let i = 0; i<v2.length; i++) {
//     if (v2[i] % 2 ==0){
//         copia.push(v2[i])
//     }
// }

let copia3 = v2.filter(elemento => {elemento % 2 != 0
    return elemento % 2 == 0
})