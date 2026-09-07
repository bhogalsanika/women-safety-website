import streamlit as st
from supabase import create_client
import pandas as pd
from datetime import datetime

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Digital Saheli - Women Safety",
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

.main {
    background-color: #fff7fb;
}

.block-container {
    padding-top: 2rem;
}

.hero {
    background: linear-gradient(135deg, #8e245d, #d94f8a);
    padding: 35px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 8px;
}

.hero p {
    font-size: 18px;
}

.card {
    background: white;
    padding: 22px;
    border-radius: 15px;
    margin-bottom: 15px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.08);
}

.warning {
    background: #fff3cd;
    padding: 18px;
    border-radius: 12px;
    border-left: 5px solid #ffb300;
}

.safe {
    background: #e8f7ee;
    padding: 18px;
    border-radius: 12px;
    border-left: 5px solid #2e9d62;
}

.danger {
    background: #ffe8e8;
    padding: 18px;
    border-radius: 12px;
    border-left: 5px solid #d93025;
}

.big-number {
    font-size: 28px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🌸 Digital Saheli")

st.sidebar.write("Women Safety & Digital Awareness")

page = st.sidebar.radio(
    "Navigation",
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
    "Digital Saheli helps women learn safe smartphone usage "
    "and protect themselves from online scams."
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
        "This website helps women understand smartphone usage, "
        "identify online scams, report cybercrime and stay safe online."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>📱 Learn Smartphone</h3>
        <p>Learn basic smartphone features, WhatsApp, Maps, UPI and privacy settings.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>🚨 Detect Scams</h3>
        <p>Learn how to identify fake messages, links, calls and payment scams.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>📝 Report Cybercrime</h3>
        <p>Find official cybercrime reporting options and important helpline numbers.</p>
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

# ============================================================
# SMARTPHONE GUIDE
# ============================================================

elif page == "📱 Smartphone Guide":

    st.title("📱 Smartphone Usage Guide")

    st.write(
        "A simple guide to help beginners use smartphones safely and confidently."
    )

    topics = {
        "📞 Making a Phone Call":
            "Open the Phone app → enter/select the contact → tap the call button.",

        "👤 Save a Contact":
            "Open Contacts → Add Contact → enter name and number → Save.",

        "💬 WhatsApp":
            "Open WhatsApp → select a contact → type your message → Send. "
            "Do not share OTPs or sensitive information.",

        "📷 Send Photos":
            "Open WhatsApp → open a chat → tap attachment/gallery → select photo → Send.",

        "📍 Google Maps":
            "Open Google Maps → search the destination → tap Directions → choose your travel mode.",

        "📲 Install an App":
            "Use the official Google Play Store/App Store. "
            "Avoid downloading APK files from unknown websites.",

        "🔐 Screen Lock":
            "Use a PIN, password or biometric lock. Avoid easy PINs such as 1234.",

        "🔄 Update Apps":
            "Keep Android/iOS and important applications updated to receive security fixes.",

        "💳 UPI Safety":
            "Never share your UPI PIN or OTP. Remember: you normally enter your UPI PIN "
            "when making a payment, not when receiving money.",

        "🔒 Privacy Settings":
            "Check app permissions for camera, microphone, contacts and location. "
            "Give permissions only when necessary."
    }

    for title, explanation in topics.items():
        with st.expander(title):
            st.write(explanation)

    st.markdown("""
    <div class="safe">
    <b>✅ Remember:</b><br>
    Never share your OTP, UPI PIN, ATM PIN, password or banking details with anyone.
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# IDENTIFY SCAMS
# ============================================================

elif page == "🚨 Identify Scams":

    st.title("🚨 How to Identify an Online Scam")

    st.write("Look for these warning signs before clicking, paying or sharing information.")

    scams = [
        (
            "🔐 OTP Scam",
            "Someone asks for your OTP and says they need it to verify your account.",
            "Never share OTP with anyone."
        ),
        (
            "💳 UPI Scam",
            "Someone sends a payment request and asks you to enter your UPI PIN to receive money.",
            "Never enter UPI PIN to receive money."
        ),
        (
            "🎁 Prize Scam",
            "You receive a message saying you won a lottery/prize and must pay a fee.",
            "Do not pay. It is likely a scam."
        ),
        (
            "💼 Fake Job Scam",
            "Someone promises a job but asks for registration or processing fees.",
            "Verify the company independently."
        ),
        (
            "🔗 Phishing Link",
            "A message asks you to urgently click a link to update your bank/account.",
            "Do not click suspicious links."
        ),
        (
            "📞 Fake Customer Care",
            "A person pretends to be customer support and asks for OTP, PIN or remote access.",
            "Use customer-care numbers from official websites/apps."
        ),
        (
            "👮 Digital Arrest Scam",
            "A caller pretends to be police/government officials and threatens arrest unless money is paid.",
            "Stay calm. Do not transfer money."
        ),
        (
            "📱 Fake Social Media Profile",
            "Someone creates a profile pretending to be a friend or known person.",
            "Verify the person through another trusted method."
        )
    ]

    for name, description, action in scams:
        st.markdown(f"""
        <div class="card">
        <h3>{name}</h3>
        <p><b>⚠️ What happens:</b> {description}</p>
        <p><b>✅ What to do:</b> {action}</p>
        </div>
        """, unsafe_allow_html=True)

    st.warning(
        "If a message creates panic or asks you to act immediately, stop and verify it first."
    )

# ============================================================
# SCAM CHECK
# ============================================================

elif page == "🔍 Scam Check":

    st.title("🔍 Scam Check")

    st.write(
        "Use this checklist to decide whether a message, call or offer looks suspicious."
    )

    message = st.text_area(
        "Paste the suspicious message here:",
        placeholder="Example: Your bank account will be blocked. Click this link immediately..."
    )

    suspicious_words = [
        "otp",
        "upi pin",
        "urgent",
        "verify immediately",
        "account blocked",
        "lottery",
        "winner",
        "pay fee",
        "click here",
        "password",
        "kyc",
        "digital arrest"
    ]

    if st.button("🔎 Check Message"):

        if not message.strip():
            st.warning("Please enter a message first.")
        else:

            text = message.lower()

            found = [
                word for word in suspicious_words
                if word in text
            ]

            if found:

                st.error("⚠️ This message contains possible scam warning signs.")

                st.write("Possible warning signs detected:")

                for item in found:
                    st.write("•", item)

                st.markdown("""
                <div class="danger">
                <b>Do not:</b><br>
                ❌ Share OTP<br>
                ❌ Share UPI PIN<br>
                ❌ Send money<br>
                ❌ Click unknown links<br>
                ❌ Give remote access to your phone
                </div>
                """, unsafe_allow_html=True)

            else:

                st.success(
                    "No common scam keywords were detected, but this does NOT guarantee that the message is safe."
                )

    st.markdown("---")

    st.subheader("🔎 Check Official Suspect Repository")

    st.write(
        "You can also check suspicious mobile numbers, email IDs, bank accounts "
        "and website URLs through the Government cybercrime portal."
    )

    st.link_button(
        "🔎 Open I4C Suspect Repository",
        "https://cybercrime.gov.in/"
    )

# ============================================================
# REPORT SCAM
# ============================================================

elif page == "📝 Report Scam":

    st.title("📝 Report Cybercrime / Scam")

    st.markdown("""
    <div class="danger">
    <h3>🚨 Financial Fraud?</h3>
    <p>Contact <b>1930</b> immediately and report the incident through the official cybercrime portal.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("1️⃣ Report Cyber Crime")

    st.write(
        "Use the Government of India's National Cyber Crime Reporting Portal "
        "to submit a cybercrime complaint."
    )

    st.link_button(
        "🌐 Report Cyber Crime",
        "https://cybercrime.gov.in/"
    )

    st.subheader("2️⃣ Report a Suspect")

    st.write(
        "The portal also provides options for reporting suspicious "
        "phone numbers, URLs, email IDs and other identifiers."
    )

    st.link_button(
        "🔎 Report Suspect",
        "https://cybercrime.gov.in/"
    )

    st.subheader("3️⃣ What Information Should You Keep?")

    st.write("""
    • Screenshot of suspicious message  
    • Phone number / email ID  
    • Website or message link  
    • Transaction ID, if money was lost  
    • Date and time of incident  
    • Bank/payment details related to the transaction  
    • Any other evidence
    """)

    st.warning(
        "Do not delete important evidence before reporting the incident."
    )

# ============================================================
# HELPLINES
# ============================================================

elif page == "☎️ Helplines":

    st.title("☎️ Important Helpline Numbers")

    helplines = [
        ("1930", "Cyber Crime Helpline", "For cyber financial fraud and cybercrime assistance."),
        ("112", "Emergency", "For immediate emergency assistance."),
        ("181", "Women Helpline", "Women-related assistance."),
        ("1098", "Child Helpline", "For children in need of help."),
        ("1915", "National Consumer Helpline", "For consumer-related complaints.")
    ]

    for number, name, description in helplines:

        st.markdown(f"""
        <div class="card">
        <div class="big-number">☎️ {number}</div>
        <h3>{name}</h3>
        <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)

    st.info(
        "In an immediate emergency, use 112. For cybercrime/financial cyber fraud, use 1930 and the official cybercrime portal."
    )

# ============================================================
# QUIZ
# ============================================================

elif page == "🧠 Safety Quiz":

    st.title("🧠 Online Safety Quiz")

    st.write("Test your digital safety knowledge.")

    questions = [
        {
            "q": "Someone asks for your OTP. What should you do?",
            "options": [
                "Share it",
                "Never share it",
                "Send it only if they sound professional",
                "Post it in chat"
            ],
            "answer": "Never share it"
        },
        {
            "q": "You receive a suspicious bank link. What should you do?",
            "options": [
                "Click immediately",
                "Forward it to everyone",
                "Open the official bank app/website yourself",
                "Enter your password"
            ],
            "answer": "Open the official bank app/website yourself"
        },
        {
            "q": "Which number is the Cyber Crime Helpline in India?",
            "options": [
                "100",
                "181",
                "1930",
                "1098"
            ],
            "answer": "1930"
        },
        {
            "q": "What should you do if someone asks for your UPI PIN to receive money?",
            "options": [
                "Give the PIN",
                "Enter the PIN",
                "Do not share the PIN",
                "Send the PIN by SMS"
            ],
            "answer": "Do not share the PIN"
        }
    ]

    score = 0

    answers = []

    for i, item in enumerate(questions):

        st.subheader(f"Question {i + 1}")

        selected = st.radio(
            item["q"],
            item["options"],
            key=f"question_{i}"
        )

        answers.append(selected)

    if st.button("✅ Submit Quiz"):

        for i, item in enumerate(questions):

            if answers[i] == item["answer"]:
                score += 1

        st.success(f"Your Score: {score}/{len(questions)}")

        if score == len(questions):
            st.balloons()
            st.success("Excellent! You have strong digital safety awareness.")
        elif score >= 2:
            st.info("Good job! Review the safety tips once more.")
        else:
            st.warning("Please review the online safety section again.")

        # Store quiz record in Supabase
        if supabase:

            try:

                supabase.table("quiz_results").insert({
                    "score": score,
                    "total_questions": len(questions),
                    "created_at": datetime.now().isoformat()
                }).execute()

                st.info("Quiz result saved successfully.")

            except Exception as e:
                st.warning("Quiz result could not be saved to database.")

# ============================================================
# WOMEN ONLINE SAFETY
# ============================================================

elif page == "👩 Women Online Safety":

    st.title("👩 Women Online Safety")

    sections = {
        "🔐 Protect Personal Information":
            "Avoid sharing your Aadhaar number, bank details, OTP, passwords, home address and other sensitive information publicly.",

        "📸 Social Media Safety":
            "Keep profiles private when appropriate. Review followers and avoid accepting unknown requests.",

        "👤 Fake Profiles":
            "If someone creates a fake profile using your identity, save screenshots and report the profile through the platform.",

        "🚫 Online Harassment":
            "Do not engage with threatening messages. Block the account, preserve evidence and report the incident.",

        "📍 Location Privacy":
            "Avoid publicly sharing your live location or routine unless necessary.",

        "🔑 Strong Password":
            "Use long, unique passwords and enable two-factor authentication whenever possible.",

        "📱 Phone Security":
            "Use screen lock, keep software updated and avoid installing apps from unknown sources."
    }

    for title, text in sections.items():

        with st.expander(title):
            st.write(text)

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

            data = response.data

            if data:
                df = pd.DataFrame(data)
                st.dataframe(
                    df,
                    use_container_width=True
                )
            else:
                st.info("No quiz records available yet.")

        except Exception:
            st.error(
                "Could not load records. Check your Supabase table and connection."
            )

    else:

        st.warning(
            "Supabase is not connected. Add SUPABASE_URL and SUPABASE_KEY in Streamlit secrets."
        )

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "🌸 Digital Saheli | Smartphone Usage & Online Safety Awareness for Women"
)
