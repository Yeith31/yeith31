function validacampos(){
    var formulario;
    formulario=document.formUser;


    if(formulario.user.value==""){
        document.getElementById("validaaUser").innerHTML="Porfavor esciba su nombre de ususario";
        formulario.user.focus();
        return false;
    }else{
        document.getElementById("validaaUser").innerHTML="";
    }


    if(formulario.email.value==""){
        document.getElementById("validaEmail").innerHTML="Porfavor esciba su EMAIL";
        formulario.email.focus();
        return false;
    }else{
        document.getElementById("validaEmail").innerHTML="";
    }

    if(formulario.password.value==""){
        document.getElementById("validaPassword").innerHTML="Porfavor esciba su Contraseña";
        formulario.password.focus();
        return false;
    }else{
        document.getElementById("validaPassword").innerHTML="";
    }

    if(formulario.passwordC.value==""){
        document.getElementById("validaPasswordC").innerHTML="Porfavor Confirme su CONTRASEÑA";
        formulario.passwordC.focus();
        return false;
    }else{
        document.getElementById("validaPasswordC").innerHTML="";
    }

    formulario.submit();

}


