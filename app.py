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
# SUPABASE CONNECTION
# ============================================================

SUPABASE_URL = st.secrets.get("SUPABASE_URL", "")
SUPABASE_KEY = st.secrets.get("SUPABASE_KEY", "")

supabase = None

if SUPABASE_URL and SUPABASE_KEY:
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    except Exception:
        supabase = None

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background-color: #fff8fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero {
    background: linear-gradient(135deg, #7b1e4d, #d84f8b);
    padding: 40px;
    border-radius: 22px;
    color: white;
    text-align: center;
    margin-bottom: 30px;
}

.hero h1 {
    font-size: 44px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 18px;
}

.card {
    background: white;
    padding: 22px;
    border-radius: 16px;
    margin-bottom: 18px;
    box-shadow: 0 3px 14px rgba(0,0,0,0.08);
}

.safe {
    background: #e8f7ee;
    padding: 18px;
    border-radius: 12px;
    border-left: 5px solid #2e9d62;
    margin: 15px 0;
}

.warning {
    background: #fff4d6;
    padding: 18px;
    border-radius: 12px;
    border-left: 5px solid #f0a500;
    margin: 15px 0;
}

.danger {
    background: #ffe8e8;
    padding: 18px;
    border-radius: 12px;
    border-left: 5px solid #d93025;
    margin: 15px 0;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🌸 Digital Saheli")
st.sidebar.write("Women Safety & Digital Awareness")

page = st.sidebar.radio(
    "Menu",
    [
        "🏠 Home",
        "📱 Smartphone Guide",
        "🚨 Identify Scams",
        "🔍 Scam Check",
        "📝 Report Scam",
        "☎️ Helplines",
        "🧠 Safety Quiz",
        "👩 Women Online Safety",
        "📊 Records"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    "Learn smartphone usage, identify scams, stay safe online "
    "and know where to report cybercrime."
)

# ============================================================
# HOME
# ============================================================

if page == "🏠 Home":

    st.markdown("""
    <div class="hero">
        <h1>🌸 Digital Saheli</h1>
        <p>Smartphone Usage & Online Safety for Women</p>
        <p>Learn • Protect • Report • Stay Safe</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Welcome to Digital Saheli 👩‍💻")

    st.write(
        "Digital Saheli is an awareness platform designed to help women "
        "use smartphones confidently and stay safe from online threats and scams."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>📱 Smartphone Learning</h3>
            <p>
            Learn calls, contacts, WhatsApp, Maps, apps,
            UPI and privacy settings.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>🚨 Scam Awareness</h3>
            <p>
            Learn how to identify OTP scams,
            phishing, fake jobs and payment fraud.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>📝 Report & Get Help</h3>
            <p>
            Find cybercrime reporting options
            and important emergency helplines.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("⚡ Quick Help")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Cyber Crime", "1930")

    with c2:
        st.metric("Emergency", "112")

    with c3:
        st.metric("Women Helpline", "181")

    with c4:
        st.metric("Child Helpline", "1098")

    st.markdown("""
    <div class="safe">
        <b>🛡️ Golden Rule:</b>
        Never share your OTP, UPI PIN, ATM PIN, password or banking
        information with anyone.
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# SMARTPHONE GUIDE
# ============================================================

elif page == "📱 Smartphone Guide":

    st.title("📱 Smartphone Usage Guide")

    st.write(
        "Basic smartphone information for women who want to use "
        "their phones safely and confidently."
    )

    topics = {
        "📞 How to Make a Call":
            "Open the Phone application → select a contact or enter a number → tap the Call button.",

        "👤 How to Save a Contact":
            "Open Contacts → tap Add Contact → enter name and phone number → tap Save.",

        "💬 How to Use WhatsApp":
            "Open WhatsApp → select a contact → type your message → tap Send. "
            "Never share OTPs or passwords through WhatsApp.",

        "📷 How to Send a Photo":
            "Open WhatsApp → open a chat → tap the attachment/gallery icon → select a photo → Send.",

        "📍 How to Use Google Maps":
            "Open Google Maps → search your destination → tap Directions → select walking, car or other travel mode.",

        "📲 How to Install Apps":
            "Download applications from the official Google Play Store or Apple App Store. "
            "Avoid unknown APK files and suspicious websites.",

        "🔐 How to Lock Your Phone":
            "Use a strong PIN, password, fingerprint or face lock to protect your phone.",

        "🔄 Keep Phone Updated":
            "Install operating-system and application updates regularly because updates often contain security fixes.",

        "💳 UPI Safety":
            "Never share your UPI PIN or OTP. Do not enter your UPI PIN just because someone says they are sending you money.",

        "🔒 Privacy Settings":
            "Check permissions given to applications. Camera, microphone, contacts and location should only be allowed when necessary.",

        "🌐 Safe Browsing":
            "Avoid suspicious websites and do not enter passwords or banking information on unknown websites.",

        "📶 Public Wi-Fi":
            "Avoid accessing sensitive banking services on unknown public Wi-Fi networks."
    }

    for title, information in topics.items():

        with st.expander(title):
            st.write(information)

    st.markdown("""
    <div class="warning">
        <b>⚠️ Important:</b><br>
        If an unknown person asks for your OTP, UPI PIN,
        password or remote access to your phone, do not provide it.
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# IDENTIFY SCAMS
# ============================================================

elif page == "🚨 Identify Scams":

    st.title("🚨 How to Identify Scams")

    st.write(
        "Scammers often create urgency, fear or excitement to make people act quickly."
    )

    scams = [
        (
            "🔐 OTP Scam",
            "Someone calls or messages asking for your OTP.",
            "Never share your OTP."
        ),

        (
            "💳 UPI Scam",
            "Someone asks you to enter your UPI PIN to receive money.",
            "Do not enter your UPI PIN to receive money."
        ),

        (
            "🎁 Lottery / Prize Scam",
            "You are told that you won a prize but must pay a fee first.",
            "Do not pay the fee."
        ),

        (
            "💼 Fake Job Scam",
            "A person promises a job and asks for registration or processing fees.",
            "Verify the company independently before paying."
        ),

        (
            "🔗 Phishing Link",
            "A message asks you to click a link to update KYC, bank or account information.",
            "Do not click suspicious links."
        ),

        (
            "📞 Fake Customer Care",
            "Someone pretends to be customer support and asks for confidential information.",
            "Find customer-care information from the official website or app."
        ),

        (
            "👮 Digital Arrest Scam",
            "A caller pretends to be a police or government official and threatens you.",
            "Stay calm and do not transfer money."
        ),

        (
            "👤 Fake Social Media Account",
            "Someone creates a fake account pretending to be you or someone you know.",
            "Verify the identity and report the fake account."
        ),

        (
            "📱 SIM / KYC Scam",
            "You receive an urgent message saying your SIM or KYC will be blocked.",
            "Do not click the provided link. Verify through the official provider."
        )
    ]

    for title, description, action in scams:

        st.markdown(f"""
        <div class="card">
            <h3>{title}</h3>
            <p><b>⚠️ Warning sign:</b> {description}</p>
            <p><b>✅ What to do:</b> {action}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="danger">
        <b>🚨 Remember:</b><br>
        If someone pressures you to act immediately,
        stop and verify the information before doing anything.
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# SCAM CHECK
# ============================================================

elif page == "🔍 Scam Check":

    st.title("🔍 Scam Check")

    st.write(
        "Paste a suspicious message below. The tool checks for common scam warning signs."
    )

    message = st.text_area(
        "📩 Enter suspicious message",
        height=150,
        placeholder="Example: Your bank account will be blocked. Click this link immediately..."
    )

    suspicious_words = [
        "otp",
        "upi pin",
        "pin",
        "urgent",
        "verify immediately",
        "account blocked",
        "account will be blocked",
        "lottery",
        "winner",
        "pay fee",
        "click here",
        "password",
        "kyc",
        "digital arrest",
        "police",
        "reward",
        "prize",
        "refund"
    ]

    if st.button("🔎 Check Message", use_container_width=True):

        if not message.strip():

            st.warning("Please enter a suspicious message first.")

        else:

            text = message.lower()

            found = [
                word for word in suspicious_words
                if word in text
            ]

            if found:

                st.error(
                    "⚠️ Possible scam warning signs detected."
                )

                st.write("The following warning signs were found:")

                for item in found:
                    st.write("•", item)

                st.markdown("""
                <div class="danger">
                    <b>Do NOT:</b><br>
                    ❌ Share OTP<br>
                    ❌ Share UPI PIN<br>
                    ❌ Send money<br>
                    ❌ Click unknown links<br>
                    ❌ Share passwords<br>
                    ❌ Give remote access to your phone
                </div>
                """, unsafe_allow_html=True)

            else:

                st.success(
                    "No common scam keywords were detected."
                )

                st.info(
                    "This does NOT guarantee that the message is safe. "
                    "Always verify suspicious messages independently."
                )

    st.markdown("---")

    st.subheader("🔎 Check Suspicious Information")

    st.write(
        "For official checking and reporting, use the National Cyber Crime Reporting Portal."
    )

    st.link_button(
        "🌐 Open Cyber Crime Portal",
        "https://cybercrime.gov.in/",
        use_container_width=True
    )

# ============================================================
# REPORT SCAM
# ============================================================

elif page == "📝 Report Scam":

    st.title("📝 Report a Scam / Cybercrime")

    st.markdown("""
    <div class="danger">
        <h3>🚨 If money has been lost</h3>
        <p>
        Contact <b>1930</b> as soon as possible and report the incident
        through the official cybercrime portal.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🌐 1. Report Cybercrime Online")

    st.write(
        "Use the official National Cyber Crime Reporting Portal "
        "to register a cybercrime complaint."
    )

    st.link_button(
        "📝 Report Cybercrime",
        "https://cybercrime.gov.in/",
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("🔎 2. Report / Check a Suspect")

    st.write(
        "The official portal provides facilities related to reporting "
        "suspicious cybercrime identifiers."
    )

    st.link_button(
        "🔎 Open Cyber Crime Portal",
        "https://cybercrime.gov.in/",
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("📋 3. Keep These Details Ready")

    details = [
        "📸 Screenshots of messages or conversations",
        "📞 Suspicious phone number",
        "📧 Suspicious email address",
        "🔗 Suspicious website or link",
        "💳 Transaction ID, if money was transferred",
        "📅 Date and time of incident",
        "💰 Amount lost, if applicable",
        "📄 Other relevant evidence"
    ]

    for item in details:
        st.write(item)

    st.markdown("""
    <div class="warning">
        <b>⚠️ Do not delete evidence.</b><br>
        Keep screenshots, transaction details and suspicious messages
        available when making a complaint.
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# HELPLINES
# ============================================================

elif page == "☎️ Helplines":

    st.title("☎️ Important Helpline Numbers")

    st.write(
        "📱 On a mobile phone, tap the Call button to open the phone dialer."
    )

    helplines = [
        (
            "1930",
            "Cyber Crime Helpline",
            "For cybercrime and financial cyber fraud assistance."
        ),

        (
            "112",
            "Emergency Helpline",
            "For immediate emergency assistance."
        ),

        (
            "181",
            "Women Helpline",
            "For women-related assistance."
        ),

        (
            "1098",
            "Child Helpline",
            "For children who need help."
        ),

        (
            "1915",
            "National Consumer Helpline",
            "For consumer-related complaints."
        )
    ]

    for number, name, description in helplines:

        st.markdown(f"""
        <div class="card">

            <h2>☎️ {number}</h2>

            <h3>{name}</h3>

            <p>{description}</p>

        </div>
        """, unsafe_allow_html=True)

        # DIRECT CALL BUTTON
        st.link_button(
            f"📞 Call {number}",
            f"tel:{number}",
            use_container_width=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="warning">
        <b>🚨 Emergency:</b> Call 112<br><br>
        <b>💻 Cybercrime / Financial Fraud:</b> Call 1930
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# SAFETY QUIZ
# ============================================================

elif page == "🧠 Safety Quiz":

    st.title("🧠 Online Safety Quiz")

    st.write(
        "Test your knowledge about smartphone and online safety."
    )

    questions = [
        {
            "question": "Someone asks you for your OTP. What should you do?",
            "options": [
                "Share it",
                "Never share it",
                "Share it if they sound professional",
                "Send it by WhatsApp"
            ],
            "answer": "Never share it"
        },

        {
            "question": "You receive a suspicious bank link. What should you do?",
            "options": [
                "Click immediately",
                "Forward it",
                "Open the official bank app or website yourself",
                "Enter your password"
            ],
            "answer": "Open the official bank app or website yourself"
        },

        {
            "question": "Which number is India's Cyber Crime Helpline?",
            "options": [
                "100",
                "181",
                "1930",
                "1098"
            ],
            "answer": "1930"
        },

        {
            "question": "Someone asks for your UPI PIN to send you money. What should you do?",
            "options": [
                "Give the PIN",
                "Enter the PIN",
                "Do not share the PIN",
                "Send the PIN by SMS"
            ],
            "answer": "Do not share the PIN"
        },

        {
            "question": "What should you do with an unknown suspicious link?",
            "options": [
                "Click it",
                "Open it on another phone",
                "Avoid clicking it",
                "Forward it"
            ],
            "answer": "Avoid clicking it"
        }
    ]

    selected_answers = []

    for i, item in enumerate(questions):

        st.subheader(f"Question {i + 1}")

        answer = st.radio(
            item["question"],
            item["options"],
            key=f"quiz_{i}"
        )

        selected_answers.append(answer)

    if st.button("✅ Submit Quiz", use_container_width=True):

        score = 0

        for i, item in enumerate(questions):

            if selected_answers[i] == item["answer"]:
                score += 1

        total = len(questions)

        st.success(f"🎉 Your Score: {score}/{total}")

        if score == total:

            st.balloons()

            st.success(
                "Excellent! You have very good digital safety awareness."
            )

        elif score >= 3:

            st.info(
                "Good job! Review the safety tips to improve further."
            )

        else:

            st.warning(
                "Please review the Smartphone Guide and Scam Awareness sections."
            )

        # SAVE RESULT TO SUPABASE

        if supabase:

            try:

                supabase.table("quiz_results").insert({
                    "score": score,
                    "total_questions": total,
                    "created_at": datetime.now().isoformat()
                }).execute()

                st.success(
                    "✅ Your quiz result has been saved."
                )

            except Exception:

                st.warning(
                    "Quiz result could not be saved. "
                    "Please check your Supabase table."
                )

# ============================================================
# WOMEN ONLINE SAFETY
# ============================================================

elif page == "👩 Women Online Safety":

    st.title("👩 Women Online Safety")

    safety_sections = {

        "🔐 Protect Personal Information":
            "Do not publicly share passwords, OTPs, banking details, "
            "Aadhaar information or your home address.",

        "📸 Social Media Safety":
            "Review your privacy settings and avoid accepting requests "
            "from unknown people.",

        "👤 Fake Profiles":
            "If someone creates a fake profile pretending to be you, "
            "take screenshots, report the account and block it.",

        "🚫 Online Harassment":
            "Do not engage with threatening messages. Save evidence, "
            "block the person and report the account.",

        "📍 Location Privacy":
            "Avoid publicly sharing your live location or daily routine.",

        "🔑 Strong Passwords":
            "Use unique and strong passwords for important accounts "
            "and enable two-factor authentication.",

        "📱 Phone Security":
            "Use a screen lock, update your phone regularly and install "
            "apps only from trusted sources.",

        "💳 Banking Safety":
            "Never share OTP, UPI PIN, ATM PIN or banking passwords with anyone."
    }

    for title, information in safety_sections.items():

        with st.expander(title):

            st.write(information)

    st.markdown("""
    <div class="safe">
        <b>🛡️ Stay Safe Online</b><br>
        Stop • Think • Verify • Then Act
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# RECORDS
# ============================================================

elif page == "📊 Records":

    st.title("📊 Quiz Records")

    if supabase:

        try:

            response = (
                supabase
                .table("quiz_results")
                .select("*")
                .order("created_at", desc=True)
                .execute()
            )

            records = response.data

            if records:

                df = pd.DataFrame(records)

                st.dataframe(
                    df,
                    use_container_width=True,
                    hide_index=True
                )

                st.metric(
                    "Total Quiz Attempts",
                    len(df)
                )

            else:

                st.info(
                    "No quiz records available yet."
                )

        except Exception as e:

            st.error(
                "Unable to load records. "
                "Please check your Supabase table."
            )

    else:

        st.warning(
            "Supabase is not connected."
        )

        st.write(
            "Add SUPABASE_URL and SUPABASE_KEY in Streamlit Secrets."
        )

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "🌸 Digital Saheli | Smartphone Usage & Online Safety for Women"
)
