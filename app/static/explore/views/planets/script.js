const PLANET_DATA = {...window.__PLANET_DATA__};
const START = 'Overview';
const dataWindow = document.querySelector('.data-window');
const viewControls = [...document.querySelectorAll('.view-select-btn')];
const openPlanetListBtns = [...document.getElementsByClassName('open-planet-list')];
const planetListContainer = document.getElementById('select-planet');

const showPlanetList = () => {
    const isOpen = planetListContainer.classList.contains('open');

    if (isOpen) {
        planetListContainer.classList.remove('open');
        planetListContainer.classList.add('close');
    } else {
        planetListContainer.classList.add('open');
        planetListContainer.classList.remove('close');
    }

    openPlanetListBtns.forEach(btn => btn.classList.toggle('active'));
}

openPlanetListBtns.forEach(btn => btn.onclick = showPlanetList)

const getKeysArr = (obj) => [ ...Object.keys(obj) ];
const getValuesArr = (obj) => [ ...Object.values(obj) ];
const getDataArr = (obj) => [ ...Object.entries(obj) ];

const getMainObj = () => PLANET_DATA?.mainData;
const getAltObj = () => PLANET_DATA?.altData;

const getMainDataArr = () => getDataArr(getMainObj()).map(([ key, data ]) => ({ key: key, data: data }));
const getAltDataArr = () => getDataArr(getAltObj()).map(([ _, data ]) => data);

const mapAllDataArr = (arr) => arr.map(([ _, data ]) => data);
const findSectionData = (arr, id) => arr.find(({ key }) => key === id);
const parseSectionDataArr = (arr, id) => arr.map(({ key }) => key == id).map(({ data }) => data);

const cache = new Map()

const clearWindow = () => dataWindow.innerHTML = '';

const updateActiveHeader = (id) => {
    viewControls.forEach(btn => {
        if (btn.id === id) {
            btn.classList.add('active')
        } else {
            btn.classList.remove('active')
        }
    });
}

const renderContainer = (type) => {
    const el = document.createElement('div');
    const classMap = {
        'panel': 'grid-panel',
        'cell': 'grid-cell',
        'row': 'grid-row'
    }
    el.classList.add(classMap[type]);
    return el;
}

const renderHeaderEl = (text, depth = 0) => {
    const depthMap = {
        0: 'h3',
        1: 'h4',
    }

    const el = document.createElement(depthMap[depth]);
    el.textContent = text;
    return el;
}

const renderContentEl = (text, isUnit = false) => {
    const classMap = {
        true: 'unit-span',
        false: 'content-span'
    }

    const el = document.createElement('span')
    el.classList.add(classMap[isUnit]);
    el.textContent = text;
    return el;
}

const renderListElementWrapper = () => {
    const el = document.createElement('div');
    el.classList.add('list-element-wrapper');
    return el;
}

const renderContentContainer = (kind) => {
    const elementMap = {
        'scalar': 'p',
        'list': 'div',
        'tuple': 'div',
    }

    const classMap = {
        'scalar': 'content-wrapper',
        'list': 'list-wrapper',
        'tuple': 'tuple-wrapper'
    }

    const el = document.createElement(elementMap[kind]);
    el.classList.add(classMap[kind]);
    return el;
}

const renderScalar = ({ type, value, unit = null }) => {
    const children = [];

    const cleanFnMap = {
        'text': (str) => `${str.split('')[0].toUpperCase()}${str.slice(1)}`,
        'string': (str) => `${str.split('')[0].toUpperCase()}${str.slice(1)}`,
        'int': (num) => num,
        'float': (num) => num.toFixed(2),
        'bool': (val) => val,
    }

    value = cleanFnMap[type](value);

    const contentEl = renderContentEl(value);
    children.push(contentEl);

    if (unit) {
        const unitEl = renderContentEl(unit, true);
        children.push(unitEl);
    }

    return children;
}

const renderList = ({ type, value, unit = null }) => {
    const children = [];

    for (let i = 0; i < value.length; i++) {
        const { key, kind, type, unit, value: data } = value[i];
        if (!data) continue;
        const contentElContainer = renderListElementWrapper();
        const headingEl = renderHeaderEl(key, 1);
        const scalarWrapper = renderContentContainer('scalar');
        const contentElChildren = renderScalar({ type, value: data, unit });
        scalarWrapper.append(...contentElChildren);
        contentElContainer.append(headingEl, scalarWrapper);
        children.push(contentElContainer);
    }

    return children;
}

const renderTuple = ({ type, value, unit = null }) => {
    const children = [];

    for (let i = 0; i < value.length; i++) {
        const { key, kind, type, unit, value: data } = value[i];
        if (!data) continue;
        const contentElContainer = renderListElementWrapper();
        const headingEl = renderHeaderEl(key, 1);
        const scalarWrapper = renderContentContainer('scalar');
        const contentElChildren = renderScalar({ type, value: data, unit });
        scalarWrapper.append(...contentElChildren);
        contentElContainer.append(headingEl, scalarWrapper);
        children.push(contentElContainer)
    }

    return children;
}

const renderSectionContent = (kind, type, value, unit = null) => {
    const container = renderContentContainer(kind);

    const contentFnMap = {
        'scalar': ({ kind, type, value, unit }) => renderScalar({ kind, type, value, unit }),
        'list': ({ value }) => renderList({ value }),
        'tuple': ({ value, unit}) => renderTuple({ value, unit })
    }

    const el = contentFnMap[kind]({ kind, type, value, unit });

    container.append(...el);
    return container;
}

const renderSection = ({ children, key = null, kind = null }) => {
    for (let i = 0; i < children.length; i++) {
        const { display, key, kind, type, unit, value } = children[i];
        if (!value) continue;

        const container = renderContainer(display);
        const header = renderHeaderEl(key, 0);
        const contentContainer = renderSectionContent(kind, type, value, unit);

        container.append(header);
        container.append(contentContainer);
        dataWindow.append(container);
    }
}

const getSectionDataFromCache = (key) => cache.get(key) || null;

const getPlanetName = (arr) => arr.find(({ key }) => key === 'name')?.data
const generateCacheKey = (str1, str2) => `${str1}-${str2}`;

const parseMetaData = () => {
    const mainData = getMainDataArr();
    const altData = getAltDataArr();

    return { mainData, altData }
}

const initCacheData = () => {
    cache.set('allData', { ...parseMetaData() });
    return getSectionDataFromCache('allData');
}

const initSectionData = (planetName, sectionKey, allData = getSectionDataFromCache('allData')) => {
    const cacheKey = generateCacheKey(planetName, sectionKey);
    const { altData } = allData;
    const sectionData = findSectionData(altData, sectionKey);
    cache.set(cacheKey, sectionData);
    return getSectionDataFromCache(cacheKey);
}

const getSectionData = (sectionKey) => {
    const allData = getSectionDataFromCache('allData') || initCacheData();
    const { mainData } = allData;
    const planetName = getPlanetName(mainData);
    const cacheKey = generateCacheKey(planetName, sectionKey);
    return getSectionDataFromCache(cacheKey) || initSectionData(planetName, sectionKey, allData);
}

const changeView = (e) => {
    let id = START;

    if (e) {
        const target = e.target.closest('.view-select-btn')
        id = target.id
    }

    clearWindow();
    updateActiveHeader(id);
    renderSection(getSectionData(id));
}

viewControls.forEach(btn => btn.onclick = changeView)

changeView()
