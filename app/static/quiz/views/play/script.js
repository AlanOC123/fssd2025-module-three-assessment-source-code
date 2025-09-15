import navigationController from "./helper/navigationController.js";
import domController from "./helper/domController.js";
import fetchAPIJSON from "./helper/fetchAPIJSON.js";
import intervalController from "./helper/intervalController.js";

const navCntrl = navigationController();
const domCntrl = domController();
const intervalCntrl = intervalController();

const submitAnswer = async () => {
    const { selectedCount, selectedValues } = domCntrl.getSelectedInputs();

    if (selectedCount === 0) {
        return;
    }

    const t = intervalCntrl.stopLocalInterval()

    const payload = {
        answers: selectedValues,
        time: t
    }

    const res = await fetchAPIJSON.postResponse(payload, 'submit');

    const {
        allCorrect,
        correctOpts,
        currentStreak,
        awardedPoints,
        runningTotal,
        timeTaken,
        redirect = null,
    } = res;

    console.log(redirect)

    if (redirect) {
        console.log(redirect);
        window.location.assign(redirect);
        return;
    }

    const text = allCorrect ? "Correct! Well Done" : "Sorry, Next Time!";

    domCntrl.updateModal(
        text, 
        allCorrect, 
        awardedPoints, 
        runningTotal, 
        timeTaken,
        currentStreak
    )
}

const nextQuestion = async () => {
    const res = await fetchAPIJSON.getResponse('next');

    const { currInd, maxCount, qText, qType, qOptions, isLast } = res;

    domCntrl.updateProgressBar(currInd, maxCount);

    domCntrl.updateCurrCount(currInd + 1);
    domCntrl.updateQText(qText)
    domCntrl.refreshOptions(qOptions, (qType === 'single-choice'))
    domCntrl.removeModal();

    intervalCntrl.startLocalInterval();
}

const init = async () => {
    const res = await fetchAPIJSON.getResponse('next?progress=false');

    const { maxCount, currInd, qText, qOptions, qType } = res;

    domCntrl.updateCurrCount(currInd + 1)
    domCntrl.updateTotalQCount(maxCount)
    domCntrl.updateQText(qText)
    domCntrl.refreshOptions(qOptions, (qType === 'single-choice'));
    domCntrl.updateProgressBar(currInd, maxCount)

    intervalCntrl.startLocalInterval();
}

init()

domCntrl.bindSubmitEvent(submitAnswer);
domCntrl.bindNextQEvent(nextQuestion);