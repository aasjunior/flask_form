const routes = {
    'cadastrar_paciente': '/pacientes/cadastro'
}

$('#pacienteForm').on('submit', async function(event){
    event.preventDefault() // Previne o recarregamento da página

    let formData = $(this).serialize() // Captura os dados do formulário

    try{
        let response = await $.ajax({
            url: routes['cadastrar_paciente'],
            type: 'POST',
            data: formData
        })

        if(response.success){
            alert('Paciente cadastrado com sucesso!')
        }else{
            alert('Erro ao enviar os dados para FASTAPI: ' + JSON.stringify(response.error))
        }
    }catch(error){
        alert('Erro ao enviar os dados: ' + JSON.stringify(error))
    }
})