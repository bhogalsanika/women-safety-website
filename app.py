import streamlit as st
from supabase import create_client, Client
import pandas as pd
import plotly.express as px
from datetime import date

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Women Safety Management System",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

body {
    background-color: #f5f7fa;
}

[data-testid="stSidebar"] {
    background-color: white;
}

h1, h2, h3 {
    color: #1f2937;
}

.stButton > button {
    background-color: #1f4e79;
    color: white;
    border-radius: 6px;
    border: none;
}

.stButton > button:hover {
    background-color: #163a5c;
    color: white;
}

.metric-card {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #e5e7eb;
    text-align: center;
}

.info-box {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #e5e7eb;
    margin-bottom: 15px;
}

.section-divider {
    margin-top: 20px;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SUPABASE CONNECTION
# =========================================================

@st.cache_resource
def init_connection() -> Client:
    return create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"]
    )

supabase = init_connection()

# =========================================================
# DATABASE FUNCTIONS
# =========================================================

def get_table(table_name):
    try:
        response = supabase.table(table_name).select("*").execute()
        return pd.DataFrame(response.data)
    except Exception as e:
        st.error(f"Error loading {table_name}: {e}")
        return pd.DataFrame()


def add_record(table_name, data):
    try:
        supabase.table(table_name).insert(data).execute()
        st.success("Record added successfully.")
        st.rerun()
    except Exception as e:
        st.error(f"Error adding record: {e}")


def update_record(table_name, record_id, id_column, data):
    try:
        supabase.table(table_name).update(data).eq(
            id_column, record_id
        ).execute()
        st.success("Record updated successfully.")
        st.rerun()
    except Exception as e:
        st.error(f"Error updating record: {e}")


def delete_record(table_name, record_id, id_column):
    try:
        supabase.table(table_name).delete().eq(
            id_column, record_id
        ).execute()
        st.success("Record deleted successfully.")
        st.rerun()
    except Exception as e:
        st.error(f"Error deleting record: {e}")


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown("## Women Safety Management System")

st.sidebar.markdown(
    "Smartphone Usage and Online Safety for Women Self Help Groups"
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Smartphone Usage Information",
        "Online Safety Information",
        "Participants",
        "Smartphone Usage",
        "Safety Events",
        "Training Sessions",
        "Reports"
    ]
)

st.sidebar.markdown("---")

st.sidebar.caption("Community Engagement Project")
st.sidebar.caption("Database Management System")


# =========================================================
# LOAD DATA
# =========================================================

participants = get_table("participants")
smartphone_usage = get_table("smartphone_usage")
safety_events = get_table("safety_events")
training_sessions = get_table("training_sessions")


# =========================================================
# DASHBOARD
# =========================================================

if page == "Dashboard":

    st.title("Dashboard")

    st.markdown(
        "Overview of smartphone usage, online safety and community activities."
    )

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Participants",
            len(participants)
        )

    with col2:
        st.metric(
            "Usage Records",
            len(smartphone_usage)
        )

    with col3:
        st.metric(
            "Safety Events",
            len(safety_events)
        )

    with col4:
        st.metric(
            "Training Sessions",
            len(training_sessions)
        )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Participants by Occupation")

        if not participants.empty and "occupation" in participants.columns:

            occupation_data = (
                participants["occupation"]
                .fillna("Not Specified")
                .value_counts()
                .reset_index()
            )

            occupation_data.columns = ["Occupation", "Count"]

            fig = px.bar(
                occupation_data,
                x="Occupation",
                y="Count",
                title="Occupation Distribution"
            )

            st.plotly_chart(fig, use_container_width=True)

        else:
            st.info("No participant data available.")

    with col2:

        st.subheader("Smartphone Users")

        if not participants.empty and "smartphone_user" in participants.columns:

            user_data = (
                participants["smartphone_user"]
                .value_counts()
                .reset_index()
            )

            user_data.columns = ["Smartphone User", "Count"]

            user_data["Smartphone User"] = user_data[
                "Smartphone User"
            ].map({
                True: "Yes",
                False: "No"
            })

            fig = px.pie(
                user_data,
                names="Smartphone User",
                values="Count",
                title="Smartphone Usage"
            )

            st.plotly_chart(fig, use_container_width=True)

        else:
            st.info("No smartphone user data available.")


# =========================================================
# SMARTPHONE USAGE INFORMATION
# =========================================================

elif page == "Smartphone Usage Information":

    st.title("Smartphone Usage Information")

    st.markdown(
        """
        Smartphones are useful tools for communication, education,
        banking, shopping, business and accessing online services.
        Women can use smartphones more effectively by understanding
        their basic functions and following safe digital practices.
        """
    )

    st.markdown("---")

    st.subheader("1. Basic Smartphone Functions")

    st.markdown(
        """
        - Making and receiving phone calls
        - Sending and receiving messages
        - Saving and managing contacts
        - Using the camera
        - Connecting to Wi-Fi and mobile data
        - Adjusting volume and brightness
        - Installing and updating applications
        - Using the internet and web browsers
        """
    )

    st.subheader("2. Common Uses of Smartphones")

    st.markdown(
        """
        Smartphones can be used for:

        - Communication through calls and messaging
        - Online education and learning
        - Digital payments and banking
        - Online shopping
        - Social media
        - Watching educational videos
        - Online work and small businesses
        - Accessing government and public services
        """
    )

    st.subheader("3. Safe Smartphone Practices")

    st.markdown(
        """
        - Keep a screen lock such as PIN, password or fingerprint.
        - Keep the phone software updated.
        - Install applications only from trusted official app stores.
        - Check application permissions before allowing access.
        - Avoid unknown or unsecured Wi-Fi networks.
        - Keep important data backed up.
        - Do not share your phone password with unknown people.
        """
    )

    st.subheader("4. Using Mobile Applications Safely")

    st.markdown(
        """
        Before installing an application:

        - Check the application name and developer.
        - Read reviews and ratings.
        - Check the permissions requested.
        - Avoid downloading applications from unknown websites.
        - Keep applications updated.
        - Remove applications that are no longer required.
        """
    )

    st.subheader("5. Digital Literacy for Women")

    st.markdown(
        """
        Smartphone knowledge can help women communicate independently,
        access education, use digital payments, find information,
        manage online services and participate safely in the digital world.
        """
    )

    st.info(
        "Remember: Understand the purpose of an application before using it "
        "and always check before sharing personal information."
    )


# =========================================================
# ONLINE SAFETY INFORMATION
# =========================================================

elif page == "Online Safety Information":

    st.title("Online Safety Information")

    st.markdown(
        """
        Online safety means protecting personal information, accounts,
        money and privacy while using smartphones and the internet.
        """
    )

    st.markdown("---")

    st.subheader("1. Password Safety")

    st.markdown(
        """
        - Use strong and unique passwords.
        - Avoid using your name, birthday or mobile number as a password.
        - Do not share passwords with other people.
        - Use different passwords for important accounts.
        - Enable two-factor authentication whenever available.
        """
    )

    st.subheader("2. OTP, PIN and Banking Safety")

    st.markdown(
        """
        - Never share OTP with anyone.
        - Never share ATM PIN, UPI PIN or CVV.
        - Do not share banking passwords.
        - Do not allow unknown people to operate your banking application.
        - Check the receiver's name before making a digital payment.
        """
    )

    st.subheader("3. Phishing and Suspicious Links")

    st.markdown(
        """
        Phishing is an attempt to steal personal information through
        fake messages, emails, websites or links.

        Be careful with messages claiming:

        - You have won a prize.
        - Your bank account will be blocked.
        - You must immediately update KYC.
        - You have received a refund.
        - You must click a link to receive money.

        Always verify the sender before clicking a link.
        """
    )

    st.subheader("4. Social Media Safety")

    st.markdown(
        """
        - Keep social media accounts private when appropriate.
        - Do not share your home address publicly.
        - Avoid sharing live location publicly.
        - Accept friend or follow requests carefully.
        - Block and report suspicious accounts.
        - Think before posting photos or personal information.
        """
    )

    st.subheader("5. Digital Payment Safety")

    st.markdown(
        """
        - Never share your UPI PIN or OTP.
        - Verify the recipient before sending money.
        - Do not scan unknown QR codes.
        - Check transaction notifications and bank statements regularly.
        - Do not click payment links received from unknown people.
        """
    )

    st.subheader("6. Online Shopping Safety")

    st.markdown(
        """
        - Use trusted shopping websites and applications.
        - Check the website address before making a payment.
        - Be careful with extremely cheap offers from unknown sellers.
        - Do not share unnecessary personal information.
        - Check seller details and reviews before purchasing.
        """
    )

    st.subheader("7. Cyberbullying and Online Harassment")

    st.markdown(
        """
        If someone is harassing or threatening you online:

        - Do not respond aggressively.
        - Block the person.
        - Report the account or content.
        - Save screenshots and other evidence.
        - Inform a trusted person.
        - Report serious incidents through appropriate cybercrime channels.
        """
    )

    st.subheader("8. What to Do After Online Fraud")

    st.markdown(
        """
        If you become a victim of online financial fraud:

        1. Contact your bank or payment service immediately.
        2. Secure or block the affected account or card if necessary.
        3. Save transaction details, screenshots and messages.
        4. Do not delete important evidence.
        5. Report the incident through the official cybercrime reporting channel.
        """
    )

    st.subheader("9. Simple Online Safety Rule")

    st.info(
        "STOP → CHECK → VERIFY → THEN CLICK OR PAY"
    )


# =========================================================
# PARTICIPANTS
# =========================================================

elif page == "Participants":

    st.title("Participants")

    st.subheader("Add Participant")

    with st.form("participant_form"):

        name = st.text_input("Name")

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=100,
            value=25
        )

        contact = st.text_input("Contact")

        occupation = st.text_input("Occupation")

        smartphone_user = st.checkbox(
            "Smartphone User",
            value=True
        )

        submitted = st.form_submit_button("Add Participant")

        if submitted:

            if name.strip() == "":
                st.error("Please enter participant name.")

            else:

                data = {
                    "name": name,
                    "age": age,
                    "contact": contact,
                    "occupation": occupation,
                    "smartphone_user": smartphone_user
                }

                add_record(
                    "participants",
                    data
                )

    st.markdown("---")

    st.subheader("Participant Records")

    if not participants.empty:

        search = st.text_input(
            "Search Participant"
        )

        filtered = participants.copy()

        if search:

            filtered = filtered[
                filtered["name"]
                .astype(str)
                .str.contains(
                    search,
                    case=False,
                    na=False
                )
            ]

        st.dataframe(
            filtered,
            use_container_width=True
        )

        st.subheader("Delete Participant")

        participant_id = st.number_input(
            "Participant ID",
            min_value=1,
            step=1
        )

        if st.button("Delete Participant"):

            delete_record(
                "participants",
                participant_id,
                "participant_id"
            )

    else:

        st.info("No participants found.")


# =========================================================
# SMARTPHONE USAGE
# =========================================================

elif page == "Smartphone Usage":

    st.title("Smartphone Usage")

    st.subheader("Add Smartphone Usage Record")

    if participants.empty:

        st.warning(
            "Please add participants first."
        )

    else:

        with st.form("usage_form"):

            participant_options = participants[
                ["participant_id", "name"]
            ]

            participant_display = {
                f"{row['participant_id']} - {row['name']}":
                row["participant_id"]
                for _, row in participant_options.iterrows()
            }

            selected_participant = st.selectbox(
                "Participant",
                list(participant_display.keys())
            )

            usage_purpose = st.selectbox(
                "Primary Usage Purpose",
                [
                    "Communication",
                    "Education",
                    "Digital Payment",
                    "Social Media",
                    "Online Shopping",
                    "Business",
                    "Entertainment",
                    "Government Services"
                ]
            )

            social_media = st.checkbox(
                "Social Media"
            )

            digital_payment = st.checkbox(
                "Digital Payment"
            )

            online_shopping = st.checkbox(
                "Online Shopping"
            )

            education = st.checkbox(
                "Education"
            )

            daily_usage_hours = st.number_input(
                "Daily Usage Hours",
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
                        participant_display[selected_participant],

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
                        daily_usage_hours
                }

                add_record(
                    "smartphone_usage",
                    data
                )

    st.markdown("---")

    st.subheader("Smartphone Usage Records")

    if not smartphone_usage.empty:

        st.dataframe(
            smartphone_usage,
            use_container_width=True
        )

    else:

        st.info(
            "No smartphone usage records found."
        )


# =========================================================
# SAFETY EVENTS
# =========================================================

elif page == "Safety Events":

    st.title("Safety Events")

    st.subheader("Add Safety Event")

    if participants.empty:

        st.warning(
            "Please add participants first."
        )

    else:

        with st.form("safety_event_form"):

            participant_options = participants[
                ["participant_id", "name"]
            ]

            participant_display = {
                f"{row['participant_id']} - {row['name']}":
                row["participant_id"]
                for _, row in participant_options.iterrows()
            }

            selected_participant = st.selectbox(
                "Participant",
                list(participant_display.keys())
            )

            event_type = st.selectbox(
                "Event Type",
                [
                    "Phishing",
                    "Online Fraud",
                    "Cyberbullying",
                    "Fake Account",
                    "Suspicious Link",
                    "Payment Fraud",
                    "Harassment",
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

            reported = st.checkbox(
                "Reported"
            )

            submitted = st.form_submit_button(
                "Add Safety Event"
            )

            if submitted:

                data = {
                    "participant_id":
                        participant_display[selected_participant],

                    "event_type":
                        event_type,

                    "event_date":
                        str(event_date),

                    "description":
                        description,

                    "action_taken":
                        action_taken,

                    "reported":
                        reported
                }

                add_record(
                    "safety_events",
                    data
                )

    st.markdown("---")

    st.subheader("Safety Event Records")

    if not safety_events.empty:

        st.dataframe(
            safety_events,
            use_container_width=True
        )

    else:

        st.info(
            "No safety events found."
        )


# =========================================================
# TRAINING SESSIONS
# =========================================================

elif page == "Training Sessions":

    st.title("Training Sessions")

    st.subheader("Add Training Session")

    with st.form("training_form"):

        session_date = st.date_input(
            "Session Date",
            value=date.today()
        )

        topic = st.text_input(
            "Topic"
        )

        trainer_name = st.text_input(
            "Trainer Name"
        )

        participants_count = st.number_input(
            "Number of Participants",
            min_value=0,
            value=0
        )

        notes = st.text_area(
            "Notes"
        )

        submitted = st.form_submit_button(
            "Add Training Session"
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

            add_record(
                "training_sessions",
                data
            )

    st.markdown("---")

    st.subheader("Training Session Records")

    if not training_sessions.empty:

        st.dataframe(
            training_sessions,
            use_container_width=True
        )

    else:

        st.info(
            "No training sessions found."
        )


# =========================================================
# REPORTS
# =========================================================

elif page == "Reports":

    st.title("Reports")

    # -----------------------------------------------------
    # SAFETY EVENTS REPORT
    # -----------------------------------------------------

    st.subheader("Safety Events Report")

    if not safety_events.empty:

        event_data = (
            safety_events["event_type"]
            .fillna("Not Specified")
            .value_counts()
            .reset_index()
        )

        event_data.columns = [
            "Event Type",
            "Count"
        ]

        fig = px.bar(
            event_data,
            x="Event Type",
            y="Count",
            title="Safety Events by Type"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.info(
            "No safety event data available."
        )

    # -----------------------------------------------------
    # SMARTPHONE USAGE REPORT
    # -----------------------------------------------------

    st.subheader("Smartphone Usage Report")

    if not smartphone_usage.empty:

        usage_data = (
            smartphone_usage["usage_purpose"]
            .fillna("Not Specified")
            .value_counts()
            .reset_index()
        )

        usage_data.columns = [
            "Usage Purpose",
            "Count"
        ]

        fig = px.bar(
            usage_data,
            x="Usage Purpose",
            y="Count",
            title="Smartphone Usage by Purpose"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        if "daily_usage_hours" in smartphone_usage.columns:

            avg_hours = pd.to_numeric(
                smartphone_usage["daily_usage_hours"],
                errors="coerce"
            ).mean()

            if pd.notna(avg_hours):

                st.metric(
                    "Average Daily Smartphone Usage",
                    f"{avg_hours:.2f} hours"
                )

    else:

        st.info(
            "No smartphone usage data available."
        )

    # -----------------------------------------------------
    # TRAINING REPORT
    # -----------------------------------------------------

    st.subheader("Training Sessions Report")

    if not training_sessions.empty:

        training_data = training_sessions.copy()

        if "topic" in training_data.columns:

            topic_data = (
                training_data["topic"]
                .fillna("Not Specified")
                .value_counts()
                .reset_index()
            )

            topic_data.columns = [
                "Topic",
                "Sessions"
            ]

            fig = px.bar(
                topic_data,
                x="Topic",
                y="Sessions",
                title="Training Sessions by Topic"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    else:

        st.info(
            "No training session data available."
        )

    # -----------------------------------------------------
    # CSV EXPORT
    # -----------------------------------------------------

    st.markdown("---")

    st.subheader("Export Reports")

    if not participants.empty:

        participants_csv = participants.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "Download Participants CSV",
            participants_csv,
            "participants.csv",
            "text/csv"
        )

    if not smartphone_usage.empty:

        usage_csv = smartphone_usage.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "Download Smartphone Usage CSV",
            usage_csv,
            "smartphone_usage.csv",
            "text/csv"
        )

    if not safety_events.empty:

        safety_csv = safety_events.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "Download Safety Events CSV",
            safety_csv,
            "safety_events.csv",
            "text/csv"
        )

    if not training_sessions.empty:

        training_csv = training_sessions.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "Download Training Sessions CSV",
            training_csv,
            "training_sessions.csv",
            "text/csv"
        )



