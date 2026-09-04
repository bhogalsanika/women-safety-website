import streamlit as st
from supabase import create_client, Client
import pandas as pd
import plotly.express as px
from datetime import date, datetime


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Women Digital Safety & Awareness System",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background: #f5f7fb;
}

.main .block-container {
    padding-top: 1.2rem;
    padding-bottom: 2rem;
    max-width: 1400px;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 1px solid #e5e7eb;
}

section[data-testid="stSidebar"] .block-container {
    padding-top: 1rem;
}

.logo-box {
    text-align: center;
    padding: 15px 5px 20px 5px;
    border-bottom: 1px solid #eeeeee;
    margin-bottom: 15px;
}

.logo-icon {
    font-size: 35px;
    margin-bottom: 5px;
}

.logo-title {
    font-size: 20px;
    font-weight: 800;
    color: #7c2850;
    line-height: 1.25;
}

.logo-subtitle {
    font-size: 11px;
    color: #777777;
    line-height: 1.5;
    margin-top: 7px;
}

/* HERO */

.hero {
    background: linear-gradient(
        135deg,
        #fff0f6 0%,
        #f4f6ff 100%
    );
    padding: 30px;
    border-radius: 18px;
    border: 1px solid #efdce6;
    margin-bottom: 25px;
}

.hero h1 {
    color: #7c2850;
    font-size: 31px;
    font-weight: 800;
    margin: 0 0 7px 0;
}

.hero p {
    color: #5f6570;
    font-size: 15px;
    margin: 0;
}

/* SECTION */

.section-title {
    font-size: 26px;
    font-weight: 800;
    color: #242936;
    margin-top: 8px;
    margin-bottom: 4px;
}

.section-subtitle {
    color: #6b7280;
    font-size: 14px;
    margin-bottom: 20px;
}

/* CARDS */

.info-card {
    background: #ffffff;
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #e6e8ef;
    box-shadow: 0 3px 12px rgba(0,0,0,0.035);
    min-height: 145px;
}

.info-card h3 {
    margin-top: 0;
    color: #7c2850;
    font-size: 18px;
}

.info-card p {
    color: #626875;
    font-size: 14px;
    line-height: 1.6;
}

/* LEARNING */

.learning-box {
    background: #ffffff;
    border-left: 5px solid #9b3565;
    padding: 23px;
    border-radius: 13px;
    margin-top: 18px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.04);
}

.learning-box h3 {
    color: #7c2850;
    margin-top: 0;
}

.step {
    background: #faf7f9;
    padding: 14px 17px;
    border-radius: 9px;
    margin: 9px 0;
    border: 1px solid #eee1e8;
    color: #444b57;
}

.step b {
    color: #7c2850;
}

/* EMERGENCY */

.emergency-card {
    background: #ffffff;
    border: 1px solid #e7e2e6;
    border-radius: 15px;
    padding: 22px;
    margin-bottom: 15px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.035);
}

.emergency-card h3 {
    color: #333944;
}

.emergency-number {
    font-size: 31px;
    font-weight: 800;
    color: #9b3565;
}

/* QUIZ */

.quiz-question {
    background: #ffffff;
    border-radius: 16px;
    padding: 27px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 4px 14px rgba(0,0,0,0.04);
    margin: 20px 0;
}

.quiz-number {
    color: #9b3565;
    font-weight: 800;
    font-size: 13px;
    letter-spacing: 0.5px;
}

.quiz-text {
    font-size: 21px;
    font-weight: 750;
    color: #282d38;
    margin-top: 10px;
}

/* BUTTONS */

.stButton > button {
    border-radius: 9px;
    border: 1px solid #d9dce5;
    font-weight: 650;
    min-height: 42px;
}

/* METRICS */

[data-testid="stMetric"] {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    padding: 17px;
    border-radius: 14px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.025);
}

/* TABLE */

[data-testid="stDataFrame"] {
    border-radius: 12px;
}

/* FORM */

[data-testid="stForm"] {
    background: #ffffff;
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #e5e7eb;
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

    supabase: Client = init_connection()

except Exception:

    st.error("Supabase connection failed.")

    st.info(
        "Please check SUPABASE_URL and SUPABASE_KEY "
        "in Streamlit Secrets."
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

        return response.data

    except Exception as e:

        st.error(
            f"Database error: {e}"
        )

        return None


def delete_record(table_name, column, value):

    try:

        supabase \
            .table(table_name) \
            .delete() \
            .eq(column, value) \
            .execute()

        return True

    except Exception as e:

        st.error(
            f"Delete error: {e}"
        )

        return False


# ============================================================
# LOAD DATABASE TABLES
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
    <div class="logo-box">

        <div class="logo-icon">🛡️</div>

        <div class="logo-title">
            Women Digital Safety<br>
            & Awareness System
        </div>

        <div class="logo-subtitle">
            Smartphone Usage & Online Safety<br>
            for Women Self Help Groups
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Navigation")

    page = st.radio(
        "Go to",
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

    st.caption("Women Digital Safety & Awareness System")
    st.caption("Community Engagement Project")
    st.caption("Smartphone & Online Safety")


# ============================================================
# HERO HEADER
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

        "options": [
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

        "options": [
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

        "options": [
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

        "options": [
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
        ["Yes", "No"],

        "answer":
        "No"
    },

    {
        "question":
        "What is safer when using social media?",

        "options": [
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

        "options": [
            "Click its link",
            "Verify through the official bank channel",
            "Share your OTP"
        ],

        "answer":
        "Verify through the official bank channel"
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
        'Overview of community participation, smartphone learning '
        'and digital safety activities.'
        '</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "👩 Participants",
            len(participants_df)
        )

    with c2:
        st.metric(
            "📱 Smartphone Records",
            len(smartphone_df)
        )

    with c3:
        st.metric(
            "🛡️ Safety Events",
            len(safety_df)
        )

    with c4:
        st.metric(
            "📝 Quiz Attempts",
            len(quiz_df)
        )

    st.markdown("### Quick Learning")

    q1, q2, q3 = st.columns(3)

    with q1:

        st.markdown("""
        <div class="info-card">

            <h3>📱 Smartphone Learning</h3>

            <p>
                Learn practical smartphone activities such as
                making calls, saving contacts, WhatsApp,
                photography, Google search and UPI payments.
            </p>

        </div>
        """, unsafe_allow_html=True)

    with q2:

        st.markdown("""
        <div class="info-card">

            <h3>🛡️ Online Safety</h3>

            <p>
                Learn practical ways to protect passwords,
                OTPs, UPI payments, social media accounts,
                privacy and personal information.
            </p>

        </div>
        """, unsafe_allow_html=True)

    with q3:

        st.markdown("""
        <div class="info-card">

            <h3>📝 Safety Quiz</h3>

            <p>
                Test your digital safety knowledge through
                an interactive quiz and save the result
                against the selected participant.
            </p>

        </div>
        """, unsafe_allow_html=True)

    if len(safety_df) > 0:

        if "event_type" in safety_df.columns:

            st.markdown("### Safety Events Overview")

            event_count = (
                safety_df["event_type"]
                .value_counts()
                .reset_index()
            )

            event_count.columns = [
                "Event Type",
                "Count"
            ]

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

            col1, col2 = st.columns(2)

            with col1:

                name = st.text_input(
                    "Full Name"
                )

                age = st.number_input(
                    "Age",
                    min_value=18,
                    max_value=100,
                    value=30
                )

                contact = st.text_input(
                    "Contact Number"
                )

            with col2:

                occupation = st.text_input(
                    "Occupation"
                )

                smartphone_user = st.selectbox(
                    "Uses Smartphone?",
                    ["Yes", "No"]
                )

            submitted = st.form_submit_button(
                "Add Participant",
                use_container_width=True
            )

            if submitted:

                if name.strip() == "":

                    st.warning(
                        "Please enter participant name."
                    )

                else:

                    data = {

                        "name":
                            name.strip(),

                        "age":
                            age,

                        "contact":
                            contact.strip(),

                        "occupation":
                            occupation.strip(),

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

    st.markdown("### Participant Records")

    if len(participants_df) > 0:

        st.dataframe(
            participants_df,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("### Delete Participant")

        participant_options = {

            f"{row.get('name', 'Unknown')} — "
            f"ID {row.get('participant_id')}":
            row.get("participant_id")

            for row in participants
        }

        if participant_options:

            selected_delete = st.selectbox(
                "Select participant",
                list(participant_options.keys()),
                key="delete_participant"
            )

            if st.button(
                "Delete Selected Participant",
                use_container_width=True
            ):

                pid = participant_options[
                    selected_delete
                ]

                if delete_record(
                    "participants",
                    "participant_id",
                    pid
                ):

                    st.success(
                        "Participant deleted."
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
        'Record how participants use smartphones for daily activities.'
        '</div>',
        unsafe_allow_html=True
    )

    if len(participants) == 0:

        st.warning(
            "Please add participants first."
        )

    else:

        participant_options = {

            f"{p.get('name', 'Unknown')} — "
            f"ID {p.get('participant_id')}":
            p.get("participant_id")

            for p in participants
        }

        with st.form("smartphone_usage_form"):

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

            submitted = st.form_submit_button(
                "Save Smartphone Usage",
                use_container_width=True
            )

            if submitted:

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

                if add_record(
                    "smartphone_usage",
                    data
                ):

                    st.success(
                        "Smartphone usage record saved."
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
        'Choose one topic and learn it step-by-step.'
        '</div>',
        unsafe_allow_html=True
    )

    smartphone_topics = {

        "📞 Make a Call": {

            "title":
                "How to Make a Call",

            "steps": [

                "Open the Phone app.",

                "Tap the keypad icon.",

                "Enter the person's mobile number.",

                "Press the green Call button.",

                "To end the call, press the red End Call button."
            ]
        },

        "👤 Save a Contact": {

            "title":
                "How to Save a Contact",

            "steps": [

                "Open the Contacts app.",

                "Tap Add Contact (+).",

                "Enter the person's name.",

                "Enter their mobile number.",

                "Tap Save."
            ]
        },

        "💬 Send a WhatsApp Message": {

            "title":
                "How to Send a WhatsApp Message",

            "steps": [

                "Open WhatsApp.",

                "Tap the chat of the person.",

                "Type your message in the message box.",

                "Press the Send button.",

                "Wait for the message to be delivered."
            ]
        },

        "📷 Take a Photo": {

            "title":
                "How to Take a Photo",

            "steps": [

                "Open the Camera app.",

                "Point the camera towards the object or person.",

                "Keep the phone steady.",

                "Tap the camera button.",

                "Open Gallery to view the photo."
            ]
        },

        "🌐 Search on Google": {

            "title":
                "How to Search on Google",

            "steps": [

                "Open Chrome or another browser.",

                "Tap the search bar.",

                "Type what you want to know.",

                "Tap Search.",

                "Read information from trusted websites."
            ]
        },

        "💳 Use UPI Payment": {

            "title":
                "How to Make a UPI Payment",

            "steps": [

                "Open your trusted UPI application.",

                "Select Send Money or Scan & Pay.",

                "Enter the receiver details or scan the QR code.",

                "Check the receiver name and amount carefully.",

                "Enter your UPI PIN only when you are sure about the payment."
            ]
        },

        "📍 Share Location": {

            "title":
                "How to Share Your Location",

            "steps": [

                "Open WhatsApp or your messaging application.",

                "Open the trusted person's chat.",

                "Tap the attachment option.",

                "Select Location.",

                "Choose whether to send your current or live location."
            ]
        }
    }

    selected_topic = st.selectbox(
        "What do you want to learn?",
        list(smartphone_topics.keys()),
        key="smartphone_topic"
    )

    topic = smartphone_topics[
        selected_topic
    ]

    st.markdown(
        f"""
        <div class="learning-box">

            <h3>{topic["title"]}</h3>

            <p>
                Follow these simple steps:
            </p>
        """,
        unsafe_allow_html=True
    )

    for i, step in enumerate(
        topic["steps"],
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
        "💡 Tip: Practice one smartphone task at a time "
        "until you feel comfortable."
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

        "🔐 Password Safety": {

            "title":
                "How to Keep Your Password Safe",

            "steps": [

                "Create a strong and unique password.",

                "Do not use your name, birthday or mobile number.",

                "Never share your password with anyone.",

                "Use two-factor authentication when available.",

                "Change your password if you think someone knows it."
            ]
        },

        "🔢 OTP Scam": {

            "title":
                "How to Stay Safe from OTP Scams",

            "steps": [

                "Never share an OTP with another person.",

                "Banks and genuine services do not normally ask you to tell them your OTP.",

                "Read the SMS carefully before entering an OTP.",

                "Do not tell anyone an OTP received on your phone.",

                "If you shared an OTP by mistake, contact your bank/service immediately."
            ]
        },

        "💳 UPI Fraud": {

            "title":
                "How to Stay Safe from UPI Fraud",

            "steps": [

                "Never enter your UPI PIN to receive money.",

                "Check the receiver's name before paying.",

                "Do not approve unknown collect requests.",

                "Do not scan unknown QR codes.",

                "Never share your UPI PIN with anyone."
            ]
        },

        "🔗 Suspicious Links": {

            "title":
                "How to Identify Suspicious Links",

            "steps": [

                "Do not click unknown links received through SMS or WhatsApp.",

                "Check the website address carefully.",

                "Be careful with messages saying you have won a prize.",

                "Never enter banking details on unknown websites.",

                "When unsure, close the message and verify through the official website."
            ]
        },

        "💬 WhatsApp Safety": {

            "title":
                "How to Stay Safe on WhatsApp",

            "steps": [

                "Do not share personal information with unknown people.",

                "Enable WhatsApp two-step verification.",

                "Check your privacy settings.",

                "Block and report suspicious contacts.",

                "Do not forward unverified information."
            ]
        },

        "👤 Fake Social Media Account": {

            "title":
                "What to Do About a Fake Account",

            "steps": [

                "Do not communicate with the fake account.",

                "Take screenshots as evidence.",

                "Block the account.",

                "Report the account to the platform.",

                "Tell a trusted person if the situation continues."
            ]
        },

        "📍 Location Privacy": {

            "title":
                "How to Protect Location Privacy",

            "steps": [

                "Avoid publicly sharing your live location.",

                "Check location permissions of apps.",

                "Turn off location access for apps that do not need it.",

                "Avoid posting your exact location in real time.",

                "Share your location only with trusted people when necessary."
            ]
        },

        "😟 Cyberbullying": {

            "title":
                "How to Handle Cyberbullying",

            "steps": [

                "Do not respond to abusive messages.",

                "Take screenshots and save evidence.",

                "Block the person.",

                "Report the account or content.",

                "Tell a trusted person and seek appropriate help."
            ]
        }
    }

    selected_safety = st.selectbox(
        "Which safety topic do you want to learn?",
        list(safety_topics.keys()),
        key="safety_topic"
    )

    topic = safety_topics[
        selected_safety
    ]

    st.markdown(
        f"""
        <div class="learning-box">

            <h3>{topic["title"]}</h3>

            <p>
                Follow these safety steps:
            </p>
        """,
        unsafe_allow_html=True
    )

    for i, step in enumerate(
        topic["steps"],
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
        'Select a participant and answer the questions one at a time.'
        '</div>',
        unsafe_allow_html=True
    )

    if len(participants) == 0:

        st.warning(
            "Please add at least one participant "
            "before starting the quiz."
        )

    else:

        participant_options = {

            f"{p.get('name', 'Unknown')} — "
            f"ID {p.get('participant_id')}":
            p.get("participant_id")

            for p in participants
        }

        # ----------------------------------------------------
        # START SCREEN
        # ----------------------------------------------------

        if not st.session_state.quiz_started:

            selected = st.selectbox(
                "👩 Select Participant",
                list(participant_options.keys()),
                key="quiz_participant_select"
            )

            st.markdown("""
            <div class="info-card">

                <h3>📝 Quiz Instructions</h3>

                <p>• Total questions: 8</p>
                <p>• One question appears at a time.</p>
                <p>• Select one answer and click Next.</p>
                <p>• The participant ID is stored with the result.</p>
                <p>• Final score and answers are stored in Supabase.</p>

            </div>
            """, unsafe_allow_html=True)

            if st.button(
                "▶ Start Quiz",
                type="primary",
                use_container_width=True,
                key="start_quiz"
            ):

                selected_id = participant_options[
                    selected
                ]

                selected_name = selected.split(
                    " — ID"
                )[0]

                st.session_state.quiz_participant_id = int(
                    selected_id
                )

                st.session_state.quiz_participant_name = (
                    selected_name
                )

                st.session_state.quiz_started = True
                st.session_state.quiz_current = 0
                st.session_state.quiz_answers = {}
                st.session_state.quiz_finished = False
                st.session_state.quiz_score = 0

                st.rerun()

        # ----------------------------------------------------
        # QUESTIONS
        # ----------------------------------------------------

        elif (
            st.session_state.quiz_started
            and
            not st.session_state.quiz_finished
        ):

            current = (
                st.session_state.quiz_current
            )

            question = quiz_questions[
                current
            ]

            st.progress(
                (current + 1) /
                len(quiz_questions)
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

            previous_answer = (
                st.session_state
                .quiz_answers
                .get(current)
            )

            selected_answer = st.radio(
                "Select your answer:",
                question["options"],
                index=(
                    question["options"].index(
                        previous_answer
                    )
                    if previous_answer in question["options"]
                    else None
                ),
                key=f"quiz_answer_{current}"
            )

            col1, col2 = st.columns(2)

            # ------------------------------------------------
            # PREVIOUS
            # ------------------------------------------------

            with col1:

                if current > 0:

                    if st.button(
                        "← Previous",
                        use_container_width=True,
                        key=f"previous_{current}"
                    ):

                        if selected_answer:

                            st.session_state.quiz_answers[
                                current
                            ] = selected_answer

                        st.session_state.quiz_current -= 1

                        st.rerun()

            # ------------------------------------------------
            # NEXT / SUBMIT
            # ------------------------------------------------

            with col2:

                if current < len(
                    quiz_questions
                ) - 1:

                    if st.button(
                        "Next →",
                        type="primary",
                        use_container_width=True,
                        key=f"next_{current}"
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

                else:

                    if st.button(
                        "✓ Submit Quiz",
                        type="primary",
                        use_container_width=True,
                        key="submit_quiz"
                    ):

                        if selected_answer is None:

                            st.warning(
                                "Please select an answer."
                            )

                        else:

                            # SAVE LAST ANSWER
                            st.session_state.quiz_answers[
                                current
                            ] = selected_answer

                            # CALCULATE SCORE
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

                            # CREATE JSON
                            answer_data = {}

                            for i, q in enumerate(
                                quiz_questions
                            ):

                                answer_data[
                                    str(i + 1)
                                ] = {

                                    "question":
                                        q["question"],

                                    "selected_answer":
                                        st.session_state
                                        .quiz_answers
                                        .get(i),

                                    "correct_answer":
                                        q["answer"]
                                }

                            # DATABASE RECORD
                            quiz_data = {

                                "participant_id":
                                    int(
                                        st.session_state
                                        .quiz_participant_id
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

                            # SAVE TO SUPABASE
                            try:

                                response = (
                                    supabase
                                    .table(
                                        "quiz_results"
                                    )
                                    .insert(
                                        quiz_data
                                    )
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
                                        "Quiz was completed, "
                                        "but no database record was returned."
                                    )

                            except Exception as e:

                                st.error(
                                    "❌ Quiz result could not be saved."
                                )

                                st.code(
                                    str(e)
                                )

                                st.info(
                                    "Please check quiz_results table, "
                                    "participant_id type and Supabase RLS policies."
                                )

        # ----------------------------------------------------
        # RESULT SCREEN
        # ----------------------------------------------------

        else:

            score = (
                st.session_state.quiz_score
            )

            total = len(
                quiz_questions
            )

            percentage = (
                score / total
            ) * 100

            participant_name = (
                st.session_state
                .quiz_participant_name
            )

            st.markdown(
                f"""
                <div class="learning-box"
                     style="text-align:center;">

                    <h3>🎉 Quiz Completed!</h3>

                    <p>
                        Participant:
                        <b>{participant_name}</b>
                    </p>

                    <div style="
                        font-size:45px;
                        font-weight:800;
                        color:#9b3565;
                    ">
                        {score}/{total}
                    </div>

                    <p style="font-size:18px;">
                        Score:
                        <b>{percentage:.0f}%</b>
                    </p>

                </div>
                """,
                unsafe_allow_html=True
            )

            if percentage >= 80:

                st.success(
                    "Excellent! You have a strong understanding "
                    "of digital safety."
                )

            elif percentage >= 50:

                st.info(
                    "Good effort! Review the safety topics "
                    "and try again."
                )

            else:

                st.warning(
                    "Keep learning! Review the Smartphone Guide "
                    "and Women Safety sections."
                )

            if st.button(
                "🔄 Take Quiz Again",
                use_container_width=True,
                key="take_quiz_again"
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
        'Record and monitor online safety incidents reported by participants.'
        '</div>',
        unsafe_allow_html=True
    )

    if len(participants) == 0:

        st.warning(
            "Please add participants first."
        )

    else:

        participant_options = {

            f"{p.get('name', 'Unknown')} — "
            f"ID {p.get('participant_id')}":
            p.get("participant_id")

            for p in participants
        }

        with st.form(
            "safety_event_form"
        ):

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

            submitted = st.form_submit_button(
                "Save Safety Event",
                use_container_width=True
            )

            if submitted:

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

                if add_record(
                    "safety_events",
                    data
                ):

                    st.success(
                        "Safety event recorded successfully."
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
                National emergency number for immediate assistance.
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
                Cyber crime helpline for online financial/cyber fraud.
            </p>

        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        "### What should you do during an online fraud?"
    )

    steps = [

        "Stay calm and do not share additional OTPs, passwords or PINs.",

        "Contact your bank or service provider through its official channel.",

        "For cyber financial fraud, report quickly through the appropriate cybercrime channel.",

        "Save screenshots, transaction details and messages as evidence.",

        "Inform a trusted family member or support person."
    ]

    for i, step in enumerate(
        steps,
        1
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

    st.warning(
        "Never share your OTP, UPI PIN, password "
        "or banking credentials with anyone."
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

    with st.form(
        "training_form"
    ):

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

        submitted = st.form_submit_button(
            "Save Training Session",
            use_container_width=True
        )

        if submitted:

            data = {

                "session_date":
                    str(session_date),

                "topic":
                    topic,

                "trainer_name":
                    trainer_name,

                "participants_count":
                    participants_count,

                "notes":
                    notes
            }

            if add_record(
                "training_sessions",
                data
            ):

                st.success(
                    "Training session saved."
                )

                st.rerun()

    st.markdown(
        "### Training Records"
    )

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
        'Analyse participant activity, safety awareness '
        'and quiz performance.'
        '</div>',
        unsafe_allow_html=True
    )

    # ========================================================
    # SAFETY REPORT
    # ========================================================

    st.markdown(
        "### 🛡️ Safety Events"
    )

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

    st.markdown(
        "### 📱 Smartphone Usage"
    )

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

    st.markdown(
        "### 📝 Quiz Performance"
    )

    if len(quiz_df) > 0:

        if (
            "score" in quiz_df.columns
            and
            "total_questions" in quiz_df.columns
        ):

            quiz_df["percentage"] = (

                quiz_df["score"].astype(float)
                /
                quiz_df["total_questions"].astype(float)

            ) * 100

            c1, c2, c3 = st.columns(3)

            with c1:

                st.metric(
                    "Quiz Attempts",
                    len(quiz_df)
                )

            with c2:

                st.metric(
                    "Average Score",
                    f"{quiz_df['percentage'].mean():.1f}%"
                )

            with c3:

                st.metric(
                    "Highest Score",
                    f"{quiz_df['percentage'].max():.1f}%"
                )

            fig = px.bar(
                quiz_df,
                x=quiz_df.index,
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

            # ------------------------------------------------
            # PARTICIPANT NAME
            # ------------------------------------------------

            if "participant_id" in quiz_df.columns:

                participant_names = {

                    p.get("participant_id"):
                        p.get("name", "Unknown")

                    for p in participants
                }

                quiz_df[
                    "Participant Name"
                ] = quiz_df[
                    "participant_id"
                ].map(
                    participant_names
                )

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

                if col in quiz_df.columns:

                    display_columns.append(col)

            if display_columns:

                st.dataframe(
                    quiz_df[
                        display_columns
                    ],
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

    st.markdown(
        "### 🎓 Training Sessions"
    )

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
    # EXPORT
    # ========================================================

    st.markdown(
        "### 📥 Export Data"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        if len(participants_df) > 0:

            st.download_button(
                "Download Participants",
                participants_df.to_csv(
                    index=False
                ),
                "participants.csv",
                "text/csv",
                use_container_width=True
            )

    with col2:

        if len(smartphone_df) > 0:

            st.download_button(
                "Download Smartphone",
                smartphone_df.to_csv(
                    index=False
                ),
                "smartphone_usage.csv",
                "text/csv",
                use_container_width=True
            )

    with col3:

        if len(safety_df) > 0:

            st.download_button(
                "Download Safety",
                safety_df.to_csv(
                    index=False
                ),
                "safety_events.csv",
                "text/csv",
                use_container_width=True
            )

    with col4:

        if len(quiz_df) > 0:

            st.download_button(
                "Download Quiz",
                quiz_df.to_csv(
                    index=False
                ),
                "quiz_results.csv",
                "text/csv",
                use_container_width=True
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown(
    """
    <div style="
        text-align:center;
        color:#888;
        font-size:13px;
        padding:12px;
    ">

        🛡️ <b>Women Digital Safety & Awareness System</b>
        <br>

        Smartphone Usage & Online Safety
        for Women Self Help Groups

        <br>

        Community Engagement Project

    </div>
    """,
    unsafe_allow_html=True
)
