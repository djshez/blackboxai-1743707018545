// DOM Elements
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const chatMessages = document.getElementById('chat-messages');
const typingIndicator = document.querySelector('.typing-indicator');

// Chat functionality
class JaycieChat {
    constructor() {
        this.messageHistory = [];
        this.isProcessing = false;
    }

    // Add a new message to the chat
    addMessage(message, isUser = false) {
        const timestamp = new Date().toLocaleTimeString();
        const messageElement = document.createElement('div');
        messageElement.className = `chat-bubble ${isUser ? 'ml-auto' : 'ml-4'} p-4 rounded-lg glass-effect`;
        
        messageElement.innerHTML = `
            <div class="flex items-start ${isUser ? 'flex-row-reverse' : ''}">
                <div class="w-8 h-8 rounded-full ${isUser ? 'bg-purple-600 ml-4' : 'bg-indigo-600 mr-4'} flex items-center justify-center">
                    <i class="fas ${isUser ? 'fa-user' : 'fa-robot'}"></i>
                </div>
                <div class="${isUser ? 'text-right' : ''}">
                    <p class="text-white">${message}</p>
                    <span class="text-xs text-gray-400 mt-2 block">${timestamp}</span>
                </div>
            </div>
        `;

        chatMessages.appendChild(messageElement);
        chatMessages.scrollTop = chatMessages.scrollHeight;
        this.messageHistory.push({ message, isUser, timestamp });
    }

    // Show typing indicator
    showTypingIndicator() {
        typingIndicator.classList.remove('hidden');
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Hide typing indicator
    hideTypingIndicator() {
        typingIndicator.classList.add('hidden');
    }

    // Process user message and get bot response
    async processMessage(userMessage) {
        if (this.isProcessing) return;
        this.isProcessing = true;

        try {
            // Add user message to chat
            this.addMessage(userMessage, true);
            
            // Show typing indicator
            this.showTypingIndicator();

            // Simulate API call delay (replace with actual API call)
            await new Promise(resolve => setTimeout(resolve, 1500));

            // Sample responses (replace with actual AI responses)
            const responses = [
                "I understand what you're saying. Could you tell me more about that?",
                "That's interesting! I'm learning from our interaction.",
                "I'm processing that information and updating my knowledge base.",
                "Based on my learning, I think we should explore this further.",
                "I'm integrating this new information with my existing knowledge."
            ];
            
            const response = responses[Math.floor(Math.random() * responses.length)];
            
            // Hide typing indicator and add bot response
            this.hideTypingIndicator();
            this.addMessage(response);

        } catch (error) {
            console.error('Error processing message:', error);
            this.hideTypingIndicator();
            this.addMessage("I apologize, but I encountered an error. Please try again.");
        }

        this.isProcessing = false;
    }
}

// Initialize chat
const jaycieChat = new JaycieChat();

// Event Listeners
chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const message = userInput.value.trim();
    
    if (message) {
        userInput.value = '';
        await jaycieChat.processMessage(message);
    }
});

// Handle enter key
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        chatForm.dispatchEvent(new Event('submit'));
    }
});

// Add smooth scroll behavior to chat messages
chatMessages.style.scrollBehavior = 'smooth';

// Initialize any tooltips or popovers
document.addEventListener('DOMContentLoaded', () => {
    // Future initialization code here
});

// Handle window resize for mobile responsiveness
window.addEventListener('resize', () => {
    chatMessages.scrollTop = chatMessages.scrollHeight;
});

// Error handling for network issues
window.addEventListener('offline', () => {
    jaycieChat.addMessage("⚠️ You're offline. Please check your internet connection.", false);
});

window.addEventListener('online', () => {
    jaycieChat.addMessage("✅ You're back online!", false);
});