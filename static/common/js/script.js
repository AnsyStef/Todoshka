function TabController(){
    var TAB = document.getElementById('tab');
    var content = document.getElementById('tab-content');
    var body = document.getElementsByTagName('body');
    if (TAB.style.width == '60px'){
        TAB.style.transition = 'width 1s';
        TAB.style.width = '220px';
        content.style.display = 'inline';
    }
    else {
        content.style.display = 'none'
        TAB.style.width = '60px';
    }
}