function frete_function(event){
    event.preventDefault();

    const form = event.target;
    const origem = form.origem.value;
    const destino = form.destino.value;

    const url = `${freteUrl}?origem=${encodeURIComponent(origem)}&destino=${encodeURIComponent(destino)}`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            const resultadoDiv = document.getElementById('resultado');
            resultadoDiv.innerHTML = data.html;
            
        })
}
