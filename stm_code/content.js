console.log("ST SuddenStop detector loaded.");

const SUDDEN_STOP_SELECTOR =
  '#project-example-get_started_fan_coil_monitoring_mlc-inference-classes > div > div.flex-1 > div:nth-child(3)';

let suddenStopWasActive = false;
let lastTriggerTime = 0;

const COOLDOWN_MS = 10000;

function checkSuddenStop() {
    const row = document.querySelector(SUDDEN_STOP_SELECTOR);

    if (!row) {
        return;
    }

    const mainRow = row.firstElementChild;

    if (!mainRow || mainRow.children.length < 2) {
        return;
    }

    const timeline = mainRow.children[1];

    const bars = Array.from(timeline.children);

    const suddenStopActive = bars.some(bar => {
        const right = parseFloat(bar.style.right);

        return !Number.isNaN(right) && right <= 0.5;
    });

    if (suddenStopActive && !suddenStopWasActive) {

        const now = Date.now();

        if (now - lastTriggerTime > COOLDOWN_MS) {

            console.log("🚨 SUDDEN STOP DETECTED");

            lastTriggerTime = now;

            chrome.runtime.sendMessage({
                type: "SUDDEN_STOP"
            });
        }
    }

    suddenStopWasActive = suddenStopActive;
}

setInterval(checkSuddenStop, 100);