import fetchAPIJSON from "./fetchAPIJSON.js";

export default () => {
    let TIME_LIMIT = Infinity;
    
    let timeLeft = TIME_LIMIT;
    let localTimeCount = 0;

    let globalInterval = null;
    let localInterval = null;

    const setLocalInterval = () => {
        localTimeCount++;
    }

    const stopGlobalInterval = (hardReset = false) => {
        if (globalInterval) {
            clearInterval(interval)
        }

        if (hardReset) {
            timeLeft = TIME_LIMIT;
        }

        globalInterval = null;
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

    const setGlobalInterval = () => {
        timeLeft--;

        if (!timeLeft) {
            stopGlobalInterval()
            stopLocalInterval()
            fetchAPIJSON.postResponse({}, 'result')
        }
    };

    const startGlobalInterval = () => {
        if (TIME_LIMIT === Infinity || !TIME_LIMIT) return;
        globalInterval = setInterval(setGlobalInterval, 1000);
    }

    const startLocalInterval = () => {
        localInterval = setInterval(setLocalInterval, 1000)
    };

    return {
        startGlobalInterval,
        startLocalInterval,
        stopGlobalInterval,
        stopLocalInterval
    }
}