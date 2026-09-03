import streamlit as st
from supabase import create_client
from datetime import datetime

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Digital Saheli",
    page_icon="🌸",
    layout="wide"
)

# ============================================================
# SUPABASE BACKEND
# ============================================================

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #fff8fc;
}

.hero {
    padding: 45px;
    border-radius: 25px;
    background: linear-gradient(135deg, #ffe4f0, #eee4ff);
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 45px;
    color: #7b2cbf;
    margin-bottom: 10px;
}

.hero p {
    font-size: 19px;
    color: #555;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.card h3 {
    color: #7b2cbf;
}

.tip {
    padding: 20px;
    border-radius: 15px;
    background: #fff0f6;
    border-left: 5px solid #e83e8c;
}

.footer {
    text-align: center;
    padding: 25px;
    color: #777;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🌸 Digital Saheli")

language = st.sidebar.selectbox(
    "Language",
    ["English", "हिंदी", "मराठी"]
)

menu = st.sidebar.radio(
    "Menu",
    [
        "🏠 Home",
        "📱 Smartphone Learning",
        "🛡️ Online Safety",
        "⚠️ Scam Detector",
        "🎯 Safety Quiz",
        "🚨 Women Safety",
        "💻 Report Cyber Crime"
    ]
)

# ============================================================
# HOME
# ============================================================

if menu == "🏠 Home":

    st.markdown("""
    <div class="hero">

    <h1>🌸 Digital Saheli</h1>

    <p>
    Learn smartphone usage, protect yourself online,
    identify scams and stay safe in the digital world.
    </p>

    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>📱 Smartphone Learning</h3>
        <p>Learn WhatsApp, UPI, Maps, Camera, Apps and phone settings.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>🛡️ Online Safety</h3>
        <p>Learn how to protect passwords, OTPs, payments and social media.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>⚠️ Scam Detector</h3>
        <p>Check whether a suspicious online situation may be a scam.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="tip">
    💡 <b>Safety Tip:</b> Never share your OTP, UPI PIN or password with anyone.
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# SMARTPHONE LEARNING
# ============================================================

elif menu == "📱 Smartphone Learning":

    st.title("📱 Smartphone Learning")

    topics = {
        "WhatsApp": [
            "Send messages and photos.",
            "Make voice and video calls.",
            "Block and report unknown contacts.",
            "Avoid clicking unknown links."
        ],

        "UPI Payments": [
            "Use trusted UPI applications.",
            "Never share your UPI PIN.",
            "PIN is required to send money, not receive money.",
            "Check the receiver's name before payment."
        ],

        "Google Maps": [
            "Search locations.",
            "Get directions.",
            "Share your location only with trusted people.",
            "Check the route before travelling."
        ],

        "Contacts": [
            "Save important emergency numbers.",
            "Create an emergency contact.",
            "Avoid sharing your contact details publicly."
        ],

        "Camera & Photos": [
            "Take photos and videos.",
            "Check app permissions.",
            "Avoid sharing private photos with strangers."
        ],

        "Apps & Updates": [
            "Install apps from trusted stores.",
            "Keep apps updated.",
            "Delete apps you do not use."
        ],

        "Phone Settings": [
            "Use screen lock.",
            "Check privacy settings.",
            "Turn on device security.",
            "Review app permissions."
        ]
    }

    for topic, points in topics.items():

        with st.expander("📌 " + topic):

            for point in points:
                st.write("• " + point)

# ============================================================
# ONLINE SAFETY
# ============================================================

elif menu == "🛡️ Online Safety":

    st.title("🛡️ Online Safety")

    safety_topics = {
        "Password Safety":
            "Use strong passwords and avoid using the same password everywhere.",

        "OTP Safety":
            "Never share OTP with anyone, even if they claim to be from a bank.",

        "Fake Links & Phishing":
            "Do not open suspicious links received through SMS, WhatsApp or email.",

        "Payment Safety":
            "Never share UPI PIN, card PIN, CVV or banking passwords.",

        "Social Media Privacy":
            "Keep personal information private and review account privacy settings.",

        "Fake Profiles":
            "Do not trust unknown profiles requesting money, photos or personal details.",

        "Suspicious Messages":
            "Verify unexpected messages before clicking links or sending information.",

        "Online Scams":
            "Be careful with lottery, job, investment and KYC-related scams."
    }

    for topic, information in safety_topics.items():

        with st.expander("🔐 " + topic):
            st.write(information)

# ============================================================
# SCAM DETECTOR
# ============================================================

elif menu == "⚠️ Scam Detector":

    st.title("⚠️ Scam Detector")

    st.write(
        "Select a situation to understand whether it may be risky."
    )

    situation = st.selectbox(
        "What happened?",
        [
            "Someone asked for my OTP",
            "I received a KYC update link",
            "Someone told me I won a lottery",
            "Someone asked for my UPI PIN",
            "I received a suspicious WhatsApp link",
            "A job offer asks me to pay money",
            "A stranger is asking for personal photos"
        ]
    )

    if st.button("🔍 Check Situation", use_container_width=True):

        if situation in [
            "Someone asked for my OTP",
            "Someone asked for my UPI PIN",
            "I received a suspicious WhatsApp link",
            "A job offer asks me to pay money",
            "A stranger is asking for personal photos"
        ]:

            st.error("🚨 HIGH RISK")

            st.write(
                "Do not share personal information or money. "
                "Verify the situation through an official source."
            )

        else:

            st.warning("⚠️ BE CAREFUL")

            st.write(
                "Verify the message or offer before taking any action."
            )

# ============================================================
# SAFETY QUIZ + SUPABASE STORAGE
# ============================================================

elif menu == "🎯 Safety Quiz":

    st.title("🎯 Online Safety Quiz")

    st.write(
        "Test your knowledge about smartphone and online safety."
    )

    # --------------------------------------------------------
    # USER NAME
    # --------------------------------------------------------

    user_name = st.text_input(
        "👩 Enter your name",
        placeholder="Enter your name before taking the quiz"
    )

    st.divider()

    # --------------------------------------------------------
    # QUESTIONS
    # --------------------------------------------------------

    q1 = st.radio(
        "1. Should you share your OTP with another person?",
        [
            "Yes",
            "No",
            "Only with friends",
            "Only on WhatsApp"
        ],
        key="q1"
    )

    q2 = st.radio(
        "2. What should you do if you receive a suspicious link?",
        [
            "Open it immediately",
            "Forward it to friends",
            "Avoid opening it and verify it",
            "Enter your bank details"
        ],
        key="q2"
    )

    q3 = st.radio(
        "3. What should you keep private while using UPI?",
        [
            "UPI PIN",
            "Mobile wallpaper",
            "App icon",
            "Contact name"
        ],
        key="q3"
    )

    q4 = st.radio(
        "4. What is a good practice for passwords?",
        [
            "Use the same password everywhere",
            "Use a strong and unique password",
            "Share passwords with friends",
            "Use your name as password"
        ],
        key="q4"
    )

    q5 = st.radio(
        "5. What should you do if someone asks for money for a fake job offer?",
        [
            "Pay immediately",
            "Send OTP",
            "Verify the offer and avoid suspicious payment",
            "Share bank password"
        ],
        key="q5"
    )

    st.divider()

    # --------------------------------------------------------
    # SUBMIT QUIZ
    # --------------------------------------------------------

    if st.button(
        "✅ Submit Quiz",
        use_container_width=True
    ):

        if not user_name.strip():

            st.warning("⚠️ Please enter your name first.")

        else:

            score = 0

            if q1 == "No":
                score += 1

            if q2 == "Avoid opening it and verify it":
                score += 1

            if q3 == "UPI PIN":
                score += 1

            if q4 == "Use a strong and unique password":
                score += 1

            if q5 == "Verify the offer and avoid suspicious payment":
                score += 1

            total = 5

            # ------------------------------------------------
            # SAVE DATA TO SUPABASE
            # ------------------------------------------------

            try:

                supabase.table("quiz_results").insert({
                    "user_name": user_name.strip(),
                    "score": score,
                    "total": total,
                    "created_at": datetime.now().isoformat()
                }).execute()

                st.success(
                    "✅ Quiz result saved successfully!"
                )

            except Exception as e:

                st.error(
                    "❌ Quiz result could not be saved."
                )

                st.write(e)

            # ------------------------------------------------
            # SHOW RESULT
            # ------------------------------------------------

            st.markdown(
                f"""
                <div class="card">
                    <h2>🎯 Your Score: {score}/{total}</h2>
                    <p>Participant: <b>{user_name}</b></p>
                </div>
                """,
                unsafe_allow_html=True
            )

            if score == 5:

                st.success(
                    "🌟 Excellent! You have strong online safety awareness."
                )
                st.balloons()

            elif score >= 3:

                st.info(
                    "👍 Good job! Keep learning about online safety."
                )

            else:

                st.warning(
                    "📚 Keep learning. The Online Safety section can help you."
                )

# ============================================================
# WOMEN SAFETY
# ============================================================

elif menu == "🚨 Women Safety":

    st.title("🚨 Women Safety")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>🚨 112</h3>
        <p>Emergency response number.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>👩 181</h3>
        <p>Women Helpline.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>💻 1930</h3>
        <p>Cyber Crime Helpline.</p>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("🛡️ Safety Tips")

    st.write("• Keep emergency contacts saved.")
    st.write("• Share your travel plan with a trusted person.")
    st.write("• Avoid sharing live location publicly.")
    st.write("• Do not share personal information with strangers.")
    st.write("• Contact authorities if you face an emergency.")

    st.subheader("📋 Emergency Contact Checklist")

    st.checkbox("Emergency number saved")
    st.checkbox("Trusted family member saved")
    st.checkbox("Phone screen lock enabled")
    st.checkbox("Important documents kept safely")

# ============================================================
# REPORT CYBER CRIME
# ============================================================

elif menu == "💻 Report Cyber Crime":

    st.title("💻 Report Cyber Crime")

    st.info(
        "If you have faced online financial fraud or cybercrime, "
        "report it through the official channels."
    )

    st.subheader("📞 Cyber Crime Helpline")

    st.write("**1930**")

    st.subheader("🌐 Official Portal")

    st.markdown(
        "[National Cyber Crime Reporting Portal](https://www.cybercrime.gov.in/)"
    )

    st.subheader("What to do if you become a victim?")

    st.write("1. Stay calm and collect the evidence.")
    st.write("2. Do not delete suspicious messages.")
    st.write("3. Contact your bank immediately in case of financial fraud.")
    st.write("4. Call 1930 for cyber financial fraud.")
    st.write("5. Report the incident through the official cybercrime portal.")

# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

🌸 <b>Digital Saheli</b><br>
Smartphone Usage & Online Safety for Women Self Help Group<br>
Community Engagement Project

</div>
""", unsafe_allow_html=True)
