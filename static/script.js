function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    if (!userInput) return;

    let chatBox = document.getElementById("chat-box");
    
    // Display user message
    let userMessage = document.createElement("p");
    userMessage.className = "user";
    userMessage.innerText = userInput;
    chatBox.appendChild(userMessage);

    // Send request to Flask API
    fetch("/query", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Display bot response
        let botMessage = document.createElement("p");
        botMessage.className = "bot";
        botMessage.innerText = data.response;
        chatBox.appendChild(botMessage);

        // Clear input
        document.getElementById("user-input").value = "";
        chatBox.scrollTop = chatBox.scrollHeight;
    });
}
