function confirmationMessage(id){
    var value = confirm("Seguro que deseas eliminar este elemento ?");
    if(value && id){
       document.forms['myform'+id].submit();
       window.close();
    }
}