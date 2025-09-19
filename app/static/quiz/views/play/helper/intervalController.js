import fetchAPIJSON from "./fetchAPIJSON.js";

export default () => {
    let time_limit = null;
    
    let timeLeft = null;
    let localTimeCount = 0;

    let globalInterval = null;
    let globalCallback = null;
    let localInterval = null;

    const setLocalInterval = () => {
        localTimeCount++;
    }

    const stopGlobalInterval = (hardReset = false) => {
        if (globalInterval) {
            clearInterval(globalInterval)
        }

        if (hardReset) {
            globalInterval = null;
            timeLeft = null;
        }
    }

    const stopLocalInterval = () => {
        if (localInterval) {
            clearInterval(localInterval);
        }
        
        localInterval = null;
        const lastStoppedAt = localTimeCount;
        localTimeCount = 0;

        return lastStoppedAt
    }

    const setGlobalInterval = async () => {
        timeLeft--;

        globalCallback(timeLeft);

        if (timeLeft <= 0) {
            stopGlobalInterval(true)
            stopLocalInterval()
            const res = await fetchAPIJSON.getResponse('next?finish=true&expired=true');
            const { redirect } = res;
            window.location.assign(redirect);
        }
    };

    const startGlobalInterval = ({ timeLimit = null, callbackFn = null }) => {
        if (!timeLimit) return;

        if (timeLeft && globalCallback) {
            globalInterval = setInterval(setGlobalInterval, 1000);
            return;
        }

        stopGlobalInterval(true);
        globalCallback = callbackFn;
        timeLeft = time_limit = timeLimit;
        globalInterval = setInterval(setGlobalInterval, 1000)
    };

    const startLocalInterval = () => {
        localInterval = setInterval(setLocalInterval, 1000)
    };

    const getTimeLeft = () => timeLeft;

    return {
        startGlobalInterval,
        startLocalInterval,
        stopGlobalInterval,
        stopLocalInterval,
        getTimeLeft,
    }
}