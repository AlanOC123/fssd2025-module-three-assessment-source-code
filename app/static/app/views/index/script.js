const containers = [...document.querySelectorAll('.preview')];

const observerOptions = {
    root: (document.querySelector('main')),
    rootMargin: '0px',
    threshold: 0.2
}

const animateContainers = (entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate')
        } else {
            entry.target.classList.remove('animate')
        }
    })
}

const intersect = new IntersectionObserver(animateContainers, observerOptions)

containers.forEach(container => intersect.observe(container))
