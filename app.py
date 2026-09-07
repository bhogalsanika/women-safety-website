import streamlit as st
from supabase import create_client
from datetime import datetime
import pandas as pd

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Digital Saheli",
    page_icon="🌸",
    layout="wide"
)

# =========================================================
# SUPABASE CONNECTION
# =========================================================

SUPABASE_URL = "PASTE_YOUR_SUPABASE_URL_HERE"
SUPABASE_KEY = "PASTE_YOUR_SUPABASE_ANON_KEY_HERE"

try:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    db_connected = True
except Exception:
    db_connected = False
    supabase = None

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #fff7fb, #f8f0ff);
}

.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    color: #922b63;
    margin-top: 10px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #54245c;
    margin-bottom: 25px;
}

.hero {
    background: linear-gradient(135deg, #f7d4e5, #ead8f7);
    padding: 35px;
    border-radius: 0 0 35px 35px;
    text-align: center;
    margin-bottom: 25px;
}

.hero h1 {
    color: #8e255c;
    font-size: 42px;
}

.hero p {
    color: #402347;
    font-size: 18px;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #efd5e5;
    box-shadow: 0 4px 15px rgba(120, 50, 100, 0.08);
    margin-bottom: 20px;
}

.card h2 {
    color: #922b63;
}

.card h3 {
    color: #6d315e;
}

.section-title {
    color: #922b63;
    font-size: 30px;
    font-weight: 700;
    margin-top: 20px;
}

div.stButton > button {
    border-radius: 12px;
    border: none;
    background-color: #922b63;
    color: white;
    font-weight: 600;
}

div.stButton > button:hover {
    background-color: #74204e;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="hero">
    <h1>🌸 DIGITAL SAHELI</h1>
    <p><b>Learn • Protect • Stay Connected</b></p>
    <p>Smartphone & Online Safety for Women</p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🌸 Digital Saheli")

page = st.sidebar.radio(
    "Choose Section",
    [
        "🏠 Home",
        "📱 Smartphone Usage",
        "🛡️ Online Safety",
        "📝 Safety Quiz",
        "👩 Add Participant",
        "📊 Records"
    ]
)

# =========================================================
# HOME
# =========================================================

if page == "🏠 Home":

    st.markdown(
        '<div class="section-title">👩 Welcome to Digital Saheli</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        <h2>Learn • Protect • Stay Connected</h2>
        <p>
        Digital Saheli is a simple learning platform designed to help women
        understand smartphones, digital services and online safety.
        </p>
        <p>
        Learn useful smartphone skills and understand how to stay safe
        while using the internet.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
            <h2>📱 Smartphone Usage</h2>
            <p>Learn basic smartphone functions:</p>
            <ul>
                <li>Making calls and sending messages</li>
                <li>Using contacts</li>
                <li>Using WhatsApp</li>
                <li>Using Google Search</li>
                <li>Using camera and gallery</li>
                <li>Using online services</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h2>🛡️ Online Safety</h2>
            <p>Learn how to protect yourself online:</p>
            <ul>
                <li>Create strong passwords</li>
                <li>Identify suspicious links</li>
                <li>Avoid sharing OTPs</li>
                <li>Protect personal information</li>
                <li>Use privacy settings</li>
                <li>Report suspicious activity</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.info(
        "💡 Start with Smartphone Usage and Online Safety, "
        "then attempt the Safety Quiz."
    )

# =========================================================
# SMARTPHONE USAGE
# =========================================================

elif page == "📱 Smartphone Usage":

    st.markdown(
        '<div class="section-title">📱 Smartphone Usage</div>',
        unsafe_allow_html=True
    )

    topics = {
        "📞 Calls & Contacts": [
            "Save important contacts with clear names.",
            "Use the phone app to make and receive calls.",
            "Block unknown or unwanted numbers when necessary."
        ],

        "💬 WhatsApp": [
            "Use WhatsApp to send messages, photos and documents.",
            "Check the name and number before sending sensitive information.",
            "Avoid forwarding unverified messages."
        ],

        "🔎 Google Search": [
            "Open Google and type your question.",
            "Check information from reliable websites.",
            "Do not blindly trust every result."
        ],

        "📷 Camera & Gallery": [
            "Use the camera to take photos and videos.",
            "Review photos before sharing them.",
            "Avoid sharing private photos publicly."
        ],

        "💳 Digital Payments": [
            "Never share your UPI PIN or OTP.",
            "Check the receiver's name before making a payment.",
            "Do not click payment links received from unknown people."
        ]
    }

    for title, points in topics.items():
        with st.expander(title):
            for point in points:
                st.write("• " + point)

# =========================================================
# ONLINE SAFETY
# =========================================================

elif page == "🛡️ Online Safety":

    st.markdown(
        '<div class="section-title">🛡️ Online Safety</div>',
        unsafe_allow_html=True
    )

    safety_topics = [
        (
            "🔐 Strong Passwords",
            "Use a long and unique password. Avoid using your name, "
            "mobile number or date of birth."
        ),
        (
            "🔢 OTP Safety",
            "Never share an OTP with another person, even if they claim "
            "to be from a bank or company."
        ),
        (
            "🔗 Suspicious Links",
            "Do not open unknown links received through SMS, WhatsApp "
            "or social media."
        ),
        (
            "📱 App Safety",
            "Download apps from trusted app stores and check permissions "
            "before allowing access."
        ),
        (
            "👤 Social Media Privacy",
            "Avoid publicly sharing your address, phone number, live "
            "location or other sensitive information."
        ),
        (
            "🚨 Cyber Fraud",
            "If you suspect online fraud, immediately contact your bank "
            "or the appropriate cybercrime authority."
        )
    ]

    for title, description in safety_topics:
        st.markdown(f"""
        <div class="card">
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# QUIZ
# =========================================================

elif page == "📝 Safety Quiz":

    st.markdown(
        '<div class="section-title">📝 Digital Safety Quiz</div>',
        unsafe_allow_html=True
    )

    st.write("Test your knowledge about smartphone and online safety.")

    participant_name = st.text_input("👩 Participant Name")

    participant_phone = st.text_input(
        "📱 Mobile Number (optional)"
    )

    st.markdown("---")

    questions = [
        {
            "question": "1. Should you share your OTP with someone who calls you?",
            "options": ["Yes", "No"],
            "answer": "No"
        },
        {
            "question": "2. What should you do with a suspicious link?",
            "options": [
                "Open it immediately",
                "Ignore it and verify the source"
            ],
            "answer": "Ignore it and verify the source"
        },
        {
            "question": "3. Which information should NOT be shared?",
            "options": [
                "OTP and UPI PIN",
                "Weather information",
                "Public news"
            ],
            "answer": "OTP and UPI PIN"
        },
        {
            "question": "4. Where should apps preferably be downloaded from?",
            "options": [
                "Trusted app store",
                "Unknown websites"
            ],
            "answer": "Trusted app store"
        },
        {
            "question": "5. What makes a password safer?",
            "options": [
                "Your name",
                "123456",
                "A long unique password"
            ],
            "answer": "A long unique password"
        }
    ]

    answers = []

    for q in questions:
        answer = st.radio(
            q["question"],
            q["options"],
            key=q["question"]
        )
        answers.append(answer)

    if st.button("Submit Quiz"):

        if participant_name.strip() == "":
            st.warning("Please enter participant name.")
        else:

            score = 0

            for i in range(len(questions)):
                if answers[i] == questions[i]["answer"]:
                    score += 1

            total = len(questions)

            st.success(
                f"🎉 {participant_name}, your score is "
                f"{score}/{total}"
            )

            # SAVE RESULT TO SUPABASE
            if db_connected:

                try:

                    data = {
                        "participant_name": participant_name,
                        "mobile": participant_phone,
                        "score": score,
                        "total_questions": total,
                        "submitted_at": datetime.now().isoformat()
                    }

                    supabase.table("quiz_results").insert(data).execute()

                    st.success(
                        "✅ Quiz result has been saved successfully."
                    )

                except Exception as e:
                    st.error(
                        "Quiz completed, but database save failed."
                    )
                    st.code(str(e))

            else:
                st.warning(
                    "Supabase is not connected. Add your URL and API key."
                )

# =========================================================
# ADD PARTICIPANT
# =========================================================

elif page == "👩 Add Participant":

    st.markdown(
        '<div class="section-title">👩 Add Participant</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        <h3>Participant Registration</h3>
        <p>
        Add women participating in the smartphone and online safety
        awareness activity.
        </p>
    </div>
    """, unsafe_allow_html=True)

    name = st.text_input("👩 Participant Name")
    mobile = st.text_input("📱 Mobile Number")
    age = st.number_input(
        "🎂 Age",
        min_value=10,
        max_value=100,
        value=25
    )

    if st.button("Add Participant"):

        if name.strip() == "":
            st.warning("Please enter participant name.")

        elif not db_connected:
            st.error(
                "Supabase is not connected. Please check your URL and API key."
            )

        else:

            try:

                data = {
                    "name": name,
                    "mobile": mobile,
                    "age": age,
                    "created_at": datetime.now().isoformat()
                }

                supabase.table("participants").insert(data).execute()

                st.success(
                    f"✅ {name} has been added successfully!"
                )

            except Exception as e:
                st.error("Participant could not be added.")
                st.code(str(e))

# =========================================================
# RECORDS
# =========================================================

elif page == "📊 Records":

    st.markdown(
        '<div class="section-title">📊 Participant & Quiz Records</div>',
        unsafe_allow_html=True
    )

    if not db_connected:

        st.error(
            "Supabase is not connected. Please add your Supabase credentials."
        )

    else:

        # ---------------------------------------------
        # PARTICIPANTS
        # ---------------------------------------------

        st.subheader("👩 Participants")

        try:

            participants = (
                supabase
                .table("participants")
                .select("*")
                .order("created_at", desc=True)
                .execute()
            )

            if participants.data:

                df_participants = pd.DataFrame(
                    participants.data
                )

                st.dataframe(
                    df_participants,
                    use_container_width=True
                )

            else:
                st.info("No participants added yet.")

        except Exception as e:
            st.error("Could not load participant records.")
            st.code(str(e))

        st.markdown("---")

        # ---------------------------------------------
        # QUIZ RESULTS
        # ---------------------------------------------

        st.subheader("📝 Quiz Results")

        try:

            results = (
                supabase
                .table("quiz_results")
                .select("*")
                .order("submitted_at", desc=True)
                .execute()
            )

            if results.data:

                df_results = pd.DataFrame(
                    results.data
                )

                st.dataframe(
                    df_results,
                    use_container_width=True
                )

                # Statistics
                st.markdown("### 📈 Quiz Summary")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "Total Attempts",
                        len(df_results)
                    )

                with col2:
                    st.metric(
                        "Highest Score",
                        df_results["score"].max()
                    )

                with col3:
                    st.metric(
                        "Average Score",
                        round(df_results["score"].mean(), 2)
                    )

            else:
                st.info("No quiz results available yet.")

        except Exception as e:
            st.error("Could not load quiz records.")
            st.code(str(e))

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    "<center>🌸 Digital Saheli | Smartphone & Online Safety for Women</center>",
    unsafe_allow_html=True
)
