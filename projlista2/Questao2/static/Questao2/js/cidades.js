function cidade_encontrada(event){
    event.preventDefault();

    const form = event.target; //coleta os dados do form
    const nome = form.cidade.value; //pega especificamente o nome da cidade

    const url = `${previsaoUrl}?cidade=${encodeURIComponent(nome)}`;
        
    fetch (url)
        .then(response => response.json())
        .then(data => {
            const body = document.getElementById('body');
            const p = document.createElement('p');
                
            if (data.erro) { //se o retorno for de erro
                p.className = "m-2 box has-background-danger-light"
                p.innerHTML = `Erro: ${data.erro}`;
            } else {
                p.className = "m-2 box has-background-success-light"
                p.innerHTML = `Cidade: ${data.nome} <br> Previsão: ${data.previsao}`;
            }
                
            body.appendChild(p);
            form.reset();
        }) 
}