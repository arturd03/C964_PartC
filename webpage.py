import streamlit as st

from spamDetection import spam_detector


def detect_spam(message,model, feature_extraction):
    isSpam = spam_detector(message, model, feature_extraction)
    st.write(f'The message is most likely {"spam" if isSpam else "not spam"}.')


def main(model,feature_extraction):

    st.title("Spam Detector")

    # Create an input box for the user to enter a message
    message = st.text_input("Enter your message:")

    # Create a submit button
    if st.button("Submit"):
        # Call the detect_spam function to check if the message is spam
        is_spam = detect_spam(message,model,feature_extraction)

if __name__ == "__main__":
    main()

