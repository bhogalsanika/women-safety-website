import streamlit as st
from supabase import create_client
from datetime import datetime

# ============================================================
# DIGITAL SAHELI
# Smartphone Usage & Online Safety for Women
# CEP Project
# ============================================================

st.set_page_config(
    page_title="Digital Saheli",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# SUPABASE BACKEND
# ============================================================

@st.cache_resource
def init_supabase():
    try:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
        return create_client(url, key)
    except Exception:
        return None

supabase = init_supabase()

# ============================================================
# MOBILE RESPONSIVE CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background: #fff8fb;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

/* Header */

.header {
    background: linear-gradient(135deg, #f8d7e6, #eadcf8);
    padding: 35px;
    border-radius: 25px;
    text-align: center;
    margin-bottom: 25px;
}

.header h1 {
    color: #8b2457;
    font-size: 46px;
    margin-bottom: 5px;
}

.header p {
    color: #4d4d4d;
    font-size: 19px;
}

/* Cards */

.card {
    background: white;
    border-radius: 20px;
    padding: 25px;
    margin-bottom: 18px;
    border: 1px solid #efd9e4;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    min-height: 190px;
}

.card h3 {
    color: #8b2457;
}

.card p {
    color: #555;
}

/* Safety box */

.safety-box {
    background: #fff0c2;
    padding: 22px;
    border-radius: 18px;
    margin: 20px 0;
}

/* Emergency */

.emergency-box {
    background: #ffe5e5;
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    border: 1px solid #f5c2c2;
}

/* Section title */

.section-title {
    color: #8b2457;
    font-size: 30px;
    font-weight: bold;
    margin-top: 15px;
}

/* Buttons */

.stButton > button {
    border-radius: 12px;
    min-height: 45px;
}

/* Footer */

.footer {
    text-align: center;
    color: #777;
    padding: 25px;
}

/* ==========================================================
   MOBILE
   ========================================================== */

@media only screen and (max-width: 768px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
        padding-top: 1rem;
    }

    .header {
        padding: 22px 15px;
        border-radius: 18px;
    }

    .header h1 {
        font-size: 32px;
    }

    .header p {
        font-size: 16px;
    }

    .card {
        padding: 18px;
        min-height: auto;
        border-radius: 16px;
    }

    .card h3 {
        font-size: 21px;
    }

    .section-title {
        font-size: 25px;
    }

    .emergency-box {
        padding: 18px 10px;
        margin-bottom: 12px;
    }

    .emergency-box h1 {
        font-size: 35px;
    }

    .emergency-box h2 {
        font-size: 25px;
    }

    h1 {
        font-size: 30px !important;
    }

    h2 {
        font-size: 25px !important;
    }

    h3 {
        font-size: 21px !important;
    }

    p {
        font-size: 15px;
    }

    .stButton > button {
        width: 100%;
        min-height: 48px;
    }

}

/* Very small phones */

@media only screen and (max-width: 480px) {

    .header h1 {
        font-size: 28px;
    }

    .header p {
        font-size: 14px;
    }

    .card {
        padding: 15px;
    }

    .safety-box {
        padding: 17px;
    }

}

</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    "<h1 style='text-align:center;color:#8b2457;'>🌸 Digital Saheli</h1>",
    unsafe_allow_html=True
)

st.sidebar.caption("Smartphone & Online Safety for Women")

language = st.sidebar.selectbox(
    "🌐 Language",
    ["English", "हिंदी", "मराठी"]
)

st.sidebar.divider()

page = st.sidebar.radio(
    "📌 Menu",
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

st.sidebar.divider()

st.sidebar.info(
    "💡 Learn digital skills and stay safe online."
)

# ============================================================
# HOME
# ============================================================

if page == "🏠 Home":

    st.markdown("""
    <div class="header">
        <h1>🌸 Digital Saheli</h1>
        <p><b>Learn • Protect • Stay Connected</b></p>
        <p>
        A simple digital safety guide designed to help women
        use smartphones and online services safely.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        "<div class='section-title'>👋 Welcome!</div>",
        unsafe_allow_html=True
    )

    st.write(
        "Explore smartphone skills, online safety tips, scam awareness "
        "and emergency support."
    )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
        <div class="card">
            <h3>📱 Smartphone Learning</h3>
            <p>
            Learn WhatsApp, UPI, Google Maps, camera,
            contacts, apps and phone settings.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "📱 Start Learning",
            use_container_width=True,
            key="home_learning"
        ):
            st.info(
                "Select '📱 Smartphone Learning' from the menu."
            )

    with col2:

        st.markdown("""
        <div class="card">
            <h3>🛡️ Online Safety</h3>
            <p>
            Learn about OTP, passwords, fake links,
            privacy, phishing and online payments.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "🛡️ Learn Safety",
            use_container_width=True,
            key="home_safety"
        ):
            st.info(
                "Select '🛡️ Online Safety' from the menu."
            )

    with col3:

        st.markdown("""
        <div class="card">
            <h3>🚨 Women Safety</h3>
            <p>
            Find emergency numbers, safety tips,
            cybercrime help and reporting information.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "🚨 Get Help",
            use_container_width=True,
            key="home_help"
        ):
            st.info(
                "Select '🚨 Women Safety' from the menu."
            )

    st.write("")

    st.markdown("""
    <div class="safety-box">
        💡 <b>Today's Safety Tip</b><br><br>
        Never share your OTP, UPI PIN, password or banking details
        with anyone over phone, message or social media.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🎯 Quick Actions")

    a, b, c, d = st.columns(4)

    with a:
        st.button(
            "📱 Learn Smartphone",
            use_container_width=True,
            key="quick_phone"
        )

    with b:
        st.button(
            "⚠️ Check Scam",
            use_container_width=True,
            key="quick_scam"
        )

    with c:
        st.button(
            "🎯 Take Quiz",
            use_container_width=True,
            key="quick_quiz"
        )

    with d:
        st.button(
            "🚨 Safety Help",
            use_container_width=True,
            key="quick_help"
        )

# ============================================================
# SMARTPHONE LEARNING
# ============================================================

elif page == "📱 Smartphone Learning":

    st.title("📱 Smartphone Learning")

    st.write(
        "Learn common smartphone features through simple step-by-step guides."
    )

    topic = st.selectbox(
        "Choose a topic",
        [
            "💬 WhatsApp",
            "💳 UPI Payments",
            "📍 Google Maps",
            "👤 Contacts",
            "📷 Camera & Photos",
            "📲 Apps & Updates",
            "⚙️ Phone Settings"
        ]
    )

    st.divider()

    if topic == "💬 WhatsApp":

        st.header("💬 WhatsApp")

        st.write(
            "WhatsApp can be used for messages, calls, photos and videos."
        )

        with st.expander("📖 How to send a message"):
            st.markdown("""
            1. Open WhatsApp.
            2. Select a contact.
            3. Type your message.
            4. Press Send.
            """)

        with st.expander("🔒 WhatsApp Safety"):
            st.markdown("""
            - Do not open suspicious links.
            - Do not share OTPs.
            - Check unknown group messages carefully.
            - Use privacy settings.
            """)

    elif topic == "💳 UPI Payments":

        st.header("💳 UPI Payments")

        st.write(
            "UPI allows users to make digital payments using a smartphone."
        )

        with st.expander("📖 How to make a UPI payment"):
            st.markdown("""
            1. Open your trusted UPI app.
            2. Select the person or merchant.
            3. Enter the amount.
            4. Verify the receiver's name.
            5. Enter your UPI PIN only when making the payment.
            """)

        st.warning(
            "⚠️ Never share your UPI PIN with anyone."
        )

    elif topic == "📍 Google Maps":

        st.header("📍 Google Maps")

        with st.expander("📖 How to find a place"):
            st.markdown("""
            1. Open Google Maps.
            2. Search the destination.
            3. Select Directions.
            4. Choose your travel method.
            5. Follow the route.
            """)

        st.info(
            "📍 Share your live location only with trusted people."
        )

    elif topic == "👤 Contacts":

        st.header("👤 Contacts")

        st.markdown("""
        ### Save a contact

        1. Open the Contacts app.
        2. Tap Add Contact.
        3. Enter the name.
        4. Enter the phone number.
        5. Tap Save.

        ### Safety Tip

        Save important family and emergency contacts in your phone.
        """)

    elif topic == "📷 Camera & Photos":

        st.header("📷 Camera & Photos")

        st.markdown("""
        ### Camera

        - Take photos and videos.
        - Check the camera before taking sensitive photos.

        ### Photos

        - Keep important photos backed up.
        - Avoid sharing private photos with unknown people.
        - Review apps that have access to your photos.
        """)

    elif topic == "📲 Apps & Updates":

        st.header("📲 Apps & Updates")

        st.markdown("""
        ### Safe App Usage

        ✅ Download apps from trusted app stores.

        ✅ Keep apps updated.

        ✅ Remove unused apps.

        ❌ Avoid unknown APK files.

        ❌ Do not give unnecessary permissions to apps.
        """)

    elif topic == "⚙️ Phone Settings":

        st.header("⚙️ Important Phone Settings")

        st.markdown("""
        Check these settings regularly:

        🔒 Screen lock / PIN

        📍 Location permissions

        🎤 Microphone permissions

        📷 Camera permissions

        👤 App permissions

        🔐 Privacy settings

        🔄 Software updates
        """)

# ============================================================
# ONLINE SAFETY
# ============================================================

elif page == "🛡️ Online Safety":

    st.title("🛡️ Online Safety")

    st.write(
        "Simple rules to protect your identity, accounts and money."
    )

    safety_topic = st.selectbox(
        "Select a topic",
        [
            "🔐 Password Safety",
            "🔢 OTP Safety",
            "🔗 Fake Links & Phishing",
            "💳 Payment Safety",
            "📱 Social Media Privacy",
            "👤 Fake Profiles",
            "📩 Suspicious Messages",
            "🎣 Online Scams"
        ]
    )

    st.divider()

    if safety_topic == "🔐 Password Safety":

        st.header("🔐 Password Safety")

        st.markdown("""
        ### ✅ Do

        - Use a strong and unique password.
        - Use different passwords for important accounts.
        - Enable two-factor authentication where available.

        ### ❌ Don't

        - Don't share your password.
        - Don't use very simple passwords.
        - Don't write passwords where everyone can see them.
        """)

    elif safety_topic == "🔢 OTP Safety":

        st.header("🔢 OTP Safety")

        st.error(
            "🚫 NEVER SHARE YOUR OTP WITH ANYONE."
        )

        st.write(
            "An OTP is meant for verification. If someone calls "
            "and asks for your OTP, do not provide it."
        )

    elif safety_topic == "🔗 Fake Links & Phishing":

        st.header("🔗 Fake Links & Phishing")

        st.markdown("""
        ### Warning signs

        ⚠️ Unknown sender

        ⚠️ Urgent message

        ⚠️ Prize or reward

        ⚠️ KYC/update warning

        ⚠️ Suspicious website address

        ### Remember

        **STOP → CHECK → DON'T CLICK → REPORT**
        """)

    elif safety_topic == "💳 Payment Safety":

        st.header("💳 Online Payment Safety")

        st.markdown("""
        ✅ Check the receiver's name.

        ✅ Keep your UPI PIN private.

        ✅ Verify payment requests.

        ❌ Never share OTP.

        ❌ Never share UPI PIN.

        ❌ Don't scan unknown QR codes.
        """)

    elif safety_topic == "📱 Social Media Privacy":

        st.header("📱 Social Media Privacy")

        st.markdown("""
        ### Protect your account

        - Keep your account private when appropriate.
        - Accept requests from people you know.
        - Avoid posting sensitive personal information.
        - Be careful with location sharing.
        - Review privacy settings regularly.
        """)

    elif safety_topic == "👤 Fake Profiles":

        st.header("👤 Fake Profiles")

        st.markdown("""
        A suspicious profile may have:

        ⚠️ Very few photos

        ⚠️ New account

        ⚠️ Few genuine connections

        ⚠️ Requests for money

        ⚠️ Requests for private photos or information

        **Do not send money or sensitive information.**
        """)

    elif safety_topic == "📩 Suspicious Messages":

        st.header("📩 Suspicious Messages")

        st.error(
            "STOP → DON'T CLICK → DON'T SHARE → REPORT"
        )

        st.write(
            "Verify suspicious messages using the official website "
            "or official contact details of the organisation."
        )

    elif safety_topic == "🎣 Online Scams":

        st.header("🎣 Common Online Scams")

        st.markdown("""
        Common examples include:

        🏦 Fake bank/KYC calls

        🎁 Lottery/prize scams

        💼 Fake job offers

        💳 Payment/UPI scams

        📱 Fake customer-care numbers

        🔗 Phishing links

        👤 Fake social-media accounts
        """)

# ============================================================
# SCAM DETECTOR
# ============================================================

elif page == "⚠️ Scam Detector":

    st.title("⚠️ Scam Detector")

    st.write(
        "Choose a situation and learn what you should do."
    )

    situation = st.selectbox(
        "What happened?",
        [
            "🏦 Someone called asking for OTP",
            "🔗 I received a KYC update link",
            "🎁 I received a lottery/prize message",
            "💳 Someone asked for my UPI PIN",
            "📱 I received a suspicious WhatsApp link",
            "💼 I received a job offer asking for money",
            "👤 A stranger is asking for personal photos"
        ]
    )

    if st.button(
        "🔍 Check Situation",
        use_container_width=True,
        key="check_scam"
    ):

        st.divider()

        if situation == "🏦 Someone called asking for OTP":

            st.error("🚨 HIGH RISK — DO NOT SHARE OTP")

            st.markdown("""
            **What to do:**

            1. Do not share the OTP.
            2. End the call.
            3. Contact the organisation using its official contact details.
            """)

        elif situation == "🔗 I received a KYC update link":

            st.warning("⚠️ POSSIBLE PHISHING")

            st.markdown("""
            **What to do:**

            1. Don't click the link.
            2. Don't enter banking information.
            3. Verify through the organisation's official website/app.
            """)

        elif situation == "🎁 I received a lottery/prize message":

            st.error("🎁 POSSIBLE SCAM")

            st.markdown("""
            Do not pay a fee or provide banking/personal information
            to claim an unexpected prize.
            """)

        elif situation == "💳 Someone asked for my UPI PIN":

            st.error("🚨 NEVER SHARE YOUR UPI PIN")

            st.write(
                "Your UPI PIN is private. Do not share it with anyone."
            )

        elif situation == "📱 I received a suspicious WhatsApp link":

            st.warning("🔗 DON'T CLICK")

            st.write(
                "Verify the sender and message before opening anything."
            )

        elif situation == "💼 I received a job offer asking for money":

            st.error("💼 POSSIBLE JOB SCAM")

            st.write(
                "Be careful if someone asks for money or sensitive "
                "information before offering a job."
            )

        elif situation == "👤 A stranger is asking for personal photos":

            st.error("🚨 DON'T SHARE PRIVATE PHOTOS")

            st.write(
                "Block/report suspicious accounts and talk to a "
                "trusted person if you feel threatened."
            )

# ============================================================
# QUIZ + DATABASE STORAGE
# ============================================================

elif page == "🎯 Safety Quiz":

    st.title("🎯 Online Safety Quiz")

    st.write(
        "Answer the questions and check your score."
    )

    # --------------------------------------------------------
    # NAME
    # --------------------------------------------------------

    user_name = st.text_input(
        "👩 Enter your name",
        placeholder="Enter your name",
        key="quiz_name"
    )

    # --------------------------------------------------------
    # QUESTIONS
    # --------------------------------------------------------

    q1 = st.radio(
        "1️⃣ Should you share your OTP with someone who calls you?",
        ["Yes", "No"],
        key="quiz_q1"
    )

    q2 = st.radio(
        "2️⃣ Should you share your UPI PIN with anyone?",
        ["Yes", "No"],
        key="quiz_q2"
    )

    q3 = st.radio(
        "3️⃣ What should you do with a suspicious link?",
        [
            "Click immediately",
            "Ignore and verify",
            "Forward to friends"
        ],
        key="quiz_q3"
    )

    q4 = st.radio(
        "4️⃣ Is a strong password important?",
        ["Yes", "No"],
        key="quiz_q4"
    )

    q5 = st.radio(
        "5️⃣ Should you accept every unknown social-media request?",
        ["Yes", "No"],
        key="quiz_q5"
    )

    # --------------------------------------------------------
    # SUBMIT
    # --------------------------------------------------------

    if st.button(
        "🎯 Submit Quiz",
        use_container_width=True,
        key="submit_quiz"
    ):

        if not user_name.strip():

            st.warning(
                "⚠️ Please enter your name before submitting the quiz."
            )

        else:

            score = 0

            if q1 == "No":
                score += 1

            if q2 == "No":
                score += 1

            if q3 == "Ignore and verify":
                score += 1

            if q4 == "Yes":
                score += 1

            if q5 == "No":
                score += 1

            total = 5

            # =================================================
            # SAVE TO SUPABASE
            # =================================================

            if supabase is not None:

                try:

                    supabase.table("quiz_results").insert({
                        "user_name": user_name.strip(),
                        "score": score,
                        "total": total,
                        "created_at": datetime.now().isoformat()
                    }).execute()

                    st.success(
                        "✅ Your quiz result has been saved!"
                    )

                except Exception as e:

                    st.error(
                        "❌ Quiz result could not be saved to database."
                    )

                    st.caption(
                        "Check your Supabase table name and column names."
                    )

            else:

                st.warning(
                    "⚠️ Supabase connection is not configured."
                )

            # =================================================
            # RESULT
            # =================================================

            st.divider()

            st.subheader(
                f"🏆 Your Score: {score}/{total}"
            )

            st.write(
                f"👩 Participant: **{user_name.strip()}**"
            )

            if score == 5:

                st.success(
                    "🌟 Excellent! You understand the basic online safety rules."
                )

                st.balloons()

            elif score >= 3:

                st.info(
                    "👍 Good job! Keep learning and practicing safe digital habits."
                )

            else:

                st.warning(
                    "📚 Keep learning. Review the Online Safety section and try again."
                )

# ============================================================
# WOMEN SAFETY
# ============================================================

elif page == "🚨 Women Safety":

    st.title("🚨 Women Safety & Emergency Help")

    st.write(
        "Keep important emergency information easily accessible."
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
        <div class="emergency-box">
        <h1>🚨</h1>
        <h2>112</h2>
        <p>Emergency</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="emergency-box">
        <h1>👩</h1>
        <h2>181</h2>
        <p>Women Helpline</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown("""
        <div class="emergency-box">
        <h1>💻</h1>
        <h2>1930</h2>
        <p>Cyber Crime</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    st.subheader("📍 Digital Location Safety")

    st.markdown("""
    - Share live location only with trusted people.
    - Avoid posting your real-time location publicly.
    - Review location permissions for apps.
    - Turn off unnecessary location sharing.
    """)

    st.subheader("📞 Emergency Contact Checklist")

    st.checkbox(
        "Save a trusted family member's number",
        key="emergency_family"
    )

    st.checkbox(
        "Save an emergency contact",
        key="emergency_contact"
    )

    st.checkbox(
        "Keep phone screen lock enabled",
        key="emergency_lock"
    )

    st.checkbox(
        "Keep important phone numbers accessible",
        key="emergency_numbers"
    )

    st.info(
        "If you are in immediate danger, contact emergency services."
    )

# ============================================================
# REPORT CYBER CRIME
# ============================================================

elif page == "💻 Report Cyber Crime":

    st.title("💻 Report Cyber Crime")

    st.write(
        "If you experience online fraud or cybercrime, use official "
        "government reporting channels."
    )

    st.warning(
        "⚠️ Do not share OTP, PIN or passwords with anyone claiming "
        "to help you file a complaint."
    )

    st.subheader("🚨 Cyber Crime Helpline")

    st.markdown("### 📞 1930")

    st.write(
        "For cyber financial fraud, contact the cybercrime helpline "
        "as soon as possible."
    )

    st.subheader("🌐 Official Cyber Crime Portal")

    st.link_button(
        "💻 Open National Cyber Crime Reporting Portal",
        "https://www.cybercrime.gov.in/"
    )

    st.subheader("📝 If You Become a Victim")

    st.markdown("""
    1. Stay calm.
    2. Do not delete important evidence.
    3. Take screenshots where appropriate.
    4. Contact your bank immediately for financial fraud.
    5. Contact 1930 for cyber financial fraud.
    6. Use the official cybercrime reporting portal.
    """)

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown("""
<div class="footer">

🌸 <b>Digital Saheli</b><br>

CEP Project — Smartphone Usage & Online Safety for Women<br>

Learn • Protect • Stay Connected

</div>
""", unsafe_allow_html=True)
