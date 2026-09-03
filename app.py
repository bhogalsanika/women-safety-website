
import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Digital Saheli",
    page_icon="🌸",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>
    .main {
        background-color: #fff8fb;
    }

    .hero {
        background: linear-gradient(135deg, #ffe4ef, #f5e8ff);
        padding: 45px;
        border-radius: 25px;
        text-align: center;
        margin-bottom: 30px;
    }

    .hero h1 {
        color: #8e2457;
        font-size: 45px;
        margin-bottom: 10px;
    }

    .hero p {
        font-size: 20px;
        color: #555;
    }

    .card {
        background: white;
        padding: 25px;
        border-radius: 20px;
        min-height: 190px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }

    .card h3 {
        color: #8e2457;
    }

    .tip {
        background: #fff0c9;
        padding: 20px;
        border-radius: 15px;
        font-size: 18px;
    }

    .emergency {
        background: #ffe5e5;
        padding: 22px;
        border-radius: 18px;
        text-align: center;
    }

    .small-title {
        color: #8e2457;
        font-size: 30px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.title("🌸 Digital Saheli")
st.sidebar.write("Smartphone & Online Safety")

page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Home",
        "📱 Smartphone Skills",
        "🛡️ Online Safety",
        "🚨 Women Safety",
        "🎯 Safety Quiz",
        "⚠️ Scam Detector"
    ]
)

# =========================================================
# HOME
# =========================================================
if page == "🏠 Home":

    st.markdown("""
    <div class="hero">
        <h1>🌸 Digital Saheli</h1>
        <p><b>Learn • Stay Safe • Stay Connected</b></p>
        <p>
        Smartphone aur online safety ko simple tarike se samjhein
        aur confidently technology use karein.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="small-title">What would you like to learn?</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>📱 Smartphone Skills</h3>
            <p>
            WhatsApp, UPI, Google Maps, contacts,
            camera aur basic smartphone settings seekhein.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>🛡️ Online Safety</h3>
            <p>
            OTP, passwords, fake links, online scams
            aur social media privacy ke baare mein seekhein.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>🚨 Women Safety</h3>
            <p>
            Emergency numbers, cybercrime help
            aur basic digital safety information.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="tip">
        💡 <b>Today's Safety Tip:</b><br>
        OTP, UPI PIN aur password kabhi bhi kisi ke saath share na karein.
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.info(
        "🎯 Tip: Sidebar se kisi bhi section ko select karke "
        "interactive information dekhein."
    )


# =========================================================
# SMARTPHONE SKILLS
# =========================================================
elif page == "📱 Smartphone Skills":

    st.title("📱 Smartphone Skills")
    st.write("Basic smartphone features ko easily samjhein.")

    topic = st.selectbox(
        "Choose a topic:",
        [
            "WhatsApp",
            "UPI Payments",
            "Google Maps",
            "Contacts",
            "Camera & Photos",
            "Apps & Updates"
        ]
    )

    if topic == "WhatsApp":
        st.subheader("💬 WhatsApp")
        st.write("WhatsApp se message, photo aur video bhej sakte hain.")
        st.markdown("""
        **Basic Steps**
        1. WhatsApp open karein.
        2. New Chat par click karein.
        3. Contact select karein.
        4. Message type karke Send karein.

        **Safety:** Unknown links aur unknown files open na karein.
        """)

    elif topic == "UPI Payments":
        st.subheader("💳 UPI Payments")
        st.write("UPI se mobile ke through payment receive aur send kiya ja sakta hai.")
        st.markdown("""
        **Remember:**
        - UPI PIN sirf payment karte waqt enter karein.
        - UPI PIN kisi ko na batayein.
        - Payment receive karne ke liye generally UPI PIN ki zarurat nahi hoti.
        """)

    elif topic == "Google Maps":
        st.subheader("📍 Google Maps")
        st.write("Google Maps location find karne aur route dekhne ke liye useful hai.")
        st.markdown("""
        **Basic Steps**
        1. Google Maps open karein.
        2. Destination search karein.
        3. Directions select karein.
        4. Route check karein.
        """)

    elif topic == "Contacts":
        st.subheader("👤 Saving a Contact")
        st.markdown("""
        1. Phone/Contacts app open karein.
        2. Add Contact select karein.
        3. Name aur phone number enter karein.
        4. Save karein.
        """)

    elif topic == "Camera & Photos":
        st.subheader("📷 Camera & Photos")
        st.markdown("""
        - Camera open karke photo le sakte hain.
        - Gallery/Photos app mein photos dekh sakte hain.
        - Important photos ka backup rakhna useful hai.
        - Private photos unknown people ke saath share na karein.
        """)

    elif topic == "Apps & Updates":
        st.subheader("📲 Apps & Updates")
        st.markdown("""
        - Apps trusted app store se install karein.
        - Apps ko regularly update karein.
        - Unused apps uninstall karein.
        - Unknown APK files install na karein.
        """)


# =========================================================
# ONLINE SAFETY
# =========================================================
elif page == "🛡️ Online Safety":

    st.title("🛡️ Online Safety")
    st.write("Internet use karte waqt in basic rules ko follow karein.")

    safety_topic = st.selectbox(
        "Select a safety topic:",
        [
            "🔐 Password Safety",
            "🔢 OTP Safety",
            "🔗 Fake Links",
            "💳 Online Payment Safety",
            "📱 Social Media Privacy",
            "📩 Suspicious Messages"
        ]
    )

    if safety_topic == "🔐 Password Safety":
        st.subheader("🔐 Strong Password")
        st.markdown("""
        **Do:**
        - Strong and unique password use karein.
        - Different accounts ke liye different passwords rakhein.
        - Two-factor authentication enable karein.

        **Don't:**
        - Password kisi ko share na karein.
        - Name ya date of birth jaise easy passwords avoid karein.
        """)

    elif safety_topic == "🔢 OTP Safety":
        st.subheader("🔢 OTP Safety")
        st.warning("⚠️ OTP kisi unknown person ko kabhi share na karein.")
        st.markdown("""
        OTP ka use account verification ke liye hota hai.
        Agar koi phone karke OTP maange, to OTP share na karein.
        """)

    elif safety_topic == "🔗 Fake Links":
        st.subheader("🔗 Fake Links")
        st.markdown("""
        **Fake link ke signs:**
        - Unknown sender
        - Spelling mistakes
        - Urgent message
        - Prize/lottery ka promise
        - Suspicious website address

        👉 Aise links par click na karein.
        """)

    elif safety_topic == "💳 Online Payment Safety":
        st.subheader("💳 Online Payment Safety")
        st.markdown("""
        - Payment karne se pehle receiver ka naam check karein.
        - UPI PIN share na karein.
        - Unknown QR code scan na karein.
        - Suspicious payment request ko reject karein.
        """)

    elif safety_topic == "📱 Social Media Privacy":
        st.subheader("📱 Social Media Privacy")
        st.markdown("""
        - Account privacy settings check karein.
        - Unknown friend requests accept na karein.
        - Personal information publicly share na karein.
        - Location sharing carefully use karein.
        """)

    elif safety_topic == "📩 Suspicious Messages":
        st.subheader("📩 Suspicious Messages")
        st.markdown("""
        Agar message suspicious lage:

        **STOP → DON'T CLICK → DON'T SHARE → REPORT**
        """)


# =========================================================
# WOMEN SAFETY
# =========================================================
elif page == "🚨 Women Safety":

    st.title("🚨 Women Safety")
    st.write("Emergency aur cyber safety ke liye important information.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="emergency">
        <h2>🚨 112</h2>
        <p>Emergency Helpline</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="emergency">
        <h2>👩 181</h2>
        <p>Women Helpline</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="emergency">
        <h2>💻 1930</h2>
        <p>Cyber Crime Helpline</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    st.subheader("📍 Location Safety")

    st.markdown("""
    - Trusted person ke saath live location share kar sakte hain.
    - Location sharing unnecessary ho to off karein.
    - Public social-media posts mein real-time location avoid karein.
    """)

    st.subheader("📞 Emergency Contacts")

    st.write(
        "Phone mein family member, trusted friend ya emergency contact "
        "save karke rakhein."
    )

    st.info(
        "Emergency situation mein local emergency services ko contact karein."
    )


# =========================================================
# QUIZ
# =========================================================
elif page == "🎯 Safety Quiz":

    st.title("🎯 Online Safety Quiz")
    st.write("Apni digital safety knowledge check karein!")

    questions = [
        {
            "q": "Kya OTP kisi unknown person ko dena safe hai?",
            "options": ["Yes", "No"],
            "answer": "No"
        },
        {
            "q": "UPI PIN kisko batana chahiye?",
            "options": ["Bank employee ko", "Friend ko", "Kisi ko nahi"],
            "answer": "Kisi ko nahi"
        },
        {
            "q": "Unknown link receive hone par kya karna chahiye?",
            "options": ["Click karna", "Ignore/verify karna", "Forward karna"],
            "answer": "Ignore/verify karna"
        },
        {
            "q": "Strong password ka use karna chahiye?",
            "options": ["Yes", "No"],
            "answer": "Yes"
        }
    ]

    score = 0

    for i, question in enumerate(questions):

        st.subheader(f"Question {i+1}")
        answer = st.radio(
            question["q"],
            question["options"],
            key=f"question_{i}"
        )

        if st.button(f"Check Answer {i+1}", key=f"check_{i}"):

            if answer == question["answer"]:
                st.success("✅ Correct!")
            else:
                st.error(
                    f"❌ Incorrect. Correct answer: {question['answer']}"
                )

    st.divider()

    st.info("Complete all questions to improve your online safety awareness.")


# =========================================================
# SCAM DETECTOR
# =========================================================
elif page == "⚠️ Scam Detector":

    st.title("⚠️ Scam Detector")
    st.write("Situation select karein aur dekhein kya karna chahiye.")

    situation = st.selectbox(
        "What happened?",
        [
            "🏦 Someone called asking for OTP",
            "🔗 I received a KYC update link",
            "🎁 I received a lottery/prize message",
            "💳 Someone asked for UPI PIN",
           

