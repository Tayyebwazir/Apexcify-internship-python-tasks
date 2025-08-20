import streamlit as st
import time

def get_chatbot_response(user_input):
    """
    Rule-based chatbot that returns responses based on user input
    """
    # Convert to lowercase for easier matching
    input_text = user_input.lower().strip()
    
    # Greetings
    if input_text in ["hello", "hi", "hey", "good morning", "good afternoon"]:
        return "Hi there! How can I help you today?"
    
    # How are you responses
    elif input_text in ["how are you", "how are you?", "how do you do", "how's it going"]:
        return "I'm doing great, thanks for asking! How are you?"
    
    # Goodbyes
    elif input_text in ["bye", "goodbye", "see you later", "see ya", "farewell"]:
        return "Goodbye! Have a wonderful day!"
    
    # Name questions
    elif input_text in ["what's your name", "what is your name", "who are you"]:
        return "I'm a simple rule-based chatbot. You can just call me Bot!"
    
    # Thank you responses
    elif input_text in ["thank you", "thanks", "thank you very much"]:
        return "You're welcome! Is there anything else I can help you with?"
    
    # Weather questions
    elif "weather" in input_text:
        return "I don't have access to weather data, but I hope it's nice where you are!"
    
    # Help requests
    elif input_text in ["help", "what can you do", "commands"]:
        return """I can respond to:
        • Greetings (hello, hi, hey)
        • How are you questions
        • Goodbyes (bye, goodbye)
        • Name questions
        • Thank you messages
        • Weather questions
        • Personal questions (Do you know me? Where do I live?)
        • Sports questions (What about Babar Azam?)
        • Help requests"""
    
    # Time questions
    elif "time" in input_text or "what time" in input_text:
        return "I don't have access to real-time data, but you can check your device's clock!"
    
    # Age questions
    elif "age" in input_text or "old are you" in input_text:
        return "I'm a computer program, so I don't have an age in the traditional sense!"
    
    # Personal questions about the user (Tayyeb)
    elif "can you know me" in input_text or "do you know me" in input_text or "who am i" in input_text:
        return "Yes, you are Tayyeb Wazir!"
    
    # Location questions
    elif "where i am living" in input_text or "where do i live" in input_text or "my location" in input_text:
        return "Yes, you are living in Bannu!"
    
    # Babar Azam questions
    elif "babar azam" in input_text or "what about babar azam" in input_text or "babar" in input_text:
        return "Babar Azam is a Pakistani cricket world class batsman and he is famous for his cover drive!"
    
    # Cricket related questions
    elif "cricket" in input_text:
        return "Cricket is a great sport! Pakistan has many talented players like Babar Azam."
    
    # Pakistan related questions
    elif "pakistan" in input_text:
        return "Pakistan is a beautiful country with amazing cricket talent!"
    
    # Default response for unrecognized input
    else:
        return "I'm not sure how to respond to that. Try saying hello, asking how I am, or type 'help' for available commands!"

# Function to demonstrate chatbot in console (for learning purposes)
def demonstrate_chatbot():
    """
    Console demonstration of the chatbot functionality
    """
    print("=== Chatbot Console Demo ===")
    test_inputs = [
        "hello",
        "how are you",
        "what's your name", 
        "can you know me",
        "where i am living",
        "what about babar azam",
        "weather",
        "help",
        "bye",
        "random text"
    ]
    
    for user_input in test_inputs:
        response = get_chatbot_response(user_input)
        print(f"User: {user_input}")
        print(f"Bot: {response}")
        print("-" * 40)

# Streamlit UI Configuration
def main():
    """
    Main function that creates the Streamlit UI
    """
   
    st.set_page_config(
        page_title="Simple Chatbot",
        page_icon="🤖",
        layout="centered"
    )
    
   
    st.title("🤖 Simple Rule-Based Chatbot")
    st.write("A basic chatbot built with Python and Streamlit")
    
   
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {"role": "bot", "message": "Hello! I'm a simple chatbot. Try saying hello, asking how I am, or type 'help' for commands!"}
        ]
    
    
    st.subheader("Chat Window")
    
    # Container for chat messages
    chat_container = st.container()
    
    with chat_container:
        for chat in st.session_state.chat_history:
            if chat["role"] == "user":
                st.write(f"**You:** {chat['message']}")
            else:
                st.write(f"**Bot:** {chat['message']}")
    
    # Input section
    st.subheader("Your Message")
    
   
    col1, col2, col3 = st.columns([3, 1, 1])
    
    with col1:
        user_input = st.text_input(
            "Type your message here:",
            key="user_message",
            placeholder="e.g., hello, how are you, bye"
        )
    
    with col2:
        send_button = st.button("Send", type="primary")
    
    with col3:
        clear_button = st.button("Clear Chat")
    
    if send_button and user_input.strip():
       
        st.session_state.chat_history.append({
            "role": "user", 
            "message": user_input
        })
        
        bot_response = get_chatbot_response(user_input)
        
        st.session_state.chat_history.append({
            "role": "bot", 
            "message": bot_response
        })
        
     
        st.rerun()
    
    
    if clear_button:
        st.session_state.chat_history = [
            {"role": "bot", "message": "Hello! I'm a simple chatbot. Try saying hello, asking how I am, or type 'help' for commands!"}
        ]
        st.rerun()
    
    # Sidebar with information
    st.sidebar.title("About This Chatbot")
    st.sidebar.write("""
    **Key Concepts Demonstrated:**
    - **if-elif statements** for response logic
    - **Functions** for modular code
    - **Loops** for processing multiple inputs
    - **Input/Output** through Streamlit interface
    
    **Try These Commands:**
    - hello, hi, hey
    - how are you
    - what's your name
    - can you know me
    - where i am living
    - what about babar azam
    - weather
    - help
    - bye, goodbye
    """)
    
  
    if st.sidebar.button("Run Console Demo"):
        st.sidebar.write("Check your terminal/console for demo output!")
        demonstrate_chatbot()


def process_multiple_inputs(input_list):
    """
    Function to demonstrate loop usage by processing multiple inputs
    """
    responses = []
    for user_input in input_list:
        response = get_chatbot_response(user_input)
        responses.append({
            "input": user_input,
            "response": response
        })
    return responses

def chat_session():
    """
    Console-based chat session (alternative to Streamlit UI)
    """
    print("=== Simple Chatbot Console Mode ===")
    print("Type 'quit' to exit")
    print("-" * 40)
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Bot: Goodbye! Thanks for chatting!")
            break
        
        if user_input:
            response = get_chatbot_response(user_input)
            print(f"Bot: {response}")
        
        print("-" * 40)


if __name__ == "__main__":
    main()
    
   