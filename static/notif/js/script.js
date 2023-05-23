function closeNotif(elem){
    var obj = document.getElementById(elem.id).parentNode;
    obj.parentNode.removeChild(obj);
    return false;
}