function comentar(event, postIndex) {
    event.preventDefault(); //impede o recarregamento da página dps do envio do form 

    const form = event.target; //coleta os dados do form
    const autor = form.autor.value; //pega especificamente o valor do autor
    const conteudo = form.conteudo.value; //pega especificamente o valor do conteudo

    //apenas scripts confiaveis conseguem enviar requisições que vão modificar os dados (post)
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value; //todo form no django tem esse name no input

    //Requisição assincrona usando post precisa refazer o cabeçalho 
    fetch(comentarUrl, { //enviando uma requisição do tipo post para o servidor 
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded', //corpo ser interpretado como um form normal
            'X-CSRFToken': csrfToken //onde o django encontra o token
        },
        body: new URLSearchParams({ //criar um corpo da requisição para ser enviada ao servidor 
            'autor': autor,
            'conteudo': conteudo,
            'post_index': postIndex
        })
    })

    //lida com a resposta do servidor depois que o coment é enviado
    .then(response => response.json()) //converte a resposta do servidor em json
    .then(data => { //data recebe o objeto 
        const lista = document.getElementById(`comentarios-${postIndex}`);
        const item = document.createElement('li');
        item.innerHTML = `<strong>${data.autor}</strong>: ${data.conteudo}`;
        lista.appendChild(item);

        form.reset();
    });
}


