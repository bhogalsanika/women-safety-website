import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Women Digital Help",
    page_icon="📱",
    layout="wide"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #f7f8fc;
}

.hero {
    text-align: center;
    padding: 45px 20px 25px 20px;
}

.hero h1 {
    font-size: 46px;
    margin-bottom: 5px;
}

.hero p {
    font-size: 20px;
    color: #666;
}

.search-box {
    background: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    margin-bottom: 30px;
}

.card {
    background: white;
    padding: 22px;
    border-radius: 16px;
    margin-bottom: 15px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.06);
}

.card h3 {
    margin-top: 0;
}

.step {
    background: #f1f3f8;
    padding: 15px;
    border-radius: 12px;
    margin: 8px 0;
}

.correct {
    padding: 15px;
    border-radius: 12px;
    background: #e8f7ee;
}

.wrong {
    padding: 15px;
    border-radius: 12px;
    background: #fdeaea;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# TOP HERO
# ============================================================

st.markdown("""
<div class="hero">
    <h1>📱 Women Digital Help</h1>
    <p>Learn smartphone usage • Practice online safety • Stay confident</p>
</div>
""", unsafe_allow_html=True)


# ============================================================
# SEARCH
# ============================================================

st.markdown('<div class="search-box">', unsafe_allow_html=True)

search = st.text_input(
    "🔍 What do you want to learn?",
    placeholder="Example: WhatsApp, UPI, OTP, Camera, Password..."
)

st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# TOPICS
# ============================================================

topics = {
    "📱 WhatsApp": "whatsapp",
    "💳 UPI Payment": "upi",
    "📸 Camera": "camera",
    "🌐 Internet": "internet",
    "📲 Install App": "apps",
    "🔐 Phone Lock": "lock",
    "📍 Location": "location",
    "🛡️ Online Safety": "safety"
}


# ============================================================
# SEARCH LOGIC
# ============================================================

selected_topic = None

if search:

    search_text = search.lower()

    if "whatsapp" in search_text:
        selected_topic = "whatsapp"

    elif "upi" in search_text or "payment" in search_text:
        selected_topic = "upi"

    elif "camera" in search_text or "photo" in search_text:
        selected_topic = "camera"

    elif "internet" in search_text or "google" in search_text:
        selected_topic = "internet"

    elif "app" in search_text or "install" in search_text:
        selected_topic = "apps"

    elif "lock" in search_text or "password" in search_text:
        selected_topic = "lock"

    elif "location" in search_text:
        selected_topic = "location"

    elif (
        "safety" in search_text
        or "otp" in search_text
        or "fraud" in search_text
        or "scam" in search_text
    ):
        selected_topic = "safety"

    else:
        st.warning(
            "Sorry, this topic is not available yet. "
            "Try WhatsApp, UPI, Camera, Internet, Apps, Password or Safety."
        )


# ============================================================
# QUICK TOPIC BUTTONS
# ============================================================

if not selected_topic:

    st.subheader("✨ What would you like to learn?")

    col1, col2, col3, col4 = st.columns(4)

    buttons = list(topics.items())

    for i, (name, value) in enumerate(buttons):

        with [col1, col2, col3, col4][i % 4]:

            if st.button(name, use_container_width=True):
                st.session_state["topic"] = value
                st.rerun()


# Get topic from session

if "topic" in st.session_state and not selected_topic:
    selected_topic = st.session_state["topic"]


# ============================================================
# WHATSAPP
# ============================================================

if selected_topic == "whatsapp":

    st.title("📱 Learn WhatsApp")

    st.write(
        "Learn basic WhatsApp features and how to stay safe while using them."
    )

    option = st.radio(
        "What do you want to learn?",
        [
            "Send a Message",
            "Send a Photo",
            "Voice Call",
            "WhatsApp Safety"
        ]
    )

    if option == "Send a Message":

        st.subheader("💬 How to send a WhatsApp message")

        steps = [
            "Open WhatsApp.",
            "Select the person you want to message.",
            "Tap the message box.",
            "Type your message.",
            "Press the Send button."
        ]

        for i, step in enumerate(steps, 1):
            st.markdown(
                f'<div class="step">Step {i}️⃣ — {step}</div>',
                unsafe_allow_html=True
            )

        if st.button("✅ I understood"):
            st.success("Great! You learned how to send a message.")

    elif option == "Send a Photo":

        st.subheader("📸 How to send a photo")

        steps = [
            "Open the WhatsApp chat.",
            "Tap the attachment/camera option.",
            "Choose a photo.",
            "Check the selected photo.",
            "Tap Send."
        ]

        for i, step in enumerate(steps, 1):
            st.markdown(
                f'<div class="step">Step {i}️⃣ — {step}</div>',
                unsafe_allow_html=True
            )

        if st.button("📸 Practice Complete"):
            st.success("Excellent! You know how to send a photo.")

    elif option == "Voice Call":

        st.subheader("📞 WhatsApp Voice Call")

        st.write("To make a voice call:")

        st.markdown("""
        <div class="step">1️⃣ Open the WhatsApp chat.</div>
        <div class="step">2️⃣ Tap the phone icon.</div>
        <div class="step">3️⃣ Wait for the person to answer.</div>
        """, unsafe_allow_html=True)

        st.info(
            "Safety Tip: Do not share private information with unknown callers."
        )

    else:

        st.subheader("🛡️ WhatsApp Safety")

        safety = [
            "Do not share OTP with anyone.",
            "Do not open suspicious links.",
            "Do not share private photos with unknown people.",
            "Check unknown group invitations carefully.",
            "Use WhatsApp privacy settings."
        ]

        for item in safety:
            st.checkbox(item)

        if st.button("🔎 Check My Safety"):
            st.success("Good! Review any unchecked safety points.")


# ============================================================
# UPI
# ============================================================

elif selected_topic == "upi":

    st.title("💳 UPI Payment Practice")

    st.write(
        "Practice common UPI situations and learn what is safe."
    )

    st.subheader("Scenario 1")

    st.info(
        "A person says: 'I am sending you money. "
        "Please enter your UPI PIN to receive it.'"
    )

    answer = st.radio(
        "What should you do?",
        [
            "Enter my UPI PIN",
            "Do not enter PIN and verify the transaction"
        ],
        key="upi1"
    )

    if st.button("Check Answer", key="checkupi"):

        if answer == "Do not enter PIN and verify the transaction":

            st.success(
                "✅ Correct! Your UPI PIN is used to authorize payments. "
                "Never share it with anyone."
            )

        else:

            st.error(
                "❌ Not safe. Never share your UPI PIN with another person."
            )

    st.divider()

    st.subheader("Scenario 2")

    st.info(
        "Someone sends you a QR code and says: "
        "'Scan this to receive ₹5,000.'"
    )

    qr_answer = st.radio(
        "What is safer?",
        [
            "Scan immediately",
            "Verify the person and transaction first"
        ],
        key="upi2"
    )

    if st.button("Check QR Answer"):

        if qr_answer == "Verify the person and transaction first":
            st.success("✅ Correct! Always verify unexpected payment requests.")
        else:
            st.error("❌ Be careful with unknown QR codes.")


# ============================================================
# CAMERA
# ============================================================

elif selected_topic == "camera":

    st.title("📸 Learn Camera")

    action = st.selectbox(
        "Choose an activity",
        [
            "Take a Photo",
            "Record a Video",
            "Keep Photos Private"
        ]
    )

    if action == "Take a Photo":

        st.subheader("📷 Taking a photo")

        steps = [
            "Open the Camera app.",
            "Point the camera at the subject.",
            "Tap the capture button.",
            "Open Gallery to view the photo."
        ]

        for i, step in enumerate(steps, 1):
            st.markdown(
                f'<div class="step">Step {i}️⃣ — {step}</div>',
                unsafe_allow_html=True
            )

        if st.button("📸 Done"):
            st.success("Photo lesson completed!")

    elif action == "Record a Video":

        st.subheader("🎥 Recording a video")

        st.write(
            "Open Camera → select Video → press Record → "
            "press Stop when finished."
        )

        st.success("Tip: Keep your phone steady while recording.")

    else:

        st.subheader("🔐 Keep photos private")

        st.warning(
            "Avoid sending private photos to unknown people. "
            "Review who can access your photos and cloud backups."
        )


# ============================================================
# INTERNET
# ============================================================

elif selected_topic == "internet":

    st.title("🌐 Learn Internet Searching")

    st.write("Practice searching for information safely.")

    query = st.text_input(
        "What would you search for?",
        placeholder="Example: nearest hospital"
    )

    if st.button("🔍 Search Practice"):

        if query:
            st.success(f'Good! You searched for: "{query}"')

            st.info(
                "Safety Tip: Check whether the website is trustworthy "
                "before entering personal information."
            )
        else:
            st.warning("Enter something to search.")


# ============================================================
# INSTALL APP
# ============================================================

elif selected_topic == "apps":

    st.title("📲 How to Install an App")

    steps = [
        "Open Google Play Store.",
        "Search for the required app.",
        "Check the app name and developer.",
        "Read reviews and check downloads.",
        "Tap Install.",
        "Open the app after installation."
    ]

    for i, step in enumerate(steps, 1):
        st.markdown(
            f'<div class="step">Step {i}️⃣ — {step}</div>',
            unsafe_allow_html=True
        )

    st.warning(
        "⚠️ Avoid installing apps from unknown links or websites."
    )

    if st.button("✅ I learned this"):
        st.success("Good! You know the basic app installation process.")


# ============================================================
# PHONE LOCK
# ============================================================

elif selected_topic == "lock":

    st.title("🔐 Protect Your Phone")

    st.write("A phone lock helps protect your personal information.")

    lock_type = st.selectbox(
        "Choose a protection method",
        [
            "PIN",
            "Password",
            "Pattern",
            "Fingerprint"
        ]
    )

    st.info(
        f"You selected: {lock_type}. "
        "Use a method that is difficult for others to guess."
    )

    if st.button("🔒 Complete Security Check"):

        st.success(
            "Remember: Never share your phone password/PIN with strangers."
        )


# ============================================================
# LOCATION
# ============================================================

elif selected_topic == "location":

    st.title("📍 Location Sharing")

    st.write(
        "Location sharing can be useful, but it should be controlled carefully."
    )

    choices = [
        "I check which apps have location permission.",
        "I avoid sharing my live location with strangers.",
        "I turn off location when it is not needed.",
        "I check location settings regularly."
    ]

    for choice in choices:
        st.checkbox(choice)

    if st.button("📍 Check Location Safety"):
        st.success(
            "Good! Review your location permissions regularly."
        )


# ============================================================
# ONLINE SAFETY
# ============================================================

elif selected_topic == "safety":

    st.title("🛡️ Online Safety Practice")

    scenario = st.selectbox(
        "Choose a situation",
        [
            "Unknown OTP Request",
            "Suspicious Link",
            "Fake Prize Message",
            "Unknown Friend Request",
            "Online Harassment"
        ]
    )

    if scenario == "Unknown OTP Request":

        st.info(
            "Someone calls you and asks for the OTP received on your phone."
        )

        ans = st.radio(
            "What will you do?",
            [
                "Tell them the OTP",
                "Do not share the OTP"
            ]
        )

        if st.button("Check OTP Answer"):

            if ans == "Do not share the OTP":
                st.success(
                    "✅ Correct! OTP should be kept private."
                )
            else:
                st.error(
                    "❌ Never share OTP with another person."
                )

    elif scenario == "Suspicious Link":

        st.info(
            "You receive: 'Your account will be blocked today. "
            "Click this link immediately.'"
        )

        ans = st.radio(
            "What should you do?",
            [
                "Click the link immediately",
                "Do not click and verify through the official app/website"
            ]
        )

        if st.button("Check Link Answer"):

            if ans.startswith("Do not"):
                st.success("✅ Correct! Verify before clicking.")
            else:
                st.error("❌ Suspicious links can lead to scams.")

    elif scenario == "Fake Prize Message":

        st.info(
            "You receive a message saying you won ₹50,000 "
            "and must pay a fee first."
        )

        ans = st.radio(
            "What should you do?",
            [
                "Pay the fee",
                "Do not pay and verify the claim"
            ]
        )

        if st.button("Check Prize Answer"):

            if ans == "Do not pay and verify the claim":
                st.success("✅ Correct! Unexpected prize claims can be scams.")
            else:
                st.error("❌ Do not send money to claim an unexpected prize.")

    elif scenario == "Unknown Friend Request":

        st.info(
            "An unknown person sends a friend request and immediately "
            "asks for your personal details."
        )

        ans = st.radio(
            "What is safer?",
            [
                "Share my details",
                "Do not share and verify the account"
            ]
        )

        if st.button("Check Profile Answer"):

            if ans.startswith("Do not"):
                st.success("✅ Correct! Be careful with unknown profiles.")
            else:
                st.error("❌ Avoid sharing personal information.")

    else:

        st.info(
            "Someone is repeatedly sending unwanted messages online."
        )

        ans = st.radio(
            "What is a safer response?",
            [
                "Keep replying",
                "Save evidence, block/report the account and seek help"
            ]
        )

        if st.button("Check Harassment Answer"):

            if ans.startswith("Save"):
                st.success(
                    "✅ Correct! Keep evidence and use block/report options."
                )
            else:
                st.error(
                    "❌ Repeatedly engaging may not solve the problem."
                )


# ============================================================
# BACK TO HOME
# ============================================================

st.divider()

if st.button("🏠 Back to Home"):
    st.session_state.pop("topic", None)
    st.rerun()
