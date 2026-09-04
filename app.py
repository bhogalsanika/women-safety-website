import streamlit as st
from supabase import create_client
import pandas as pd
import plotly.express as px
from datetime import datetime


# ============================================================
# PAGE CONFIG
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

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #7b1e3a;
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


def delete_record(table_name, column, value):

    try:

        (
            supabase
            .table(table_name)
            .delete()
            .eq(column, value)
            .execute()
        )

        return True

    except Exception as e:

        st.error(
            f"Delete error: {e}"
        )

        return False


# ============================================================
# SESSION STATE
# ============================================================

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

if "quiz_current" not in st.session_state:
    st.session_state.quiz_current = 0

if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = {}

if "quiz_participant_id" not in st.session_state:
    st.session_state.quiz_participant_id = None

if "quiz_participant_name" not in st.session_state:
    st.session_state.quiz_participant_name = ""

if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0


# ============================================================
# SIDEBAR
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
        "📝 Safety Quiz",
        "🚨 Safety Records",
        "☎️ Help & Emergency",
        "🎓 Training Sessions",
        "📊 Reports"
    ]
)


# ============================================================
# LOAD DATA
# ============================================================

participants = get_table("participants")

participants_df = pd.DataFrame(participants)


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
        "A simple digital awareness platform to help women "
        "learn smartphone usage, online safety and safe digital practices."
    )

    st.divider()

    quiz_results = get_table("quiz_results")
    safety_events = get_table("safety_events")
    training_sessions = get_table("training_sessions")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "👩 Participants",
            len(participants)
        )

    with col2:

        st.metric(
            "📝 Quiz Attempts",
            len(quiz_results)
        )

    with col3:

        st.metric(
            "🚨 Safety Records",
            len(safety_events)
        )

    with col4:

        st.metric(
            "🎓 Training Sessions",
            len(training_sessions)
        )

    st.divider()

    st.subheader("📌 What this system provides")

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
            "Learn password safety, OTP safety, "
            "UPI safety, phishing and social media privacy."
        )

    with c3:

        st.success(
            "📝 **Interactive Quiz**\n\n"
            "Test your knowledge and store participant "
            "quiz results in the database."
        )


# ============================================================
# PARTICIPANTS
# ============================================================

elif page == "👩 Participants":

    st.title("👩 Participants")

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

        with st.form("participant_form"):

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
                        "name": name.strip(),
                        "age": int(age),
                        "phone": phone.strip(),
                        "group_name": group_name.strip()
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
    # VIEW PARTICIPANTS
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

    st.title("📱 Smartphone Usage")

    st.write(
        "Basic smartphone skills that can help women use "
        "digital services confidently."
    )

    st.divider()

    topics = {

        "📞 Making a Call":
            "Open the Phone app → select a contact or enter "
            "a number → press the call button → speak clearly → "
            "press the red button to end the call.",

        "👥 Saving Contacts":
            "Open Contacts → select Add Contact → enter name "
            "and phone number → save the contact.",

        "💬 Sending WhatsApp Messages":
            "Open WhatsApp → select a contact → type your message "
            "→ press Send.",

        "📷 Using Camera":
            "Open Camera → point the camera at the subject → "
            "press the capture button → open Gallery to view the photo.",

        "🌐 Using Internet":
            "Open Chrome or another browser → type what you want "
            "to search → check information from trusted websites.",

        "📧 Using Email":
            "Open the email application → select Compose → "
            "enter receiver email → write message → press Send.",

        "📍 Using Maps":
            "Open Google Maps → search for a location → "
            "check directions → follow the route carefully."
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

    st.title("📚 Smartphone Guide")

    st.write(
        "Select a topic to see simple step-by-step instructions."
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
            "Open Gallery to see the photo."
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
            "Choose walking, car or public transport.",
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

    st.title("🛡️ Women Online Safety")

    st.write(
        "Select a safety topic to learn practical protection steps."
    )

    st.divider()

    safety_topics = {

        "🔐 Password Safety": [
            "Use a strong password.",
            "Do not use your name or date of birth as a password.",
            "Use different passwords for important accounts.",
            "Never share your password with anyone.",
            "Change your password if you think it has been exposed."
        ],

        "🔢 OTP Safety": [
            "OTP means One Time Password.",
            "Never share OTP with anyone.",
            "Banks and genuine companies do not need your OTP over a phone call.",
            "Do not enter OTP on suspicious websites.",
            "If you shared an OTP by mistake, contact the service provider immediately."
        ],

        "💳 UPI & Payment Safety": [
            "Never share your UPI PIN.",
            "Check the receiver name before payment.",
            "Remember: entering UPI PIN usually authorizes a payment.",
            "Do not accept unknown collect requests.",
            "Contact your bank immediately if you notice an unauthorized transaction."
        ],

        "🎣 Phishing & Fake Links": [
            "Do not click unknown links.",
            "Check the website address carefully.",
            "Avoid links promising prizes or urgent rewards.",
            "Never enter passwords or banking details on suspicious websites.",
            "Verify important messages through official channels."
        ],

        "📱 Social Media Privacy": [
            "Keep your social media profile private when appropriate.",
            "Avoid posting personal information publicly.",
            "Do not accept requests from unknown people.",
            "Review privacy settings regularly.",
            "Block and report suspicious accounts."
        ],

        "🚫 Cyberbullying": [
            "Do not respond aggressively.",
            "Take screenshots as evidence.",
            "Block the person.",
            "Report the account or content.",
            "Tell a trusted person or authority if the situation is serious."
        ],

        "📍 Location Privacy": [
            "Avoid sharing your live location publicly.",
            "Check location permissions for apps.",
            "Turn off location access when it is not needed.",
            "Be careful when posting photos that reveal your home or routine."
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
# SAFETY QUIZ
# ============================================================

elif page == "📝 Safety Quiz":

    st.title("📝 Online Safety Quiz")

    st.write(
        "Test your knowledge about smartphone and online safety."
    )

    st.divider()

    # --------------------------------------------------------
    # QUESTIONS
    # --------------------------------------------------------

    quiz_questions = [

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
                    "Check receiver name and amount",
                    "Share your PIN",
                    "Click any link"
                ],
            "answer":
                "Check receiver name and amount"
        },

        {
            "question":
                "What should you do with a suspicious link?",
            "options":
                [
                    "Click immediately",
                    "Ignore and verify it",
                    "Forward it to everyone"
                ],
            "answer":
                "Ignore and verify it"
        },

        {
            "question":
                "Which is a good password practice?",
            "options":
                [
                    "Use your birthday",
                    "Use the same password everywhere",
                    "Use a strong unique password"
                ],
            "answer":
                "Use a strong unique password"
        },

        {
            "question":
                "What should you do if someone is cyberbullying you?",
            "options":
                [
                    "Save evidence and report/block",
                    "Give them your password",
                    "Share more personal information"
                ],
            "answer":
                "Save evidence and report/block"
        },

        {
            "question":
                "Should your UPI PIN be shared with anyone?",
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
                "What is safer when using social media?",
            "options":
                [
                    "Share everything publicly",
                    "Use privacy settings",
                    "Accept every unknown person"
                ],
            "answer":
                "Use privacy settings"
        },

        {
            "question":
                "What should you do if you receive a suspicious banking message?",
            "options":
                [
                    "Click its link",
                    "Verify through the official bank channel",
                    "Share your OTP"
                ],
            "answer":
                "Verify through the official bank channel"
        }
    ]

    # --------------------------------------------------------
    # PARTICIPANT SELECTION
    # --------------------------------------------------------

    if not participants:

        st.warning(
            "⚠️ Please add at least one participant before taking the quiz."
        )

    else:

        participants_df = pd.DataFrame(
            participants
        )

        participant_options = {
            f"{row['participant_id']} - {row['name']}":
            row["participant_id"]
            for _, row in participants_df.iterrows()
        }

        # ----------------------------------------------------
        # BEFORE QUIZ
        # ----------------------------------------------------

        if not st.session_state.quiz_started:

            selected_participant = st.selectbox(
                "👩 Select Participant",
                list(participant_options.keys())
            )

            if st.button(
                "▶️ Start Quiz",
                use_container_width=True
            ):

                st.session_state.quiz_participant_id = (
                    participant_options[selected_participant]
                )

                st.session_state.quiz_participant_name = (
                    selected_participant.split(" - ", 1)[1]
                )

                st.session_state.quiz_started = True
                st.session_state.quiz_current = 0
                st.session_state.quiz_answers = {}
                st.session_state.quiz_finished = False
                st.session_state.quiz_score = 0

                st.rerun()

        # ----------------------------------------------------
        # QUIZ FINISHED
        # ----------------------------------------------------

        elif st.session_state.quiz_finished:

            st.success(
                "🎉 Quiz completed successfully!"
            )

            st.subheader(
                f"Participant: {st.session_state.quiz_participant_name}"
            )

            score = st.session_state.quiz_score

            total = len(
                quiz_questions
            )

            percentage = (
                score / total
            ) * 100

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Score",
                    f"{score}/{total}"
                )

            with col2:

                st.metric(
                    "Percentage",
                    f"{percentage:.1f}%"
                )

            with col3:

                if percentage >= 60:
                    result = "Passed"
                else:
                    result = "Needs Improvement"

                st.metric(
                    "Result",
                    result
                )

            if st.button(
                "🔄 Take Quiz Again",
                use_container_width=True
            ):

                st.session_state.quiz_started = False
                st.session_state.quiz_current = 0
                st.session_state.quiz_answers = {}
                st.session_state.quiz_finished = False
                st.session_state.quiz_score = 0
                st.rerun()

        # ----------------------------------------------------
        # ACTIVE QUIZ
        # ----------------------------------------------------

        else:

            current = st.session_state.quiz_current

            question_data = quiz_questions[current]

            st.info(
                f"👩 Participant: "
                f"{st.session_state.quiz_participant_name}"
            )

            st.progress(
                (current + 1) /
                len(quiz_questions)
            )

            st.subheader(
                f"Question {current + 1} of {len(quiz_questions)}"
            )

            st.write(
                f"### {question_data['question']}"
            )

            previous_answer = (
                st.session_state.quiz_answers.get(
                    current
                )
            )

            if previous_answer:

                default_index = (
                    question_data["options"].index(
                        previous_answer
                    )
                )

            else:

                default_index = 0

            selected_answer = st.radio(
                "Select your answer:",
                question_data["options"],
                index=default_index,
                key=f"question_{current}"
            )

            col1, col2 = st.columns(2)

            with col1:

                if current > 0:

                    if st.button(
                        "⬅️ Previous",
                        use_container_width=True
                    ):

                        st.session_state.quiz_answers[
                            current
                        ] = selected_answer

                        st.session_state.quiz_current -= 1

                        st.rerun()

            with col2:

                if current < len(quiz_questions) - 1:

                    if st.button(
                        "Next ➡️",
                        use_container_width=True
                    ):

                        st.session_state.quiz_answers[
                            current
                        ] = selected_answer

                        st.session_state.quiz_current += 1

                        st.rerun()

                else:

                    if st.button(
                        "✅ Submit Quiz",
                        use_container_width=True
                    ):

                        st.session_state.quiz_answers[
                            current
                        ] = selected_answer

                        score = 0

                        answer_data = {}

                        for index, question in enumerate(
                            quiz_questions
                        ):

                            user_answer = (
                                st.session_state.quiz_answers.get(
                                    index,
                                    ""
                                )
                            )

                            correct_answer = (
                                question["answer"]
                            )

                            if user_answer == correct_answer:

                                score += 1

                            answer_data[str(index + 1)] = {
                                "question":
                                    question["question"],
                                "selected_answer":
                                    user_answer,
                                "correct_answer":
                                    correct_answer
                            }

                        # ------------------------------------
                        # SAVE QUIZ RESULT
                        # ------------------------------------

                        quiz_data = {

                            "participant_id":
                                int(
                                    st.session_state.quiz_participant_id
                                ),

                            "score":
                                int(score),

                            "total_questions":
                                int(
                                    len(quiz_questions)
                                ),

                            "answers":
                                answer_data,

                            "completed_at":
                                datetime.now().isoformat()
                        }

                        try:

                            response = (
                                supabase
                                .table("quiz_results")
                                .insert(quiz_data)
                                .execute()
                            )

                            if response.data:

                                st.session_state.quiz_score = score

                                st.session_state.quiz_finished = True

                                st.success(
                                    "✅ Quiz result saved successfully!"
                                )

                                st.rerun()

                            else:

                                st.error(
                                    "❌ Quiz result was not saved."
                                )

                        except Exception as e:

                            st.error(
                                "❌ Database error while saving quiz."
                            )

                            st.code(
                                str(e)
                            )

                            st.info(
                                "Check quiz_results table and Supabase RLS policies."
                            )


# ============================================================
# SAFETY RECORDS
# ============================================================

elif page == "🚨 Safety Records":

    st.title("🚨 Online Safety Records")

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
        # RECORD EVENT
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
                    "📝 What happened?",
                    placeholder="Enter a short description..."
                )

                action_taken = st.text_area(
                    "✅ Action Taken",
                    placeholder="Enter what action was taken..."
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

    st.title("☎️ Help & Emergency")

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

        "Contact your bank immediately for unauthorized financial transactions.",

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

    st.title("🎓 Training Sessions")

    st.write(
        "Record smartphone and online safety awareness sessions."
    )

    st.divider()

    tab1, tab2 = st.tabs(
        [
            "➕ Add Session",
            "📋 Session Records"
        ]
    )

    # --------------------------------------------------------
    # ADD SESSION
    # --------------------------------------------------------

    with tab1:

        with st.form(
            "training_form"
        ):

            session_date = st.date_input(
                "📅 Session Date"
            )

            topic = st.selectbox(
                "📚 Training Topic",
                [
                    "Basic Smartphone Usage",
                    "WhatsApp Safety",
                    "Password Safety",
                    "OTP Safety",
                    "UPI Safety",
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
                value=1
            )

            notes = st.text_area(
                "📝 Notes"
            )

            submitted = st.form_submit_button(
                "💾 Save Training Session",
                use_container_width=True
            )

            if submitted:

                data = {

                    "session_date":
                        str(session_date),

                    "topic":
                        topic,

                    "trainer":
                        trainer,

                    "participants_count":
                        int(
                            participants_count
                        ),

                    "notes":
                        notes
                }

                if add_record(
                    "training_sessions",
                    data
                ):

                    st.success(
                        "✅ Training session saved!"
                    )

    # --------------------------------------------------------
    # VIEW SESSIONS
    # --------------------------------------------------------

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

            st.dataframe(
                training_df,
                use_container_width=True,
                hide_index=True
            )


# ============================================================
# REPORTS
# ============================================================

elif page == "📊 Reports":

    st.title("📊 Reports & Analysis")

    st.write(
        "View participant quiz performance and safety records."
    )

    st.divider()

    participants = get_table(
        "participants"
    )

    quiz_results = get_table(
        "quiz_results"
    )

    safety_events = get_table(
        "safety_events"
    )

    # --------------------------------------------------------
    # QUIZ REPORT
    # --------------------------------------------------------

    st.subheader(
        "📝 Quiz Performance"
    )

    if not quiz_results:

        st.info(
            "No quiz results available yet."
        )

    else:

        quiz_df = pd.DataFrame(
            quiz_results
        )

        participant_names = {

            p.get("participant_id"):
                p.get("name", "Unknown")

            for p in participants
        }

        if "participant_id" in quiz_df.columns:

            quiz_df["Participant Name"] = (
                quiz_df["participant_id"]
                .map(participant_names)
            )

        show_columns = []

        for col in [

            "quiz_id",
            "Participant Name",
            "participant_id",
            "score",
            "total_questions",
            "completed_at"

        ]:

            if col in quiz_df.columns:

                show_columns.append(
                    col
                )

        st.dataframe(
            quiz_df[
                show_columns
            ],
            use_container_width=True,
            hide_index=True
        )

        # ----------------------------------------------------
        # SCORE CHART
        # ----------------------------------------------------

        if (
            "score" in quiz_df.columns
            and "participant_id" in quiz_df.columns
        ):

            chart_df = quiz_df.copy()

            chart_df["Participant"] = (
                chart_df["participant_id"]
                .map(participant_names)
            )

            fig = px.bar(
                chart_df,
                x="Participant",
                y="score",
                title="Quiz Scores"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    st.divider()

    # --------------------------------------------------------
    # SAFETY REPORT
    # --------------------------------------------------------

    st.subheader(
        "🚨 Safety Event Report"
    )

    if not safety_events:

        st.info(
            "No safety events available yet."
        )

    else:

        safety_df = pd.DataFrame(
            safety_events
        )

        if "participant_id" in safety_df.columns:

            safety_df["Participant Name"] = (
                safety_df["participant_id"]
                .map(participant_names)
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
