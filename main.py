import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import time

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI"))
file_id = 'file-tWDjaLWYr85RtjaF8YVSJzhP'
assistant_id = "asst_7aMJYGOFx8Li3qDwc9OTQZ3y"
thread_id = "thread_2yHRETtOdQf3cX1CawZI9wAO"


def polling_for_run_status(run):
    while True:
        # Retrieve the run status
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )

        # Check and print the step details
        run_steps = client.beta.threads.runs.steps.list(
            thread_id=thread_id,
            run_id=run.id
        )
        for step in run_steps.data:
            if step.type == 'tool_calls':
                print(f"Tool {step.type} invoked.")

            # If step involves code execution, print the code
            if step.type == 'code_interpreter':
                print(
                    f"Python Code Executed: {step.step_details['code_interpreter']['input']}")

        if run_status.status == 'completed':
            # Retrieve all messages from the thread
            messages = client.beta.threads.messages.list(
                thread_id=thread_id
            )

            # Print all messages from the thread
            for msg in messages.data:
                role = msg.role
                content = msg.content[0].text.value
                print(f"{role.capitalize()}: {content}")
            break  # Exit the polling loop since the run is complete
        elif run_status.status in ['queued', 'in_progress']:
            print(f'{run_status.status.capitalize()}... Please wait.')
            time.sleep(1.5)  # Wait before checking again
        else:
            print(f"Run status: {run_status.status}")
            break  # Exit the polling loop if the status is neither 'in_progress' nor 'completed'


def create_new_message(prompt):
    try:

        client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=prompt
        )
        run = client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id,
        )
        polling_for_run_status(run=run)

    except Exception as e:
        print(str(e))


def main():
    st.title('Chat with AI')
    if 'conversation' not in st.session_state:
        st.session_state.conversation = ''
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ''

    # Text input for user message
    user_input = st.text_input(
        "Type your message here:", key="input", value=st.session_state.user_input)

    if (st.session_state.conversation == ""):
        messages = client.beta.threads.messages.list(
            thread_id=thread_id
        )
        for msg in messages.data[::-1]:
            role = msg.role
            content = msg.content[0].text.value
            if (role.capitalize() == "Assistant"):
                st.session_state.conversation += f"{role.capitalize()}: {content}\n\n"
            else:
                st.session_state.conversation += f"{role.capitalize()}: {content}\n"

    # When user sends a message
    if st.button("Send"):
        # Append user message to conversation and clear input
        if user_input:
            create_new_message(user_input)
            messages = client.beta.threads.messages.list(
                thread_id=thread_id
            )
            st.session_state.conversation = ""
            for msg in messages.data[::-1]:
                role = msg.role
                content = msg.content[0].text.value
                if (role.capitalize() == "Assistant"):
                    st.session_state.conversation += f"{role.capitalize()}: {content}\n\n\n"
                else:
                    st.session_state.conversation += f"{role.capitalize()}: {content}\n"

        # Reset the input box
        st.session_state.user_input = ""

    # Display conversation in a single text area
    st.text_area("Conversation", value=st.session_state.conversation,
                 height=1500, disabled=True)


if __name__ == '__main__':
    main()
