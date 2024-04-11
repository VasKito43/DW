function soma(a, b){
    let total = a + b
    return total
}

const funcaoSoma = function(a, b){
    return a+b
}

const funcaoMultiplicação = (a, b) => a

function operacao(a, b, op){
    if (op == "+") {
        return a + b
    } else if (op == "-") {
        return a - b
    }else if (op == "*") {
        return a * b
    }else if (op == "/") {
        return a / b
    }

    return undefined
}

function operacao_V2(a, b, op){
    let resultado = op(a,b)
    return resultado
}

console.log(soma(10, 20))
console.log(funcaoSoma(50, 50))
console.log(multiplicacao(4, 25))

const multi = operacao(10, 2, "*")
console.log(operacao(10, 5, "/"))

// let valor = operacao_V2(10, 2, funcaoMultiplicação)
// console.log(valor)


console.log(operacao_V2(10, 2, (a,b) => a*b))
console.log(operacao_V2(10, 2, (a,b) => a+b))
console.log(operacao_V2(10, 2, (a,b) => a-b))
console.log(operacao_V2(10, 2, (a,b) => a**b))

let valor = operacao_V2(10, 2, function(a,b){
    return a+b
})

console.log(valor)