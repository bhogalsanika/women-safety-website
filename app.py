
import streamlit as st
from supabase import create_client, Client
import pandas as pd
import plotly.express as px
from datetime import date


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Women Safety Management System",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #f7f8fa;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e2e5e9;
    }

    /* Main headings */
    h1, h2, h3 {
        color: #1f2937;
        font-weight: 600;
    }

    /* Normal text */
    p, label, div {
        color: #374151;
    }

    /* Metric cards */
    div[data-testid="stMetric"] {
        background-color: #ffffff;
        border: 1px solid #e2e5e9;
        border-radius: 10px;
        padding: 18px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }

    /* Buttons */
    .stButton > button {
        border-radius: 6px;
        border: 1px solid #1f4e79;
        background-color: #1f4e79;
        color: white;
        font-weight: 500;
        padding: 8px 18px;
    }

    .stButton > button:hover {
        background-color: #163a5c;
        border-color: #163a5c;
        color: white;
    }

    /* Dataframe */
    div[data-testid="stDataFrame"] {
        border: 1px solid #e2e5e9;
        border-radius: 8px;
    }

    /* Info boxes */
    .info-box {
        background-color: #ffffff;
        border-left: 4px solid #1f4e79;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 20px;
    }

    /* Section divider */
    .section-line {
        border-bottom: 1px solid #e2e5e9;
        margin: 10px 0 25px 0;
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
except Exception as e:
    st.error("Unable to connect to Supabase. Please verify the database credentials in Streamlit Secrets.")
    st.stop()


# ============================================================
# DATABASE FUNCTIONS
# ============================================================

def get_table(table_name):
    try:
        response = supabase.table(table_name).select("*").execute()
        return response.data
    except Exception as e:
        st.error(f"Unable to retrieve data from {table_name}.")
        return []


def add_record(table_name, data):
    try:
        supabase.table(table_name).insert(data).execute()
        return True
    except Exception as e:
        st.error(f"Unable to add record: {e}")
        return False


def update_record(table_name, column, value, data):
    try:
        supabase.table(table_name).update(data).eq(column, value).execute()
        return True
    except Exception as e:
        st.error(f"Unable to update record: {e}")
        return False


def delete_record(table_name, column, value):
    try:
        supabase.table(table_name).delete().eq(column, value).execute()
        return True
    except Exception as e:
        st.error(f"Unable to delete record: {e}")
        return False


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

st.sidebar.markdown("## Women Safety Management System")
st.sidebar.markdown(
    "Smartphone Usage and Online Safety for Women Self Help Groups"
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
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


# ============================================================
# LOAD DATA
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
# DASHBOARD
# ============================================================

if page == "Dashboard":

    st.title("Dashboard")
    st.markdown(
        "Overview of smartphone usage and online safety activities "
        "within the Women Self Help Group."
    )

    st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Participants",
        len(participants_df)
    )

    col2.metric(
        "Usage Records",
        len(usage_df)
    )

    col3.metric(
        "Safety Events",
        len(events_df)
    )

    col4.metric(
        "Training Sessions",
        len(training_df)
    )

    st.markdown("### System Overview")

    if participants_df.empty:
        st.info("No participant records are available yet.")
    else:

        col1, col2 = st.columns(2)

        with col1:

            if "occupation" in participants_df.columns:

                occupation_data = (
                    participants_df["occupation"]
                    .fillna("Not Specified")
                    .value_counts()
                    .reset_index()
                )

                occupation_data.columns = [
                    "Occupation",
                    "Participants"
                ]

                fig = px.bar(
                    occupation_data,
                    x="Occupation",
                    y="Participants",
                    title="Participants by Occupation"
                )

                fig.update_layout(
                    template="simple_white",
                    height=350
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

        with col2:

            if "smartphone_user" in participants_df.columns:

                smartphone_data = (
                    participants_df["smartphone_user"]
                    .map({
                        True: "Smartphone User",
                        False: "Non-Smartphone User"
                    })
                    .value_counts()
                    .reset_index()
                )

                smartphone_data.columns = [
                    "Category",
                    "Participants"
                ]

                fig = px.pie(
                    smartphone_data,
                    names="Category",
                    values="Participants",
                    title="Smartphone Usage Status"
                )

                fig.update_layout(
                    height=350
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )


# ============================================================
# PARTICIPANTS
# ============================================================

elif page == "Participants":

    st.title("Participant Management")

    st.markdown(
        "Manage participant information associated with the Women Self Help Group."
    )

    st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs([
        "Add Participant",
        "View Participants"
    ])

    # --------------------------------------------------------
    # ADD PARTICIPANT
    # --------------------------------------------------------

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
                    st.warning("Please enter the participant name.")

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

    # --------------------------------------------------------
    # VIEW PARTICIPANTS
    # --------------------------------------------------------

    with tab2:

        if participants_df.empty:

            st.info("No participant records found.")

        else:

            search = st.text_input(
                "Search participant"
            )

            display_df = participants_df.copy()

            if search:

                display_df = display_df[
                    display_df["name"]
                    .astype(str)
                    .str.contains(
                        search,
                        case=False,
                        na=False
                    )
                ]

            st.dataframe(
                display_df,
                use_container_width=True,
                hide_index=True
            )

            st.markdown("### Delete Participant")

            participant_ids = display_df["participant_id"].tolist()

            if participant_ids:

                selected_id = st.selectbox(
                    "Select Participant ID",
                    participant_ids
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
# SMARTPHONE USAGE
# ============================================================

elif page == "Smartphone Usage":

    st.title("Smartphone Usage Management")

    st.markdown(
        "Record and analyze how participants use smartphones and digital services."
    )

    st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)

    if participants_df.empty:

        st.warning(
            "Please add participants before recording smartphone usage."
        )

    else:

        tab1, tab2 = st.tabs([
            "Add Usage Record",
            "View Usage Records"
        ])

        with tab1:

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
                        "Daily Smartphone Usage (Hours)",
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
                            "Smartphone usage record added successfully."
                        )
                        st.rerun()

        with tab2:

            if usage_df.empty:

                st.info(
                    "No smartphone usage records found."
                )

            else:

                st.dataframe(
                    usage_df,
                    use_container_width=True,
                    hide_index=True
                )


# ============================================================
# SAFETY EVENTS
# ============================================================

elif page == "Safety Events":

    st.title("Online Safety Events")

    st.markdown(
        "Record online safety concerns and actions taken by participants."
    )

    st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)

    if participants_df.empty:

        st.warning(
            "Please add participants before recording safety events."
        )

    else:

        tab1, tab2 = st.tabs([
            "Report Safety Event",
            "View Events"
        ])

        with tab1:

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
                            "Safety event recorded successfully."
                        )
                        st.rerun()

        with tab2:

            if events_df.empty:

                st.info(
                    "No safety events have been recorded."
                )

            else:

                st.dataframe(
                    events_df,
                    use_container_width=True,
                    hide_index=True
                )


# ============================================================
# TRAINING SESSIONS
# ============================================================

elif page == "Training Sessions":

    st.title("Training and Awareness Sessions")

    st.markdown(
        "Manage digital literacy and online safety awareness sessions."
    )

    st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs([
        "Add Session",
        "View Sessions"
    ])

    with tab1:

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
                "Add Training Session"
            )

            if submitted:

                data = {
                    "session_date":
                        str(session_date),
                    "topic":
                        topic,
                    "trainer_name":
                        trainer_name.strip(),
                    "participants_count":
                        participants_count,
                    "notes":
                        notes.strip()
                }

                if add_record(
                    "training_sessions",
                    data
                ):
                    st.success(
                        "Training session added successfully."
                    )
                    st.rerun()

    with tab2:

        if training_df.empty:

            st.info(
                "No training sessions found."
            )

        else:

            st.dataframe(
                training_df,
                use_container_width=True,
                hide_index=True
            )


# ============================================================
# REPORTS
# ============================================================

elif page == "Reports":

    st.title("Reports and Analysis")

    st.markdown(
        "Analyze smartphone usage, online safety events, and training activities."
    )

    st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)

    # --------------------------------------------------------
    # SAFETY EVENT ANALYSIS
    # --------------------------------------------------------

    if not events_df.empty and "event_type" in events_df.columns:

        st.subheader("Online Safety Event Analysis")

        event_counts = (
            events_df["event_type"]
            .value_counts()
            .reset_index()
        )

        event_counts.columns = [
            "Event Type",
            "Number of Events"
        ]

        fig = px.bar(
            event_counts,
            x="Event Type",
            y="Number of Events",
            title="Safety Events by Type"
        )

        fig.update_layout(
            template="simple_white",
            height=400
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # --------------------------------------------------------
    # SMARTPHONE USAGE ANALYSIS
    # --------------------------------------------------------

    if not usage_df.empty:

        st.subheader("Smartphone Usage Analysis")

        if "usage_purpose" in usage_df.columns:

            purpose_counts = (
                usage_df["usage_purpose"]
                .value_counts()
                .reset_index()
            )

            purpose_counts.columns = [
                "Purpose",
                "Records"
            ]

            fig = px.bar(
                purpose_counts,
                x="Purpose",
                y="Records",
                title="Primary Smartphone Usage Purpose"
            )

            fig.update_layout(
                template="simple_white",
                height=400
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        if "daily_usage_hours" in usage_df.columns:

            average_hours = usage_df[
                "daily_usage_hours"
            ].mean()

            st.metric(
                "Average Daily Smartphone Usage",
                f"{average_hours:.2f} hours"
            )

    # --------------------------------------------------------
    # TRAINING ANALYSIS
    # --------------------------------------------------------

    if not training_df.empty:

        st.subheader("Training Activity")

        if "topic" in training_df.columns:

            training_counts = (
                training_df["topic"]
                .value_counts()
                .reset_index()
            )

            training_counts.columns = [
                "Topic",
                "Sessions"
            ]

            fig = px.bar(
                training_counts,
                x="Topic",
                y="Sessions",
                title="Training Sessions by Topic"
            )

            fig.update_layout(
                template="simple_white",
                height=400
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    # --------------------------------------------------------
    # EXPORT DATA
    # --------------------------------------------------------

    st.subheader("Data Export")

    export_option = st.selectbox(
        "Select Dataset",
        [
            "Participants",
            "Smartphone Usage",
            "Safety Events",
            "Training Sessions"
        ]
    )

    export_mapping = {
        "Participants": participants_df,
        "Smartphone Usage": usage_df,
        "Safety Events": events_df,
        "Training Sessions": training_df
    }

    selected_df = export_mapping[export_option]

    if not selected_df.empty:

        csv_data = selected_df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "Download CSV Report",
            data=csv_data,
            file_name=(
                export_option.lower()
                .replace(" ", "_")
                + "_report.csv"
            ),
            mime="text/csv"
        )

    else:

        st.info(
            "No data available for export."
        )
```

