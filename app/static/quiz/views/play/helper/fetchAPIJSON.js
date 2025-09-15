const postResponse = async (payload, endpoint) => {
    const res = await fetch(`/quiz/${endpoint}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CRSFToken": window.CSRF,
        },
        body: JSON.stringify(payload),
    });

    return res.json();
};

const getResponse = async (endpoint) => {
    const res = await fetch(`/quiz/${endpoint}`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "X-CRSFToken": window.CSRF,
        }
    });

    return res.json();
}

export default {
    postResponse,
    getResponse
}