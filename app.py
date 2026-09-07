import streamlit as st
from supabase import create_client
from datetime import date

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Digital Saheli",
    page_icon="🌸",
    layout="wide"
)

# =========================================================
# SUPABASE CONNECTION
# =========================================================

SUPABASE_URL = "PASTE_YOUR_SUPABASE_URL_HERE"
SUPABASE_KEY = "PASTE_YOUR_SUPABASE_ANON_KEY_HERE"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #fff8fb;
}

.title {
    font-size: 42px;
    font-weight: 700;
    color: #8e2452;
}

.subtitle {
    font-size: 18px;
    color: #555;
}

.card {
    padding: 22px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0 3px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🌸 Digital Saheli")

page = st.sidebar.radio(
    "Menu",
    [
        "🏠 Home",
        "📱 Smartphone Safety",
        "🔐 Online Safety",
        "🚨 Report a Scam",
        "📊 Admin Dashboard"
    ]
)

# =========================================================
# HOME
# =========================================================

if page == "🏠 Home":

    st.markdown(
        '<div class="title">🌸 Digital Saheli</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Smartphone Usage & Online Safety for Women'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("📱 Smartphone Learning")
        st.write("Learn useful smartphone features and settings.")

    with col2:
        st.warning("🔐 Online Safety")
        st.write("Learn how to stay safe from online scams.")

    with col3:
        st.error("🚨 Scam Reporting")
        st.write("Record and review online scam incidents.")

# =========================================================
# SMARTPHONE SAFETY
# =========================================================

elif page == "📱 Smartphone Safety":

    st.title("📱 Smartphone Safety")

    st.markdown("""
    ### Basic Smartphone Skills

    - 📞 Save and manage contacts
    - 📸 Take screenshots
    - 📶 Use Wi-Fi and mobile data
    - 📍 Manage location settings
    - 📲 Install and uninstall applications
    - 🔒 Use screen lock
    - 🔄 Keep your phone updated
    """)

# =========================================================
# ONLINE SAFETY
# =========================================================

elif page == "🔐 Online Safety":

    st.title("🔐 Online Safety")

    st.markdown("""
    ### Important Safety Rules

    **🔑 Password**
    
    Use a strong and unique password.

    **🔢 OTP**
    
    Never share your OTP with anyone.

    **💳 UPI**
    
    Never enter your UPI PIN to receive money.

    **🔗 Unknown Links**
    
    Do not open suspicious links.

    **📱 Social Media**
    
    Keep your personal information private.

    **🚨 Suspicious Messages**
    
    Do not respond to unknown people asking for money or personal information.
    """)

# =========================================================
# REPORT A SCAM
# =========================================================

elif page == "🚨 Report a Scam":

    st.title("🚨 Report a Scam")

    st.warning(
        "This form records your report for the project. "
        "It does not replace an official cybercrime complaint."
    )

    with st.form("scam_form"):

        name = st.text_input("👩 Your Name")

        scam_type = st.selectbox(
            "🔴 Scam Type",
            [
                "UPI / Payment Scam",
                "OTP Scam",
                "WhatsApp Scam",
                "Fake Job Scam",
                "Online Shopping Scam",
                "Social Media Scam",
                "Phishing / Fake Link",
                "Other"
            ]
        )

        incident_date = st.date_input(
            "📅 Date of Incident",
            value=date.today()
        )

        amount = st.number_input(
            "💰 Amount Lost (₹)",
            min_value=0.0,
            step=100.0
        )

        description = st.text_area(
            "📝 What happened?"
        )

        submitted = st.form_submit_button(
            "🚨 Submit Scam Report"
        )

        if submitted:

            if name.strip() == "":
                st.error("Please enter your name.")

            elif description.strip() == "":
                st.error("Please describe what happened.")

            else:

                try:

                    data = {
                        "name": name,
                        "scam_type": scam_type,
                        "description": description,
                        "amount": amount,
                        "incident_date": str(incident_date),
                        "status": "Pending",
                        "admin_response": ""
                    }

                    supabase.table(
                        "scam_reports"
                    ).insert(data).execute()

                    st.success(
                        "✅ Your scam report has been submitted successfully."
                    )

                    st.info(
                        "For actual cyber fraud, please contact "
                        "1930 and report it through the official "
                        "National Cyber Crime Reporting Portal."
                    )

                except Exception as e:

                    st.error(
                        "Unable to submit the report."
                    )

                    st.code(str(e))

# =========================================================
# ADMIN DASHBOARD
# =========================================================

elif page == "📊 Admin Dashboard":

    st.title("📊 Admin Dashboard")

    st.caption(
        "View and review submitted scam reports."
    )

    try:

        response = (
            supabase
            .table("scam_reports")
            .select("*")
            .order("created_at", desc=True)
            .execute()
        )

        reports = response.data

        if not reports:

            st.info("No scam reports submitted yet.")

        else:

            st.metric(
                "Total Scam Reports",
                len(reports)
            )

            st.divider()

            for report in reports:

                with st.expander(
                    f"🚨 {report['name']} — {report['scam_type']}"
                ):

                    st.write(
                        "**Date:**",
                        report["incident_date"]
                    )

                    st.write(
                        "**Amount:** ₹",
                        report["amount"]
                    )

                    st.write(
                        "**Description:**"
                    )

                    st.write(
                        report["description"]
                    )

                    st.divider()

                    current_status = report["status"]

                    status_options = [
                        "Pending",
                        "Under Review",
                        "Guided",
                        "Closed"
                    ]

                    status_index = (
                        status_options.index(current_status)
                        if current_status in status_options
                        else 0
                    )

                    new_status = st.selectbox(
                        "📌 Status",
                        status_options,
                        index=status_index,
                        key=f"status_{report['id']}"
                    )

                    admin_response = st.text_area(
                        "✍️ Admin Guidance / Response",
                        value=report["admin_response"] or "",
                        key=f"response_{report['id']}"
                    )

                    if st.button(
                        "💾 Save Review",
                        key=f"save_{report['id']}"
                    ):

                        try:

                            supabase.table(
                                "scam_reports"
                            ).update({
                                "status": new_status,
                                "admin_response": admin_response
                            }).eq(
                                "id",
                                report["id"]
                            ).execute()

                            st.success(
                                "✅ Review saved successfully."
                            )

                            st.rerun()

                        except Exception as e:

                            st.error(
                                "Unable to update report."
                            )

                            st.code(str(e))

    except Exception as e:

        st.error(
            "Unable to load scam reports."
        )

        st.code(str(e))
