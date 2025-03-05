import streamlit as st
import random

class EngineeringBanter:
    def __init__(self):
        self.banters = {
            "Refinement": [
                "This story is so vague, it could describe literally anything.",
                "We have 37 user stories and 2 hours. Math checks out, right?",
                "Another story with 'just' and 'simple' in the description. Famous last words.",
                "Story points are basically just astrology for engineers.",
                "This task is 'high priority' until someone actually has to do it.",
                "We're estimating this story like we're guessing jelly beans in a jar.",
                "Technical debt? More like technical bankruptcy.",
                "I see we're playing story point bingo again.",
                "This story is so ambiguous, it could be a philosophy dissertation.",
                "Another day, another story that'll take 'just a couple hours'."
            ],
            "Daily Standup": [
                "I'm working on it... *nervously closes 17 browser tabs*",
                "Yesterday? Oh, you know, debugging. Today? Still debugging.",
                "Sorry, I need help. By help, I mean someone to magically fix my code.",
                "Blocked? No, just... creatively waiting.",
                "I'm 90% done. That last 10% will only take another week.",
                "Deploying is just a state of mind, right?",
                "My task was way bigger than I thought. Shocking, I know.",
                "I'll have it done by end of sprint. *narrator: he will not*",
                "Meetings are my most productive time. *stares into void*",
                "Technically, I'm making progress. If you squint. And use imagination."
            ],
            "Sprint Review": [
                "We completed 60% of what we planned. That's basically an A, right?",
                "Here's a feature no one asked for but everyone will love!",
                "Scope creep? I prefer the term 'dynamic requirements'.",
                "We didn't fail. We just found 99 ways that didn't work.",
                "This sprint was a journey. A very, very long journey.",
                "Look at all these beautiful bugs we've cultivated.",
                "We're not behind schedule. We're just giving extra buffer time.",
                "Technically, this is a minimum viable product. Emphasis on minimum.",
                "Our velocity is... let's call it 'interpretive'.",
                "We solved problems you didn't even know you had!"
            ]
        }

    def get_random_banter(self, category):
        return random.choice(self.banters[category])

def main():
    st.set_page_config(
        page_title="Engineering Banter Generator",
        page_icon="🤖",
        layout="centered"
    )

    # Custom CSS for colorful tiles
    st.markdown("""
    <style>
    .stButton>button {
        background-color: #F0F2F6;
        color: black;
        border: 2px solid;
        width: 100%;
        height: 100px;
    }
    .stButton>button:hover {
        background-color: #E6E9EF;
        border-color: #4CAF50;
    }
    .refinement-button {
        border-color: #FF6B6B !important;
    }
    .standup-button {
        border-color: #4ECDC4 !important;
    }
    .review-button {
        border-color: #45B7D1 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🚀 Engineering Banter Generator")
    st.subheader("Laugh at (with) your daily engineering struggles!")

    banter_generator = EngineeringBanter()
    
    # Reset the session state when the page loads
    if 'current_quote' not in st.session_state:
        st.session_state.current_quote = None
        st.session_state.current_category = None

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Refinement Banter", key="refinement", 
                     help="Generate a sarcastic refinement quote", 
                     type="primary", 
                     use_container_width=True):
            # Clear previous quotes
            st.session_state.current_quote = banter_generator.get_random_banter("Refinement")
            st.session_state.current_category = "Refinement"
    
    with col2:
        if st.button("Standup Banter", key="standup", 
                     help="Generate a witty standup quote", 
                     type="primary", 
                     use_container_width=True):
            # Clear previous quotes
            st.session_state.current_quote = banter_generator.get_random_banter("Daily Standup")
            st.session_state.current_category = "Daily Standup"
    
    with col3:
        if st.button("Sprint Review Banter", key="review", 
                     help="Generate a humorous sprint review quote", 
                     type="primary", 
                     use_container_width=True):
            # Clear previous quotes
            st.session_state.current_quote = banter_generator.get_random_banter("Sprint Review")
            st.session_state.current_category = "Sprint Review"

    # Display the current quote if it exists
    if st.session_state.current_quote:
        st.subheader(f"{st.session_state.current_category} Banter")
        st.write(st.session_state.current_quote)
        
        # Copy button
        if st.button("Copy Quote", key="copy_quote"):
            st.clipboard.copy(st.session_state.current_quote)
            st.success("Quote copied to clipboard!")

if __name__ == "__main__":
    main()
