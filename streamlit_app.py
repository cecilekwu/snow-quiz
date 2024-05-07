import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

image = Image.open('Summit banner.png')

# Function to display header image
def display_header_image():
    st.image(image, use_column_width=True)

# Intro page
def intro_page():
    display_header_image()
    st.title("What Snowflake Product Are You?")
    st.write("In anticipation for the upcoming Data Cloud Summit, find out which Snowflake product you are based on your answers. You will also be recommended a Summit session at the end to help you lean into your newly discovered “spirit product.”  \n\nFor internal sharing only.")
    if st.button("Start Quiz"):
        st.session_state.current_question_index = 1
        st.experimental_rerun()

# Question pages
def question_page(question, options):
    display_header_image()
    st.title("What Snowflake Product Are You?")
    st.header("Question:")
    st.write(question)
    selected_option = st.radio("Choose one:", options)
    if st.button("Next"):
        st.session_state[f"answer_{st.session_state.current_question_index}"] = selected_option
        st.session_state.current_question_index += 1
        st.experimental_rerun()

# Results page
def result_page():
    display_header_image()
    st.title("Results - What Snowflake Product Are You?")
    st.write("Thank you for completing the quiz!")

    # Get answers
    answers = [st.session_state.get(f"answer_{i}") for i in range(1, 5)]

    # Determine personality
    personality = determine_personality(answers)

    # Display personality type
    st.write("Your product is:", personality)

    # Display personality description and image
    personality_descriptions = {
        "Snowflake Cortex": {
            "description": "You're innovative. You're always looking for the next big thing. You're knowledgeable on a lot of different topics (so you're also great at trivia).  \nSession: Platform Keynote",
            "image": "https://www.snowflake.com/wp-content/uploads/2023/11/Figure-1-platform.png"
        },
        "Data Clean Rooms": {
            "description": "You're collaborative. You try to include everyone in the conversation. You'd rather work on a group project than alone.  \nSession: “How Snowflake Data Clean Rooms Are Powering Advanced, AI-Driven, Multi-party Collaboration”",
            "image": "https://www.snowflake.com/wp-content/uploads/2022/04/ShareButNotShow-3.png"
        },
        "Snowflake Horizon": {
            "description": "You're responsible. You're the one at the airport making sure everyone has their passport and tickets. You have a spreadsheet for every occasion.  \nSession: “What's New: Snowflake Horizon for Data Teams”",
            "image": "https://s26.q4cdn.com/463892824/files/doc_multimedia/Snowflake_Snowday23_PR_Horizon_Diagram.jpg"
        },
        "Streamlit": {
            "description": "You're creative. You love to make things visually pleasing. Your home is full of nifty tools, like an efficient vegetable cutter or handy phone stand.  \nSession: Builders Keynote",
            "image": "https://images.datacamp.com/image/upload/v1640050215/image27_frqkzv.png"
        }
    }


    if personality in personality_descriptions:
        st.write(personality_descriptions[personality]["description"])
        st.image(personality_descriptions[personality]["image"])
    else:
        st.write("No description available for this personality type.")

# Determine personality based on answers
def determine_personality(answers):
    # Define personality types and their corresponding answer combinations
    personality_types = {
        ("How productive it is in harvesting data insights!", "The data is ingested very fast and efficiently", "Compile a robust inventory of resources and guides for them to follow", "The Architecture of Snowflake: Understanding the Intricacies of the Data Cloud"): "Snowflake Cortex",
        ("How productive it is in harvesting data insights!", "The data is ingested without any errors or inconsistencies", "Compile a robust inventory of resources and guides for them to follow", "The Architecture of Snowflake: Understanding the Intricacies of the Data Cloud"): "Snowflake Cortex",
        ("How productive it is in harvesting data insights!", "The data is ingested without any errors or inconsistencies", "Set up a meeting and walk them through the platform yourself", "The Architecture of Snowflake: Understanding the Intricacies of the Data Cloud"): "Snowflake Cortex",
        ("How productive it is in harvesting data insights!", "The data is ingested very fast and efficiently", "Set up a meeting and walk them through the platform yourself", "The Architecture of Snowflake: Understanding the Intricacies of the Data Cloud"): "Snowflake Cortex",
        ("How expansive it is - the possibilities are endless!", "The data is ingested without any errors or inconsistencies", "Set up a meeting and walk them through the platform yourself", "The Architecture of Snowflake: Understanding the Intricacies of the Data Cloud"): "Data Clean Rooms",
        ("How expansive it is - the possibilities are endless!", "The data is ingested very fast and efficiently", "Set up a meeting and walk them through the platform yourself", "The Architecture of Snowflake: Understanding the Intricacies of the Data Cloud"): "Data Clean Rooms",
        ("How productive it is in harvesting data insights!", "The data is ingested very fast and efficiently", "Set up a meeting and walk them through the platform yourself", "The Beauty in the Numbers: Making Data Fun and Accessible"): "Data Clean Rooms",
        ("How productive it is in harvesting data insights!", "The data is ingested without any errors or inconsistencies", "Set up a meeting and walk them through the platform yourself", "The Beauty in the Numbers: Making Data Fun and Accessible"): "Data Clean Rooms",
        ("How productive it is in harvesting data insights!", "The data is ingested very fast and efficiently", "Compile a robust inventory of resources and guides for them to follow", "The Beauty in the Numbers: Making Data Fun and Accessible"): "Snowflake Horizon",
        ("How productive it is in harvesting data insights!", "The data is ingested without any errors or inconsistencies", "Compile a robust inventory of resources and guides for them to follow", "The Beauty in the Numbers: Making Data Fun and Accessible"): "Snowflake Horizon",
        ("How expansive it is - the possibilities are endless!", "The data is ingested without any errors or inconsistencies", "Compile a robust inventory of resources and guides for them to follow", "The Architecture of Snowflake: Understanding the Intricacies of the Data Cloud"): "Snowflake Horizon",
        ("How expansive it is - the possibilities are endless!", "The data is ingested very fast and efficiently", "Compile a robust inventory of resources and guides for them to follow", "The Architecture of Snowflake: Understanding the Intricacies of the Data Cloud"): "Snowflake Horizon",
        ("How expansive it is - the possibilities are endless!", "The data is ingested without any errors or inconsistencies", "Set up a meeting and walk them through the platform yourself", "The Beauty in the Numbers: Making Data Fun and Accessible"): "Streamlit",
        ("How expansive it is - the possibilities are endless!", "The data is ingested very fast and efficiently", "Set up a meeting and walk them through the platform yourself", "The Beauty in the Numbers: Making Data Fun and Accessible"): "Streamlit",
        ("How expansive it is - the possibilities are endless!", "The data is ingested without any errors or inconsistencies", "Compile a robust inventory of resources and guides for them to follow", "The Beauty in the Numbers: Making Data Fun and Accessible"): "Streamlit",
        ("How expansive it is - the possibilities are endless!", "The data is ingested very fast and efficiently", "Compile a robust inventory of resources and guides for them to follow", "The Beauty in the Numbers: Making Data Fun and Accessible"): "Streamlit",
        # Add more combinations as needed
    }

    # Check if the answers match any of the predefined combinations
    for combination, personality in personality_types.items():
        if all(answer in combination for answer in answers):
            return personality

    return "Unknown"

# Initialize current_question_index if not already initialized
if 'current_question_index' not in st.session_state:
    st.session_state.current_question_index = 0

# Main function
def main():
    if st.session_state.current_question_index == 0:
        intro_page()
    elif st.session_state.current_question_index < 5:
        questions = [
            "What's your favorite thing about the Snowflake platform?",
            "Which do you care more about when ingesting data?",
            "Someone has a question about using Snowflake. Do you…",
            "What Data Cloud Summit session would you (hypothetically) host?"
        ]
        options = [
            ("How productive it is in harvesting data insights!", "How expansive it is - the possibilities are endless!"),
            ("The data is ingested very fast and efficiently", "The data is ingested without any errors or inconsistencies"),
            ("Compile a robust inventory of resources and guides for them to follow", "Set up a meeting and walk them through the platform yourself"),
            ("The Architecture of Snowflake: Understanding the Intricacies of the Data Cloud", "The Beauty in the Numbers: Making Data Fun and Accessible")
        ]
        question = questions[st.session_state.current_question_index - 1]
        option = options[st.session_state.current_question_index - 1]
        question_page(question, option)
    else:
        result_page()

if __name__ == "__main__":
    main()
