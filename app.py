import streamlit as st
from supabase import create_client, Client
from datetime import datetime
import pandas as pd

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Digital Saheli - Women Safety",
    page_icon="🌸",
    layout="wide"
)

# ============================================================
# SUPABASE CONNECTION
# ============================================================

SUPABASE_URL = "PASTE_YOUR_SUPABASE_URL_HERE"
SUPABASE_KEY = "PASTE_YOUR_SUPABASE_ANON_KEY_HERE"

try:
    supabase: Client = create_client(
        SUPABASE_URL,
        SUPABASE_KEY
    )
    db_connected = True
except Exception:
    db_connected = False

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #fff8fb;
}

.block-container {
    padding-top: 2rem;
}

.hero {
    padding: 35px;
    border-radius: 20px;
    background: linear-gradient(135deg, #8e2de2, #ff4b8b);
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 10px;
}

.card {
    padding: 22px;
    border-radius: 16px;
    background-color: white;
    border: 1px solid #eeeeee;
    margin-bottom: 15px;
}

.small-card {
    padding: 18px;
    border-radius: 15px;
    background-color: #ffffff;
    border: 1px solid #eeeeee;
    min-height: 150px;
}

.help-card {
    padding: 20px;
    border-radius: 16px;
    background-color: #fff0f5;
    border: 1px solid #ffd1df;
    text-align: center;
}

.warning {
    padding: 18px;
    border-radius: 12px;
    background-color: #fff4e5;
    border-left: 5px solid #ff9800;
}

.safe {
    padding: 18px;
    border-radius: 12px;
    background-color: #eafaf0;
    border-left: 5px solid #28a745;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🌸 Digital Saheli")
st.sidebar.caption("Smartphone Usage & Online Safety")

page = st.sidebar.radio(
    "Navigation",
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

if db_connected:
    st.sidebar.success("Database Connected")
else:
    st.sidebar.error("Database Not Connected")

# ============================================================
# HOME
# ============================================================

if page == "🏠 Home":

    st.markdown("""
    <div class="hero">
        <h1>🌸 Digital Saheli</h1>
        <p>Smartphone Usage and Online Safety for Women Self Help Groups</p>
        <p>Learn • Stay Safe • Report • Get Help</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Welcome 👋")

    st.write(
        "Digital Saheli is an awareness and learning platform designed "
        "to help women understand smartphone usage, digital payments, "
        "online safety and cybercrime awareness."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="small-card">
        <h3>📱 Learn</h3>
        <p>Learn basic smartphone and internet usage.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="small-card">
        <h3>🛡️ Protect</h3>
        <p>Learn how to protect your accounts and personal information.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="small-card">
        <h3>🆘 Get Help</h3>
        <p>Find emergency and cybercrime reporting resources.</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.subheader("Important Safety Rule")

    st.warning(
        "Never share your OTP, UPI PIN, ATM PIN, password or verification code "
        "with anyone."
    )

# ============================================================
# SMARTPHONE USAGE
# ============================================================

elif page == "📱 Smartphone Usage":

    st.title("📱 Smartphone Usage")

    topics = {
        "📞 Calls & Contacts": [
            "Make and receive calls.",
            "Save important contacts.",
            "Block unknown numbers.",
            "Use emergency contacts."
        ],
        "💬 WhatsApp": [
            "Send messages and photos.",
            "Make voice/video calls.",
            "Block unwanted contacts.",
            "Check privacy settings."
        ],
        "🌐 Internet": [
            "Use Google Search.",
            "Identify trusted websites.",
            "Avoid suspicious links.",
            "Do not download unknown files."
        ],
        "📲 Apps": [
            "Install apps from trusted stores.",
            "Check app permissions.",
            "Keep apps updated.",
            "Remove apps that are not required."
        ],
        "⚙️ Phone Settings": [
            "Use screen lock.",
            "Manage location settings.",
            "Control camera and microphone permissions.",
            "Keep software updated."
        ],
        "💳 Digital Payments": [
            "Never share UPI PIN.",
            "Verify the receiver before payment.",
            "Do not approve unknown payment requests.",
            "Check transaction details carefully."
        ]
    }

    for title, points in topics.items():

        with st.expander(title):

            for point in points:
                st.write("• " + point)

# ============================================================
# ONLINE SAFETY
# ============================================================

elif page == "🛡️ Online Safety":

    st.title("🛡️ Online Safety")

    safety_topics = [
        (
            "🔐 Strong Password",
            "Use a long and unique password for important accounts. "
            "Avoid using your name, birth date or simple numbers."
        ),
        (
            "🔑 OTP Safety",
            "OTP is private. Never tell your OTP to callers, messages or strangers."
        ),
        (
            "💳 UPI Safety",
            "A UPI PIN is required to send money. Never enter your UPI PIN "
            "just because someone asks you to receive money."
        ),
        (
            "🔒 Privacy",
            "Review privacy settings on WhatsApp and social media. "
            "Avoid publicly sharing personal information."
        ),
        (
            "🔗 Suspicious Links",
            "Do not click unknown links received through SMS, WhatsApp, email "
            "or social media."
        ),
        (
            "📍 Location Safety",
            "Avoid sharing your live location publicly or with unknown people."
        )
    ]

    for title, description in safety_topics:

        st.markdown(
            f"""
            <div class="card">
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# ============================================================
# SCAMS
# ============================================================

elif page == "🚨 Scams & Fraud":

    st.title("🚨 Scams & Fraud Awareness")

    st.info(
        "Scammers often create urgency or fear to make people share "
        "personal information or send money."
    )

    scams = {
        "📩 Fake KYC Message":
            "A message says your bank account or SIM will be blocked and asks you to click a link.",

        "💼 Fake Job Offer":
            "Someone promises a job and asks for registration or processing fees.",

        "🎁 Lottery Scam":
            "You receive a message claiming that you won money or a prize.",

        "💳 UPI Scam":
            "Someone tricks you into approving a payment request or sharing your UPI PIN.",

        "🔗 Phishing Link":
            "A fake website tries to collect your password, card details or OTP.",

        "👤 Fake Customer Care":
            "A fake support account asks for remote access, OTP or payment details."
    }

    for title, explanation in scams.items():

        with st.expander(title):
            st.write(explanation)
            st.error("Safety Tip: Stop, verify and do not share confidential information.")

# ============================================================
# WOMEN SAFETY
# ============================================================

elif page == "👩 Women Safety":

    st.title("👩 Women Online Safety")

    issues = {
        "🚫 Online Harassment":
            "Do not engage with abusive accounts. Block and report them.",

        "👤 Fake Profile":
            "Check suspicious profiles carefully and avoid sharing personal information.",

        "📸 Photo Misuse":
            "Avoid sharing sensitive photos publicly. Save evidence if misuse occurs.",

        "👀 Cyberstalking":
            "Keep accounts private and block people who repeatedly contact or monitor you.",

        "💬 Threatening Messages":
            "Do not respond with personal information. Save evidence and seek appropriate help.",

        "🔐 Social Media Privacy":
            "Review who can see your posts, profile information and stories."
    }

    for title, description in issues.items():

        st.markdown(
            f"""
            <div class="card">
                <h3>{title}</h3>
                <p>{description}</p>
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
        "You can submit an awareness/report record here. "
        "For an official cybercrime complaint, use the government portal below."
    )

    with st.form("incident_form"):

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

        submitted = st.form_submit_button(
            "Submit Report"
        )

        if submitted:

            if description.strip() == "":
                st.error("Please describe the problem.")
            elif not db_connected:
                st.error("Supabase is not connected.")
            else:

                try:

                    data = {
                        "name": name,
                        "category": category,
                        "description": description,
                        "incident_date": str(incident_date),
                        "contact": contact,
                        "created_at": datetime.now().isoformat()
                    }

                    supabase.table("reports").insert(data).execute()

                    st.success(
                        "✅ Report submitted successfully."
                    )

                except Exception as e:
                    st.error("Unable to submit report.")
                    st.code(str(e))

    st.divider()

    st.subheader("Official Cyber Crime Reporting")

    st.write(
        "For official cybercrime complaints, use the National Cyber Crime "
        "Reporting Portal."
    )

    st.link_button(
        "💻 Report Cyber Crime Online",
        "https://www.cybercrime.gov.in/"
    )

# ============================================================
# HELP & HELPLINES
# ============================================================

elif page == "🆘 Help & Helplines":

    st.title("🆘 Help & Emergency")

    st.write(
        "If you are facing an emergency or cyber-related problem, "
        "contact the appropriate official service."
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
        <div class="help-card">
        <h2>🚨 112</h2>
        <h4>Emergency</h4>
        <p>For immediate emergency assistance.</p>
        </div>
        """, unsafe_allow_html=True)

        st.link_button(
            "📞 Call 112",
            "tel:112"
        )

    with col2:

        st.markdown("""
        <div class="help-card">
        <h2>👩 181</h2>
        <h4>Women Helpline</h4>
        <p>Women-related assistance and support.</p>
        </div>
        """, unsafe_allow_html=True)

        st.link_button(
            "📞 Call 181",
            "tel:181"
        )

    with col3:

        st.markdown("""
        <div class="help-card">
        <h2>💻 1930</h2>
        <h4>Cyber Crime</h4>
        <p>Report financial/cyber fraud.</p>
        </div>
        """, unsafe_allow_html=True)

        st.link_button(
            "📞 Call 1930",
            "tel:1930"
        )

    st.divider()

    st.subheader("Official Reporting")

    st.link_button(
        "🌐 National Cyber Crime Reporting Portal",
        "https://www.cybercrime.gov.in/"
    )

    st.warning(
        "In case of financial cyber fraud, report as soon as possible. "
        "Keep transaction details and relevant evidence available."
    )

# ============================================================
# QUIZ
# ============================================================

elif page == "🧠 Safety Quiz":

    st.title("🧠 Online Safety Quiz")

    questions = [
        {
            "q": "Should you share your OTP with a caller?",
            "options": ["Yes", "No"],
            "answer": "No"
        },
        {
            "q": "Should you share your UPI PIN with someone?",
            "options": ["Yes", "No"],
            "answer": "No"
        },
        {
            "q": "What should you do with a suspicious link?",
            "options": ["Click it", "Ignore and verify"],
            "answer": "Ignore and verify"
        },
        {
            "q": "Should you use the same password everywhere?",
            "options": ["Yes", "No"],
            "answer": "No"
        },
        {
            "q": "Is it safe to share your live location publicly?",
            "options": ["Yes", "No"],
            "answer": "No"
        },
        {
            "q": "What should you do with an abusive online account?",
            "options": ["Share personal details", "Block and report"],
            "answer": "Block and report"
        },
        {
            "q": "Should you verify a payment recipient before sending money?",
            "options": ["Yes", "No"],
            "answer": "Yes"
        },
        {
            "q": "Can scammers create fake customer-care numbers?",
            "options": ["Yes", "No"],
            "answer": "Yes"
        },
        {
            "q": "Should you install apps from unknown sources?",
            "options": ["Yes", "No"],
            "answer": "No"
        },
        {
            "q": "Should you keep your phone software updated?",
            "options": ["Yes", "No"],
            "answer": "Yes"
        }
    ]

    participant_name = st.text_input(
        "Participant Name"
    )

    answers = []

    for i, question in enumerate(questions):

        st.subheader(
            f"Q{i + 1}. {question['q']}"
        )

        answer = st.radio(
            "Choose one:",
            question["options"],
            key=f"question_{i}"
        )

        answers.append(answer)

    if st.button("Submit Quiz"):

        score = 0

        for i in range(len(questions)):

            if answers[i] == questions[i]["answer"]:
                score += 1

        percentage = int(
            (score / len(questions)) * 100
        )

        st.success(
            f"🎉 Your Score: {score}/{len(questions)} ({percentage}%)"
        )

        if percentage >= 80:
            st.balloons()
            st.success("Excellent! You have good online safety awareness.")
        elif percentage >= 50:
            st.info("Good attempt! Review the safety topics once again.")
        else:
            st.warning("Please learn the safety topics and try again.")

        if db_connected and participant_name.strip():

            try:

                quiz_data = {
                    "participant_name": participant_name,
                    "score": score,
                    "total_questions": len(questions),
                    "percentage": percentage,
                    "created_at": datetime.now().isoformat()
                }

                supabase.table(
                    "quiz_results"
                ).insert(quiz_data).execute()

                st.success(
                    "Quiz result saved to database."
                )

            except Exception as e:

                st.error(
                    "Quiz result could not be saved."
                )

# ============================================================
# ADD PARTICIPANT
# ============================================================

elif page == "👩‍💼 Add Participant":

    st.title("👩‍💼 Add Participant")

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

        submit = st.form_submit_button(
            "Add Participant"
        )

        if submit:

            if name.strip() == "":
                st.error("Please enter participant name.")

            elif not db_connected:
                st.error("Supabase is not connected.")

            else:

                try:

                    participant = {
                        "name": name,
                        "age_group": age_group,
                        "shg_name": shg_name,
                        "smartphone_level": smartphone_level,
                        "created_at": datetime.now().isoformat()
                    }

                    supabase.table(
                        "participants"
                    ).insert(participant).execute()

                    st.success(
                        "✅ Participant added successfully."
                    )

                except Exception as e:

                    st.error(
                        "Could not add participant."
                    )

                    st.code(str(e))

# ============================================================
# DASHBOARD
# ============================================================

elif page == "📊 Dashboard":

    st.title("📊 Awareness Dashboard")

    if not db_connected:

        st.error(
            "Supabase is not connected. Please check your URL and API key."
        )

    else:

        try:

            participants = supabase.table(
                "participants"
            ).select("*").execute().data

            reports = supabase.table(
