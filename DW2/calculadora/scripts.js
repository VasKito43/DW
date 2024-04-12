/****************************************************************
 * Seleção dos elementos HTML
 ****************************************************************/

// Botões
const btnBotoes = document.querySelectorAll("[btn-numero]");
const btnOperacoes = document.querySelectorAll("[btn-operador]");
const btnIgual = document.querySelector("[btn-igual]");
const btnDelete = document.querySelector("[btn-delete]");
const btnAC = document.querySelector("[btn-ac]");

// As divs que vão exibir os valores da calculadora
const bufferElemento = document.querySelector("[txt-buffer]");
const displayElemento = document.querySelector("[txt-display]");

// Objeto que irá representar e armazenar os dados da calculadora
const calculadora = {
  operandoAnterior: undefined,
  operandoAtual: undefined,
  operador: "",
  bufferTextoElemento: bufferElemento, // DIV buffer
  displayTextoElemento: displayElemento, // DIV display
};

/****************************************************************
 * Associar funções aos eventos dos elementos HTML
 ****************************************************************/
// Botão AC
btnAC.addEventListener("click", () => {
  limpaVariaveis(calculadora);
});

// Botão Delete
btnDelete.addEventListener("click", () => {
  apagaDigito(calculadora);
});

// Botão de igual
btnIgual.addEventListener("click", () => {
  executaCalculo(calculadora, 1);
});


// Botões dos números

for (let i = 0; i < btnBotoes.length; i++) {
    btnBotoes[i].addEventListener("click", () => {
        adicionaNumero(calculadora, btnBotoes[i].innerText);
      });
}


// Botões dos operadores
for (let i = 0; i < btnBotoes.length; i++) {
    btnOperacoes[i].addEventListener("click", () => {
        escolheOperador(calculadora, btnOperacoes[i].innerText);
      });
}


/****************************************************************
 * Regras da aplicação
 ****************************************************************/

/* Atualiza o display da calculadora.
 *  A atualização consiste em atualizar os elementos HTML buffer e display
 *  O elemento buffer é atulizado com o atributo operandoAnterior
 *  O elemento display é atualizado com o atributo operandoAtual
 */
function atualizaDisplay(calculadora, botao) {
    if (botao == "+" || botao == "-" || botao == "x" || botao == "÷"){
        bufferElemento.innerText = calculadora[0] + "  " + botao
        displayElemento.innerText = ""
    } else if (botao == "="){
        bufferElemento.innerText = ""
        displayElemento.innerText = calculadora[0]
    }else if (botao == "AC"){
        bufferElemento.innerText = ""
        displayElemento.innerText = ""
    }else if (botao == "DEL"){
        displayElemento.innerText = calculadora[1]
    }else {
        displayElemento.innerText += botao
       
    }
}

/* Limpa os atributos do objeto calculadora e atualiza o display.
 * Para atualizar o dispay, chame a função responsável por isso.
 */
function limpaVariaveis(calculadora) {
    calculadora[0] = undefined
    calculadora[1] = undefined

    atualizaDisplay(calculadora, "AC")
}

/* Função chamada quando um botão de número é pressionado
 * A função recebe o objeto calculadora e o número a ser exibido no display.
 * - Adiciona um dígito no atributo operandoAtual e atualiza o display
 * O dígito "." deve receber um tratamento especial
 */
function adicionaNumero(calculadora, numero) {
    // if (calculadora[2] === "-"){
    //     calculadora[1] = calculadora[2] + numero
    // } else{
    if (calculadora[1] === undefined){

        calculadora[1] = numero
    } else{
        calculadora[1] += numero
    }

    atualizaDisplay(calculadora, numero)
    

}

/* Função chamada quando um botão de operador é pressionado
 * Essa função tem comportamentos diferentes dependendo do estado da calculadora.
 * Se o operandoAnterior e o operandoAtual estiverem preenchidos
 * - executar o cálculo (chamar outra função para realizar o cálculo).
 * Caso o operandoAnterior estiver vazio,
 * - armazenar o operador recebido por parâmetro no atributo operador do objeto calculadora.
 * - copiar operandoAtual para o operandoAnterior, deixando a calculadora preparada para receber o próximo número
 */
function escolheOperador(calculadora, operador) {
    if (calculadora[2] === undefined){
        calculadora[2] = operador

    }
    if (calculadora[1] !== undefined || calculadora[0] !== undefined){

        executaCalculo(calculadora, 0)
    }
    calculadora[2] = operador
    atualizaDisplay(calculadora, operador)

}
    

/* A função recebe o objeto calculadora e executa o calculo
 * - Verificar a operação a ser executada
 * - Executar a operação
 * - Atualizar os atributos operador, operandoAnterior e operandoAtual
 * - Atualizar o display
 */
function executaCalculo(calculadora, numero) {
    if (calculadora[0] === undefined && (calculadora[2] === "÷" || calculadora[2] === "x")){
        calculadora[0] = "1"
    } else if (calculadora[1] === undefined && (calculadora[2] === "÷" || calculadora[2] === "x")){
        calculadora[1] = "1"
    } else if (calculadora[0] === undefined && (calculadora[2] === "+" || calculadora[2] === "-")){
        calculadora[0] = "0"
    } else if (calculadora[1] === undefined && (calculadora[2] === "+" || calculadora[2] === "-")){
        calculadora[1] = "0"
    }

    
    if (calculadora[2] === "÷"){
        calculadora[2] = "/"
    } else if (calculadora[2] === "x"){
        calculadora[2] = "*"
    }

    if (numero === 1){
        calculadora[0] = String(eval(calculadora[0] + calculadora[2] + calculadora[1]))
        calculadora[1] =  undefined
        atualizaDisplay(calculadora, "=")
    } else {
        calculadora[0] = String(eval(calculadora[0] + calculadora[2] + calculadora[1]))
        calculadora[1] =  undefined
    }
    
    if (calculadora[2] === "/"){
        calculadora[2] = "÷"
    } else if (calculadora[2] === "*"){
        calculadora[2] = "x"
    }
   
}

/* Função chamada quando o botão delete for pressionado
 * Apaga o último dígito digitado no
 */
function apagaDigito(calculadora) {
    calculadora[1] = calculadora[1].slice(0, -1)
    atualizaDisplay(calculadora, "DEL")
}
