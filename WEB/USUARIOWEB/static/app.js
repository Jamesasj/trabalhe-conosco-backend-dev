$(document).ready(
    function(){
        $('#tx_nome_username').keypress(
            function(e){
                var tx_nome_username = $('#tx_nome_username').val();
                tx_nome_username = tx_nome_username + e.key
                consultar_nome_username(tx_nome_username);
            }
        );
});
function consultar_nome_username(tx_nome_username){
    var servico = 'http://localhost:5000/usuario/'+tx_nome_username;
    $.getJSON(servico, preencher_lista)
}

function preencher_lista(data) {
    var lUsuarios = data.lUsuario;
    $('#lista_usuarios').empty();
    for (var i = 0; i < lUsuarios.length; i++) {
        adicionar(lUsuarios[i]);
    }
}

function adicionar(usuario){
    lista = $('#lista_usuarios');
    lista.append(
        $('<div></div>').append(
            $('<div></div>').append(usuario.nome).addClass('coluna1'),
            $('<div></div>').append(usuario.username).addClass('coluna2'),
            $('<div></div>').append(usuario.id).addClass('coluna3')
        ).addClass('linha')
    )
}
