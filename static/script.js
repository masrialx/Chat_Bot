$(document).ready(function() {
    // Send message when user presses the send button
    $('#send-button').on('click', function() {
        let message = $('#message-input').val();
        if (message.trim() !== "") {
            appendMessage('user', message); // Append user's message
            $('#message-input').val(''); // Clear input field
            sendMessageToBot(message); // Send the message to the backend
        }
    });

    // Send message when user presses Enter
    $('#message-input').on('keypress', function(e) {
        if (e.which === 13) {
            $('#send-button').click();
        }
    });

    // Append message to the chat
    function appendMessage(sender, message) {
        const messageElement = `<div class="chat-message ${sender}">
            <p>${message}</p>
        </div>`;
        $('#chat-body').append(messageElement);
        $('#chat-body').scrollTop($('#chat-body')[0].scrollHeight); // Auto-scroll to the bottom
    }

    // Send message to the bot via AJAX
    function sendMessageToBot(message) {
        $.ajax({
            url: '/api/chat',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ "message": message }),
            success: function(response) {
                appendMessage('bot', response.response); // Append bot's response
            },
            error: function(error) {
                appendMessage('bot', 'Sorry, there was an error. Please try again.');
            }
        });
    }
});
