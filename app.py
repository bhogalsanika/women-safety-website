import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Smartphone Usage and Online Safety",
    layout="wide"
)

# ---------------- STYLE ----------------
st.markdown("""
<style>
.main {
    background-color: #f7f8fa;
}

h1, h2, h3 {
    color: #1f2937;
}

.info-card {
    background: white;
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #e1e5ea;
    margin-bottom: 15px;
}

.section-title {
    color: #1f4e79;
    font-size: 24px;
    font-weight: 600;
}

.tip {
    background-color: #eef4f8;
    padding: 15px;
    border-left: 4px solid #1f4e79;
    border-radius: 5px;
}
</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------
st.sidebar.title("Women Digital Safety")

page = st.sidebar.radio(
    "Select Section",
    [
        "Home",
        "Smartphone Usage Guide",
        "Online Safety Guide",
        "Digital Payments",
        "Emergency and Reporting"
    ]
)


# ==========================================================
# HOME
# ==========================================================

if page == "Home":

    st.title("Smartphone Usage and Online Safety")

    st.write(
        "A digital awareness platform designed to help women "
        "Self Help Groups use smartphones effectively and safely."
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Smartphone Skills")
        st.write(
            "Learn basic smartphone operations, applications, "
            "internet usage and communication."
        )

    with col2:
        st.subheader("Online Safety")
        st.write(
            "Understand passwords, privacy, phishing, scams, "
            "social media safety and safe browsing."
        )

    with col3:
        st.subheader("Digital Payments")
        st.write(
            "Learn safe practices while using UPI, mobile banking "
            "and other digital payment services."
        )

    st.markdown("---")

    st.subheader("Purpose of the Project")

    st.write(
        "The purpose of this project is to create awareness among "
        "women Self Help Groups about smartphone usage and online "
        "safety. The system provides simple and practical information "
        "that can help users use digital services confidently and safely."
    )


# ==========================================================
# SMARTPHONE USAGE GUIDE
# ==========================================================

elif page == "Smartphone Usage Guide":

    st.title("Smartphone Usage Guide")

    st.write(
        "Basic information for using smartphones effectively."
    )

    st.markdown("---")

    st.subheader("1. Basic Smartphone Operations")

    st.markdown("""
    - Turn the smartphone on and off correctly.
    - Use the touchscreen by tapping, swiping and scrolling.
    - Adjust volume and screen brightness.
    - Connect to Wi-Fi or mobile data.
    - Charge the phone using a suitable charger.
    - Keep the phone and operating system updated.
    """)

    st.subheader("2. Making and Receiving Calls")

    st.markdown("""
    - Open the Phone application.
    - Select a contact or enter a phone number.
    - Check the number before making important calls.
    - Avoid sharing sensitive information with unknown callers.
    - Block unwanted or suspicious numbers.
    """)

    st.subheader("3. Saving Contacts")

    st.markdown("""
    - Save important family and emergency contacts.
    - Use clear names for contacts.
    - Avoid saving unknown numbers as trusted contacts.
    - Review and remove unnecessary contacts regularly.
    """)

    st.subheader("4. Using WhatsApp and Messaging Apps")

    st.markdown("""
    - Send messages only to trusted people.
    - Check the identity of unknown contacts.
    - Do not forward unverified information.
    - Avoid opening suspicious links.
    - Do not share OTPs, passwords or banking details.
    - Use privacy settings to control who can see your profile information.
    """)

    st.subheader("5. Internet Browsing")

    st.markdown("""
    - Use trusted websites.
    - Check the website address before entering information.
    - Avoid downloading files from unknown websites.
    - Do not click suspicious advertisements or pop-ups.
    - Do not enter passwords on websites received through unknown links.
    """)

    st.subheader("6. Installing Mobile Applications")

    st.markdown("""
    - Download applications from official app stores.
    - Check the developer and reviews before installing an app.
    - Avoid downloading APK files from unknown websites.
    - Review the permissions requested by an application.
    - Remove applications that are no longer required.
    """)

    st.subheader("7. Smartphone Privacy")

    st.markdown("""
    - Use a screen lock such as PIN, password or biometric lock.
    - Keep your phone updated.
    - Review application permissions.
    - Turn off unnecessary location access.
    - Avoid giving unnecessary access to contacts, camera or microphone.
    - Do not leave your phone unlocked in public places.
    """)

    st.markdown(
        '<div class="tip"><b>Important:</b> Never share your '
        'phone password, OTP, UPI PIN or banking password with anyone.</div>',
        unsafe_allow_html=True
    )


# ==========================================================
# ONLINE SAFETY
# ==========================================================

elif page == "Online Safety Guide":

    st.title("Online Safety Guide")

    st.write(
        "Important safety practices for protecting personal information "
        "and avoiding online fraud."
    )

    st.markdown("---")

    st.subheader("Strong Passwords")

    st.markdown("""
    - Create a unique password for important accounts.
    - Avoid using names, birthdays or simple numbers.
    - Do not use the same password everywhere.
    - Never share passwords with other people.
    - Enable two-factor authentication whenever available.
    """)

    st.subheader("OTP Safety")

    st.markdown("""
    - OTP means One-Time Password.
    - Never share an OTP with anyone.
    - Banks and legitimate services do not require you to reveal your OTP.
    - Do not enter an OTP on an unknown website.
    """)

    st.subheader("Phishing and Suspicious Links")

    st.markdown("""
    Phishing is an attempt to trick users into providing personal,
    banking or login information.

    Warning signs include:

    - Unexpected messages asking for urgent action.
    - Unknown links.
    - Fake offers or prizes.
    - Messages asking for OTP or passwords.
    - Requests to install unknown applications.
    """)

    st.subheader("Social Media Safety")

    st.markdown("""
    - Keep personal information private.
    - Avoid publicly sharing your address or financial information.
    - Review account privacy settings.
    - Do not accept requests from unknown people without checking them.
    - Block and report suspicious accounts.
    - Think carefully before posting photographs or personal information.
    """)

    st.subheader("Online Shopping Safety")

    st.markdown("""
    - Use trusted shopping websites and applications.
    - Check the website address before making payments.
    - Avoid offers that appear unrealistic.
    - Do not share your banking PIN or OTP.
    - Keep payment confirmations and transaction records.
    """)

    st.subheader("Cyberbullying and Harassment")

    st.markdown("""
    If someone is threatening, harassing or repeatedly contacting you:

    1. Do not respond to the person.
    2. Save screenshots or other evidence.
    3. Block the account or number.
    4. Report the account on the platform.
    5. Inform a trusted person.
    6. Report serious incidents to the appropriate authorities.
    """)


# ==========================================================
# DIGITAL PAYMENTS
# ==========================================================

elif page == "Digital Payments":

    st.title("Digital Payment Safety")

    st.write(
        "Basic safety practices for UPI, mobile banking and digital payments."
    )

    st.markdown("---")

    st.subheader("Safe UPI Practices")

    st.markdown("""
    - Never share your UPI PIN.
    - A UPI PIN is required to authorize a payment.
    - You generally do not need to enter your UPI PIN to receive money.
    - Verify the recipient before approving a payment.
    - Check the amount before entering your UPI PIN.
    - Do not scan an unknown QR code without understanding the purpose.
    """)

    st.subheader("Banking Safety")

    st.markdown("""
    - Never share ATM PIN, UPI PIN, CVV, password or OTP.
    - Do not provide banking details to unknown callers.
    - Use official banking applications.
    - Keep banking applications updated.
    - Check transaction notifications regularly.
    - Contact your bank immediately if you notice an unauthorized transaction.
    """)

    st.markdown(
        '<div class="tip"><b>Remember:</b> Receiving money does not '
        'normally require you to enter your UPI PIN.</div>',
        unsafe_allow_html=True
    )


# ==========================================================
# EMERGENCY AND REPORTING
# ==========================================================

elif page == "Emergency and Reporting":

    st.title("Emergency and Reporting Information")

    st.write(
        "Steps to follow when facing an online safety problem."
    )

    st.markdown("---")

    st.subheader("If You Suspect Online Fraud")

    st.markdown("""
    1. Stop communicating with the suspected person.
    2. Do not provide additional information.
    3. Do not make further payments.
    4. Save transaction details and screenshots.
    5. Contact your bank or payment service.
    6. Report the incident through the appropriate official cybercrime channel.
    """)

    st.subheader("Evidence to Keep")

    st.markdown("""
    - Screenshots of messages.
    - Phone numbers.
    - Website or message links.
    - Transaction IDs.
    - Payment receipts.
    - Dates and times of communication.
    """)

    st.subheader("Important Safety Rule")

    st.markdown(
        '<div class="tip"><b>STOP — CHECK — REPORT</b><br><br>'
        'Stop before responding to suspicious requests.<br>'
        'Check the source and information carefully.<br>'
        'Report the incident when necessary.</div>',
        unsafe_allow_html=True
    )

    st.subheader("Official Cybercrime Reporting")

    st.write(
        "For cybercrime-related assistance in India, users can "
        "refer to the official National Cyber Crime Reporting Portal "
        "and Cyber Crime Helpline 1930."
    )


