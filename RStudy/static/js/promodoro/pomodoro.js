// pomodoro.js

document.addEventListener('DOMContentLoaded', () => {
    const startButton = document.getElementById('start-timer');
    const stopButton = document.getElementById('stop-timer');
    const timerDisplay = document.getElementById('timer');
    let timer = null;
    let timeLeft = 25 * 60; // 25 minutes

    startButton.addEventListener('click', () => {
        if (timer === null) {
            timer = startTimer();
            startButton.disabled = true;
            stopButton.disabled = false;
        }
    });

    stopButton.addEventListener('click', () => {
        if (timer !== null) {
            clearInterval(timer);
            timer = null;
            timeLeft = 25 * 60; // Reset timer to 25 minutes
            timerDisplay.textContent = '25:00';
            startButton.disabled = false;
            stopButton.disabled = true;
        }
    });

    function startTimer() {
        console.log('Timer started');
        return setInterval(() => {
            timeLeft--;
            const minutes = Math.floor(timeLeft / 60);
            const seconds = timeLeft % 60;
            timerDisplay.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;

            if (timeLeft <= 0) {
                clearInterval(timer);
                timer = null;
                timeLeft = 25 * 60; // Reset timer
                const completedSessionsElement = document.getElementById('completed-sessions');
                const completedSessions = parseInt(completedSessionsElement.textContent, 10);
                completedSessionsElement.textContent = completedSessions + 1;
                timerDisplay.textContent = '25:00';
                startButton.disabled = false;
                stopButton.disabled = true;
                // Here you might want to trigger a break or stop the work interval
            }
        }, 1000);
    }
});
