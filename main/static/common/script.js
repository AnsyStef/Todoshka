function add_new_note() {
    document.getElementById('add').style.display = 'none';
}
function get_data(){
    var name = '{{ note | escapejs }}'
    alert(`Name: ${name}`);
}