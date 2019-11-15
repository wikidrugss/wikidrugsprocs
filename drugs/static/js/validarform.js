function revisar(elemento){
    if  (elemento.value==''){
        elemento.className='error';
        }
    else {
        elemento.className='input';
    }
}
function revisanombre(elemento){
    if(elemento.value!==''){
        var data = elemento.value;
        var expresion = /^[A-Z]+$/;
        if (!expresion.test(data)) {
            elemento.className = 'error';
        }
        else {
            elemento.className = 'input';        
        }
    }
}
function revisanumero(elemento){
    if (elemento.value!==''){
        var data = elemento.value;
        if(isNaN(data)){
            elemento.className='error';
            alert("Campo Numero no es numerico")
        }
        else {
            elemento.className='input';
        }
    }
}
function revisaemail(elemento){
    if (elemento.value!=='') {
        var data = elemento.value;
        var expresion = /\w+@\w+\.+[a-z]/;
        if (!expresion.test(data)){
            elemento.className='error';
        }
        else {
            elemento.className='input';
        }
    }
}
    