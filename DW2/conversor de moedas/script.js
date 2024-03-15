let form = document.getElementById('conversor');
let valorInput = document.getElementById('valor');
let moedaOrigemSelect = document.getElementById('moeda-origem');
let moedaDestinoSelect = document.getElementById('moeda-destino');
let valorConvertidoSpan = document.getElementById('valor-convertido');

let taxasDeCambio = {
    BRL: {
        USD: 0.19,
        EUR: 0.17,
    },
    USD: {
        BRL: 5.26,
        EUR: 0.90,
    },
    EUR: {
        BRL: 5.88,
        USD: 1.11,
    },
};

form.addEventListener('submit', (event) => {
    event.preventDefault();

    let valor = valorInput.value;
    let moedaOrigem = moedaOrigemSelect.value;
    let moedaDestino = moedaDestinoSelect.value;

    let taxaDeCambio = taxasDeCambio[moedaOrigem][moedaDestino];
    let valorConvertido = valor * taxaDeCambio;

    valorConvertidoSpan.textContent = `${valorConvertido} ${moedaDestino}`;
});