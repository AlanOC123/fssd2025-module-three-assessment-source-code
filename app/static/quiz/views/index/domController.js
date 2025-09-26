const domController = () => {
    const cache = {
        randomiseBtn: document.getElementById("randomise"),
        countFieldset: document.getElementById("question-count"),
        countOptions: null,
        difficultyFieldset: document.getElementById("question-difficulty"),
        difficultyOptions: null,
        timeLimitFieldset: document.getElementById("time-limit"),
        timeLimitOptions: null,
        explorationFieldset: document.getElementById("exploration"),
        explorationOptions: null,
        historyFieldset: document.getElementById("history"),
        historyOptions: null,
    };

    const init = () => {
        const { 
            countFieldset, 
            difficultyFieldset, 
            timeLimitFieldset, 
            explorationFieldset, 
            historyFieldset 
        } = cache;

        cache.countOptions = [...countFieldset.querySelectorAll('input')];
        cache.difficultyOptions = [...difficultyFieldset.querySelectorAll("input")];
        cache.timeLimitOptions = [...timeLimitFieldset.querySelectorAll("input")];
        cache.explorationOptions = [...explorationFieldset.querySelectorAll("input")];
        cache.historyOptions = [...historyFieldset.querySelectorAll("input")];
    }

    init();

    const clearSubjects = () => {
        const { explorationOptions, historyOptions } = cache;
        [...explorationOptions, ...historyOptions].forEach(el => el.checked = false)
    }

    const randomiseOptions = () => {
        const { countOptions, difficultyOptions, timeLimitOptions, explorationOptions, historyOptions } = cache;

        const randChoice = (len) => Math.floor(Math.random() * len);

        const countSelect = countOptions[randChoice(countOptions.length)];
        const difficultySelect = difficultyOptions[randChoice(difficultyOptions.length)];
        const timeLimitSelect = timeLimitOptions[randChoice(timeLimitOptions.length)];

        [countSelect, difficultySelect, timeLimitSelect].forEach(el => el.checked = true)

        const isShort = ['five', 'ten'].includes(countSelect.id)
        || ['short', 'medium'].includes(timeLimitSelect.id);

        const isLong =
            ["fifteen", "twenty"].includes(countSelect.id) ||
            ["long"].includes(timeLimitSelect.id);

        let minSubjects;

        if (isShort) {
            minSubjects = 6;
        } else if (isLong) {
            minSubjects = 12;
        } else {
            minSubjects = null
        }

        if (minSubjects) {
            clearSubjects();
            for (let i = 0; i < minSubjects; i++) {
                const boxes = i % 2 === 0 ? explorationOptions : historyOptions;
                let elSelected = false;

                while (!elSelected) {
                    const selectEl = boxes[randChoice(boxes.length)];
                    if (!selectEl.checked) selectEl.checked = elSelected = true;
                }
            }
        }
    }

    const updateSubjectCounter = (counter, count, isSelected) => {
        const counter = target.querySelector(".selected-count");
        counter.textContent = count;
    };

    const updateSubjectWindow = (windowEl) => {
        const { explorationFieldset, historyFieldset } = cache;
        const isClosed = !windowEl.classList.contains("active");
        const { id } = windowEl;
        const target = id === 'exploration' ? explorationFieldset : historyFieldset;

        const counter = target.querySelector(".selected-count");
        const count = [...target.querySelectorAll('input')].filter(el => el.checked);
        updateSubjectCounter(counter, count)
    }

    function toggleWindow(e) {
        e.preventDefault();
        let target = e.target;
        target = target.closest(".subject-container");
        target.classList.toggle("active");

        const isClosed = !target.classList.contains("active");
        const { id } = target;

        if (isClosed) {
            const counter = target.querySelector(".selected-count");
            const boxArr = checkboxs[id];
            const count = getCheckedCount(boxArr);
            counter.textContent = count;
            if (count) {
                target.classList.add("selected");
            } else {
                target.classList.remove("selected");
            }
        }
    }

    const bindRandomEv = (e) => {
        e.preventDefault();
        randomiseOptions();
    }

    cache.randomiseBtn.addEventListener("click", bindRandomEv);

    return {

    }
}

export default domController;