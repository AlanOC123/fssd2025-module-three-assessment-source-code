import navigationController from "./helper/navigationController.js";
import domController from "./helper/domController.js";
import fetchAPIJSON from "./helper/fetchAPIJSON.js";
import intervalController from "./helper/intervalController.js";

const navCntrl = navigationController();
const domCntrl = domController();
const intervalCntrl = intervalController();

const submitAnswer = async () => {
    const { selectedCount, selectedValues } = domCntrl.getSelectedInputs();

    console.log(selectedCount)

    if (domCntrl.checkOptionErrors(selectedCount)) {
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

const finishQuiz = async () => {
    const res = await fetchAPIJSON.getResponse('next?finish=true');
    intervalCntrl.stopLocalInterval();
    intervalCntrl.stopGlobalInterval(true);

    const { redirect } = res;
    
    window.location.assign(redirect)
}

const nextQuestion = async () => {
    const res = await fetchAPIJSON.getResponse('next');

    const { currInd, maxCount, qText, qType, qOptions, isLast } = res;

    if (isLast) {

    }

    domCntrl.updateProgressBar(currInd, maxCount);

    domCntrl.updateCurrCount(currInd + 1);
    domCntrl.updateQText(qText)
    domCntrl.refreshOptions(qOptions, (qType === 'single-choice'))
    domCntrl.removeModal();

    if (isLast) {
        domCntrl.updateNextQButton('Finish', finishQuiz)
    }

    intervalCntrl.startLocalInterval();
}

const init = async () => {
    const res = await fetchAPIJSON.getResponse('next?progress=false');

    const { maxCount, currInd, qText, qOptions, qType, totalTime } = res;

    domCntrl.updateCurrCount(currInd + 1)
    domCntrl.updateTotalQCount(maxCount)
    domCntrl.updateQText(qText)
    domCntrl.refreshOptions(qOptions, (qType === 'single-choice'));
    domCntrl.updateProgressBar(currInd, maxCount);

    const intervalSettings = { timeLimit:totalTime, callbackFn: domCntrl.updateTimer }
    intervalCntrl.startLocalInterval();
    intervalCntrl.startGlobalInterval(intervalSettings)
}

const unloadData = async () => {
    intervalCntrl.stopGlobalInterval();
    intervalCntrl.stopLocalInterval();
    const payload = { timeS: intervalCntrl.getTimeLeft() }
    fetchAPIJSON.postResponse(payload, '/unload')
}

init()

window.addEventListener('beforeunload', unloadData)

domCntrl.bindSubmitEvent(submitAnswer);
domCntrl.bindNextQEvent(nextQuestion);