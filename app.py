import streamlit as st

st.set_page_config(
    page_title="Smartphone Usage & Online Safety",
    page_icon="📱",
    layout="wide"
)

st.title("Smartphone Usage and Online Safety")
st.subheader("For Women Self Help Groups")

menu = st.sidebar.selectbox(
    "Select Topic",
    [
        "Home",
        "Basic Smartphone Usage",
        "Internet & Apps",
        "WhatsApp & Social Media",
        "Digital Payments",
        "Online Safety",
        "Women Safety",
        "Emergency Help"
    ]
)

if menu == "Home":
    st.header("Welcome")
    st.write("""
    This website provides simple information to help women use smartphones
    confidently and safely. Learn basic smartphone functions, internet usage,
    digital payments and online safety practices.
    """)

elif menu == "Basic Smartphone Usage":
    st.header("Basic Smartphone Usage")

    st.write("### 1. Switch On and Off")
    st.write("Press and hold the power button to switch the phone on or off.")

    st.write("### 2. Make a Phone Call")
    st.write("Open the Phone app, enter a number or select a saved contact, and tap the Call button.")

    st.write("### 3. Save a Contact")
    st.write("Open Contacts → Add Contact → Enter name and phone number → Save.")

    st.write("### 4. Send a Message")
    st.write("Open the Messages app → New Message → Select contact → Type message → Send.")

    st.write("### 5. Take a Photo")
    st.write("Open the Camera app and tap the capture button to take a photo.")

    st.write("### 6. Connect to Wi-Fi")
    st.write("Go to Settings → Wi-Fi → Select your network → Enter the password.")

    st.write("### 7. Use Mobile Data")
    st.write("Open Settings or Quick Settings and turn Mobile Data on when internet access is needed.")

    st.write("### 8. Install Apps")
    st.write("Download applications only from trusted app stores such as Google Play Store.")

    st.write("### 9. Update Phone and Apps")
    st.write("Keep the operating system and applications updated for better security and performance.")

    st.write("### 10. Screen Lock")
    st.write("Use a PIN, password, pattern or biometric lock to protect your smartphone.")

elif menu == "Internet & Apps":
    st.header("Internet and Apps")

    st.write("""
    • Use Google Search to find useful information.
    
    • Download apps only from trusted sources.
    
    • Check app permissions before allowing access to camera, microphone,
      contacts or location.
    
    • Avoid downloading unknown APK files or applications from suspicious websites.
    
    • Keep important apps updated.
    
    • Log out from accounts when using a shared device.
    """)

elif menu == "WhatsApp & Social Media":
    st.header("WhatsApp and Social Media Safety")

    st.write("""
    • Do not accept requests from unknown people.
    
    • Do not share personal information publicly.
    
    • Avoid sharing live location with strangers.
    
    • Check privacy settings regularly.
    
    • Do not click suspicious links sent through messages.
    
    • Block and report accounts that harass or threaten you.
    
    • Do not share private photos or documents with unknown people.
    """)

elif menu == "Digital Payments":
    st.header("UPI and Digital Payment Safety")

    st.write("""
    • Never share your UPI PIN, ATM PIN, OTP or password.
    
    • A UPI PIN is required to SEND money, not to RECEIVE money.
    
    • Do not scan an unknown QR code for receiving money.
    
    • Verify the receiver's name before making a payment.
    
    • Do not trust fake payment screenshots.
    
    • Never give remote access to your phone to an unknown person.
    
    • Check your bank SMS and transaction history regularly.
    """)

elif menu == "Online Safety":
    st.header("Online Safety")

    st.write("""
    ### Protect Your Account
    • Use a strong and unique password.
    
    • Enable two-factor authentication.
    
    • Never share OTPs or passwords.
    
    ### Avoid Online Fraud
    • Do not click unknown links.
    
    • Be careful of fake job offers, lottery messages and investment scams.
    
    • Never provide bank details to unknown callers.
    
    ### Protect Privacy
    • Keep social media accounts private when possible.
    
    • Avoid sharing Aadhaar, PAN, bank details and other personal documents online.
    """)

elif menu == "Women Safety":
    st.header("Women Online Safety")

    st.write("""
    Women should be especially careful about online harassment, fake profiles,
    cyberstalking and misuse of personal photographs.

    ### If Someone Harasses You Online:
    1. Do not respond to threats.
    2. Take screenshots and save evidence.
    3. Block the person.
    4. Report the account on the platform.
    5. Report serious cybercrime to the appropriate authorities.

    Never share private information, passwords, OTPs or personal photographs
    with strangers.
    """)

elif menu == "Emergency Help":
    st.header("Emergency and Cybercrime Help")

    st.write("""
    **Cybercrime Reporting:** 1930

    **National Cyber Crime Reporting Portal:** 
    https://www.cybercrime.gov.in/

    For financial cyber fraud, contact your bank immediately and report the
    incident as soon as possible.

    Keep screenshots, transaction details, phone numbers and messages as
    evidence when reporting a cybercrime.
    """)
