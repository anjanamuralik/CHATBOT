// script.js
function sendMessage() {
    var userInput = document.getElementById('user-input').value;
    var chatBox = document.getElementById('chat-box');

    if (userInput.trim() === '') {
        return;
    }

    // Display user message
    var userMessage = `
        <div class="message-container">
            <div class="message user-message">
                ${userInput}
            </div>
        </div>
    `;
    chatBox.innerHTML += userMessage;

    // Simulate bot response after a short delay
    setTimeout(function() {
        var botMessage = `
            <div class="message-container">
                <div class="message bot-message">
                    This is a bot response.
                </div>
            </div>
        `;
        chatBox.innerHTML += botMessage;
        chatBox.scrollTop = chatBox.scrollHeight; // Scroll to bottom of chat box
    }, 500);

    // Clear input field
    document.getElementById('user-input').value = '';
}
