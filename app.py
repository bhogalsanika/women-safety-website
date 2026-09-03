import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Women Digital Safety",
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

/* Logo */
.logo {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin-top: 35px;
}

.tagline {
    text-align: center;
    color: #666;
    font-size: 18px;
    margin-bottom: 35px;
}

/* Search */
.search-area {
    background: white;
    padding: 10px 20px;
    border-radius: 40px;
    box-shadow: 0 5px 25px rgba(0,0,0,.10);
    margin-bottom: 30px;
}

/* Cards */
.card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 4px 18px rgba(0,0,0,.07);
    min-height: 150px;
}

.card-title {
    font-size: 21px;
    font-weight: 700;
}

.card-text {
    color: #666;
    margin-top: 7px;
}

/* Phone */
.phone {
    background: #111;
    border-radius: 30px;
    padding: 15px;
    max-width: 350px;
    margin: auto;
}

.phone-screen {
    background: white;
    border-radius: 20px;
    padding: 20px;
    min-height: 430px;
}

.chat {
    background: #e8f5e9;
    padding: 12px;
    border-radius: 15px;
    margin: 10px 0;
}

/* Scam */
.scam {
    background: #fff3f3;
    border: 1px solid #ffbaba;
    padding: 18px;
    border-radius: 15px;
}

/* Result */
.success-box {
    padding: 18px;
    background: #e8f7ee;
    border-radius: 15px;
}

.warning-box {
    padding: 18px;
    background: #fff4dd;
    border-radius: 15px;
}

.footer {
    text-align: center;
    color: #777;
    padding: 30px;
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
# HOME
# =========================================================

def home():

    st.markdown(
        '<div class="logo">📱 Women Digital Safety</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="tagline">'
        'Learn Smart. Stay Safe. Use Technology with Confidence.'
        '</div>',
        unsafe_allow_html=True
    )

    # ---------------- SEARCH ----------------

    st.markdown('<div class="search-area">', unsafe_allow_html=True)

    search = st.text_input(
        "Search",
        placeholder="Search: WhatsApp, UPI, OTP, Camera, Scam, Password...",
        label_visibility="collapsed"
    )

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- SEARCH RESULTS ----------------

    if search:

        q = search.lower()

        st.subheader("🔎 Search Results")

        results = []

        if "whatsapp" in q:
            results.append(
                ("💬 WhatsApp Practice",
                 "Practice messages and learn WhatsApp safety.",
                 "whatsapp")
            )

        if "upi" in q or "payment" in q:
            results.append(
                ("💳 UPI Safety Practice",
                 "Practice safe digital payment situations.",
                 "upi")
            )

        if "otp" in q:
            results.append(
                ("🔐 OTP Safety",
                 "Learn what to do when someone asks for your OTP.",
                 "otp")
            )

        if "scam" in q or "fraud" in q:
            results.append(
                ("🚨 Scam Detective",
                 "Find warning signs in suspicious messages.",
                 "scam")
            )

        if "camera" in q or "photo" in q:
            results.append(
                ("📸 Camera Learning",
                 "Learn camera use and photo safety.",
                 "camera")
            )

        if "password" in q or "lock" in q:
            results.append(
                ("🔒 Phone Security",
                 "Practice choosing a safer phone password.",
                 "password")
            )

        if "internet" in q or "google" in q:
            results.append(
                ("🌐 Internet Practice",
                 "Learn safer internet searching.",
                 "internet")
            )

        if results:

            for title, description, page in results:

                st.markdown(
                    f"""
                    <div class="card">
                    <div class="card-title">{title}</div>
                    <div class="card-text">{description}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if st.button(
                    "Open →",
                    key=f"search_{page}",
                    use_container_width=True
                ):
                    go(page)

        else:

            st.info(
                "No result found. Try WhatsApp, UPI, OTP, "
                "Scam, Camera, Password or Internet."
            )

        return

    # =====================================================
    # LEARN & PRACTICE
    # =====================================================

    st.subheader("✨ Learn & Practice")

    col1, col2, col3 = st.columns(3)

    # WhatsApp
    with col1:

        st.markdown("""
        <div class="card">
        <div class="card-title">💬 WhatsApp</div>
        <div class="card-text">
        Practice messages and identify unsafe chats.
        </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Practice WhatsApp",
            use_container_width=True
        ):
            go("whatsapp")

    # UPI
    with col2:

        st.markdown("""
        <div class="card">
        <div class="card-title">💳 UPI</div>
        <div class="card-text">
        Learn safe digital payments through situations.
        </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Practice UPI",
            use_container_width=True
        ):
            go("upi")

    # Scam
    with col3:

        st.markdown("""
        <div class="card">
        <div class="card-title">🚨 Scam Detective</div>
        <div class="card-text">
        Can you identify a suspicious message?
        </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Start Challenge",
            use_container_width=True
        ):
            go("scam")

    st.write("")

    col4, col5, col6 = st.columns(3)

    # Camera
    with col4:

        st.markdown("""
        <div class="card">
        <div class="card-title">📸 Camera</div>
        <div class="card-text">
        Learn camera use and protect private photos.
        </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Learn Camera",
            use_container_width=True
        ):
            go("camera")

    # Password
    with col5:

        st.markdown("""
        <div class="card">
        <div class="card-title">🔐 Phone Security</div>
        <div class="card-text">
        Practice choosing a strong phone lock.
        </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Secure Phone",
            use_container_width=True
        ):
            go("password")

    # Internet
    with col6:

        st.markdown("""
        <div class="card">
        <div class="card-title">🌐 Internet</div>
        <div class="card-text">
        Practice searching online safely.
        </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Practice Internet",
            use_container_width=True
        ):
            go("internet")

    # =====================================================
    # PROGRESS
    # =====================================================

    st.divider()

    st.subheader("🏆 My Learning Progress")

    progress = min(st.session_state.score / 10, 1.0)

    st.progress(progress)

    st.write(
        f"Completed safety practices: "
        f"**{st.session_state.score}**"
    )

    st.markdown(
        '<div class="footer">'
        'Women Digital Safety • Community Engagement Project'
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# WHATSAPP
# =========================================================

def whatsapp():

    st.title("💬 WhatsApp Safety Practice")

    st.caption(
        "This is a simulated conversation for learning purposes."
    )

    st.markdown("""
    <div class="phone">

        <div class="phone-screen">

        <h3>WhatsApp</h3>

        <hr>

        <div class="chat">
        👩 Friend: Hi! How are you?
        </div>

        <div class="chat">
        👤 Unknown: Congratulations! 🎉
        You won ₹25,000.
        </div>

        <div class="chat">
        👤 Unknown: Send me the OTP to receive your money.
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

    if st.button("← Back to Home"):
        go("home")


# =========================================================
# UPI
# =========================================================

def upi():

    st.title("💳 UPI Safety Simulator")

    st.write(
        "Imagine you received this payment request."
    )

    st.markdown("""
    <div class="card">

    <h3>💰 Payment Request</h3>

    <b>Person:</b> Unknown Seller

    <br><br>

    "Scan this QR code and enter your UPI PIN.
    You will receive ₹5,000."

    </div>
    """, unsafe_allow_html=True)

    choice = st.radio(
        "What will you do?",
        [
            "Scan and enter my UPI PIN",
            "Verify the transaction first"
        ]
    )

    if st.button("💡 Check Decision"):

        if choice == "Verify the transaction first":

            st.session_state.score += 1

            st.success(
                "✅ Correct! Verify unexpected payment requests."
            )

        else:

            st.warning(
                "⚠️ Never enter your UPI PIN just to receive money."
            )

    if st.button("← Back to Home"):
        go("home")


# =========================================================
# OTP
# =========================================================

def otp():

    st.title("🔐 OTP Safety Challenge")

    st.info(
        "Someone calls and says: "
        "\"I am from the bank. Tell me the OTP you received.\""
    )

    answer = st.radio(
        "What will you do?",
        [
            "Tell them the OTP",
            "Do not share the OTP"
        ]
    )

    if st.button("Check Answer"):

        if answer == "Do not share the OTP":

            st.session_state.score += 1

            st.success(
                "✅ Correct! OTP should never be shared."
            )

        else:

            st.error(
                "❌ Never share your OTP with another person."
            )

    if st.button("← Back to Home"):
        go("home")


# =========================================================
# SCAM DETECTIVE
# =========================================================

def scam():

    st.title("🚨 Scam Detective")

    st.write(
        "You are the detective. Find the warning signs."
    )

    st.markdown("""
    <div class="scam">

    <b>📩 MESSAGE RECEIVED</b>

    <br><br>

    🎉 Congratulations! You have won ₹50,000!

    <br><br>

    Click this link immediately and pay ₹499
    to claim your prize.

    <br><br>

    ⚠️ Offer expires in 10 minutes!

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    suspicious = st.multiselect(
        "🔎 Select the warning signs",
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
                "✅ Excellent! You identified several warning signs."
            )

        else:

            st.warning(
                "Look carefully. There are multiple warning signs."
            )

    if st.button("← Back to Home"):
        go("home")


# =========================================================
# CAMERA
# =========================================================

def camera():

    st.title("📸 Camera Learning")

    activity = st.selectbox(
        "Choose an activity",
        [
            "Take a Photo",
            "Record a Video",
            "Protect Private Photos"
        ]
    )

    if activity == "Take a Photo":

        st.subheader("📷 Your Task")

        answer = st.radio(
            "Which button normally takes a photo?",
            [
                "Capture / Camera button",
                "Airplane mode",
                "Volume settings"
            ]
        )

        if st.button("Check"):

            if answer == "Capture / Camera button":

                st.session_state.score += 1

                st.success(
                    "✅ Correct! That is the camera capture button."
                )

            else:

                st.error("❌ Try again.")

    elif activity == "Record a Video":

        st.subheader("🎥 Record a Video")

        st.write(
            "Camera → Video → Record → Stop"
        )

        if st.button("I Understand"):

            st.session_state.score += 1

            st.success(
                "✅ Video lesson completed."
            )

    else:

        st.subheader("🔒 Protect Private Photos")

        st.warning(
            "Do not share private photos with unknown people. "
            "Check photo-sharing and app permissions."
        )

        if st.button("Complete Lesson"):

            st.session_state.score += 1

            st.success(
                "✅ Safety lesson completed."
            )

    if st.button("← Back to Home"):
        go("home")


# =========================================================
# PASSWORD
# =========================================================

def password():

    st.title("🔒 Strong Password Challenge")

    st.write(
        "Choose the safer password."
    )

    answer = st.radio(
        "Select one:",
        [
            "123456",
            "password",
            "sanika123",
            "My@Safe2026#Phone"
        ]
    )

    if st.button("Check Password"):

        if answer == "My@Safe2026#Phone":

            st.session_state.score += 1

            st.success(
                "✅ Better choice! Use strong and unique passwords."
            )

        else:

            st.error(
                "❌ This password is easier to guess."
            )

    st.info(
        "Never share your phone password, UPI PIN or account password."
    )

    if st.button("← Back to Home"):
        go("home")


# =========================================================
# INTERNET
# =========================================================

def internet():

    st.title("🌐 Internet Search Practice")

    query = st.text_input(
        "🔍 What would you search?",
        placeholder="Example: nearest hospital"
    )

    if query:

        st.success(
            f'You searched for: "{query}"'
        )

    st.subheader("🔎 Which result is safer?")

    choice = st.radio(
        "Choose one:",
        [
            "Official government or organization website",
            "Unknown website promising free money"
        ]
    )

    if st.button("Check Choice"):

        if choice == "Official government or organization website":

            st.session_state.score += 1

            st.success(
                "✅ Correct! Prefer official and trusted sources."
            )

        else:

            st.error(
                "❌ Be careful with websites making unrealistic promises."
            )

    if st.button("← Back to Home"):
        go("home")


# =========================================================
# ROUTER
# =========================================================

if st.session_state.page == "home":
    home()

elif st.session_state.page == "whatsapp":
    whatsapp()

elif st.session_state.page == "upi":
    upi()

elif st.session_state.page == "otp":
    otp()

elif st.session_state.page == "scam":
    scam()

elif st.session_state.page == "camera":
    camera()

elif st.session_state.page == "password":
    password()

elif st.session_state.page == "internet":
    internet()
