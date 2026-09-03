import streamlit as st
from supabase import create_client, Client
import pandas as pd
import plotly.express as px
from datetime import date

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Women Digital Safety",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>
.stApp {
    background-color: #f7f8fa;
}

section[data-testid="stSidebar"] {
    background-color: white;
    border-right: 1px solid #e5e7eb;
}

h1, h2, h3 {
    color: #1f2937;
}

.stButton > button {
    width: 100%;
    border-radius: 8px;
    background-color: #1f4e79;
    color: white;
    border: none;
    padding: 10px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #163a5c;
}

.card {
    background-color: white;
    padding: 22px;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
    margin-bottom: 15px;
}

.safe {
    background-color: #eef8f0;
    border-left: 5px solid #2e7d32;
    padding: 15px;
    border-radius: 8px;
    margin: 10px 0;
}

.warning {
    background-color: #fff8e6;
    border-left: 5px solid #d99000;
    padding: 15px;
    border-radius: 8px;
    margin: 10px 0;
}

.danger {
    background-color: #fff0f0;
    border-left: 5px solid #c62828;
    padding: 15px;
    border-radius: 8px;
    margin: 10px 0;
}

.hero {
    background-color: white;
    padding: 35px;
    border-radius: 15px;
    border: 1px solid #e5e7eb;
    margin-bottom: 25px;
}

.small-text {
    color: #6b7280;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# SUPABASE CONNECTION
# ============================================================

@st.cache_resource
def init_connection() -> Client:
    return create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"]
    )

try:
    supabase = init_connection()
except Exception:
    st.error(
        "Unable to connect to Supabase. "
        "Please check SUPABASE_URL and SUPABASE_KEY."
    )
    st.stop()

# ============================================================
# DATABASE FUNCTIONS
# ============================================================

def get_table(table_name):
    try:
        response = supabase.table(table_name).select("*").execute()
        return response.data
    except Exception as e:
        st.error(f"Unable to retrieve data from {table_name}: {e}")
        return []


def add_record(table_name, data):
    try:
        supabase.table(table_name).insert(data).execute()
        return True
    except Exception as e:
        st.error(f"Unable to add record: {e}")
        return False


def delete_record(table_name, column, value):
    try:
        supabase.table(table_name).delete().eq(column, value).execute()
        return True
    except Exception as e:
        st.error(f"Unable to delete record: {e}")
        return False


# ============================================================
# LOAD DATABASE
# ============================================================

participants = get_table("participants")
usage_records = get_table("smartphone_usage")
safety_events = get_table("safety_events")
training_sessions = get_table("training_sessions")

participants_df = pd.DataFrame(participants)
usage_df = pd.DataFrame(usage_records)
events_df = pd.DataFrame(safety_events)
training_df = pd.DataFrame(training_sessions)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🛡️ Women Digital Safety")

st.sidebar.caption(
    "Smartphone Usage and Online Safety "
    "for Women Self Help Groups"
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📱 Smartphone Guide",
        "🔐 Online Safety",
        "💳 Digital Payment Safety",
        "👩 Women Safety",
        "🚨 Emergency Help",
        "❓ Safety Quiz",
        "📊 Dashboard",
        "👥 Participants",
        "📱 Usage Records",
        "⚠️ Safety Events",
        "🎓 Training Sessions",
        "📄 Reports"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("Community Engagement Project")
st.sidebar.caption("Database Management System")

# ============================================================
# HOME
# ============================================================

if page == "🏠 Home":

    st.markdown("""
    <div class="hero">
        <h1>Smartphone Usage & Online Safety</h1>
        <p>
        A simple digital awareness platform created to help women
        use smartphones safely and confidently.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Learn • Protect • Stay Safe")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>📱 Smartphone Skills</h3>
        <p>Learn basic smartphone and internet usage.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>🔐 Online Protection</h3>
        <p>Learn how to protect passwords, OTPs and personal information.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>🚨 Emergency Support</h3>
        <p>Find important emergency and cyber-fraud helpline information.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("Explore Safety Topics")

    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button("📱 Smartphone Guide"):
            st.info("Use the Smartphone Guide from the sidebar.")

        if st.button("🔐 Online Safety"):
            st.info("Use the Online Safety section from the sidebar.")

    with c2:
        if st.button("💳 Payment Safety"):
            st.info("Learn safe UPI and digital payment practices.")

        if st.button("👩 Women Safety"):
            st.info("Learn about online harassment, fake accounts and privacy.")

    with c3:
        if st.button("🚨 Emergency Help"):
            st.info("Open Emergency Help from the sidebar.")

        if st.button("❓ Take Safety Quiz"):
            st.info("Open Safety Quiz from the sidebar.")

# ============================================================
# SMARTPHONE GUIDE
# ============================================================

elif page == "📱 Smartphone Guide":

    st.title("📱 Smartphone Guide")

    st.write(
        "Basic smartphone skills for safe and confident digital usage."
    )

    topics = [
        (
            "📞 Making Calls",
            "Open the Phone app, select a contact and tap the call button. "
            "Avoid sharing personal information with unknown callers."
        ),
        (
            "💬 WhatsApp",
            "Use WhatsApp to communicate with trusted contacts. "
            "Check privacy settings and avoid opening suspicious links."
        ),
        (
            "🌐 Internet",
            "Use trusted websites and avoid downloading files from unknown sources."
        ),
        (
            "📲 Installing Apps",
            "Download applications from official app stores. "
            "Check the app name, developer and permissions before installing."
        ),
        (
            "🔒 Phone Lock",
            "Use a PIN, password, fingerprint or other available screen lock "
            "to protect your phone."
        ),
        (
            "⚙️ Privacy Settings",
            "Review camera, microphone, location and contact permissions "
            "regularly."
        )
    ]

    for title, information in topics:
        with st.expander(title):
            st.write(information)

            st.markdown("""
            <div class="safe">
            ✅ <b>Do:</b> Keep your phone updated and use a screen lock.
            </div>

            <div class="danger">
            ❌ <b>Don't:</b> Give your unlocked phone to unknown people.
            </div>
            """, unsafe_allow_html=True)

# ============================================================
# ONLINE SAFETY
# ============================================================

elif page == "🔐 Online Safety":

    st.title("🔐 Online Safety")

    st.write("Learn what to do and what not to do while using the internet.")

    with st.expander("🔑 Password Safety"):
        st.markdown("""
        ### ✅ What to Do
        - Use a strong and unique password.
        - Use different passwords for important accounts.
        - Enable two-factor authentication where available.

        ### ❌ What NOT to Do
        - Do not share your password with anyone.
        - Do not use simple passwords such as 123456.
        - Do not save passwords on public computers.
        """)

    with st.expander("🔢 OTP Safety"):
        st.markdown("""
        ### ✅ What to Do
        - Read the message before entering an OTP.
        - Enter OTP only on the genuine website or application.

        ### ❌ What NOT to Do
        - Never share an OTP with anyone over phone or message.
        - Do not enter OTP on suspicious websites.
        """)

    with st.expander("🔗 Unknown Links & Phishing"):
        st.markdown("""
        ### ✅ What to Do
        - Check the sender before opening a link.
        - Verify important messages through the official website or app.

        ### ❌ What NOT to Do
        - Do not click suspicious links.
        - Do not download unknown files.
        - Do not provide passwords or banking details through unknown links.
        """)

    with st.expander("📱 Social Media Safety"):
        st.markdown("""
        ### ✅ What to Do
        - Keep profiles private when appropriate.
        - Accept requests only from people you know.
        - Review privacy settings regularly.

        ### ❌ What NOT to Do
        - Do not share your address, financial details or passwords.
        - Do not share sensitive personal photographs publicly.
        """)

    with st.expander("👤 Fake Accounts"):
        st.markdown("""
        ### Warning Signs
        - Unknown profile asking for money.
        - Very new or suspicious account.
        - Requests for personal photographs or information.

        ### What to Do
        - Block the account.
        - Report the account.
        - Save evidence if harassment or fraud is involved.
        """)

# ============================================================
# DIGITAL PAYMENT SAFETY
# ============================================================

elif page == "💳 Digital Payment Safety":

    st.title("💳 Digital Payment Safety")

    st.write("Follow these practices when using UPI, banking and online payments.")

    with st.expander("📲 UPI Safety"):
        st.markdown("""
        ### ✅ Do
        - Verify the recipient before making a payment.
        - Keep your UPI PIN private.
        - Use official banking applications.

        ### ❌ Don't
        - Never share your UPI PIN.
        - Never share OTPs.
        - Do not approve an unknown payment request.
        """)

    with st.expander("🔳 QR Code Safety"):
        st.markdown("""
        A QR code can be used to make or receive payments.

        ### Remember
        - Verify who sent the QR code.
        - Check the amount before confirming.
        - Do not scan unknown QR codes just because someone asks you to.
        """)

    with st.expander("🚨 Payment Fraud"):
        st.markdown("""
        If you notice an unauthorized transaction:

        1. Contact your bank/payment provider immediately.
        2. Report suspected cyber financial fraud promptly.
        3. Keep transaction details and screenshots.
        4. Do not continue communicating with the suspected fraudster.
        """)

# ============================================================
# WOMEN SAFETY
# ============================================================

elif page == "👩 Women Safety":

    st.title("👩 Women Online Safety")

    st.write(
        "Practical guidance for protecting personal information "
        "and dealing with online harassment."
    )

    with st.expander("🚫 Online Harassment"):
        st.markdown("""
        ### ✅ What to Do
        - Block the person.
        - Report the account.
        - Save relevant evidence.
        - Tell a trusted person.

        ### ❌ What NOT to Do
        - Do not share more personal information.
        - Do not meet an unknown person privately.
        - Do not send money because of threats.
        """)

    with st.expander("👀 Cyberstalking"):
        st.markdown("""
        Cyberstalking can include repeated unwanted messages,
        monitoring or threatening online behaviour.

        ### Safety Steps
        - Review privacy settings.
        - Block unwanted accounts.
        - Change compromised passwords.
        - Enable two-factor authentication.
        - Keep records of serious incidents.
        """)

    with st.expander("📸 Personal Photos & Videos"):
        st.markdown("""
        ### ✅ Do
        - Share sensitive photographs only when you are comfortable
          and trust the recipient.
        - Keep social media accounts appropriately private.

        ### ❌ Don't
        - Do not send sensitive photographs to strangers.
        - Do not share another person's private content without permission.
        """)

    with st.expander("🚩 Block & Report"):
        st.markdown("""
        If an account is abusive, threatening or suspicious:

        **Block → Report → Save evidence → Inform a trusted person**

        For serious threats or crimes, contact appropriate authorities.
        """)

# ============================================================
# EMERGENCY HELP
# ============================================================

elif page == "🚨 Emergency Help":

    st.title("🚨 Emergency & Cyber Safety Help")

    st.warning(
        "If you are in immediate danger, contact emergency services "
        "or a trusted person immediately."
    )

    st.markdown("""
    <div class="card">
    <h3>112 — Emergency Response</h3>
    <p>For emergencies requiring immediate assistance in India.</p>
    </div>

    <div class="card">
    <h3>1091 — Women Helpline</h3>
    <p>Women’s helpline number. Availability and service may vary by location.</p>
    </div>

    <div class="card">
    <h3>1930 — Cyber Fraud Helpline</h3>
    <p>For reporting financial cyber fraud in India.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("What to do after an online scam")

    st.markdown("""
    1. Stay calm and stop further communication with the scammer.
    2. Contact your bank/payment service immediately if money is involved.
    3. Report financial cyber fraud promptly through the appropriate official channel.
    4. Change compromised passwords.
    5. Keep screenshots, transaction IDs and other relevant evidence.
    """)

# ============================================================
# SAFETY QUIZ
# ============================================================

elif page == "❓ Safety Quiz":

    st.title("❓ Online Safety Quiz")

    questions = [
        (
            "Should you share your OTP with someone who calls you?",
            ["Yes", "No"],
            "No"
        ),
        (
            "Should you use a strong password?",
            ["Yes", "No"],
            "Yes"
        ),
        (
            "Should you click every link received by SMS?",
            ["Yes", "No"],
            "No"
        ),
        (
            "Should you keep your UPI PIN private?",
            ["Yes", "No"],
            "Yes"
        ),
        (
            "What should you do with a suspicious social media account?",
            ["Block and Report", "Send personal information"],
            "Block and Report"
        )
    ]

    score = 0

    for i, (question, options, answer) in enumerate(questions):

        st.subheader(f"Q{i+1}. {question}")

        selected = st.radio(
            "Select an answer:",
            options,
            key=f"quiz_{i}"
        )

        if selected == answer:
            score += 1

    if st.button("Check My Score"):

        st.success(
            f"Your score is {score} / {len(questions)}"
        )

        if score == len(questions):
            st.balloons()
            st.success("Excellent! You have strong online safety awareness.")
        elif score >= 3:
            st.info("Good job! Review the safety sections to improve further.")
        else:
            st.warning("Please review the Online Safety and Payment Safety sections.")

# ============================================================
# DASHBOARD
# ============================================================

elif page == "📊 Dashboard":

    st.title("📊 Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Participants", len(participants_df))
    c2.metric("Usage Records", len(usage_df))
    c3.metric("Safety Events", len(events_df))
    c4.metric("Training Sessions", len(training_df))

    st.markdown("---")

    if not participants_df.empty:

        col1, col2 = st.columns(2)

        with col1:

            if "occupation" in participants_df.columns:

                data = (
                    participants_df["occupation"]
                    .fillna("Not Specified")
                    .value_counts()
                    .reset_index()
                )

                data.columns = ["Occupation", "Participants"]

                fig = px.bar(
                    data,
                    x="Occupation",
                    y="Participants",
                    title="Participants by Occupation"
                )

                fig.update_layout(template="simple_white")

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

        with col2:

            if "smartphone_user" in participants_df.columns:

                data = (
                    participants_df["smartphone_user"]
                    .map({
                        True: "Smartphone User",
                        False: "Non-Smartphone User"
                    })
                    .value_counts()
                    .reset_index()
                )

                data.columns = ["Category", "Participants"]

                fig = px.pie(
                    data,
                    names="Category",
                    values="Participants",
                    title="Smartphone Usage Status"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

# ============================================================
# PARTICIPANTS
# ============================================================

elif page == "👥 Participants":

    st.title("👥 Participant Management")

    tab1, tab2 = st.tabs(
        ["Add Participant", "View Participants"]
    )

    with tab1:

        with st.form("participant_form"):

            col1, col2 = st.columns(2)

            with col1:
                name = st.text_input("Full Name")
                age = st.number_input(
                    "Age",
                    min_value=18,
                    max_value=100,
                    value=25
                )
                contact = st.text_input("Contact Number")

            with col2:
                occupation = st.text_input("Occupation")

                smartphone_user = st.selectbox(
                    "Smartphone User",
                    ["Yes", "No"]
                )

            submitted = st.form_submit_button(
                "Add Participant"
            )

            if submitted:

                if not name.strip():

                    st.warning("Please enter participant name.")

                else:

                    data = {
                        "name": name.strip(),
                        "age": age,
                        "contact": contact.strip(),
                        "occupation": occupation.strip(),
                        "smartphone_user": smartphone_user == "Yes"
                    }

                    if add_record(
                        "participants",
                        data
                    ):

                        st.success(
                            "Participant added successfully."
                        )

                        st.rerun()

    with tab2:

        if participants_df.empty:

            st.info("No participant records found.")

        else:

            st.dataframe(
                participants_df,
                use_container_width=True,
                hide_index=True
            )

            if "participant_id" in participants_df.columns:

                selected_id = st.selectbox(
                    "Select Participant ID to Delete",
                    participants_df["participant_id"].tolist()
                )

                if st.button("Delete Participant"):

                    if delete_record(
                        "participants",
                        "participant_id",
                        selected_id
                    ):

                        st.success(
                            "Participant deleted successfully."
                        )

                        st.rerun()

# ============================================================
# USAGE RECORDS
# ============================================================

elif page == "📱 Usage Records":

    st.title("📱 Smartphone Usage Records")

    if participants_df.empty:

        st.warning(
            "Please add participants first."
        )

    else:

        participant_options = {
            f"{row['participant_id']} - {row['name']}":
            row["participant_id"]
            for _, row in participants_df.iterrows()
        }

        with st.form("usage_form"):

            participant = st.selectbox(
                "Participant",
                list(participant_options.keys())
            )

            usage_purpose = st.selectbox(
                "Primary Usage Purpose",
                [
                    "Communication",
                    "Social Media",
                    "Education",
                    "Digital Payments",
                    "Online Shopping",
                    "Entertainment",
                    "Business",
                    "Other"
                ]
            )

            col1, col2 = st.columns(2)

            with col1:

                social_media = st.checkbox(
                    "Uses Social Media"
                )

                digital_payment = st.checkbox(
                    "Uses Digital Payments"
                )

                online_shopping = st.checkbox(
                    "Uses Online Shopping"
                )

            with col2:

                education = st.checkbox(
                    "Uses Smartphone for Education"
                )

                daily_hours = st.number_input(
                    "Daily Smartphone Usage Hours",
                    min_value=0.0,
                    max_value=24.0,
                    value=2.0,
                    step=0.5
                )

            submitted = st.form_submit_button(
                "Add Usage Record"
            )

            if submitted:

                data = {
                    "participant_id":
                    participant_options[participant],

                    "usage_purpose":
                    usage_purpose,

                    "social_media":
                    social_media,

                    "digital_payment":
                    digital_payment,

                    "online_shopping":
                    online_shopping,

                    "education":
                    education,

                    "daily_usage_hours":
                    daily_hours
                }

                if add_record(
                    "smartphone_usage",
                    data
                ):

                    st.success(
                        "Usage record added successfully."
                    )

                    st.rerun()

        st.markdown("---")

        if usage_df.empty:

            st.info("No usage records found.")

        else:

            st.dataframe(
                usage_df,
                use_container_width=True,
                hide_index=True
            )

# ============================================================
# SAFETY EVENTS
# ============================================================

elif page == "⚠️ Safety Events":

    st.title("⚠️ Online Safety Events")

    if participants_df.empty:

        st.warning(
            "Please add participants first."
        )

    else:

        participant_options = {
            f"{row['participant_id']} - {row['name']}":
            row["participant_id"]
            for _, row in participants_df.iterrows()
        }

        with st.form("safety_form"):

            participant = st.selectbox(
                "Participant",
                list(participant_options.keys())
            )

            event_type = st.selectbox(
                "Event Type",
                [
                    "Suspicious Message",
                    "Phishing Link",
                    "Online Scam",
                    "Fake Account",
                    "Cyberbullying",
                    "Payment Fraud Attempt",
                    "Privacy Concern",
                    "Other"
                ]
            )

            event_date = st.date_input(
                "Event Date",
                value=date.today()
            )

            description = st.text_area(
                "Description"
            )

            action_taken = st.text_area(
                "Action Taken"
            )

            reported = st.selectbox(
                "Reported",
                ["Yes", "No"]
            )

            submitted = st.form_submit_button(
                "Save Safety Event"
            )

            if submitted:

                data = {
                    "participant_id":
                    participant_options[participant],

                    "event_type":
                    event_type,

                    "event_date":
                    str(event_date),

                    "description":
                    description,

                    "action_taken":
                    action_taken,

                    "reported":
                    reported == "Yes"
                }

                if add_record(
                    "safety_events",
                    data
                ):

                    st.success(
                        "Safety event saved successfully."
                    )

                    st.rerun()

        st.markdown("---")

        if events_df.empty:

            st.info("No safety events found.")

        else:

            st.dataframe(
                events_df,
                use_container_width=True,
                hide_index=True
            )

# ============================================================
# TRAINING SESSIONS
# ============================================================

elif page == "🎓 Training Sessions":

    st.title("🎓 Training & Awareness Sessions")

    with st.form("training_form"):

        session_date = st.date_input(
            "Session Date",
            value=date.today()
        )

        topic = st.selectbox(
            "Training Topic",
            [
                "Smartphone Basics",
                "Password Security",
                "Online Banking Safety",
                "Digital Payments",
                "Social Media Safety",
                "Phishing Awareness",
                "Privacy Settings",
                "Cyber Fraud Awareness",
                "Other"
            ]
        )

        trainer_name = st.text_input(
            "Trainer / Resource Person"
        )

        participants_count = st.number_input(
            "Number of Participants",
            min_value=1,
            max_value=1000,
            value=10
        )

        notes = st.text_area(
            "Notes"
        )

        submitted = st.form_submit_button(
            "Save Training Session"
        )

        if submitted:

            data = {
                "session_date":
                str(session_date),

                "topic":
                topic,

                "trainer_name":
                trainer_name,

                "participants_count":
                participants_count,

                "notes":
                notes
            }

            if add_record(
                "training_sessions",
                data
            ):

                st.success(
                    "Training session saved successfully."
                )

                st.rerun()

    st.markdown("---")

    if training_df.empty:

        st.info("No training sessions found.")

    else:

        st.dataframe(
            training_df,
            use_container_width=True,
            hide_index=True
        )

# ============================================================
# REPORTS
# ============================================================

elif page == "📄 Reports":

    st.title("📄 Reports")

    st.write(
        "Summary of participant, smartphone usage and safety information."
    )

    st.markdown("---")

    st.subheader("Participants")

    if participants_df.empty:
        st.info("No participant data available.")
    else:
        st.dataframe(
            participants_df,
            use_container_width=True,
            hide_index=True
        )

    st.subheader("Smartphone Usage")

    if usage_df.empty:
        st.info("No smartphone usage data available.")
    else:
        st.dataframe(
            usage_df,
            use_container_width=True,
            hide_index=True
        )

    st.subheader("Safety Events")

    if events_df.empty:
        st.info("No safety event data available.")
    else:
        st.dataframe(
            events_df,
            use_container_width=True,
            hide_index=True
        )

    st.subheader("Training Sessions")

    if training_df.empty:
        st.info("No training session data available.")
    else:
        st.dataframe(
            training_df,
            use_container_width=True,
            hide_index=True
        )

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Community Engagement Project | "
    "Smartphone Usage and Online Safety for Women Self Help Groups"
)
