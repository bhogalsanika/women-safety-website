import streamlit as st
from supabase import create_client
import pandas as pd
import plotly.express as px
from datetime import datetime


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Women Digital Safety & Awareness System",
    page_icon="📱",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #f8f9fc;
}

h1, h2, h3 {
    color: #7b1e3a;
}

[data-testid="stSidebar"] {
    background-color: #fff5f8;
}

.stButton > button {
    border-radius: 8px;
    font-weight: 600;
}

div[data-testid="metric-container"] {
    background-color: white;
    border-radius: 12px;
    padding: 15px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SUPABASE CONNECTION
# ============================================================

@st.cache_resource
def init_connection():
    return create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"]
    )


supabase = init_connection()


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

        return response.data if response.data else []

    except Exception as e:

        st.error(
            f"Unable to load {table_name}: {e}"
        )

        return []


def add_record(table_name, data):

    try:

        response = (
            supabase
            .table(table_name)
            .insert(data)
            .execute()
        )

        return True

    except Exception as e:

        st.error(
            f"Database error: {e}"
        )

        return False


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

st.sidebar.title("🌸 Digital Safety")

st.sidebar.markdown(
    "**Women Digital Safety & Awareness System**"
)

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "👩 Participants",
        "📱 Smartphone Usage",
        "📚 Smartphone Guide",
        "🛡️ Women Safety",
        "🚨 Safety Records",
        "☎️ Help & Emergency",
        "🎓 Training Sessions",
        "📊 Reports"
    ]
)


# ============================================================
# LOAD PARTICIPANTS
# ============================================================

participants = get_table("participants")

participants_df = pd.DataFrame(
    participants
)


# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    st.title(
        "🌸 Women Digital Safety & Awareness System"
    )

    st.subheader(
        "Smartphone Usage & Online Safety for Women Self Help Groups"
    )

    st.write(
        "A simple digital awareness platform that helps women "
        "learn smartphone usage, online safety and safe digital practices."
    )

    st.divider()

    safety_events = get_table(
        "safety_events"
    )

    training_sessions = get_table(
        "training_sessions"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "👩 Participants",
            len(participants)
        )

    with col2:

        st.metric(
            "🚨 Safety Records",
            len(safety_events)
        )

    with col3:

        st.metric(
            "🎓 Training Sessions",
            len(training_sessions)
        )

    st.divider()

    st.subheader(
        "📌 System Features"
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.info(
            "📱 **Smartphone Learning**\n\n"
            "Learn calls, contacts, WhatsApp, camera, "
            "internet and other smartphone features."
        )

    with c2:

        st.warning(
            "🛡️ **Online Safety**\n\n"
            "Learn password safety, OTP safety, UPI safety, "
            "phishing and social media privacy."
        )

    with c3:

        st.success(
            "🎓 **Training Management**\n\n"
            "Record awareness sessions and store training "
            "information in the database."
        )


# ============================================================
# PARTICIPANTS
# ============================================================

elif page == "👩 Participants":

    st.title(
        "👩 Participants"
    )

    st.write(
        "Add and manage women participating in the awareness program."
    )

    st.divider()

    tab1, tab2 = st.tabs(
        [
            "➕ Add Participant",
            "📋 Participant Records"
        ]
    )


    # --------------------------------------------------------
    # ADD PARTICIPANT
    # --------------------------------------------------------

    with tab1:

        with st.form(
            "participant_form"
        ):

            name = st.text_input(
                "👩 Participant Name"
            )

            age = st.number_input(
                "Age",
                min_value=18,
                max_value=100,
                value=25
            )

            phone = st.text_input(
                "📞 Phone Number"
            )

            group_name = st.text_input(
                "👥 Self Help Group Name"
            )

            submitted = st.form_submit_button(
                "💾 Add Participant",
                use_container_width=True
            )

            if submitted:

                if name.strip() == "":

                    st.error(
                        "Please enter participant name."
                    )

                else:

                    data = {

                        "name":
                            name.strip(),

                        "age":
                            int(age),

                        "phone":
                            phone.strip(),

                        "group_name":
                            group_name.strip()
                    }

                    if add_record(
                        "participants",
                        data
                    ):

                        st.success(
                            "✅ Participant added successfully!"
                        )

                        st.rerun()


    # --------------------------------------------------------
    # PARTICIPANT RECORDS
    # --------------------------------------------------------

    with tab2:

        participants = get_table(
            "participants"
        )

        if not participants:

            st.info(
                "No participants added yet."
            )

        else:

            df = pd.DataFrame(
                participants
            )

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )


# ============================================================
# SMARTPHONE USAGE
# ============================================================

elif page == "📱 Smartphone Usage":

    st.title(
        "📱 Smartphone Usage"
    )

    st.write(
        "Basic smartphone skills for everyday digital activities."
    )

    st.divider()

    topics = {

        "📞 Making a Call":
            "Open the Phone app → select a contact or enter "
            "a number → press the Call button → talk → "
            "press the red button to end the call.",

        "👥 Saving Contacts":
            "Open Contacts → Add Contact → enter name and "
            "phone number → press Save.",

        "💬 WhatsApp":
            "Open WhatsApp → select a contact → type your "
            "message → press Send.",

        "📷 Camera":
            "Open Camera → point the camera → keep the phone "
            "steady → press the capture button.",

        "🌐 Internet":
            "Open Chrome → type your search → check information "
            "from trusted websites.",

        "📧 Email":
            "Open Email → Compose → enter receiver email → "
            "write message → press Send.",

        "📍 Google Maps":
            "Open Maps → search your destination → select "
            "Directions → follow the route."
    }

    selected_topic = st.selectbox(
        "Select a smartphone skill",
        list(topics.keys())
    )

    st.success(
        topics[selected_topic]
    )


# ============================================================
# SMARTPHONE GUIDE
# ============================================================

elif page == "📚 Smartphone Guide":

    st.title(
        "📚 Smartphone Guide"
    )

    st.write(
        "Select one topic to see simple step-by-step instructions."
    )

    st.divider()

    guides = {

        "📞 Make a Call": [

            "Open the Phone application.",

            "Select a saved contact or enter a phone number.",

            "Press the green Call button.",

            "Talk to the person.",

            "Press the red button to end the call."
        ],

        "👥 Save a Contact": [

            "Open Contacts.",

            "Press Add Contact.",

            "Enter the person's name.",

            "Enter the phone number.",

            "Press Save."
        ],

        "💬 WhatsApp": [

            "Open WhatsApp.",

            "Select a contact.",

            "Type your message.",

            "Check the message before sending.",

            "Press Send."
        ],

        "📷 Camera": [

            "Open Camera.",

            "Point the camera toward the object.",

            "Keep the phone steady.",

            "Press the camera button.",

            "Open Gallery to view the photo."
        ],

        "🌐 Internet Search": [

            "Open Chrome or another browser.",

            "Type your question in the search box.",

            "Read information from trusted websites.",

            "Avoid suspicious links.",

            "Do not enter personal information on unknown websites."
        ],

        "📍 Google Maps": [

            "Open Google Maps.",

            "Search for your destination.",

            "Select Directions.",

            "Choose your travel method.",

            "Follow the displayed route."
        ]
    }

    selected = st.selectbox(
        "📌 Choose a topic",
        list(guides.keys())
    )

    st.subheader(
        selected
    )

    for i, step in enumerate(
        guides[selected],
        1
    ):

        st.write(
            f"**Step {i}:** {step}"
        )


# ============================================================
# WOMEN SAFETY
# ============================================================

elif page == "🛡️ Women Safety":

    st.title(
        "🛡️ Women Online Safety"
    )

    st.write(
        "Select a safety topic to learn practical protection steps."
    )

    st.divider()

    safety_topics = {

        "🔐 Password Safety": [

            "Use a strong password.",

            "Do not use your name or date of birth.",

            "Use different passwords for important accounts.",

            "Never share your password.",

            "Change your password if it is exposed."
        ],

        "🔢 OTP Safety": [

            "OTP means One Time Password.",

            "Never share OTP with anyone.",

            "Do not provide OTP over phone calls.",

            "Do not enter OTP on suspicious websites.",

            "Contact the service provider if you shared an OTP by mistake."
        ],

        "💳 UPI & Payment Safety": [

            "Never share your UPI PIN.",

            "Check the receiver name before payment.",

            "Never enter your PIN because someone asks you to receive money.",

            "Do not accept unknown payment requests.",

            "Contact your bank immediately for unauthorized transactions."
        ],

        "🎣 Phishing & Fake Links": [

            "Do not click unknown links.",

            "Check the website address carefully.",

            "Avoid links promising prizes or urgent rewards.",

            "Never enter banking information on suspicious websites.",

            "Verify important messages through official channels."
        ],

        "📱 Social Media Privacy": [

            "Keep your profile private when appropriate.",

            "Avoid posting personal information publicly.",

            "Do not accept unknown people.",

            "Review privacy settings regularly.",

            "Block and report suspicious accounts."
        ],

        "🚫 Cyberbullying": [

            "Do not respond aggressively.",

            "Take screenshots as evidence.",

            "Block the person.",

            "Report the account or content.",

            "Tell a trusted person if the situation is serious."
        ],

        "📍 Location Privacy": [

            "Avoid sharing live location publicly.",

            "Check location permissions for apps.",

            "Turn off location access when it is not needed.",

            "Be careful with photos that reveal your home or routine."
        ]
    }

    selected_safety = st.selectbox(
        "Select safety topic",
        list(safety_topics.keys())
    )

    st.subheader(
        selected_safety
    )

    for i, step in enumerate(
        safety_topics[selected_safety],
        1
    ):

        st.write(
            f"**Step {i}:** {step}"
        )


# ============================================================
# SAFETY RECORDS
# ============================================================

elif page == "🚨 Safety Records":

    st.title(
        "🚨 Online Safety Records"
    )

    st.write(
        "Record online safety concerns reported by participants."
    )

    st.divider()

    participants = get_table(
        "participants"
    )

    participants_df = pd.DataFrame(
        participants
    )

    if participants_df.empty:

        st.warning(
            "⚠️ Please add participants first."
        )

    else:

        tab1, tab2 = st.tabs(
            [
                "➕ Record Safety Event",
                "📋 View Records"
            ]
        )


        # ----------------------------------------------------
        # RECORD SAFETY EVENT
        # ----------------------------------------------------

        with tab1:

            participant_options = {

                f"{row['participant_id']} - {row['name']}":
                row["participant_id"]

                for _, row in participants_df.iterrows()
            }

            with st.form(
                "safety_event_form"
            ):

                participant = st.selectbox(
                    "👩 Participant",
                    list(
                        participant_options.keys()
                    )
                )

                event_type = st.selectbox(
                    "⚠️ Safety Issue",
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
                    "📅 Date"
                )

                description = st.text_area(
                    "📝 What happened?"
                )

                action_taken = st.text_area(
                    "✅ Action Taken"
                )

                reported = st.selectbox(
                    "🚨 Reported?",
                    [
                        "Yes",
                        "No"
                    ]
                )

                submitted = st.form_submit_button(
                    "💾 Save Safety Record",
                    use_container_width=True
                )

                if submitted:

                    data = {

                        "participant_id":
                            participant_options[
                                participant
                            ],

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
                            "✅ Safety record saved successfully!"
                        )

                        st.rerun()


        # ----------------------------------------------------
        # VIEW RECORDS
        # ----------------------------------------------------

        with tab2:

            safety_events = get_table(
                "safety_events"
            )

            if not safety_events:

                st.info(
                    "No safety records have been recorded yet."
                )

            else:

                events_df = pd.DataFrame(
                    safety_events
                )

                st.dataframe(
                    events_df,
                    use_container_width=True,
                    hide_index=True
                )


# ============================================================
# HELP & EMERGENCY
# ============================================================

elif page == "☎️ Help & Emergency":

    st.title(
        "☎️ Help & Emergency"
    )

    st.write(
        "Important emergency and cybercrime assistance numbers."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:

        st.error(
            "### 🚨 112\n"
            "Emergency assistance number."
        )

    with col2:

        st.warning(
            "### 👩 181\n"
            "Women Helpline."
        )

    with col3:

        st.info(
            "### 💻 1930\n"
            "Cybercrime / financial fraud helpline."
        )

    st.divider()

    st.subheader(
        "🛡️ If you face an online safety problem"
    )

    steps = [

        "Stay calm and do not respond to suspicious messages.",

        "Take screenshots and keep relevant evidence.",

        "Block suspicious accounts or numbers.",

        "Contact your bank for unauthorized financial transactions.",

        "Report cybercrime through the appropriate official channel.",

        "For immediate danger, contact emergency services."
    ]

    for i, step in enumerate(
        steps,
        1
    ):

        st.write(
            f"**{i}.** {step}"
        )


# ============================================================
# TRAINING SESSIONS
# ============================================================

elif page == "🎓 Training Sessions":

    st.title(
        "🎓 Training Sessions"
    )

    st.write(
        "Add awareness training sessions and store their "
        "information in the Supabase database."
    )

    st.divider()

    tab1, tab2 = st.tabs(
        [
            "➕ Add Training Session",
            "📋 Training Records"
        ]
    )


    # ========================================================
    # ADD TRAINING
    # ========================================================

    with tab1:

        with st.form(
            "training_form",
            clear_on_submit=True
        ):

            session_date = st.date_input(
                "📅 Session Date"
            )

            topic = st.selectbox(
                "📚 Training Topic",
                [
                    "Basic Smartphone Usage",
                    "Making Calls & Saving Contacts",
                    "WhatsApp Safety",
                    "Internet Usage",
                    "Password Safety",
                    "OTP Safety",
                    "UPI & Payment Safety",
                    "Social Media Safety",
                    "Phishing Awareness",
                    "Cybercrime Awareness"
                ]
            )

            trainer = st.text_input(
                "👨‍🏫 Trainer Name"
            )

            participants_count = st.number_input(
                "👩 Number of Participants",
                min_value=1,
                value=1,
                step=1
            )

            notes = st.text_area(
                "📝 Training Notes",
                placeholder="Enter details about the training session..."
            )

            submitted = st.form_submit_button(
                "💾 Save Training Session",
                use_container_width=True
            )

            if submitted:

                if trainer.strip() == "":

                    st.error(
                        "Please enter trainer name."
                    )

                else:

                    training_data = {

                        "session_date":
                            str(session_date),

                        "topic":
                            topic,

                        "trainer":
                            trainer.strip(),

                        "participants_count":
                            int(participants_count),

                        "notes":
                            notes.strip()
                    }

                    try:

                        response = (
                            supabase
                            .table("training_sessions")
                            .insert(training_data)
                            .execute()
                        )

                        if response.data:

                            st.success(
                                "✅ Training session saved successfully in database!"
                            )

                            st.rerun()

                        else:

                            st.error(
                                "❌ Training session could not be saved."
                            )

                    except Exception as e:

                        st.error(
                            "❌ Database error while saving training session."
                        )

                        st.code(
                            str(e)
                        )


    # ========================================================
    # VIEW TRAINING RECORDS
    # ========================================================

    with tab2:

        training_sessions = get_table(
            "training_sessions"
        )

        if not training_sessions:

            st.info(
                "No training sessions recorded yet."
            )

        else:

            training_df = pd.DataFrame(
                training_sessions
            )

            st.success(
                f"✅ {len(training_df)} training session(s) found in database."
            )

            st.dataframe(
                training_df,
                use_container_width=True,
                hide_index=True
            )


# ============================================================
# REPORTS
# ============================================================

elif page == "📊 Reports":

    st.title(
        "📊 Reports & Analysis"
    )

    st.write(
        "View participant, safety and training information."
    )

    st.divider()

    participants = get_table(
        "participants"
    )

    safety_events = get_table(
        "safety_events"
    )

    training_sessions = get_table(
        "training_sessions"
    )


    # --------------------------------------------------------
    # SUMMARY
    # --------------------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "👩 Total Participants",
            len(participants)
        )

    with col2:

        st.metric(
            "🚨 Safety Events",
            len(safety_events)
        )

    with col3:

        st.metric(
            "🎓 Training Sessions",
            len(training_sessions)
        )


    st.divider()


    # ========================================================
    # TRAINING REPORT
    # ========================================================

    st.subheader(
        "🎓 Training Session Report"
    )

    if not training_sessions:

        st.info(
            "No training data available."
        )

    else:

        training_df = pd.DataFrame(
            training_sessions
        )

        st.dataframe(
            training_df,
            use_container_width=True,
            hide_index=True
        )

        if "topic" in training_df.columns:

            topic_count = (
                training_df[
                    "topic"
                ]
                .value_counts()
                .reset_index()
            )

            topic_count.columns = [
                "Training Topic",
                "Sessions"
            ]

            fig = px.bar(
                topic_count,
                x="Training Topic",
                y="Sessions",
                title="Training Sessions by Topic"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


    st.divider()


    # ========================================================
    # SAFETY REPORT
    # ========================================================

    st.subheader(
        "🚨 Safety Event Report"
    )

    if not safety_events:

        st.info(
            "No safety event data available."
        )

    else:

        safety_df = pd.DataFrame(
            safety_events
        )

        st.dataframe(
            safety_df,
            use_container_width=True,
            hide_index=True
        )

        if "event_type" in safety_df.columns:

            event_count = (
                safety_df[
                    "event_type"
                ]
                .value_counts()
                .reset_index()
            )

            event_count.columns = [
                "Safety Issue",
                "Count"
            ]

            fig2 = px.bar(
                event_count,
                x="Safety Issue",
                y="Count",
                title="Safety Issues Recorded"
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Women Digital Safety & Awareness System | "
    "Smartphone Usage & Online Safety for Women Self Help Groups"
)
