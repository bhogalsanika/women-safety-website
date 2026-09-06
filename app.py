
import streamlit as st
from supabase import create_client
import pandas as pd
from datetime import datetime

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
# SUPABASE CONFIGURATION
# ============================================================

SUPABASE_URL = "PASTE_YOUR_SUPABASE_URL_HERE"
SUPABASE_KEY = "PASTE_YOUR_SUPABASE_ANON_KEY_HERE"

supabase = None
database_connected = False

try:
    if (
        SUPABASE_URL != "PASTE_YOUR_SUPABASE_URL_HERE"
        and SUPABASE_KEY != "PASTE_YOUR_SUPABASE_ANON_KEY_HERE"
    ):
        supabase = create_client(
            SUPABASE_URL,
            SUPABASE_KEY
        )
        database_connected = True
except Exception:
    database_connected = False


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #fff8fb;
    }

    [data-testid="stSidebar"] {
        background-color: #fff0f6;
    }

    .hero {
        padding: 45px;
        border-radius: 25px;
        background: linear-gradient(
            135deg,
            #8e2de2,
            #ff4b8b
        );
        color: white;
        margin-bottom: 30px;
    }

    .hero h1 {
        font-size: 48px;
        margin-bottom: 10px;
    }

    .hero p {
        font-size: 19px;
    }

    .card {
        background: white;
        padding: 25px;
        border-radius: 18px;
        border: 1px solid #eeeeee;
        margin-bottom: 20px;
    }

    .help-card {
        background: white;
        padding: 25px;
        border-radius: 18px;
        border: 2px solid #ffd4e4;
        text-align: center;
        margin-bottom: 15px;
    }

    .number {
        font-size: 35px;
        font-weight: bold;
    }

    .section-title {
        font-size: 30px;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    """
    <h1 style="text-align:center;">🌸</h1>
    <h2 style="text-align:center;">Digital Saheli</h2>
    <p style="text-align:center;">
    Women Digital Safety Platform
    </p>
    """,
    unsafe_allow_html=True
)

st.sidebar.divider()

page = st.sidebar.radio(
    "📌 Menu",
    [
        "🏠 Home",
        "📱 Smartphone Usage",
        "🛡️ Online Safety",
        "🚨 Scams & Fraud",
        "👩 Women Safety",
        "📝 Report an Incident",
        "🆘 Help & Helplines",
        "🧠 Safety Quiz",
        "👩‍💼 Add Participant",
        "📊 Dashboard"
    ]
)

st.sidebar.divider()

if database_connected:
    st.sidebar.success("🟢 Database Connected")
else:
    st.sidebar.warning("🟠 Database Not Connected")


# ============================================================
# HOME PAGE
# ============================================================

if page == "🏠 Home":

    st.markdown(
        """
        <div class="hero">
            <h1>🌸 Digital Saheli</h1>
            <p>
            Smartphone Usage and Online Safety
            for Women Self Help Groups
            </p>
            <p>
            Learn • Protect • Report • Get Help
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.title("Welcome to Digital Saheli 👋")

    st.write(
        """
        Digital Saheli is an awareness platform designed to help
        women learn smartphone usage, internet safety, digital
        payment safety and protection against online fraud.
        """
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="card">
                <h2>📱 Learn</h2>
                <p>
                Learn basic smartphone, internet,
                WhatsApp and digital payment usage.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="card">
                <h2>🛡️ Protect</h2>
                <p>
                Learn about passwords, OTP,
                UPI, privacy and online scams.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="card">
                <h2>🆘 Get Help</h2>
                <p>
                Find emergency numbers and
                cybercrime reporting information.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    st.subheader("⭐ Important Safety Rules")

    rules = [
        "Never share your OTP with anyone.",
        "Never share your UPI PIN.",
        "Do not click suspicious links.",
        "Use strong and unique passwords.",
        "Keep your phone and apps updated.",
        "Block and report suspicious accounts.",
        "Verify before making online payments."
    ]

    for rule in rules:
        st.write("✅ " + rule)


# ============================================================
# SMARTPHONE USAGE
# ============================================================

elif page == "📱 Smartphone Usage":

    st.title("📱 Smartphone Usage")

    st.write(
        "Learn the basic smartphone skills required for everyday life."
    )

    smartphone_topics = {

        "📞 Calls & Contacts": [
            "Make and receive phone calls.",
            "Save a new contact.",
            "Search for a saved contact.",
            "Block an unwanted number.",
            "Use emergency contacts."
        ],

        "💬 WhatsApp": [
            "Send text messages.",
            "Send photos and documents.",
            "Make voice and video calls.",
            "Block unwanted contacts.",
            "Use WhatsApp privacy settings."
        ],

        "🌐 Internet & Google": [
            "Open a browser.",
            "Search information using Google.",
            "Check whether a website is trustworthy.",
            "Avoid suspicious links.",
            "Do not download unknown files."
        ],

        "📲 Apps": [
            "Install apps from trusted app stores.",
            "Update applications.",
            "Remove unwanted applications.",
            "Check application permissions."
        ],

        "⚙️ Phone Settings": [
            "Set a screen lock.",
            "Manage Wi-Fi and mobile data.",
            "Manage location permissions.",
            "Manage camera and microphone permissions.",
            "Update phone software."
        ],

        "💳 Digital Payments": [
            "Use UPI carefully.",
            "Verify the receiver before sending money.",
            "Never share UPI PIN.",
            "Do not approve unknown payment requests.",
            "Check transaction details before paying."
        ]
    }

    for title, information in smartphone_topics.items():

        with st.expander(title):

            for item in information:
                st.write("• " + item)


# ============================================================
# ONLINE SAFETY
# ============================================================

elif page == "🛡️ Online Safety":

    st.title("🛡️ Online Safety")

    safety_topics = {

        "🔐 Password Safety":
            """
            Create strong passwords using a combination of letters,
            numbers and symbols. Avoid using your name, mobile number
            or simple passwords.
            """,

        "🔑 OTP Safety":
            """
            OTP is private information. Banks, payment services and
            genuine support staff should not ask you to disclose your OTP.
            """,

        "💳 UPI Safety":
            """
            Never share your UPI PIN. Always verify the receiver before
            sending money. Be careful with unknown payment requests.
            """,

        "🔒 Privacy":
            """
            Check privacy settings on WhatsApp and social media.
            Avoid publicly sharing personal information.
            """,

        "🔗 Suspicious Links":
            """
            Do not click unknown links received through SMS, email,
            WhatsApp or social media. Verify the sender first.
            """,

        "📍 Location Safety":
            """
            Avoid publicly sharing your live location.
            Review location permissions of apps.
            """,

        "📲 App Permissions":
            """
            Give applications only the permissions they actually need.
            Review permissions regularly.
            """,

        "🔄 Software Updates":
            """
            Keep your smartphone operating system and applications
            updated to receive security improvements.
            """
    }

    for title, information in safety_topics.items():

        st.markdown(
            f"""
            <div class="card">
                <h3>{title}</h3>
                <p>{information}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# SCAMS & FRAUD
# ============================================================

elif page == "🚨 Scams & Fraud":

    st.title("🚨 Scams & Fraud Awareness")

    st.warning(
        "Scammers may create fear, urgency or excitement to make you "
        "share information or send money."
    )

    scam_list = {

        "📩 Fake KYC Message":
            "A message says your account will be blocked and asks you to click a link.",

        "💼 Fake Job Offer":
            "Someone offers a job and asks for registration or processing fees.",

        "🎁 Lottery Scam":
            "A message claims that you have won a prize or large amount of money.",

        "💳 UPI Scam":
            "Someone tricks you into approving a payment or sharing your UPI PIN.",

        "🔗 Phishing":
            "A fake website attempts to collect passwords, card details or OTP.",

        "👤 Fake Customer Care":
            "A fake support number asks for OTP, payment or remote access."
    }

    for title, explanation in scam_list.items():

        with st.expander(title):

            st.write(explanation)

            st.error(
                "Safety Tip: Stop → Verify → Do not share confidential information."
            )


# ============================================================
# WOMEN SAFETY
# ============================================================

elif page == "👩 Women Safety":

    st.title("👩 Women Online Safety")

    women_safety = {

        "🚫 Online Harassment":
            "Block and report abusive or unwanted accounts. Save relevant evidence.",

        "👤 Fake Profiles":
            "Do not share personal information with suspicious profiles.",

        "📸 Photo / Video Misuse":
            "Avoid publicly sharing sensitive photos and save evidence if misuse occurs.",

        "👀 Cyberstalking":
            "Review privacy settings, block unwanted users and seek appropriate help.",

        "💬 Threatening Messages":
            "Do not share personal information. Preserve messages/screenshots and seek help.",

        "🔐 Social Media Privacy":
            "Control who can view your profile, posts, stories and personal information.",

        "📍 Personal Information":
            "Avoid publicly sharing your address, phone number, routine or live location."
    }

    for title, information in women_safety.items():

        st.markdown(
            f"""
            <div class="card">
                <h3>{title}</h3>
                <p>{information}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# REPORT INCIDENT
# ============================================================

elif page == "📝 Report an Incident":

    st.title("📝 Report an Incident")

    st.info(
        """
        This form stores an awareness/report record in the project
        database. For an official cybercrime complaint, use the
        National Cyber Crime Reporting Portal.
        """
    )

    with st.form("report_form"):

        name = st.text_input(
            "Name (Optional)"
        )

        category = st.selectbox(
            "Problem Type",
            [
                "Cyber Fraud",
                "Online Harassment",
                "Fake Profile",
                "Scam Message",
                "UPI / Payment Fraud",
                "Cyberstalking",
                "Photo / Video Misuse",
                "Threatening Message",
                "Other"
            ]
        )

        description = st.text_area(
            "Describe the problem"
        )

        incident_date = st.date_input(
            "Date of Incident"
        )

        contact = st.text_input(
            "Contact Information (Optional)"
        )

        submit_report = st.form_submit_button(
            "🚨 Submit Report"
        )

    if submit_report:

        if description.strip() == "":

            st.error(
                "Please describe the problem."
            )

        elif not database_connected:

            st.error(
                "Database is not connected. Please check Supabase URL and key."
            )

        else:

            try:

                report_data = {
                    "name": name,
                    "category": category,
                    "description": description,
                    "incident_date": str(incident_date),
                    "contact": contact,
                    "created_at": datetime.now().isoformat()
                }

                supabase.table(
                    "reports"
                ).insert(
                    report_data
                ).execute()

                st.success(
                    "✅ Your report has been saved successfully."
                )

            except Exception as error:

                st.error(
                    "Unable to save report."
                )

                st.code(str(error))

    st.divider()

    st.subheader("💻 Official Cyber Crime Complaint")

    st.write(
        """
        If you want to make an official cybercrime complaint,
        use the Government of India's National Cyber Crime
        Reporting Portal.
        """
    )

    st.link_button(
        "🌐 Report Cyber Crime Online",
        "https://www.cybercrime.gov.in/"
    )


# ============================================================
# HELP & HELPLINES
# ============================================================

elif page == "🆘 Help & Helplines":

    st.title("🆘 Help & Helplines")

    st.write(
        "Use the appropriate official service depending on the situation."
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="help-card">
                <div class="number">🚨 112</div>
                <h3>Emergency</h3>
                <p>Emergency assistance.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.link_button(
            "📞 Call 112",
            "tel:112"
        )

    with col2:

        st.markdown(
            """
            <div class="help-card">
                <div class="number">👩 181</div>
                <h3>Women Helpline</h3>
                <p>Women-related support.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.link_button(
            "📞 Call 181",
            "tel:181"
        )

    with col3:

        st.markdown(
            """
            <div class="help-card">
                <div class="number">💻 1930</div>
                <h3>Cyber Crime</h3>
                <p>Cyber/financial fraud reporting.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.link_button(
            "📞 Call 1930",
            "tel:1930"
        )

    st.divider()

    st.subheader("🌐 Official Cybercrime Reporting")

    st.link_button(
        "Report Cyber Crime",
        "https://www.cybercrime.gov.in/"
    )

    st.info(
        "Keep screenshots, transaction information and other relevant "
        "evidence available when reporting an incident."
    )


# ============================================================
# SAFETY QUIZ
# ============================================================

elif page == "🧠 Safety Quiz":

    st.title("🧠 Online Safety Quiz")

    st.write(
        "Test your knowledge about smartphone and online safety."
    )

    participant_name = st.text_input(
        "Participant Name"
    )

    questions = [

        {
            "question": "Should you share your OTP with a caller?",
            "options": ["Yes", "No"],
            "answer": "No"
        },

        {
            "question": "Should you share your UPI PIN with someone?",
            "options": ["Yes", "No"],
            "answer": "No"
        },

        {
            "question": "What should you do with a suspicious link?",
            "options": [
                "Click it immediately",
                "Ignore it and verify"
            ],
            "answer": "Ignore it and verify"
        },

        {
            "question": "Should you use the same password everywhere?",
            "options": ["Yes", "No"],
            "answer": "No"
        },

        {
            "question": "Should you publicly share your live location?",
            "options": ["Yes", "No"],
            "answer": "No"
        },

        {
            "question": "What should you do with an abusive account?",
            "options": [
                "Share personal information",
                "Block and report"
            ],
            "answer": "Block and report"
        },

        {
            "question": "Should you verify the receiver before making a payment?",
            "options": ["Yes", "No"],
            "answer": "Yes"
        },

        {
            "question": "Can scammers create fake customer-care accounts?",
            "options": ["Yes", "No"],
            "answer": "Yes"
        },

        {
            "question": "Should you install apps from unknown sources?",
            "options": ["Yes", "No"],
            "answer": "No"
        },

        {
            "question": "Should you keep your phone software updated?",
            "options": ["Yes", "No"],
            "answer": "Yes"
        }
    ]

    selected_answers = []

    for number, question in enumerate(
        questions,
        start=1
    ):

        st.subheader(
            f"Q{number}. {question['question']}"
        )

        answer = st.radio(
            "Select your answer:",
            question["options"],
            key=f"quiz_{number}"
        )

        selected_answers.append(answer)

    if st.button(
        "📝 Submit Quiz",
        type="primary"
    ):

        score = 0

        for i in range(
            len(questions)
        ):

            if (
                selected_answers[i]
                == questions[i]["answer"]
            ):
                score += 1

        total = len(questions)

        percentage = int(
            (score / total) * 100
        )

        st.divider()

        st.success(
            f"🎉 Your Score: {score}/{total}"
        )

        st.metric(
            "Quiz Percentage",
            f"{percentage}%"
        )

        if percentage >= 80:

            st.balloons()

            st.success(
                "Excellent! You have good online safety awareness."
            )

        elif percentage >= 50:

            st.info(
                "Good attempt! Review the safety section once again."
            )

        else:

            st.warning(
                "Please review the online safety topics and try again."
            )

        if (
            database_connected
            and participant_name.strip() != ""
        ):

            try:

                quiz_data = {
                    "participant_name": participant_name,
                    "score": score,
                    "total_questions": total,
                    "percentage": percentage,
                    "created_at": datetime.now().isoformat()
                }

                supabase.table(
                    "quiz_results"
                ).insert(
                    quiz_data
                ).execute()

                st.success(
                    "✅ Quiz result saved to database."
                )

            except Exception as error:

                st.error(
                    "Quiz result could not be saved."
                )

                st.code(str(error))


# ============================================================
# ADD PARTICIPANT
# ============================================================

elif page == "👩‍💼 Add Participant":

    st.title("👩‍💼 Add Participant")

    st.write(
        "Register women participating in the awareness program."
    )

    with st.form("participant_form"):

        name = st.text_input(
            "Participant Name"
        )

        age_group = st.selectbox(
            "Age Group",
            [
                "18-25",
                "26-35",
                "36-45",
                "46-55",
                "56+"
            ]
        )

        shg_name = st.text_input(
            "Self Help Group Name"
        )

        smartphone_level = st.selectbox(
            "Smartphone Experience",
            [
                "Beginner",
                "Basic",
                "Intermediate",
                "Advanced"
            ]
        )

        submit_participant = st.form_submit_button(
            "➕ Add Participant"
        )

    if submit_participant:

        if name.strip() == "":

            st.error(
                "Please enter participant name."
            )

        elif not database_connected:

            st.error(
                "Database is not connected."
            )

        else:

            try:

                participant_data = {
                    "name": name,
                    "age_group": age_group,
                    "shg_name": shg_name,
                    "smartphone_level": smartphone_level,
                    "created_at": datetime.now().isoformat()
                }

                supabase.table(
                    "participants"
                ).insert(
                    participant_data
                ).execute()

                st.success(
                    "✅ Participant added successfully."
                )

            except Exception as error:

                st.error(
                    "Unable to add participant."
                )

                st.code(str(error))


# ============================================================
# DASHBOARD
# ============================================================

elif page == "📊 Dashboard":

    st.title("📊 Dashboard")

    if not database_connected:

        st.warning(
            "Connect Supabase to view database records."
        )

    else:

        try:

            participants_response = (
                supabase
                .table("participants")
                .select("*")
                .execute()
            )

            reports_response = (
                supabase
                .table("reports")
                .select("*")
                .execute()
            )

            quiz_response = (
                supabase
                .table("quiz_results")
                .select("*")
                .execute()
            )

            participants = (
                participants_response.data
                or []
            )

            reports = (
                reports_response.data
                or []
            )

            quiz_results = (
                quiz_response.data
                or []
            )

            participant_count = len(
                participants
            )

            report_count = len(
                reports
            )

            quiz_count = len(
                quiz_results
            )

            if quiz_count > 0:

                average_score = sum(
                    int(
                        item.get(
                            "percentage",
                            0
                        )
                    )
                    for item in quiz_results
                ) / quiz_count

            else:

                average_score = 0

            col1, col2, col3, col4 = st.columns(4)

            with col1:

                st.metric(
                    "👩 Participants",
                    participant_count
                )

            with col2:

                st.metric(
                    "📝 Reports",
                    report_count
                )

            with col3:

                st.metric(
                    "🧠 Quizzes",
                    quiz_count
                )

            with col4:

                st.metric(
                    "📈 Average Score",
                    f"{average_score:.1f}%"
                )

            st.divider()

            # ------------------------------------------------
            # PARTICIPANTS
            # ------------------------------------------------

            st.subheader(
                "👩 Participant Records"
            )

            if participants:

                participant_df = pd.DataFrame(
                    participants
                )

                st.dataframe(
                    participant_df,
                    use_container_width=True
                )

            else:

                st.info(
                    "No participants registered yet."
                )

            # ------------------------------------------------
            # REPORTS
            # ------------------------------------------------

            st.subheader(
                "📝 Incident Reports"
            )

            if reports:

                reports_df = pd.DataFrame(
                    reports
                )

                st.dataframe(
                    reports_df,
                    use_container_width=True
                )

            else:

                st.info(
                    "No incident reports submitted yet."
                )

            # ------------------------------------------------
            # QUIZ RESULTS
            # ------------------------------------------------

            st.subheader(
                "🧠 Quiz Results"
            )

            if quiz_results:

                quiz_df = pd.DataFrame(
                    quiz_results
                )

                st.dataframe(
                    quiz_df,
                    use_container_width=True
                )

            else:

                st.info(
                    "No quiz results available yet."
                )

        except Exception as error:

            st.error(
                "Unable to load database records."
            )

            st.code(str(error))


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div style="text-align:center;">
        <p>
        🌸 <b>Digital Saheli</b> |
        Smartphone Usage & Online Safety
        </p>
        <p>
        Made for Women Self Help Group Awareness
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

