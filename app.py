import streamlit as st
from supabase import create_client, Client
import pandas as pd
import plotly.express as px
from datetime import date
import json


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Digital Saheli",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background-color: #f7f8fa;
}

section[data-testid="stSidebar"] {
    background-color: #ffffff;
    border-right: 1px solid #e2e5e9;
}

h1, h2, h3 {
    color: #1f2937;
    font-weight: 600;
}

p, label {
    color: #374151;
}

div[data-testid="stMetric"] {
    background-color: #ffffff;
    border: 1px solid #e2e5e9;
    border-radius: 10px;
    padding: 18px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}

.stButton > button {
    border-radius: 6px;
    border: 1px solid #1f4e79;
    background-color: #1f4e79;
    color: white;
    font-weight: 500;
    padding: 8px 18px;
}

.stButton > button:hover {
    background-color: #163a5c;
    border-color: #163a5c;
    color: white;
}

.info-box {
    background-color: #ffffff;
    border-left: 4px solid #1f4e79;
    padding: 15px;
    border-radius: 5px;
    margin-bottom: 20px;
}

.safety-card {
    background-color: #ffffff;
    border: 1px solid #e2e5e9;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 15px;
}

.section-line {
    border-bottom: 1px solid #e2e5e9;
    margin: 10px 0 25px 0;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SUPABASE CONNECTION
# ============================================================

@st.cache_resource
def init_connection() -> Client:
    return create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"]
    )


try:
    supabase = init_connection()

except Exception:
    st.error(
        "Unable to connect to Supabase. "
        "Please verify SUPABASE_URL and SUPABASE_KEY."
    )
    st.stop()


# ============================================================
# DATABASE FUNCTIONS
# ============================================================

def get_table(table_name):
    try:
        response = (
            supabase
            .table(table_name)
            .select("*")
            .execute()
        )

        return response.data

    except Exception as e:
        st.error(f"Unable to retrieve data from {table_name}: {e}")
        return []


def add_record(table_name, data):
    try:
        supabase.table(table_name).insert(data).execute()
        return True

    except Exception as e:
        st.error(f"Unable to add record: {e}")
        return False


def delete_record(table_name, column, value):
    try:
        supabase.table(table_name).delete().eq(
            column,
            value
        ).execute()

        return True

    except Exception as e:
        st.error(f"Unable to delete record: {e}")
        return False


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown("## 🌸 Digital Saheli")

st.sidebar.markdown(
    "Smartphone Usage and Online Safety "
    "for Women Self Help Groups"
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Participants",
        "Smartphone Usage",
        "Smartphone Guide",
        "Women Safety",
        "Safety Quiz",
        "Safety Events",
        "Help & Emergency",
        "Training Sessions",
        "Reports"
    ]
)

st.sidebar.markdown("---")

st.sidebar.caption("Community Engagement Project")
st.sidebar.caption("Database Management System")


# ============================================================
# LOAD DATA
# ============================================================

participants = get_table("participants")
usage_records = get_table("smartphone_usage")
safety_events = get_table("safety_events")
training_sessions = get_table("training_sessions")
quiz_results = get_table("quiz_results")

participants_df = pd.DataFrame(participants)
usage_df = pd.DataFrame(usage_records)
events_df = pd.DataFrame(safety_events)
training_df = pd.DataFrame(training_sessions)
quiz_df = pd.DataFrame(quiz_results)


# ============================================================
# DASHBOARD
# ============================================================

if page == "Dashboard":

    st.title("🌸 Digital Saheli Dashboard")

    st.markdown(
        "Overview of smartphone usage, online safety, "
        "participants and awareness activities."
    )

    st.markdown(
        '<div class="section-line"></div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Participants",
        len(participants_df)
    )

    col2.metric(
        "Usage Records",
        len(usage_df)
    )

    col3.metric(
        "Safety Events",
        len(events_df)
    )

    col4.metric(
        "Quiz Attempts",
        len(quiz_df)
    )

    st.markdown("### System Overview")

    if participants_df.empty:

        st.info(
            "No participant records are available yet."
        )

    else:

        col1, col2 = st.columns(2)

        with col1:

            if "occupation" in participants_df.columns:

                occupation_data = (
                    participants_df["occupation"]
                    .fillna("Not Specified")
                    .value_counts()
                    .reset_index()
                )

                occupation_data.columns = [
                    "Occupation",
                    "Participants"
                ]

                fig = px.bar(
                    occupation_data,
                    x="Occupation",
                    y="Participants",
                    title="Participants by Occupation"
                )

                fig.update_layout(
                    template="simple_white",
                    height=350
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

        with col2:

            if "smartphone_user" in participants_df.columns:

                smartphone_data = (
                    participants_df["smartphone_user"]
                    .map({
                        True: "Smartphone User",
                        False: "Non-Smartphone User"
                    })
                    .value_counts()
                    .reset_index()
                )

                smartphone_data.columns = [
                    "Category",
                    "Participants"
                ]

                fig = px.pie(
                    smartphone_data,
                    names="Category",
                    values="Participants",
                    title="Smartphone Usage Status"
                )

                fig.update_layout(
                    height=350
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )


# ============================================================
# PARTICIPANTS
# ============================================================

elif page == "Participants":

    st.title("Participant Management")

    st.markdown(
        "Add and manage women participating in the "
        "self-help group activities."
    )

    st.markdown(
        '<div class="section-line"></div>',
        unsafe_allow_html=True
    )

    tab1, tab2 = st.tabs([
        "Add Participant",
        "View Participants"
    ])

    with tab1:

        with st.form("participant_form"):

            col1, col2 = st.columns(2)

            with col1:

                name = st.text_input(
                    "Full Name"
                )

                age = st.number_input(
                    "Age",
                    min_value=18,
                    max_value=100,
                    value=25
                )

                contact = st.text_input(
                    "Contact Number"
                )

            with col2:

                occupation = st.text_input(
                    "Occupation"
                )

                smartphone_user = st.selectbox(
                    "Smartphone User",
                    ["Yes", "No"]
                )

            submitted = st.form_submit_button(
                "Add Participant"
            )

            if submitted:

                if not name.strip():

                    st.warning(
                        "Please enter the participant name."
                    )

                else:

                    data = {
                        "name": name.strip(),
                        "age": age,
                        "contact": contact.strip(),
                        "occupation": occupation.strip(),
                        "smartphone_user":
                            smartphone_user == "Yes"
                    }

                    if add_record(
                        "participants",
                        data
                    ):

                        st.success(
                            "Participant added successfully."
                        )

                        st.rerun()

    with tab2:

        if participants_df.empty:

            st.info(
                "No participant records found."
            )

        else:

            search = st.text_input(
                "Search participant"
            )

            display_df = participants_df.copy()

            if search:

                display_df = display_df[
                    display_df["name"]
                    .astype(str)
                    .str.contains(
                        search,
                        case=False,
                        na=False
                    )
                ]

            st.dataframe(
                display_df,
                use_container_width=True,
                hide_index=True
            )

            st.markdown("### Delete Participant")

            participant_ids = (
                display_df["participant_id"]
                .tolist()
            )

            if participant_ids:

                selected_id = st.selectbox(
                    "Select Participant ID",
                    participant_ids
                )

                if st.button(
                    "Delete Participant"
                ):

                    if delete_record(
                        "participants",
                        "participant_id",
                        selected_id
                    ):

                        st.success(
                            "Participant deleted successfully."
                        )

                        st.rerun()


# ============================================================
# SMARTPHONE USAGE
# ============================================================

elif page == "Smartphone Usage":

    st.title("📱 Smartphone Usage Management")

    st.markdown(
        "Record and analyze how participants use "
        "smartphones and digital services."
    )

    st.markdown(
        '<div class="section-line"></div>',
        unsafe_allow_html=True
    )

    if participants_df.empty:

        st.warning(
            "Please add participants before recording "
            "smartphone usage."
        )

    else:

        tab1, tab2 = st.tabs([
            "Add Usage Record",
            "View Usage Records"
        ])

        with tab1:

            participant_options = {
                f"{row['participant_id']} - {row['name']}":
                row["participant_id"]
                for _, row in participants_df.iterrows()
            }

            with st.form("usage_form"):

                participant = st.selectbox(
                    "Participant",
                    list(participant_options.keys())
                )

                usage_purpose = st.selectbox(
                    "Primary Usage Purpose",
                    [
                        "Communication",
                        "Social Media",
                        "Education",
                        "Digital Payments",
                        "Online Shopping",
                        "Entertainment",
                        "Business",
                        "Other"
                    ]
                )

                col1, col2 = st.columns(2)

                with col1:

                    social_media = st.checkbox(
                        "Uses Social Media"
                    )

                    digital_payment = st.checkbox(
                        "Uses Digital Payments"
                    )

                    online_shopping = st.checkbox(
                        "Uses Online Shopping"
                    )

                with col2:

                    education = st.checkbox(
                        "Uses Smartphone for Education"
                    )

                    daily_hours = st.number_input(
                        "Daily Smartphone Usage (Hours)",
                        min_value=0.0,
                        max_value=24.0,
                        value=2.0,
                        step=0.5
                    )

                submitted = st.form_submit_button(
                    "Add Usage Record"
                )

                if submitted:

                    data = {
                        "participant_id":
                            participant_options[participant],

                        "usage_purpose":
                            usage_purpose,

                        "social_media":
                            social_media,

                        "digital_payment":
                            digital_payment,

                        "online_shopping":
                            online_shopping,

                        "education":
                            education,

                        "daily_usage_hours":
                            daily_hours
                    }

                    if add_record(
                        "smartphone_usage",
                        data
                    ):

                        st.success(
                            "Smartphone usage record "
                            "added successfully."
                        )

                        st.rerun()

        with tab2:

            if usage_df.empty:

                st.info(
                    "No smartphone usage records found."
                )

            else:

                st.dataframe(
                    usage_df,
                    use_container_width=True,
                    hide_index=True
                )


# ============================================================
# SMARTPHONE GUIDE
# ============================================================

elif page == "Smartphone Guide":

    st.title("📱 Smartphone Usage Guide")

    st.markdown(
        "Simple practical information to help women "
        "use smartphones confidently."
    )

    st.markdown(
        '<div class="section-line"></div>',
        unsafe_allow_html=True
    )

    tab1, tab2, tab3, tab4 = st.tabs([
        "Basic Smartphone Use",
        "Internet & Apps",
        "Digital Payments",
        "Useful Tips"
    ])

    with tab1:

        st.subheader("Basic Smartphone Skills")

        st.markdown("""
        ### 1. Making a Phone Call
        - Open the Phone application.
        - Enter the mobile number.
        - Press the call button.
        - To end the call, press the red end-call button.

        ### 2. Saving a Contact
        - Open Contacts.
        - Select Add Contact.
        - Enter the person's name and number.
        - Press Save.

        ### 3. Sending a Message
        - Open Messages or WhatsApp.
        - Select the contact.
        - Type your message.
        - Press Send.

        ### 4. Taking a Photo
        - Open Camera.
        - Keep the phone steady.
        - Press the camera button.
        """)

    with tab2:

        st.subheader("Internet and Applications")

        st.markdown("""
        ### Using the Internet
        - Open a trusted browser such as Chrome.
        - Type the information you want to search.
        - Check information from reliable websites.
        - Avoid clicking unknown links.

        ### Installing Apps
        - Use Google Play Store or Apple App Store.
        - Check the app name and developer.
        - Read reviews before installing.
        - Avoid downloading applications from unknown websites.

        ### WhatsApp
        - Use it to communicate with trusted contacts.
        - Do not share OTPs.
        - Do not forward suspicious messages.
        - Check links before opening them.
        """)

    with tab3:

        st.subheader("Digital Payment Safety")

        st.markdown("""
        ### UPI and Digital Payments

        - Never share your UPI PIN.
        - Never share an OTP.
        - Check the receiver's name before paying.
        - Remember: receiving money does NOT require entering your UPI PIN.
        - Do not scan unknown QR codes.
        - Do not allow strangers to control your phone remotely.
        - Keep payment applications updated.
        """)

        st.warning(
            "Important: Your OTP, PIN and passwords should "
            "always remain private."
        )

    with tab4:

        st.subheader("Everyday Smartphone Tips")

        st.markdown("""
        ✅ Keep your phone updated.

        ✅ Use a screen lock.

        ✅ Use strong passwords.

        ✅ Keep important contacts saved.

        ✅ Backup important photos and documents.

        ✅ Check app permissions.

        ✅ Avoid unknown Wi-Fi networks for banking.

        ✅ Log out from accounts on shared devices.

        ✅ Do not give your phone to unknown persons for remote access.
        """)


# ============================================================
# WOMEN SAFETY
# ============================================================

elif page == "Women Safety":

    st.title("🛡️ Women Safety & Online Security")

    st.markdown(
        "Learn simple steps to stay safe while using "
        "smartphones and the internet."
    )

    st.markdown(
        '<div class="section-line"></div>',
        unsafe_allow_html=True
    )

    tab1, tab2, tab3, tab4 = st.tabs([
        "Password Safety",
        "Social Media Safety",
        "Scam Protection",
        "Privacy"
    ])

    with tab1:

        st.subheader("🔐 Password Safety")

        st.markdown("""
        - Create a strong and unique password.
        - Avoid using your name, birthday or phone number.
        - Do not use the same password everywhere.
        - Never share passwords with strangers.
        - Enable two-factor authentication where available.
        """)

    with tab2:

        st.subheader("📱 Social Media Safety")

        st.markdown("""
        - Keep your social media profile private when appropriate.
        - Do not accept requests from unknown people.
        - Avoid sharing your home address.
        - Avoid publicly posting travel plans.
        - Block and report abusive accounts.
        - Do not share private photographs with unknown people.
        """)

    with tab3:

        st.subheader("⚠️ Scam and Fraud Protection")

        st.markdown("""
        ### Common Warning Signs

        🚨 Someone asks for an OTP.

        🚨 Someone asks for your UPI PIN.

        🚨 Someone says you won a prize.

        🚨 Someone sends an urgent payment request.

        🚨 Someone asks you to install a remote-access application.

        🚨 Someone sends a suspicious link.

        ### What to Do

        1. Stop and do not make the payment.
        2. Do not share OTP or PIN.
        3. Verify the person or organization independently.
        4. Save relevant evidence.
        5. Report the incident if necessary.
        """)

    with tab4:

        st.subheader("🔒 Privacy Protection")

        st.markdown("""
        - Review app permissions regularly.
        - Turn off location access for apps that do not need it.
        - Do not give unnecessary camera or microphone permissions.
        - Use a screen lock.
        - Avoid saving passwords on shared devices.
        - Keep your operating system and apps updated.
        """)

        st.info(
            "Think before you click, share or pay."
        )


# ============================================================
# SAFETY QUIZ
# ============================================================

elif page == "Safety Quiz":

    st.title("📝 Online Safety Quiz")

    st.markdown(
        "Test your knowledge about smartphone usage "
        "and online safety."
    )

    st.markdown(
        '<div class="section-line"></div>',
        unsafe_allow_html=True
    )

    if participants_df.empty:

        st.warning(
            "Please add a participant before attempting the quiz."
        )

    else:

        participant_options = {
            f"{row['participant_id']} - {row['name']}":
            row["participant_id"]
            for _, row in participants_df.iterrows()
        }

        selected_participant = st.selectbox(
            "Select Participant",
            list(participant_options.keys())
        )

        questions = [

            {
                "question":
                    "Should you share your OTP with another person?",

                "options":
                    ["Yes", "No"],

                "answer":
                    "No"
            },

            {
                "question":
                    "What should you do before making a UPI payment?",

                "options":
                    [
                        "Check the receiver's name",
                        "Share your PIN",
                        "Share your OTP",
                        "Click any link"
                    ],

                "answer":
                    "Check the receiver's name"
            },

            {
                "question":
                    "Where should you download mobile applications from?",

                "options":
                    [
                        "Unknown websites",
                        "Official app store",
                        "Random links",
                        "Unknown messages"
                    ],

                "answer":
                    "Official app store"
            },

            {
                "question":
                    "What should you do with a suspicious link?",

                "options":
                    [
                        "Open it immediately",
                        "Forward it",
                        "Avoid opening it",
                        "Enter your password"
                    ],

                "answer":
                    "Avoid opening it"
            },

            {
                "question":
                    "Which information should remain private?",

                "options":
                    [
                        "OTP and UPI PIN",
                        "Weather",
                        "Public news",
                        "General information"
                    ],

                "answer":
                    "OTP and UPI PIN"
            },

            {
                "question":
                    "What should you do if you receive an online scam message?",

                "options":
                    [
                        "Send money",
                        "Share OTP",
                        "Ignore/verify and report if necessary",
                        "Give your password"
                    ],

                "answer":
                    "Ignore/verify and report if necessary"
            },

            {
                "question":
                    "Should you accept friend requests from unknown people?",

                "options":
                    [
                        "Always",
                        "Only after checking who they are",
                        "Never check",
                        "Share private information first"
                    ],

                "answer":
                    "Only after checking who they are"
            },

            {
                "question":
                    "What helps protect your smartphone?",

                "options":
                    [
                        "Screen lock",
                        "Sharing passwords",
                        "Unknown apps",
                        "No updates"
                    ],

                "answer":
                    "Screen lock"
            },

            {
                "question":
                    "Should your UPI PIN be entered to receive money?",

                "options":
                    [
                        "Yes",
                        "No"
                    ],

                "answer":
                    "No"
            },

            {
                "question":
                    "What is a good practice for social media?",

                "options":
                    [
                        "Share home address publicly",
                        "Accept every unknown request",
                        "Keep privacy settings secure",
                        "Share passwords"
                    ],

                "answer":
                    "Keep privacy settings secure"
            }
        ]

        st.markdown("### Answer the following questions")

        answers = {}

        for i, q in enumerate(questions):

            st.markdown(
                f"**Q{i + 1}. {q['question']}**"
            )

            answers[f"Q{i + 1}"] = st.radio(
                "Select answer:",
                q["options"],
                key=f"quiz_question_{i}"
            )

            st.markdown("---")

        if st.button(
            "Submit Quiz",
            type="primary"
        ):

            score = 0

            for i, q in enumerate(questions):

                if answers[f"Q{i + 1}"] == q["answer"]:
                    score += 1

            total = len(questions)

            quiz_data = {
                "participant_id":
                    participant_options[selected_participant],

                "score":
                    score,

                "total_questions":
                    total,

                "answers":
                    json.dumps(answers)
            }

            if add_record(
                "quiz_results",
                quiz_data
            ):

                percentage = (
                    score / total
                ) * 100

                st.success(
                    f"Quiz submitted successfully! "
                    f"Your score is {score}/{total} "
                    f"({percentage:.0f}%)."
                )

                if percentage >= 80:

                    st.balloons()

                    st.success(
                        "Excellent! You have good awareness "
                        "of online safety."
                    )

                elif percentage >= 50:

                    st.info(
                        "Good effort! Review the safety guide "
                        "to improve your knowledge."
                    )

                else:

                    st.warning(
                        "Please review the Smartphone Guide "
                        "and Women Safety sections."
                    )


# ============================================================
# HELP & EMERGENCY
# ============================================================

elif page == "Help & Emergency":

    st.title("🆘 Help & Emergency")

    st.markdown(
        "If you face an online safety problem, stay calm "
        "and take appropriate action."
    )

    st.markdown(
        '<div class="section-line"></div>',
        unsafe_allow_html=True
    )

    st.subheader("Immediate Safety")

    st.markdown("""
    ### If you are in immediate physical danger

    **Call 112 – Emergency Response Support System**

    ### Women Helpline

    **181 – Women Helpline**

    ### Cyber Crime

    **1930 – Cyber Crime Helpline**

    You can also report cybercrime through the official "
    "government cybercrime reporting system.
    """)

    st.warning(
        "Never share your OTP, UPI PIN, password or banking "
        "credentials with anyone claiming to provide help."
    )

    st.subheader("What to do after an online fraud")

    st.markdown("""
    1. Contact your bank/payment provider immediately.
    2. If money has been lost, report it quickly.
    3. Save screenshots and transaction details.
    4. Do not delete important evidence.
    5. Change compromised passwords.
    6. Block suspicious contacts/accounts.
    7. Report the incident through appropriate official channels.
    """)

    st.subheader("Useful Safety Contacts")

    st.info(
        "Emergency: 112\n\n"
        "Women Helpline: 181\n\n"
        "Cyber Crime Helpline: 1930"
    )


# ============================================================
# SAFETY EVENTS
# ============================================================

elif page == "Safety Events":

    st.title("Online Safety Events")

    st.markdown(
        "Record online safety concerns and actions "
        "taken by participants."
    )

    st.markdown(
        '<div class="section-line"></div>',
        unsafe_allow_html=True
    )

    if participants_df.empty:

        st.warning(
            "Please add participants before recording "
            "safety events."
        )

    else:

        tab1, tab2 = st.tabs([
            "Report Safety Event",
            "View Events"
        ])

        with tab1:

            participant_options = {
                f"{row['participant_id']} - {row['name']}":
                row["participant_id"]
                for _, row in participants_df.iterrows()
            }

            with st.form("safety_form"):

                participant = st.selectbox(
                    "Participant",
                    list(participant_options.keys())
                )

                event_type = st.selectbox(
                    "Event Type",
                    [
                        "Suspicious Message",
                        "Phishing Link",
                        "Online Scam",
                        "Fake Account",
                        "Cyberbullying",
                        "Payment Fraud Attempt",
                        "Privacy Concern",
                        "Other"
                    ]
                )

                event_date = st.date_input(
                    "Event Date",
                    value=date.today()
                )

                description = st.text_area(
                    "Description"
                )

                action_taken = st.text_area(
                    "Action Taken"
                )

                reported = st.selectbox(
                    "Reported",
                    ["Yes", "No"]
                )

                submitted = st.form_submit_button(
                    "Save Safety Event"
                )

                if submitted:

                    data = {
                        "participant_id":
                            participant_options[participant],

                        "event_type":
                            event_type,

                        "event_date":
                            str(event_date),

                        "description":
                            description,

                        "action_taken":
                            action_taken,

                        "reported":
                            reported == "Yes"
                    }

                    if add_record(
                        "safety_events",
                        data
                    ):

                        st.success(
                            "Safety event recorded successfully."
                        )

                        st.rerun()

        with tab2:

            if events_df.empty:

                st.info(
                    "No safety events have been recorded."
                )

            else:

                st.dataframe(
                    events_df,
                    use_container_width=True,
                    hide_index=True
                )


# ============================================================
# TRAINING SESSIONS
# ============================================================

elif page == "Training Sessions":

    st.title("Training and Awareness Sessions")

    st.markdown(
        "Manage digital literacy and online safety "
        "awareness sessions."
    )

    st.markdown(
        '<div class="section-line"></div>',
        unsafe_allow_html=True
    )

    tab1, tab2 = st.tabs([
        "Add Session",
        "View Sessions"
    ])

    with tab1:

        with st.form("training_form"):

            session_date = st.date_input(
                "Session Date",
                value=date.today()
            )

            topic = st.selectbox(
                "Training Topic",
                [
                    "Smartphone Basics",
                    "Password Security",
                    "Online Banking Safety",
                    "Digital Payments",
                    "Social Media Safety",
                    "Phishing Awareness",
                    "Privacy Settings",
                    "Cyber Fraud Awareness",
                    "Other"
                ]
            )

            trainer_name = st.text_input(
                "Trainer / Resource Person"
            )

            participants_count = st.number_input(
                "Number of Participants",
                min_value=1,
                max_value=1000,
                value=10
            )

            notes = st.text_area(
                "Notes"
            )

            submitted = st.form_submit_button(
                "Add Training Session"
            )

            if submitted:

                data = {
                    "session_date":
                        str(session_date),

                    "topic":
                        topic,

                    "trainer_name":
                        trainer_name.strip(),

                    "participants_count":
                        participants_count,

                    "notes":
                        notes.strip()
                }

                if add_record(
                    "training_sessions",
                    data
                ):

                    st.success(
                        "Training session added successfully."
                    )

                    st.rerun()

    with tab2:

        if training_df.empty:

            st.info(
                "No training sessions found."
            )

        else:

            st.dataframe(
                training_df,
                use_container_width=True,
                hide_index=True
            )


# ============================================================
# REPORTS
# ============================================================

elif page == "Reports":

    st.title("Reports and Analysis")

    st.markdown(
        "Analyze smartphone usage, online safety events, "
        "training activities and quiz performance."
    )

    st.markdown(
        '<div class="section-line"></div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # SAFETY EVENT ANALYSIS
    # --------------------------------------------------------

    if (
        not events_df.empty
        and "event_type" in events_df.columns
    ):

        st.subheader(
            "Online Safety Event Analysis"
        )

        event_counts = (
            events_df["event_type"]
            .value_counts()
            .reset_index()
        )

        event_counts.columns = [
            "Event Type",
            "Number of Events"
        ]

        fig = px.bar(
            event_counts,
            x="Event Type",
            y="Number of Events",
            title="Safety Events by Type"
        )

        fig.update_layout(
            template="simple_white",
            height=400
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # --------------------------------------------------------
    # SMARTPHONE USAGE ANALYSIS
    # --------------------------------------------------------

    if not usage_df.empty:

        st.subheader(
            "Smartphone Usage Analysis"
        )

        if "usage_purpose" in usage_df.columns:

            purpose_counts = (
                usage_df["usage_purpose"]
                .value_counts()
                .reset_index()
            )

            purpose_counts.columns = [
                "Purpose",
                "Records"
            ]

            fig = px.bar(
                purpose_counts,
                x="Purpose",
                y="Records",
                title="Primary Smartphone Usage Purpose"
            )

            fig.update_layout(
                template="simple_white",
                height=400
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        if "daily_usage_hours" in usage_df.columns:

            average_hours = usage_df[
                "daily_usage_hours"
            ].mean()

            st.metric(
                "Average Daily Smartphone Usage",
                f"{average_hours:.2f} hours"
            )


    # --------------------------------------------------------
    # TRAINING ANALYSIS
    # --------------------------------------------------------

    if not training_df.empty:

        st.subheader(
            "Training Activity"
        )

        if "topic" in training_df.columns:

            training_counts = (
                training_df["topic"]
                .value_counts()
                .reset_index()
            )

            training_counts.columns = [
                "Topic",
                "Sessions"
            ]

            fig = px.bar(
                training_counts,
                x="Topic",
                y="Sessions",
                title="Training Sessions by Topic"
            )

            fig.update_layout(
                template="simple_white",
                height=400
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


    # --------------------------------------------------------
    # QUIZ ANALYSIS
    # --------------------------------------------------------

    if not quiz_df.empty:

        st.subheader(
            "Safety Quiz Performance"
        )

        if "score" in quiz_df.columns:

            average_score = quiz_df[
                "score"
            ].mean()

            st.metric(
                "Average Quiz Score",
                f"{average_score:.1f}"
            )

        st.dataframe(
            quiz_df,
            use_container_width=True,
            hide_index=True
        )


    # --------------------------------------------------------
    # EXPORT DATA
    # --------------------------------------------------------

    st.subheader("Data Export")

    export_option = st.selectbox(
        "Select Dataset",
        [
            "Participants",
            "Smartphone Usage",
            "Safety Events",
            "Training Sessions",
            "Quiz Results"
        ]
    )

    export_mapping = {
        "Participants":
            participants_df,

        "Smartphone Usage":
            usage_df,

        "Safety Events":
            events_df,

        "Training Sessions":
            training_df,

        "Quiz Results":
            quiz_df
    }

    selected_df = export_mapping[
        export_option
    ]

    if not selected_df.empty:

        csv_data = selected_df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "Download CSV Report",
            data=csv_data,
            file_name=(
                export_option
                .lower()
                .replace(" ", "_")
                + "_report.csv"
            ),
            mime="text/csv"
        )

    else:

        st.info(
            "No data available for export."
        )
