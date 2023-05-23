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
document.addEventListener('DOMContentLoaded', () => {

    const getSort = ({ target }) => {
        const order = (target.dataset.order = -(target.dataset.order || -1));
        const index = [...target.parentNode.cells].indexOf(target);
        const collator = new Intl.Collator(['en', 'ru'], { numeric: true });
        const comparator = (index, order) => (a, b) => order * collator.compare(
            a.children[index].innerHTML,
            b.children[index].innerHTML
        );

        for(const tBody of target.closest('table').tBodies)
            tBody.append(...[...tBody.rows].sort(comparator(index, order)));

        for(const cell of target.parentNode.cells)
            cell.classList.toggle('sorted', cell === target);
    };

    document.querySelectorAll('.table_sort thead').forEach(tableTH => tableTH.addEventListener('click', () => getSort(event)));

});