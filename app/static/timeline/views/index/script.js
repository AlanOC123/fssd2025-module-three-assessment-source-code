const nodes = [...document.querySelectorAll('.decade-list-item')];

const activateNode = (e) => {
    const target = e.target.closest('.decade-list-item');

    if (target.classList.contains('active')) {
        const link = target.querySelector('.decade-link')
        link.click();
        return;
    }

    nodes.forEach(node => {
        node.classList.remove('active');
        if (node === target) node.classList.add('active');
    })
}

nodes.forEach(node => node.onclick = activateNode);
