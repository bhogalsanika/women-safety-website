import streamlit as st
from supabase import create_client
import pandas as pd
import plotly.express as px
from datetime import date, datetime


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Women Digital Safety & Awareness System",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background-color: #f7f7fb;
}

.block-container {
    padding-top: 1.5rem;
}

.hero {
    background: linear-gradient(135deg, #fff0f6, #f3f0ff);
    padding: 30px;
    border-radius: 18px;
    margin-bottom: 25px;
    border: 1px solid #eadce5;
}

.hero h1 {
    color: #7b2850;
    margin-bottom: 8px;
}

.hero p {
    color: #666;
    font-size: 15px;
}

.section-title {
    font-size: 27px;
    font-weight: 800;
    color: #282b35;
    margin-bottom: 5px;
}

.section-subtitle {
    color: #737780;
    margin-bottom: 20px;
}

.info-card {
    background: white;
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #e5e5eb;
    min-height: 150px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.04);
}

.info-card h3 {
    color: #7b2850;
    margin-top: 0;
}

.info-card p {
    color: #666;
    line-height: 1.6;
}

.learning-box {
    background: white;
    padding: 25px;
    border-radius: 15px;
    border-left: 5px solid #9b3565;
    margin-top: 20px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.04);
}

.learning-box h3 {
    color: #7b2850;
}

.step {
    background: #faf7f9;
    border: 1px solid #eee1e8;
    padding: 14px;
    border-radius: 9px;
    margin: 10px 0;
    color: #444;
}

.step b {
    color: #7b2850;
}

.quiz-question {
    background: white;
    padding: 28px;
    border-radius: 16px;
    border: 1px solid #e5e5eb;
    margin: 20px 0;
    box-shadow: 0 4px 14px rgba(0,0,0,0.04);
}

.quiz-number {
    color: #9b3565;
    font-weight: 800;
}

.quiz-text {
    font-size: 21px;
    font-weight: 700;
    margin-top: 10px;
}

.emergency-card {
    background: white;
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #e5e5eb;
    box-shadow: 0 3px 12px rgba(0,0,0,0.04);
}

.emergency-number {
    font-size: 32px;
    font-weight: 800;
    color: #9b3565;
}

[data-testid="stMetric"] {
    background: white;
    border-radius: 14px;
    padding: 15px;
    border: 1px solid #e5e5eb;
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


try:
    supabase = init_connection()

except Exception as e:
    st.error("Supabase connection failed.")
    st.code(str(e))
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

        return response.data or []

    except Exception as e:
        st.error(f"Unable to load {table_name}: {e}")
        return []


def add_record(table_name, data):
    try:
        response = (
            supabase
            .table(table_name)
            .insert(data)
            .execute()
        )

        return response.data

    except Exception as e:
        st.error(f"Database error: {e}")
        return None


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
        st.error(f"Delete error: {e}")
        return False


# ============================================================
# LOAD DATA
# ============================================================

participants = get_table("participants")
smartphone_usage = get_table("smartphone_usage")
safety_events = get_table("safety_events")
training_sessions = get_table("training_sessions")
quiz_results = get_table("quiz_results")

participants_df = pd.DataFrame(participants)
smartphone_df = pd.DataFrame(smartphone_usage)
safety_df = pd.DataFrame(safety_events)
training_df = pd.DataFrame(training_sessions)
quiz_df = pd.DataFrame(quiz_results)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("""
    <div style="text-align:center; padding:15px;">

        <div style="font-size:38px;">🛡️</div>

        <div style="
            font-size:20px;
            font-weight:800;
            color:#7b2850;
        ">
            Women Digital Safety
            <br>
            & Awareness System
        </div>

        <div style="
            font-size:11px;
            color:#777;
            margin-top:8px;
        ">
            Smartphone Usage & Online Safety
            <br>
            for Women Self Help Groups
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "👩 Participants",
            "📱 Smartphone Usage",
            "📚 Smartphone Guide",
            "🛡️ Women Safety",
            "📝 Safety Quiz",
            "🚨 Safety Events",
            "☎️ Help & Emergency",
            "🎓 Training Sessions",
            "📊 Reports"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.caption("Community Engagement Project")
    st.caption("Smartphone & Online Safety")


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

    <h1>
        🛡️ Women Digital Safety & Awareness System
    </h1>

    <p>
        Learn smartphone skills, understand online safety,
        practice through interactive learning and quizzes,
        and access important support resources.
    </p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# QUIZ QUESTIONS
# ============================================================

quiz_questions = [

    {
        "question": "Should you share your OTP with another person?",
        "options": ["Yes", "No"],
        "answer": "No"
    },

    {
        "question": "What should you do before making a UPI payment?",
        "options": [
            "Check receiver name and amount",
            "Share your PIN",
            "Click any link"
        ],
        "answer": "Check receiver name and amount"
    },

    {
        "question": "What should you do with a suspicious link?",
        "options": [
            "Click immediately",
            "Ignore and verify it",
            "Forward it to everyone"
        ],
        "answer": "Ignore and verify it"
    },

    {
        "question": "Which is a good password practice?",
        "options": [
            "Use your birthday",
            "Use the same password everywhere",
            "Use a strong unique password"
        ],
        "answer": "Use a strong unique password"
    },

    {
        "question": "What should you do if someone is cyberbullying you?",
        "options": [
            "Save evidence and report/block",
            "Give them your password",
            "Share more personal information"
        ],
        "answer": "Save evidence and report/block"
    },

    {
        "question": "Should your UPI PIN be shared with anyone?",
        "options": ["Yes", "No"],
        "answer": "No"
    },

    {
        "question": "What is safer when using social media?",
        "options": [
            "Share everything publicly",
            "Use privacy settings",
            "Accept every unknown person"
        ],
        "answer": "Use privacy settings"
    },

    {
        "question": "What should you do if you receive a suspicious banking message?",
        "options": [
            "Click its link",
            "Verify through the official bank channel",
            "Share your OTP"
        ],
        "answer": "Verify through the official bank channel"
    }
]


# ============================================================
# QUIZ SESSION STATE
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
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    st.markdown(
        '<div class="section-title">Dashboard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Overview of community participation and digital safety activities.'
        '</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("👩 Participants", len(participants_df))

    with c2:
        st.metric("📱 Smartphone Records", len(smartphone_df))

    with c3:
        st.metric("🛡️ Safety Events", len(safety_df))

    with c4:
        st.metric("📝 Quiz Attempts", len(quiz_df))

    st.markdown("### Quick Learning")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="info-card">

            <h3>📱 Smartphone Learning</h3>

            <p>
                Learn calling, contacts, WhatsApp,
                camera, Google search, UPI payments
                and location sharing.
            </p>

        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="info-card">

            <h3>🛡️ Online Safety</h3>

            <p>
                Learn password safety, OTP protection,
                UPI fraud prevention, privacy and
                social media safety.
            </p>

        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="info-card">

            <h3>📝 Safety Quiz</h3>

            <p>
                Test digital safety knowledge with
                an interactive quiz and save the
                participant result.
            </p>

        </div>
        """, unsafe_allow_html=True)

    if len(safety_df) > 0 and "event_type" in safety_df.columns:

        st.markdown("### Safety Events Overview")

        event_count = (
            safety_df["event_type"]
            .value_counts()
            .reset_index()
        )

        event_count.columns = ["Event Type", "Count"]

        fig = px.bar(
            event_count,
            x="Event Type",
            y="Count",
            title="Reported Safety Events"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# ============================================================
# PARTICIPANTS
# ============================================================

elif page == "👩 Participants":

    st.markdown(
        '<div class="section-title">👩 Participants</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Register and manage women participating in the programme.'
        '</div>',
        unsafe_allow_html=True
    )

    with st.expander(
        "➕ Add New Participant",
        expanded=True
    ):

        with st.form("participant_form"):

            c1, c2 = st.columns(2)

            with c1:

                name = st.text_input("Full Name")

                age = st.number_input(
                    "Age",
                    min_value=18,
                    max_value=100,
                    value=30
                )

                contact = st.text_input(
                    "Contact Number"
                )

            with c2:

                occupation = st.text_input(
                    "Occupation"
                )

                smartphone_user = st.selectbox(
                    "Uses Smartphone?",
                    ["Yes", "No"]
                )

            submit = st.form_submit_button(
                "Add Participant",
                use_container_width=True
            )

            if submit:

                if not name.strip():

                    st.warning(
                        "Please enter participant name."
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

                    result = add_record(
                        "participants",
                        data
                    )

                    if result is not None:

                        st.success(
                            "Participant added successfully."
                        )

                        st.rerun()

    st.markdown("### Participant Records")

    if len(participants_df) > 0:

        st.dataframe(
            participants_df,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("### Delete Participant")

        delete_options = {
            f"{p.get('name', 'Unknown')} - ID {p.get('participant_id')}":
            p.get("participant_id")
            for p in participants
        }

        if delete_options:

            selected_delete = st.selectbox(
                "Select participant",
                list(delete_options.keys())
            )

            if st.button(
                "Delete Selected Participant",
                use_container_width=True
            ):

                pid = delete_options[selected_delete]

                if delete_record(
                    "participants",
                    "participant_id",
                    pid
                ):

                    st.success(
                        "Participant deleted successfully."
                    )

                    st.rerun()

    else:

        st.info(
            "No participants added yet."
        )


# ============================================================
# SMARTPHONE USAGE
# ============================================================

elif page == "📱 Smartphone Usage":

    st.markdown(
        '<div class="section-title">📱 Smartphone Usage</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Record how participants use smartphones in daily life.'
        '</div>',
        unsafe_allow_html=True
    )

    if len(participants) == 0:

        st.warning(
            "Please add participants first."
        )

    else:

        participant_options = {
            f"{p.get('name', 'Unknown')} - ID {p.get('participant_id')}":
            p.get("participant_id")
            for p in participants
        }

        with st.form("smartphone_form"):

            selected = st.selectbox(
                "Participant",
                list(participant_options.keys())
            )

            purpose = st.selectbox(
                "Main Smartphone Purpose",
                [
                    "Communication",
                    "Education",
                    "Business",
                    "Entertainment",
                    "Digital Payments",
                    "Social Media",
                    "Online Shopping",
                    "Government Services"
                ]
            )

            c1, c2 = st.columns(2)

            with c1:

                social_media = st.selectbox(
                    "Uses Social Media?",
                    ["Yes", "No"]
                )

                digital_payment = st.selectbox(
                    "Uses Digital Payment?",
                    ["Yes", "No"]
                )

            with c2:

                online_shopping = st.selectbox(
                    "Uses Online Shopping?",
                    ["Yes", "No"]
                )

                education = st.selectbox(
                    "Uses Smartphone for Education?",
                    ["Yes", "No"]
                )

            daily_hours = st.number_input(
                "Daily Smartphone Usage (hours)",
                min_value=0.0,
                max_value=24.0,
                value=2.0,
                step=0.5
            )

            submit = st.form_submit_button(
                "Save Smartphone Usage",
                use_container_width=True
            )

            if submit:

                data = {
                    "participant_id":
                        participant_options[selected],

                    "usage_purpose":
                        purpose,

                    "social_media":
                        social_media == "Yes",

                    "digital_payment":
                        digital_payment == "Yes",

                    "online_shopping":
                        online_shopping == "Yes",

                    "education":
                        education == "Yes",

                    "daily_usage_hours":
                        daily_hours
                }

                result = add_record(
                    "smartphone_usage",
                    data
                )

                if result is not None:

                    st.success(
                        "Smartphone usage saved successfully."
                    )

                    st.rerun()

    st.markdown("### Smartphone Usage Records")

    if len(smartphone_df) > 0:

        st.dataframe(
            smartphone_df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No smartphone usage records yet."
        )


# ============================================================
# SMARTPHONE GUIDE
# ============================================================

elif page == "📚 Smartphone Guide":

    st.markdown(
        '<div class="section-title">📚 Smartphone Guide</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Select one topic to learn the activity step-by-step.'
        '</div>',
        unsafe_allow_html=True
    )

    smartphone_topics = {

        "📞 Make a Call": [
            "Open the Phone application.",
            "Tap the keypad.",
            "Enter the mobile number.",
            "Press the green Call button.",
            "Press the red End Call button to finish."
        ],

        "👤 Save a Contact": [
            "Open the Contacts application.",
            "Tap Add Contact (+).",
            "Enter the person's name.",
            "Enter the mobile number.",
            "Tap Save."
        ],

        "💬 Send WhatsApp Message": [
            "Open WhatsApp.",
            "Open the person's chat.",
            "Type your message.",
            "Press the Send button.",
            "Wait for the message to be delivered."
        ],

        "📷 Take a Photo": [
            "Open the Camera application.",
            "Point the camera at the subject.",
            "Keep the phone steady.",
            "Tap the camera button.",
            "Open Gallery to view the photo."
        ],

        "🌐 Search on Google": [
            "Open Chrome or another browser.",
            "Tap the search bar.",
            "Type what you want to search.",
            "Tap Search.",
            "Prefer information from trusted websites."
        ],

        "💳 Use UPI Payment": [
            "Open your trusted UPI application.",
            "Select Send Money or Scan & Pay.",
            "Enter receiver details or scan the QR code.",
            "Check receiver name and amount.",
            "Enter your UPI PIN only after checking the payment."
        ],

        "📍 Share Location": [
            "Open WhatsApp or your messaging application.",
            "Open the trusted person's chat.",
            "Tap the attachment option.",
            "Select Location.",
            "Choose current or live location."
        ]
    }

    selected_topic = st.selectbox(
        "Choose a topic",
        list(smartphone_topics.keys())
    )

    st.markdown(
        '<div class="learning-box">'
        f'<h3>{selected_topic}</h3>',
        unsafe_allow_html=True
    )

    for i, step in enumerate(
        smartphone_topics[selected_topic],
        start=1
    ):

        st.markdown(
            f"""
            <div class="step">
                <b>Step {i}</b><br>
                {step}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    st.success(
        "💡 Practice one activity at a time."
    )


# ============================================================
# WOMEN SAFETY
# ============================================================

elif page == "🛡️ Women Safety":

    st.markdown(
        '<div class="section-title">🛡️ Women Online Safety</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Select a safety topic to learn practical protection steps.'
        '</div>',
        unsafe_allow_html=True
    )

    safety_topics = {

        "🔐 Password Safety": [
            "Create a strong and unique password.",
            "Do not use your birthday or mobile number.",
            "Never share your password.",
            "Use two-factor authentication when available.",
            "Change your password if you think someone knows it."
        ],

        "🔢 OTP Safety": [
            "Never share an OTP with anyone.",
            "Read the message carefully before entering an OTP.",
            "Do not tell OTPs over phone calls.",
            "Never share banking OTPs.",
            "Contact your bank immediately if you shared an OTP accidentally."
        ],

        "💳 UPI Fraud": [
            "Never enter your UPI PIN to receive money.",
            "Check receiver name before paying.",
            "Do not approve unknown payment requests.",
            "Do not scan unknown QR codes.",
            "Never share your UPI PIN."
        ],

        "🔗 Suspicious Links": [
            "Do not click unknown links.",
            "Check the website address carefully.",
            "Be careful with prize or reward messages.",
            "Never enter banking information on unknown websites.",
            "Verify through the official website if unsure."
        ],

        "💬 WhatsApp Safety": [
            "Do not share personal information with unknown people.",
            "Enable two-step verification.",
            "Check privacy settings.",
            "Block and report suspicious contacts.",
            "Do not forward unverified information."
        ],

        "👤 Fake Social Media Account": [
            "Do not communicate with the fake account.",
            "Take screenshots as evidence.",
            "Block the account.",
            "Report the account.",
            "Tell a trusted person if the problem continues."
        ],

        "📍 Location Privacy": [
            "Avoid publicly sharing live location.",
            "Check location permissions.",
            "Turn off unnecessary location access.",
            "Avoid posting your exact location in real time.",
            "Share location only with trusted people."
        ],

        "😟 Cyberbullying": [
            "Do not respond to abusive messages.",
            "Save screenshots and evidence.",
            "Block the person.",
            "Report the account or content.",
            "Tell a trusted person and seek help."
        ]
    }

    selected_safety = st.selectbox(
        "Choose a safety topic",
        list(safety_topics.keys())
    )

    st.markdown(
        '<div class="learning-box">'
        f'<h3>{selected_safety}</h3>',
        unsafe_allow_html=True
    )

    for i, step in enumerate(
        safety_topics[selected_safety],
        start=1
    ):

        st.markdown(
            f"""
            <div class="step">
                <b>Step {i}</b><br>
                {step}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


# ============================================================
# SAFETY QUIZ
# ============================================================

elif page == "📝 Safety Quiz":

    st.markdown(
        '<div class="section-title">📝 Digital Safety Quiz</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Select a participant and answer eight questions one at a time.'
        '</div>',
        unsafe_allow_html=True
    )

    if len(participants) == 0:

        st.warning(
            "Please add a participant before starting the quiz."
        )

    else:

        participant_options = {
            f"{p.get('name', 'Unknown')} - ID {p.get('participant_id')}":
            p.get("participant_id")
            for p in participants
        }

        # ====================================================
        # QUIZ START
        # ====================================================

        if not st.session_state.quiz_started:

            selected_participant = st.selectbox(
                "👩 Select Participant",
                list(participant_options.keys()),
                key="quiz_participant"
            )

            st.markdown("""
            <div class="info-card">

                <h3>📝 Quiz Instructions</h3>

                <p>• Total Questions: 8</p>
                <p>• One question will appear at a time.</p>
                <p>• Select one answer for each question.</p>
                <p>• Your result will be connected to the participant.</p>
                <p>• Score and answers will be saved in the database.</p>

            </div>
            """, unsafe_allow_html=True)

            if st.button(
                "▶ Start Quiz",
                type="primary",
                use_container_width=True
            ):

                st.session_state.quiz_participant_id = int(
                    participant_options[selected_participant]
                )

                st.session_state.quiz_participant_name = (
                    selected_participant.split(" - ID")[0]
                )

                st.session_state.quiz_started = True
                st.session_state.quiz_current = 0
                st.session_state.quiz_answers = {}
                st.session_state.quiz_finished = False
                st.session_state.quiz_score = 0

                st.rerun()

        # ====================================================
        # QUIZ QUESTIONS
        # ====================================================

        elif (
            st.session_state.quiz_started
            and
            not st.session_state.quiz_finished
        ):

            current = st.session_state.quiz_current

            question = quiz_questions[current]

            st.progress(
                (current + 1) / len(quiz_questions)
            )

            st.markdown(
                f"""
                <div class="quiz-question">

                    <div class="quiz-number">
                        QUESTION {current + 1}
                        OF {len(quiz_questions)}
                    </div>

                    <div class="quiz-text">
                        {question["question"]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            old_answer = st.session_state.quiz_answers.get(
                current
            )

            if old_answer in question["options"]:
                old_index = question["options"].index(
                    old_answer
                )
            else:
                old_index = None

            selected_answer = st.radio(
                "Select your answer:",
                question["options"],
                index=old_index,
                key=f"answer_{current}"
            )

            col1, col2 = st.columns(2)

            # =================================================
            # PREVIOUS
            # =================================================

            with col1:

                if current > 0:

                    if st.button(
                        "← Previous",
                        use_container_width=True
                    ):

                        if selected_answer:
                            st.session_state.quiz_answers[
                                current
                            ] = selected_answer

                        st.session_state.quiz_current -= 1

                        st.rerun()

            # =================================================
            # NEXT
            # =================================================

            with col2:

                if current < len(quiz_questions) - 1:

                    if st.button(
                        "Next →",
                        type="primary",
                        use_container_width=True
                    ):

                        if selected_answer is None:

                            st.warning(
                                "Please select an answer."
                            )

                        else:

                            st.session_state.quiz_answers[
                                current
                            ] = selected_answer

                            st.session_state.quiz_current += 1

                            st.rerun()

                # =============================================
                # SUBMIT
                # =============================================

                else:

                    if st.button(
                        "✓ Submit Quiz",
                        type="primary",
                        use_container_width=True
                    ):

                        if selected_answer is None:

                            st.warning(
                                "Please select an answer."
                            )

                        else:

                            # Save last answer
                            st.session_state.quiz_answers[
                                current
                            ] = selected_answer

                            # Calculate score
                            score = 0

                            for i, q in enumerate(
                                quiz_questions
                            ):

                                user_answer = (
                                    st.session_state
                                    .quiz_answers
                                    .get(i)
                                )

                                if user_answer == q["answer"]:
                                    score += 1

                            # Create JSON data
                            answer_data = {}

                            for i, q in enumerate(
                                quiz_questions
                            ):

                                answer_data[str(i + 1)] = {
                                    "question":
                                        q["question"],

                                    "selected_answer":
                                        st.session_state
                                        .quiz_answers
                                        .get(i),

                                    "correct_answer":
                                        q["answer"]
                                }

                            # =================================
                            # DATABASE DATA
                            # =================================

                            quiz_data = {
                                "participant_id":
                                    int(
                                        st.session_state
                                        .quiz_participant_id
                                    ),

                                "score":
                                    int(score),

                                "total_questions":
                                    int(len(quiz_questions)),

                                "answers":
                                    answer_data,

                                "completed_at":
                                    datetime.now().isoformat()
                            }

                            # =================================
                            # SAVE RESULT
                            # =================================

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

                                st.code(str(e))

                                st.info(
                                    "Check the quiz_results table "
                                    "and Supabase RLS policies."
                                )

        # ====================================================
        # RESULT
        # ====================================================

        else:

            score = st.session_state.quiz_score

            total = len(quiz_questions)

            percentage = (
                score / total
            ) * 100

            st.markdown(
                f"""
                <div class="learning-box"
                     style="text-align:center;">

                    <h3>🎉 Quiz Completed!</h3>

                    <p>
                        Participant:
                        <b>
                            {st.session_state.quiz_participant_name}
                        </b>
                    </p>

                    <div style="
                        font-size:45px;
                        font-weight:800;
                        color:#9b3565;
                    ">
                        {score}/{total}
                    </div>

                    <p style="font-size:18px;">
                        Score: <b>{percentage:.0f}%</b>
                    </p>

                </div>
                """,
                unsafe_allow_html=True
            )

            if percentage >= 80:

                st.success(
                    "Excellent! You have a strong understanding of digital safety."
                )

            elif percentage >= 50:

                st.info(
                    "Good effort! Review the safety topics and try again."
                )

            else:

                st.warning(
                    "Keep learning! Review the Smartphone Guide and Women Safety sections."
                )

            if st.button(
                "🔄 Take Quiz Again",
                use_container_width=True
            ):

                st.session_state.quiz_started = False
                st.session_state.quiz_current = 0
                st.session_state.quiz_answers = {}
                st.session_state.quiz_participant_id = None
                st.session_state.quiz_participant_name = ""
                st.session_state.quiz_finished = False
                st.session_state.quiz_score = 0

                st.rerun()


# ============================================================
# SAFETY EVENTS
# ============================================================

elif page == "🚨 Safety Events":

    st.markdown(
        '<div class="section-title">🚨 Safety Events</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Record online safety incidents reported by participants.'
        '</div>',
        unsafe_allow_html=True
    )

    if len(participants) == 0:

        st.warning(
            "Please add participants first."
        )

    else:

        participant_options = {
            f"{p.get('name', 'Unknown')} - ID {p.get('participant_id')}":
            p.get("participant_id")
            for p in participants
        }

        with st.form("safety_event_form"):

            selected = st.selectbox(
                "Participant",
                list(participant_options.keys())
            )

            event_type = st.selectbox(
                "Safety Event Type",
                [
                    "OTP Scam",
                    "UPI Fraud",
                    "Suspicious Link",
                    "Fake Account",
                    "Cyberbullying",
                    "Harassment",
                    "Privacy Issue",
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
                "Reported to Authority?",
                ["Yes", "No"]
            )

            submit = st.form_submit_button(
                "Save Safety Event",
                use_container_width=True
            )

            if submit:

                data = {
                    "participant_id":
                        participant_options[selected],

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

                result = add_record(
                    "safety_events",
                    data
                )

                if result is not None:

                    st.success(
                        "Safety event saved successfully."
                    )

                    st.rerun()

    st.markdown("### Safety Event Records")

    if len(safety_df) > 0:

        st.dataframe(
            safety_df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No safety events recorded."
        )


# ============================================================
# HELP & EMERGENCY
# ============================================================

elif page == "☎️ Help & Emergency":

    st.markdown(
        '<div class="section-title">☎️ Help & Emergency</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Important emergency and cyber safety contacts.'
        '</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown("""
        <div class="emergency-card">

            <h3>🚨 Emergency</h3>

            <div class="emergency-number">
                112
            </div>

            <p>
                National emergency number.
            </p>

        </div>
        """, unsafe_allow_html=True)

    with c2:

        st.markdown("""
        <div class="emergency-card">

            <h3>👩 Women Helpline</h3>

            <div class="emergency-number">
                181
            </div>

            <p>
                Women helpline for support and assistance.
            </p>

        </div>
        """, unsafe_allow_html=True)

    with c3:

        st.markdown("""
        <div class="emergency-card">

            <h3>💻 Cyber Crime</h3>

            <div class="emergency-number">
                1930
            </div>

            <p>
                Cyber crime helpline for online financial fraud.
            </p>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("### What to do during online fraud?")

    steps = [
        "Stay calm and do not share additional OTPs, passwords or PINs.",
        "Contact your bank through its official channel.",
        "Report cyber financial fraud as quickly as possible.",
        "Save screenshots, transaction details and messages.",
        "Inform a trusted person."
    ]

    for i, step in enumerate(steps, 1):

        st.markdown(
            f"""
            <div class="step">
                <b>Step {i}</b><br>
                {step}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.warning(
        "Never share your OTP, UPI PIN, password or banking credentials."
    )


# ============================================================
# TRAINING SESSIONS
# ============================================================

elif page == "🎓 Training Sessions":

    st.markdown(
        '<div class="section-title">🎓 Training Sessions</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Record digital literacy and online safety training activities.'
        '</div>',
        unsafe_allow_html=True
    )

    with st.form("training_form"):

        session_date = st.date_input(
            "Session Date",
            value=date.today()
        )

        topic = st.selectbox(
            "Training Topic",
            [
                "Basic Smartphone Usage",
                "WhatsApp Safety",
                "UPI & Digital Payments",
                "Password Safety",
                "Online Fraud Awareness",
                "Social Media Safety",
                "Cyberbullying Awareness"
            ]
        )

        trainer_name = st.text_input(
            "Trainer Name"
        )

        participants_count = st.number_input(
            "Number of Participants",
            min_value=1,
            value=10
        )

        notes = st.text_area(
            "Notes"
        )

        submit = st.form_submit_button(
            "Save Training Session",
            use_container_width=True
        )

        if submit:

            data = {
                "session_date": str(session_date),
                "topic": topic,
                "trainer_name": trainer_name,
                "participants_count": participants_count,
                "notes": notes
            }

            result = add_record(
                "training_sessions",
                data
            )

            if result is not None:

                st.success(
                    "Training session saved successfully."
                )

                st.rerun()

    st.markdown("### Training Records")

    if len(training_df) > 0:

        st.dataframe(
            training_df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No training sessions recorded."
        )


# ============================================================
# REPORTS
# ============================================================

elif page == "📊 Reports":

    st.markdown(
        '<div class="section-title">📊 Reports & Analysis</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Analyse participant activity, safety awareness and quiz performance.'
        '</div>',
        unsafe_allow_html=True
    )

    # ========================================================
    # SAFETY REPORT
    # ========================================================

    st.markdown("### 🛡️ Safety Events")

    if (
        len(safety_df) > 0
        and
        "event_type" in safety_df.columns
    ):

        event_count = (
            safety_df["event_type"]
            .value_counts()
            .reset_index()
        )

        event_count.columns = [
            "Event Type",
            "Count"
        ]

        fig = px.pie(
            event_count,
            names="Event Type",
            values="Count",
            title="Safety Event Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.info(
            "No safety event data available."
        )

    # ========================================================
    # SMARTPHONE REPORT
    # ========================================================

    st.markdown("### 📱 Smartphone Usage")

    if (
        len(smartphone_df) > 0
        and
        "usage_purpose" in smartphone_df.columns
    ):

        purpose_count = (
            smartphone_df["usage_purpose"]
            .value_counts()
            .reset_index()
        )

        purpose_count.columns = [
            "Purpose",
            "Count"
        ]

        fig = px.bar(
            purpose_count,
            x="Purpose",
            y="Count",
            title="Main Smartphone Usage Purpose"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.info(
            "No smartphone usage data available."
        )

    # ========================================================
    # QUIZ REPORT
    # ========================================================

    st.markdown("### 📝 Quiz Performance")

    if len(quiz_df) > 0:

        if (
            "score" in quiz_df.columns
            and
            "total_questions" in quiz_df.columns
        ):

            quiz_report = quiz_df.copy()

            quiz_report["percentage"] = (
                quiz_report["score"].astype(float)
                /
                quiz_report["total_questions"].astype(float)
            ) * 100

            # -----------------------------------------------
            # PARTICIPANT NAME
            # -----------------------------------------------

            if "participant_id" in quiz_report.columns:

                participant_names = {
                    p.get("participant_id"):
                    p.get("name", "Unknown")
                    for p in participants
                }

                quiz_report["Participant Name"] = (
                    quiz_report["participant_id"]
                    .map(participant_names)
                    .fillna("Unknown")
                )

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric(
                    "Quiz Attempts",
                    len(quiz_report)
                )

            with c2:
                st.metric(
                    "Average Score",
                    f"{quiz_report['percentage'].mean():.1f}%"
                )

            with c3:
                st.metric(
                    "Highest Score",
                    f"{quiz_report['percentage'].max():.1f}%"
                )

            # -----------------------------------------------
            # QUIZ CHART
            # -----------------------------------------------

            fig = px.bar(
                quiz_report,
                x=quiz_report.index,
                y="percentage",
                title="Quiz Attempt Scores"
            )

            fig.update_xaxes(
                title="Attempt"
            )

            fig.update_yaxes(
                title="Score (%)"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            # -----------------------------------------------
            # TABLE
            # -----------------------------------------------

            display_columns = []

            for col in [
                "quiz_id",
                "Participant Name",
                "participant_id",
                "score",
                "total_questions",
                "percentage",
                "completed_at"
            ]:

                if col in quiz_report.columns:
                    display_columns.append(col)

            if display_columns:

                st.dataframe(
                    quiz_report[display_columns],
                    use_container_width=True,
                    hide_index=True
                )

    else:

        st.info(
            "No quiz attempts available yet."
        )

    # ========================================================
    # TRAINING REPORT
    # ========================================================

    st.markdown("### 🎓 Training Sessions")

    if len(training_df) > 0:

        st.metric(
            "Total Training Sessions",
            len(training_df)
        )

        if "topic" in training_df.columns:

            topic_count = (
                training_df["topic"]
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
                title="Training Topics"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    else:

        st.info(
            "No training data available."
        )

    # ========================================================
    # DOWNLOAD
    # ========================================================

    st.markdown("### 📥 Export Data")

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        if len(participants_df) > 0:

            st.download_button(
                "Download Participants",
                participants_df.to_csv(index=False),
                "participants.csv",
                "text/csv",
                use_container_width=True
            )

    with c2:

        if len(smartphone_df) > 0:

            st.download_button(
                "Download Smartphone",
                smartphone_df.to_csv(index=False),
                "smartphone_usage.csv",
                "text/csv",
                use_container_width=True
            )

    with c3:

        if len(safety_df) > 0:

            st.download_button(
                "Download Safety",
                safety_df.to_csv(index=False),
                "safety_events.csv",
                "text/csv",
                use_container_width=True
            )

    with c4:

        if len(quiz_df) > 0:

            st.download_button(
                "Download Quiz",
                quiz_df.to_csv(index=False),
                "quiz_results.csv",
                "text/csv",
                use_container_width=True
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown("""
<div style="
    text-align:center;
    color:#888;
    font-size:13px;
    padding:10px;
">

    🛡️ <b>Women Digital Safety & Awareness System</b>
    <br>
    Smartphone Usage & Online Safety for Women Self Help Groups
    <br>
    Community Engagement Project

</div>
""", unsafe_allow_html=True)
