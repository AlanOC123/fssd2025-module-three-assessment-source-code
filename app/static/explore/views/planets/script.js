const PLANET_DATA = {...window.__PLANET_DATA__};
const START = 'Overview';
const dataWindow = document.querySelector('.data-wrapper');
const viewControls = [...document.querySelectorAll('.section-nav-item')]

console.log()

const getKeys = () => PLANET_DATA.map(data => data?.key);
const getValues = () => PLANET_DATA.map(data => Object.values(data));
const getData = (id) => getValues().filter(data => data.includes(id))[0].slice(0, -1)[0];

const renderP = (content, ...spans) => {
    const el = document.createElement('p');
    let isHeader = !spans.length;

    el.classList.add(`card-${({ true: 'header', false: 'content' }[isHeader])}`);
    el.textContent = content;

    if (isHeader) return el;
    spans = spans.filter(el => !!el)
    el.append(...spans);

    return el;
}

const renderSpan = (content, isUnit = false) => {
    const el = document.createElement('span');
    const className = { true: 'unit', false: 'content' }[isUnit] || "";

    el.classList.add((className ? `card-${className}-wrapper` : className));
    el.textContent = content;

    return el;
}

const renderGridCard = () => {
    const el = document.createElement('div');
    el.classList.add('grid-card');
    return el;
}

const contentWrapper = (...children) => {
    const el = document.createElement('div');

    el.classList.add('content-container');
    el.append(children);

    return el;
}

const renderContentCard = (header, content, unit = null, isGridItem = true) => {
    const el = renderGridCard();
    const headerP = renderP(header);
    const contentSpan = renderSpan(content);
    let unitSpan = null;

    if (unit) {
        unitSpan = renderSpan(unit, true)
    }

    el.classList.add((isGridItem ? "span-1" : "content-container"));

    const contentP = renderP("", contentSpan, unitSpan)

    el.append(headerP, contentP);
    return el;
}

const renderLongCard = (heading, content) => {
    const el = renderGridCard()
    el.classList.add('span-4');
    const headerP = renderP(heading);
    const contentSpan = renderSpan(content);
    const contentP = renderP("", contentSpan);
    el.append(headerP, contentP);
    return el;
}

const renderSpanColCardWithContainer = (data, types) => {
    const el = renderGridCard();
    el.classList.add('span-4');
    const children = [];

    for (let i = 0; i < data.length; i++) {
        console.log(data[i]);
        console.log(types[i]);
    }
    return el;
}

const renderSpanAllCard = (content) => {
    const el = renderGridCard()
    const p = document.createElement('p');
    p.textContent = content;
    el.classList.add('span-all');
    el.append(p);
    return el;
}

const clearWindow = () => dataWindow.innerHTML = '';

const changeView = (e) => {
    let target = null;
    let id = null;

    if (e) {
        target = e.target.closest('.section-nav-item');
        id = target.id;
    } else {
        id = START
    }

    clearWindow()
    const data = getData(id) || [];
    if (!data.length) throw new Error("Error getting data");

    for (let i = 0; i < data.length; i++) {
        const { key, value, dataType, unit } = data[i];

        if (value === 'N/A') continue;

        let el = null;
        if (dataType === 'int' || dataType === 'float') {
            el = renderContentCard(key, value, (unit !== 'None' ? unit : null))
        } else if (dataType === 'long') {
            el = renderSpanAllCard(value);
        } else if (dataType === 'short') {
            el = renderLongCard(key, value);
        } else {
            renderSpanColCardWithContainer(value, dataType)
        }

        if (el) {
            dataWindow.append(el);
        }
    }

}

viewControls.forEach(btn => btn.onclick = changeView)

changeView()
