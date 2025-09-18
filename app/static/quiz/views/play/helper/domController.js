export default () => {
    const cache = {
        qText: document.getElementById("question-text"),
        currQCount: document.getElementById("curr-q-count"),
        totalQCount: document.getElementById("total-q-count"),
        inputOptions: [...document.querySelectorAll("input")],
        optionContainers: [...document.querySelectorAll(".question-option")],
        submitBtn: document.getElementById("check-answer"),
        progressBar: document.querySelector(".progress-bar"),
        resultModal: document.getElementById("result-modal"),
        resultMsg: document.getElementById("result-message"),
        resultScore: document.getElementById("result-score"),
        resultScoreStreak: document.getElementById("result-score-streak"),
        resultTotalScore: document.getElementById("result-total-score"),
        resultTimeTaken: document.getElementById("result-time-taken"),
        nextQBtn: document.getElementById("next-question"),
        typeIndicator: document.getElementById('type-indicator')
    };

    let currSubmitFn = null;
    let currNextFn = null;

    const bindSubmitEvent = (callbackFn) => {
        const { submitBtn } = cache;
        currSubmitFn = callbackFn;
        submitBtn.removeEventListener('click', currSubmitFn);
        submitBtn.onclick = currSubmitFn;
    }

    const bindNextQEvent = (callbackFn) => {
        const { nextQBtn } = cache;
        currNextFn = callbackFn;
        nextQBtn.removeEventListener('click', currNextFn);
        nextQBtn.onclick = currNextFn;
    }

    const updateQText = (newText) => {
        const { qText } = cache;
        qText.textContent = newText;
    }

    const updateCurrCount = (newCount) => {
        const { currQCount } = cache;
        currQCount.textContent = newCount
    }

    const updateTypeIndicator = (isSingle) => {
        const { typeIndicator } = cache;
        typeIndicator.textContent = isSingle ? 'Single Answer' : 'Multiple Answers'
    }

    const updateProgressBar = (newCount, maxCount) => {
        const { progressBar } = cache;
        const percentageProgress = (newCount / maxCount) * 100;
        progressBar.style.width = `${percentageProgress}%`;
    }

    const getInputContainer = (queryID) => {
        const { optionContainers } = cache;
        const foundContainer = optionContainers.find(({ id }) => id === `opt-${queryID}`);
        return foundContainer;
    }

    const getOptionInputs = () => [...cache.inputOptions];

    const getSelectedInputs = () => {
        const { inputOptions } = cache;

        const selectedValues = inputOptions
        .filter(input => input.checked)
        .map(input => input.value);
    
        return {
            selectedValues,
            selectedCount: selectedValues.length
        }
    }

    const updateInputValues = (newOptions) => {
        for (let i = 0; i < newOptions.length; i++) {
            const { id, label } = newOptions[i];
            const container = getInputContainer(id);
            const labelEl = container.querySelector('label');
            const labelVal = labelEl.querySelector('.option-value');
            labelVal.textContent = label;
        }
    }

    const showModal = (isCorrect) => {
        const { resultModal } = cache;

        const className = {
            true: 'correct',
            false: 'incorrect'
        }[isCorrect]

        resultModal.classList.add('active', className)
    }

    const updateModalMessage = (text) => {
        const { resultMsg } = cache;
        resultMsg.textContent = text;
    }

    const updateModalScore = (score) => {
        const { resultScore } = cache;
        resultScore.textContent = `+${score}`;
    }

    const updateModalScoreStreak = (streak) => {
        const { resultScoreStreak } = cache;
        resultScoreStreak.textContent = `Streak: ${streak}`;
    }

    const updateModalTotalScore = (totalScore) => {
        const { resultTotalScore } = cache;
        resultTotalScore.textContent = `Current Score: ${totalScore}`;
    }

    const updateModalTimeTaken = (timeS) => {
        const { resultTimeTaken } = cache;
        resultTimeTaken.textContent = `Time Taken: ${timeS}s`
    }

    const updateModal = (text, isCorrect, score, totalScore, timeS, streak) => {
        updateModalMessage(text);
        updateModalScore(score);
        updateModalScoreStreak(streak);
        updateModalTotalScore(totalScore);
        updateModalTimeTaken(timeS)
        showModal(isCorrect);
    }

    const removeModal = () => {
        const { resultModal, resultMsg, resultScore } = cache;

        resultModal.classList.remove('correct', 'incorrect', 'active');
        resultMsg.textContent = '';
        resultScore.textContent = '';
    }

    const resetOptions = () => {
        const { inputOptions } = cache;
        inputOptions.forEach(optEl => optEl.checked = false)
    }

    const changeOptionType = (isSingle) => {
        const newType = {
            true: 'radio',
            false: 'checkbox'
        }[isSingle]

        const { inputOptions } = cache;
        inputOptions.forEach(optEl => optEl.type = newType);
    }

    const toggleTypeError = (isError = false) => {
        const { typeIndicator } = cache;

        if (isError) {
            typeIndicator.textContent = "Select an Answer";
            typeIndicator.classList.add("invalid");
            return;
        }

        typeIndicator.classList.remove("invalid");
    };

    const refreshOptions = (newValues, isSingle) => {
        updateInputValues(newValues);
        changeOptionType(isSingle)
        toggleTypeError()
        updateTypeIndicator(isSingle)
        resetOptions()
    }

    const updateTotalQCount = (totalQs) => {
        const { totalQCount } = cache;
        totalQCount.textContent = totalQs;
    }

    const updateNextQButton = (text, callbackFn) => {
        const { nextQBtn } = cache;
        nextQBtn.textContent = text;
        if (currNextFn) {
            bindNextQEvent(callbackFn)
        }
    }

    const checkOptionErrors = (totalSelected) => {
        const { optionContainers } = cache;

        optionContainers.forEach(el => el.classList.remove('invalid'))

        if (totalSelected) return false;

        optionContainers.forEach((el) => el.classList.add("invalid"));

        toggleTypeError(true);

        return true;
    }

    const removeInvalidContainer = (e) => {
        let target = e.target;
        target = target.closest(".question-option");
        target.classList.remove('invalid')
    }

    cache.optionContainers.forEach(el => el.addEventListener('click', removeInvalidContainer))

    return {
        bindSubmitEvent,
        bindNextQEvent,
        updateQText,
        updateCurrCount,
        updateProgressBar,
        getInputContainer,
        getOptionInputs,
        getSelectedInputs,
        updateInputValues,
        updateModal,
        removeModal,
        refreshOptions,
        updateTotalQCount,
        updateNextQButton,
        checkOptionErrors
    };
};
