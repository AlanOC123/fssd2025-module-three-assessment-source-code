const cache = {};
const trail = '-img';

['explore', 'timeline', 'quiz'].forEach(section => {
    const key = `${section}${trail}`
    cache[section] = document.getElementById(key)
})

