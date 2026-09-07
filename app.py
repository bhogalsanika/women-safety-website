import streamlit as st
from supabase import create_client
from datetime import date

# ============================================================
# DIGITAL SAHELI
# Smartphone Usage & Online Safety for Women
# CEP PROJECT
# ============================================================

st.set_page_config(
    page_title="Digital Saheli",
    page_icon="🌸",
    layout="wide"
)

# ============================================================
# SUPABASE CONNECTION
# ============================================================

@st.cache_resource
def connect_supabase():
    try:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
        return create_client(url, key)
    except Exception as e:
        return None


supabase = connect_supabase()


# ============================================================
# DATABASE FUNCTIONS
# ============================================================

def get_records(table_name):
    if supabase is None:
        return []

    try:
        response = (
            supabase
            .table(table_name)
            .select("*")
            .execute()
        )
        return response.data
    except Exception as e:
        st.error("Database error: " + str(e))
        return []


def save_record(table_name, data):
    if supabase is None:
        st.error("Supabase connection not available.")
        return False

    try:
        supabase.table(table_name).insert(data).execute()
        return True
    except Exception as e:
        st.error("Unable to save data: " + str(e))
        return False


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background: #fff8fb;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }

    .header {
        background: linear-gradient(
            135deg,
            #f8d7e6,
            #eadcf8
        );
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

    .card {
        background: white;
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 18px;
        border: 1px solid #efd9e4;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    }

    .card h3 {
        color: #8b2457;
    }

    .safety-box {
        background: #fff0c2;
        padding: 22px;
        border-radius: 18px;
        margin: 20px 0;
    }

    .emergency-box {
        background: #ffe5e5;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        border: 1px solid #f5c2c2;
        margin-bottom: 15px;
    }

    .stButton > button {
        border-radius: 12px;
        min-height: 45px;
    }

    .footer {
        text-align: center;
        color: #777;
        padding: 25px;
    }

    @media only screen and (max-width: 768px) {

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
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
            border-radius: 16px;
        }

        .stButton > button {
            width: 100%;
            min-height: 48px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    """
    <h1 style="
        text-align:center;
        color:#8b2457;
    ">
    🌸 DIGITAL SAHELI
    </h1>
    """,
    unsafe_allow_html=True
)

st.sidebar.caption(
    "Smartphone & Online Safety for Women"
)

st.sidebar.divider()

page = st.sidebar.radio(
    "📌 Menu",
    [
        "🏠 Home",
        "📱 Learn",
        "🛡️ Safety",
        "⚠️ Scam Check",
        "🎯 Quiz",
        "👩 Participants",
        "📋 Records",
        "🚨 Help"
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

    st.markdown(
        """
        <div class="header">
            <h1>🌸 DIGITAL SAHELI</h1>

            <p>
            <b>Learn • Protect • Stay Connected</b>
            </p>

            <p>
            Smartphone & Online Safety for Women
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card">
            <h3>👩 Welcome to Digital Saheli</h3>

            <p>
            Learn how to use smartphones and online services
            safely and confidently.
            </p>

            <h4>
            🔍 What do you want to learn?
            </h4>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="card">
                <h3>📱 LEARN</h3>
                <p>
                Smartphone usage, WhatsApp,
                UPI, Maps and phone settings.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "Explore Smartphone",
            use_container_width=True
        ):
            st.info("Open 📱 Learn from the menu.")

    with col2:

        st.markdown(
            """
            <div class="card">
                <h3>🛡️ PROTECT</h3>
                <p>
                Learn OTP, password,
                phishing and payment safety.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "Explore Safety",
            use_container_width=True
        ):
            st.info("Open 🛡️ Safety from the menu.")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="card">
                <h3>⚠️ SCAM CHECK</h3>
                <p>
                Check suspicious calls,
                messages and online situations.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="card">
                <h3>🎯 QUIZ</h3>
                <p>
                Test your knowledge of
                online safety.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="safety-box">
            💡 <b>TODAY'S SAFETY TIP</b>
            <br><br>
            Never share your OTP or UPI PIN with anyone.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("🚨 NEED HELP?")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown(
            """
            <div class="emergency-box">
                <h1>112</h1>
                <p>Emergency</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            """
            <div class="emergency-box">
                <h1>181</h1>
                <p>Women Helpline</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:

        st.markdown(
            """
            <div class="emergency-box">
                <h1>1930</h1>
                <p>Cyber Crime</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# SMARTPHONE LEARNING
# ============================================================

elif page == "📱 Learn":

    st.title("📱 Smartphone Learning")

    st.write(
        "Learn common smartphone features step by step."
    )

    topic = st.selectbox(
        "🔍 What do you want to learn?",
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

        st.markdown(
            """
            ### How to send a message

            1. Open WhatsApp.
            2. Select a contact.
            3. Type your message.
            4. Press Send.

            ### 🔒 Safety

            - Don't open suspicious links.
            - Never share OTP.
            - Check unknown messages carefully.
            """
        )

    elif topic == "💳 UPI Payments":

        st.header("💳 UPI Payments")

        st.markdown(
            """
            ### How to make a payment

            1. Open your trusted UPI app.
            2. Select the person or merchant.
            3. Enter amount.
            4. Check receiver's name.
            5. Enter UPI PIN only to authorize your payment.

            ⚠️ Never share your UPI PIN.
            """
        )

    elif topic == "📍 Google Maps":

        st.header("📍 Google Maps")

        st.markdown(
            """
            1. Open Google Maps.
            2. Search your destination.
            3. Select Directions.
            4. Choose your travel method.
            5. Follow the route.

            📍 Share live location only with trusted people.
            """
        )

    elif topic == "👤 Contacts":

        st.header("👤 Contacts")

        st.markdown(
            """
            ### Save a contact

            1. Open Contacts.
            2. Tap Add Contact.
            3. Enter name.
            4. Enter phone number.
            5. Tap Save.

            Save important family and emergency numbers.
            """
        )

    elif topic == "📷 Camera & Photos":

        st.header("📷 Camera & Photos")

        st.markdown(
            """
            - Take photos and videos.
            - Avoid sharing private photos with strangers.
            - Review which apps can access your photos.
            """
        )

    elif topic == "📲 Apps & Updates":

        st.header("📲 Apps & Updates")

        st.markdown(
            """
            ✅ Download apps from trusted app stores.

            ✅ Keep apps updated.

            ✅ Remove unused apps.

            ❌ Avoid unknown APK files.
            """
        )

    elif topic == "⚙️ Phone Settings":

        st.header("⚙️ Phone Settings")

        st.markdown(
            """
            Check these settings regularly:

            🔒 Screen Lock

            📍 Location Permission

            🎤 Microphone Permission

            📷 Camera Permission

            🔐 Privacy Settings

            🔄 Software Updates
            """
        )


# ============================================================
# ONLINE SAFETY
# ============================================================

elif page == "🛡️ Safety":

    st.title("🛡️ Online Safety")

    safety_topic = st.selectbox(
        "🔍 Select a topic",
        [
            "🔐 Password Safety",
            "🔢 OTP Safety",
            "🔗 Fake Links & Phishing",
            "💳 Payment Safety",
            "📱 Social Media Privacy",
            "👤 Fake Profiles",
            "🎣 Online Scams"
        ]
    )

    st.divider()

    if safety_topic == "🔐 Password Safety":

        st.header("🔐 Password Safety")

        st.markdown(
            """
            ✅ Use a strong password.

            ✅ Use different passwords for important accounts.

            ✅ Enable two-factor authentication.

            ❌ Never share your password.
            """
        )

    elif safety_topic == "🔢 OTP Safety":

        st.header("🔢 OTP Safety")

        st.error(
            "🚫 NEVER SHARE YOUR OTP WITH ANYONE."
        )

        st.write(
            "An OTP is private and should not be shared."
        )

    elif safety_topic == "🔗 Fake Links & Phishing":

        st.header("🔗 Fake Links & Phishing")

        st.markdown(
            """
            Warning signs:

            ⚠️ Unknown sender

            ⚠️ Urgent message

            ⚠️ Prize or reward

            ⚠️ KYC/update warning

            ⚠️ Suspicious website

            ### Remember

            **STOP → CHECK → DON'T CLICK → REPORT**
            """
        )

    elif safety_topic == "💳 Payment Safety":

        st.header("💳 Payment Safety")

        st.markdown(
            """
            ✅ Check receiver's name.

            ✅ Keep UPI PIN private.

            ❌ Never share OTP.

            ❌ Never share UPI PIN.

            ❌ Don't scan unknown QR codes.
            """
        )

    elif safety_topic == "📱 Social Media Privacy":

        st.header("📱 Social Media Privacy")

        st.markdown(
            """
            - Keep your account private when appropriate.
            - Accept requests from people you know.
            - Avoid sharing sensitive personal information.
            - Be careful with location sharing.
            """
        )

    elif safety_topic == "👤 Fake Profiles":

        st.header("👤 Fake Profiles")

        st.markdown(
            """
            Warning signs:

            ⚠️ New account

            ⚠️ Few genuine connections

            ⚠️ Requests for money

            ⚠️ Requests for private photos

            **Block and report suspicious accounts.**
            """
        )

    elif safety_topic == "🎣 Online Scams":

        st.header("🎣 Common Online Scams")

        st.markdown(
            """
            🏦 Fake bank/KYC calls

            🎁 Lottery scams

            💼 Fake job offers

            💳 Payment scams

            🔗 Phishing links

            👤 Fake social-media accounts
            """
        )


# ============================================================
# SCAM CHECK
# ============================================================

elif page == "⚠️ Scam Check":

    st.title("⚠️ Scam Detector")

    situation = st.selectbox(
        "🔍 What happened?",
        [
            "🏦 Someone called asking for OTP",
            "🔗 I received a KYC link",
            "🎁 I received a lottery message",
            "💳 Someone asked for my UPI PIN",
            "📱 I received a suspicious WhatsApp link",
            "💼 Job offer asking for money",
            "👤 Stranger asking for private photos"
        ]
    )

    if st.button(
        "🔍 Check Situation",
        use_container_width=True
    ):

        if "OTP" in situation:

            st.error(
                "🚨 HIGH RISK — DO NOT SHARE OTP"
            )

            st.write(
                "End the call and contact the organisation officially."
            )

        elif "KYC" in situation:

            st.warning(
                "⚠️ POSSIBLE PHISHING"
            )

            st.write(
                "Do not click the link. Verify using the official app."
            )

        elif "lottery" in situation:

            st.error(
                "🎁 POSSIBLE SCAM"
            )

            st.write(
                "Do not pay money to claim an unexpected prize."
            )

        elif "UPI PIN" in situation:

            st.error(
                "🚨 NEVER SHARE YOUR UPI PIN"
            )

        elif "WhatsApp" in situation:

            st.warning(
                "🔗 DON'T CLICK"
            )

            st.write(
                "Verify the sender before opening the link."
            )

        elif "Job" in situation:

            st.error(
                "💼 POSSIBLE JOB SCAM"
            )

            st.write(
                "Do not pay money or share sensitive information."
            )

        elif "photos" in situation:

            st.error(
                "🚨 DON'T SHARE PRIVATE PHOTOS"
            )

            st.write(
                "Block and report the account."
            )


# ============================================================
# QUIZ
# ============================================================

elif page == "🎯 Quiz":

    st.title("🎯 Online Safety Quiz")

    st.write(
        "Select the participant and answer the questions."
    )

    participants = get_records("participants")

    if len(participants) == 0:

        st.warning(
            "⚠️ No participants found."
        )

        st.info(
            "Please add a participant from 👩 Participants."
        )

    else:

        participant_names = []

        for person in participants:

            if person.get("name"):

                participant_names.append(
                    person["name"]
                )

        selected_participant = st.selectbox(
            "👩 Select Participant",
            participant_names
        )

        st.divider()

        q1 = st.radio(
            "1️⃣ Should you share your OTP with someone who calls you?",
            ["Yes", "No"],
            key="question_1"
        )

        q2 = st.radio(
            "2️⃣ Should you share your UPI PIN with anyone?",
            ["Yes", "No"],
            key="question_2"
        )

        q3 = st.radio(
            "3️⃣ What should you do with a suspicious link?",
            [
                "Click immediately",
                "Ignore and verify",
                "Forward to friends"
            ],
            key="question_3"
        )

        q4 = st.radio(
            "4️⃣ Is a strong password important?",
            ["Yes", "No"],
            key="question_4"
        )

        q5 = st.radio(
            "5️⃣ Should you accept every unknown social-media request?",
            ["Yes", "No"],
            key="question_5"
        )

        if st.button(
            "🎯 Submit Quiz",
            use_container_width=True
        ):

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

            quiz_data = {
                "participant_name": selected_participant,
                "score": score,
                "total_questions": 5,
                "quiz_date": str(date.today())
            }

            saved = save_record(
                "quiz_results",
                quiz_data
            )

            if saved:

                st.success(
                    "✅ Quiz result saved successfully!"
                )

                st.subheader(
                    "🏆 Score: "
                    + str(score)
                    + "/5"
                )

                if score == 5:

                    st.success(
                        "🌟 Excellent! Great understanding of online safety."
                    )

                    st.balloons()

                elif score >= 3:

                    st.info(
                        "👍 Good job! Keep learning about digital safety."
                    )

                else:

                    st.warning(
                        "📚 Review the Safety section and try again."
                    )


# ============================================================
# PARTICIPANTS
# ============================================================

elif page == "👩 Participants":

    st.title("👩 Participants")

    st.write(
        "Add women participating in the Self Help Group."
    )

    tab1, tab2 = st.tabs(
        [
            "➕ Add Participant",
            "📋 View Participants"
        ]
    )

    # --------------------------------------------------------
    # ADD PARTICIPANT
    # --------------------------------------------------------

    with tab1:

        with st.form("add_participant_form"):

            name = st.text_input(
                "👩 Full Name"
            )

            age = st.number_input(
                "Age",
                min_value=18,
                max_value=100,
                value=25
            )

            contact = st.text_input(
                "📞 Contact Number"
            )

            occupation = st.text_input(
                "💼 Occupation"
            )

            submitted = st.form_submit_button(
                "➕ Add Participant"
            )

            if submitted:

                if name.strip() == "":

                    st.warning(
                        "⚠️ Please enter participant name."
                    )

                else:

                    participant_data = {
                        "name": name.strip(),
                        "age": age,
                        "contact": contact.strip(),
                        "occupation": occupation.strip()
                    }

                    saved = save_record(
                        "participants",
                        participant_data
                    )

                    if saved:

                        st.success(
                            "✅ Participant added successfully!"
                        )

                        st.rerun()

    # --------------------------------------------------------
    # VIEW PARTICIPANTS
    # --------------------------------------------------------

    with tab2:

        participants = get_records(
            "participants"
        )

        if len(participants) > 0:

            st.dataframe(
                participants,
                use_container_width=True,
                hide_index=True
            )

            st.metric(
                "Total Participants",
                len(participants)
            )

        else:

            st.info(
                "No participants added yet."
            )


# ============================================================
# RECORDS
# ============================================================

elif page == "📋 Records":

    st.title("📋 Records")

    st.write(
        "View saved participant and quiz information."
    )

    tab1, tab2 = st.tabs(
        [
            "👩 Participant Records",
            "🎯 Quiz Records"
        ]
    )

    # --------------------------------------------------------
    # PARTICIPANT RECORDS
    # --------------------------------------------------------

    with tab1:

        participants = get_records(
            "participants"
        )

        if len(participants) > 0:

            st.dataframe(
                participants,
                use_container_width=True,
                hide_index=True
            )

            st.metric(
                "Total Participants",
                len(participants)
            )

        else:

            st.info(
                "No participant records found."
            )

    # --------------------------------------------------------
    # QUIZ RECORDS
    # --------------------------------------------------------

    with tab2:

        quiz_results = get_records(
            "quiz_results"
        )

        if len(quiz_results) > 0:

            st.dataframe(
                quiz_results,
                use_container_width=True,
                hide_index=True
            )

            st.metric(
                "Total Quiz Attempts",
                len(quiz_results)
            )

        else:

            st.info(
                "No quiz records found."
            )


# ============================================================
# HELP
# ============================================================

elif page == "🚨 Help":

    st.title("🚨 Women Safety & Emergency Help")

    st.write(
        "Keep important emergency numbers easily accessible."
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown(
            """
            <div class="emergency-box">
                <h1>🚨</h1>
                <h2>112</h2>
                <p>Emergency</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            """
            <div class="emergency-box">
                <h1>👩</h1>
                <h2>181</h2>
                <p>Women Helpline</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:

        st.markdown(
            """
            <div class="emergency-box">
                <h1>💻</h1>
                <h2>1930</h2>
                <p>Cyber Crime</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.subheader("📍 Digital Safety")

    st.markdown(
        """
        - Share live location only with trusted people.
        - Avoid posting real-time location publicly.
        - Keep phone screen lock enabled.
        - Save emergency contacts.
        """
    )

    st.subheader("💻 Report Cyber Crime")

    st.write(
        "Cyber Crime Helpline: **1930**"
    )

    st.link_button(
        "🌐 Open National Cyber Crime Reporting Portal",
        "https://www.cybercrime.gov.in/"
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div class="footer">
        🌸 <b>Digital Saheli</b>
        <br>
        CEP Project — Smartphone Usage & Online Safety for Women
        <br>
        Learn • Protect • Stay Connected
    </div>
    """,
    unsafe_allow_html=True
)
