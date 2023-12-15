const regex = {
    'email': /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
    'cpf': /^\\d{3}\\.\\d{3}\\.\\d{3}\\-\\d{2}$/ 
}

$('#patientForm').ready(function(){
    applyMasks()
})

function applyMasks(){
    $('#phone').mask('(00) 00000-0000')

    $('#email').on('input', function(){
        if(!isValidEmail($(this).val())){
            $(this).addClass('erro')
        }else{
            $(this).removeClass('erro')
        }
    })

    $('#cpf').mask('000.000.000-00')
}

function isValidEmail(email){
    return regex.email.test(email)
}