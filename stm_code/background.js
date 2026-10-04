chrome.runtime.onMessage.addListener((message) => {

    if (message.type === "SUDDEN_STOP") {

        console.log("SuddenStop received. Contacting Python...");

        fetch("http://127.0.0.1:5000/crash", {
            method: "POST"
        })
        .then(response => {
            console.log("Python response:", response.status);
        })
        .catch(error => {
            console.error("Could not contact Python server:", error);
        });
    }
});