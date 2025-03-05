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

    st.title("🚀 Engineering Banter Generator")
    st.subheader("Laugh at (with) your daily engineering struggles!")

    banter_generator = EngineeringBanter()
    
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Refinement Banter"):
            st.session_state.refinement_quote = banter_generator.get_random_banter("Refinement")
    
    with col2:
        if st.button("Standup Banter"):
            st.session_state.standup_quote = banter_generator.get_random_banter("Daily Standup")
    
    with col3:
        if st.button("Sprint Review Banter"):
            st.session_state.review_quote = banter_generator.get_random_banter("Sprint Review")

    # Display quotes if they exist
    if hasattr(st.session_state, 'refinement_quote'):
        st.subheader("Refinement Banter")
        st.write(st.session_state.refinement_quote)
        st.button("Copy Refinement Quote", key="copy_ref", 
                  on_click=lambda: st.clipboard.copy(st.session_state.refinement_quote))

    if hasattr(st.session_state, 'standup_quote'):
        st.subheader("Standup Banter")
        st.write(st.session_state.standup_quote)
        st.button("Copy Standup Quote", key="copy_standup", 
                  on_click=lambda: st.clipboard.copy(st.session_state.standup_quote))

    if hasattr(st.session_state, 'review_quote'):
        st.subheader("Sprint Review Banter")
        st.write(st.session_state.review_quote)
        st.button("Copy Review Quote", key="copy_review", 
                  on_click=lambda: st.clipboard.copy(st.session_state.review_quote))

if __name__ == "__main__":
    main()
