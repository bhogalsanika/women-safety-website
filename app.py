import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Sakhi Digital Saathi",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp {
    background: #f8f9fc;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}

/* Main Logo */
.logo {
    text-align:center;
    font-size:42px;
    font-weight:800;
    margin-top:35px;
}

.tagline {
    text-align:center;
    color:#666;
    font-size:18px;
    margin-bottom:35px;
}

/* Search */
.search-area {
    background:white;
    padding:10px 20px;
    border-radius:40px;
    box-shadow:0 5px 25px rgba(0,0,0,.10);
    margin-bottom:30px;
}

/* Cards */
.card {
    background:white;
    padding:25px;
    border-radius:20px;
    box-shadow:0 4px 18px rgba(0,0,0,.07);
    height:100%;
}

.card-title {
    font-size:21px;
    font-weight:700;
}

.card-text {
    color:#666;
    margin-top:7px;
}

/* Simulation */
.phone {
    background:#111;
    border-radius:30px;
    padding:15px;
    max-width:350px;
    margin:auto;
}

.phone-screen {
    background:white;
    border-radius:20px;
    padding:20px;
    min-height:430px;
}

.chat {
    background:#e8f5e9;
    padding:12px;
    border-radius:15px;
    margin:10px 0;
}

.scam {
    background:#fff3f3;
    border:1px solid #ffbaba;
    padding:15px;
    border-radius:15px;
}

.success-box {
    padding:18px;
    background:#e8f7ee;
    border-radius:15px;
}

.warning-box {
    padding:18px;
    background:#fff4dd;
    border-radius:15px;
}

.footer {
    text-align:center;
    color:#777;
    padding:30px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "score" not in st.session_state:
    st.session_state.score = 0


# =========================================================
# NAVIGATION
# =========================================================

def go(page):
    st.session_state.page = page
    st.rerun()


# =========================================================
# HOME PAGE
# =========================================================

def home():

    st.markdown(
        '<div class="logo">📱 Sakhi Digital Saathi</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="tagline">'
        'Learn smartphones. Practice safely. Stay confident online.'
        '</div>',
        unsafe_allow_html=True
    )

    # Search
    st.markdown('<div class="search-area">', unsafe_allow_html=True)

    search = st.text_input(
        "🔍",
        placeholder="Search: WhatsApp, UPI, OTP, Camera, Scam, Password...",
        label_visibility="collapsed"
    )

    st.markdown('</div>', unsafe_allow_html=True)

    # Search result
    if search:

        q = search.lower()

        st.subheader("Search results")

        results = []

        if "whatsapp" in q:
            results.append(("💬 WhatsApp Practice", "whatsapp"))

        if "upi" in q or "payment" in q:
            results.append(("💳 UPI Safety Practice", "upi"))

        if "otp" in q:
            results.append(("🔐 OTP Safety", "otp"))

        if "scam" in q or "fraud" in q:
            results.append(("🚨 Scam Detective", "scam"))

        if "camera" in q or "photo" in q:
            results.append(("📸 Camera Learning", "camera"))

        if "password" in q or "phone lock" in q:
            results.append(("🔒 Phone Security", "password"))

        if "internet" in q or "google" in q:
            results.append(("🌐 Internet Practice", "internet"))

        if results:

            for title, page in results:

                if st.button(title, use_container_width=True):
                    go(page)

        else:

            st.info(
                "Try searching: WhatsApp, UPI, OTP, Scam, Camera, "
                "Password or Internet."
            )

        return

    # -----------------------------------------------------
    # QUICK LEARNING
    # -----------------------------------------------------

    st.subheader("✨ Learn & Practice")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="card">
        <div class="card-title">💬 WhatsApp</div>
        <div class="card-text">
        Practice messages, photos and identify unsafe chats.
        </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Practice WhatsApp", use_container_width=True):
            go("whatsapp")

    with c2:
        st.markdown("""
        <div class="card">
        <div class="card-title">💳 UPI</div>
        <div class="card-text">
        Learn safe digital payments through real-life situations.
        </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Practice UPI", use_container_width=True):
            go("upi")

    with c3:
        st.markdown("""
        <div class="card">
        <div class="card-title">🚨 Scam Detective</div>
        <div class="card-text">
        Can you identify a fake message or online scam?
        </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Start Challenge", use_container_width=True):
            go("scam")

    st.write("")

    c4, c5, c6 = st.columns(3)

    with c4:
        st.markdown("""
        <div class="card">
        <div class="card-title">📸 Camera</div>
        <div class="card-text">
        Learn how to take photos and protect private pictures.
        </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Learn Camera", use_container_width=True):
            go("camera")

    with c5:
        st.markdown("""
        <div class="card">
        <div class="card-title">🔐 Phone Security</div>
        <div class="card-text">
        Practice choosing a strong phone lock and safe password.
        </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Secure Phone", use_container_width=True):
            go("password")

    with c6:
        st.markdown("""
        <div class="card">
        <div class="card-title">🌐 Internet</div>
        <div class="card-text">
        Learn how to search online and recognize unsafe websites.
        </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Practice Internet", use_container_width=True):
            go("internet")

    st.write("")
    st.divider()

    # Score
    st.subheader("🏆 My Learning Progress")

    st.progress(min(st.session_state.score / 10, 1.0))

    st.write(
        f"You have completed **{st.session_state.score} safety practices**."
    )


# =========================================================
# WHATSAPP SIMULATOR
# =========================================================

def whatsapp():

    st.title("💬 WhatsApp Safety Practice")

    st.caption("You are looking at a simulated WhatsApp conversation.")

    st.markdown("""
    <div class="phone">
        <div class="phone-screen">

        <b>WhatsApp</b>
        <hr>

        <div class="chat">
        👩 Friend: Hi! How are you?
        </div>

        <div class="chat">
        👤 Unknown: Congratulations! 🎉
        You won ₹25,000. Send me the OTP to receive your money.
        </div>

        <div class="chat">
        👤 Unknown: Send OTP quickly!
        </div>

        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    answer = st.radio(
        "What should you do?",
        [
            "Send the OTP",
            "Ignore the request and do not share OTP"
        ]
    )

    if st.button("🔎 Check My Decision"):

        if answer == "Ignore the request and do not share OTP":

            st.session_state.score += 1

            st.success(
                "✅ Correct! Never share an OTP with another person."
            )

        else:

            st.error(
                "❌ Unsafe choice. OTPs should remain private."
            )

    if st.button("← Home"):
        go("home")


# =========================================================
# UPI SIMULATOR
# =========================================================

def upi():

    st.title("💳 UPI Safety Simulator")

    st.write(
        "Imagine you are making a digital payment."
    )

    st.markdown("""
    <div class="card">
    <h3>Payment Request</h3>

    <b>Person:</b> Unknown Seller<br><br>

    “Scan this QR code and enter your UPI PIN.
    You will receive ₹5,000.”

    </div>
    """, unsafe_allow_html=True)

    choice = st.radio(
        "What will you do?",
        [
            "Scan and enter my UPI PIN",
            "Verify the transaction before doing anything"
        ]
    )

    if st.button("💡 Check Decision"):

        if choice == "Verify the transaction before doing anything":

            st.session_state.score += 1

            st.markdown(
                '<div class="success-box">'
                '✅ Excellent! Always verify unexpected payment requests.'
                '</div>',
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                '<div class="warning-box">'
                '⚠️ Be careful. Never enter your UPI PIN just to receive money.'
                '</div>',
                unsafe_allow_html=True
            )

    st.write("")

    if st.button("← Home"):
        go("home")


# =========================================================
# OTP
# =========================================================

def otp():

    st.title("🔐 OTP Safety Challenge")

    st.info(
        "Someone calls and says: "
        "'I am from the bank. Tell me the OTP you just received.'"
    )

    answer = st.radio(
        "Your action?",
        [
            "Tell them the OTP",
            "Do not share the OTP and contact the bank through official channels"
        ]
    )

    if st.button("Check Answer"):

        if answer.startswith("Do not"):

            st.session_state.score += 1

            st.success(
                "✅ Correct! Never share OTP with callers."
            )

        else:

            st.error(
                "❌ Never share OTP, PIN or password with anyone."
            )

    if st.button("← Home"):
        go("home")


# =========================================================
# SCAM DETECTIVE
# =========================================================

def scam():

    st.title("🚨 Scam Detective")

    st.write(
        "You are the detective! Find out whether this message is safe."
    )

    st.markdown("""
    <div class="scam">

    <b>📩 Message received</b><br><br>

    🎉 Congratulations! You have won ₹50,000!<br><br>

    Click this link immediately and pay ₹499
    to claim your prize.<br><br>

    <b>WARNING: Offer expires in 10 minutes!</b>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    suspicious = st.multiselect(
        "Which warning signs can you find?",
        [
            "Unexpected prize",
            "Asking for money",
            "Urgent deadline",
            "Unknown link"
        ]
    )

    if st.button("🕵️ Submit Investigation"):

        if len(suspicious) >= 3:

            st.session_state.score += 1

            st.success(
                "✅ Great investigation! Multiple warning signs are present."
            )

        else:

            st.warning(
                "Look carefully. Prize claims, urgency, payment requests "
                "and unknown links are important warning signs."
            )

    if st.button("← Home"):
        go("home")


# =========================================================
# CAMERA
# =========================================================

def camera():

    st.title("📸 Camera Learning")

    st.write(
        "Let's learn camera use through a simple activity."
    )

    activity = st.selectbox(
        "Choose what you want to learn",
        [
            "Take a Photo",
            "Record a Video",
            "Protect Private Photos"
        ]
    )

    if activity == "Take a Photo":

        st.subheader("📷 Your task")

        st.write(
            "Which button would you normally press to take a photo?"
        )

        answer = st.radio(
            "Choose:",
            [
                "Capture / Camera button",
                "Volume settings",
                "Airplane mode"
            ]
        )

        if st.button("Check"):

            if answer == "Capture / Camera button":

                st.session_state.score += 1
                st.success("✅ Correct!")

            else:
                st.error("❌ Try again.")

    elif activity == "Record a Video":

        st.subheader("🎥 Basic steps")

        st.write(
            "Open Camera → Select Video → Press Record → Press Stop."
        )

        if st.button("I Understand"):
            st.session_state.score += 1
            st.success("✅ Video lesson completed.")

    else:

        st.subheader("🔒 Private Photos")

        st.warning(
            "Do not send private photos to unknown people. "
            "Review app permissions and cloud/photo sharing settings."
        )

        if st.button("Complete Safety Lesson"):
            st.session_state.score += 1
            st.success("✅ Safety lesson completed.")


    if st.button("← Home"):
        go("home")


# =========================================================
# PASSWORD
# =========================================================

def password():

    st.title("🔒 Strong Password Challenge")

    st.write(
        "Choose which password is safer."
    )

    answer = st.radio(
        "Select one:",
        [
            "123456",
            "sanika123",
            "My@Safe2026#Phone",
            "password"
        ]
    )

    if st.button("Check Password"):

        if answer == "My@Safe2026#Phone":

            st.session_state.score += 1

            st.success(
                "✅ Better choice! Strong passwords should be difficult to guess."
            )

        else:

            st.error(
                "❌ This password is easier to guess. "
                "Use a unique password with a mix of characters."
            )

    st.write("")

    st.info(
        "Never share your phone password, UPI PIN or account password."
    )

    if st.button("← Home"):
        go("home")


# =========================================================
# INTERNET
# =========================================================

def internet():

    st.title("🌐 Internet Search Practice")

    st.write(
        "Practice identifying a safer search result."
    )

    st.text_input(
        "🔍 What would you search?",
        placeholder="Example: nearest hospital"
    )

    st.subheader("Which website would you trust more?")

    choice = st.radio(
        "Choose:",
        [
            "Official government/organization website",
            "Unknown website promising free money"
        ]
    )

    if st.button("Check Choice"):

        if choice == "Official government/organization website":

            st.session_state.score += 1

            st.success(
                "✅ Correct! Prefer official and trusted sources."
            )

        else:

            st.error(
                "❌ Be careful with websites making unrealistic promises."
            )

    if st.button("← Home"):
        go("home")


# =========================================================
# ROUTER
# =========================================================

page = st.session_state.page

if page == "home":
    home()

elif page == "whatsapp":
    whatsapp()

elif page == "upi":
    upi()

elif page == "otp":
    otp()

elif page == "scam":
    scam()

elif page == "camera":
    camera()

elif page == "password":
    password()

elif page == "internet":
    internet()
