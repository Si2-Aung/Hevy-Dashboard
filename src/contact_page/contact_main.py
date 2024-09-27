import streamlit as st


def create_contact_page():
    st.header("Contact me")

    # Initialize session state for form submission
    if 'form_submitted' not in st.session_state:
        st.session_state.form_submitted = False

    # Check for URL parameters (for example ?submitted=true)
    if 'submitted' in st.query_params:
        st.session_state.form_submitted = True

    # If the form has not been submitted, show the form
    if not st.session_state.form_submitted:
        contact_form = """
        <form action="https://formsubmit.co/streamlit-page@mail.de" method="POST">
            <input type="hidden" name="_next" value="?submitted=true">
            <input type="text" name="_honey" style="display:none">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your message here"></textarea>
            <button type="submit">Send</button>
        </form>
        """

        st.markdown(contact_form, unsafe_allow_html=True)
    else:
        st.success("Message sent successfully! You cannot submit another message.")

    # Load CSS for styling
    local_css("style.css")


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def create_buttons():
    st.header ("Follow me on social media")
    st.write("")

    col1, col2, col3 = st.columns([4, 4, 3])  
    logo_width = 100
    # GitHub
    with col1:
        github_logo = "https://pngimg.com/uploads/github/github_PNG23.png"
        st.image(github_logo, width=logo_width)
        st.markdown('<a href="https://github.com/Si2-Aung" target="_blank"><button style="background-color:#24292e;color:white;width:100px;margin-top:1px;">GitHub</button></a>', unsafe_allow_html=True)

    # LinkedIn
    with col2:
        linkedin_logo = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/LinkedIn_logo.svg/800px-LinkedIn_logo.svg.png"
        st.image(linkedin_logo, width=logo_width)
        st.markdown('<a href="https://www.linkedin.com/in/si-thu-aung-31203532a/" target="_blank"><button style="background-color:#0a66c2;color:white;width:100px;margin-top:10px;">LinkedIn</button></a>', unsafe_allow_html=True)

    # Hevy
    with col3:
        hevy_logo = "https://www.hevyapp.com/wp-content/uploads/hevy-logo.svg" 
        st.image(hevy_logo, width=logo_width)
        st.markdown('<a href="https://www.hevy.com" target="_blank"><button style="background-color:#f44336;color:white;width:100px;margin-top:10px;">Hevy</button></a>', unsafe_allow_html=True)


def main():
    create_contact_page()
    create_buttons()
