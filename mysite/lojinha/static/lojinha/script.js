"use strict"


function abrirSiteDeCompra(link){
    if(!link){
        return;
    }
    //alert("Ir para o site?")
    return window.open(link, '_blank');
}

function toCurrency(value) {
    return Number(value).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })
}

document.querySelectorAll('.curr_brl').forEach(element => {
    const value = Number(element.innerText.replace(',', '.'));
    element.innerText = toCurrency(value)
});