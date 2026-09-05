import streamlit as st
from supabase import create_client, Client
import pandas as pd
import plotly.express as px
from datetime import datetime

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Digital Saheli",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# SUPABASE CONFIG
# ============================================================

SUPABASE_URL = "PASTE_YOUR_SUPABASE_URL_HERE"
SUPABASE_KEY = "PASTE_YOUR_SUPABASE_ANON_KEY_HERE"

supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #fff8fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.hero {
    padding: 35px;
    border-radius: 25px;
    background: linear-gradient(135deg, #ffe1ec, #f4e3ff);
    margin-bottom: 25px;
}

.hero h1 {
    color: #8b2252;
    font-size: 42px;
    margin-bottom: 5px;
}

.hero p {
    color: #5f4b55;
    font-size: 18px;
}

.card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

.card h3 {
    color: #8b2252;
}

.stat {
    background: white;
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.08);
}

.stat-number {
    font-size: 32px;
    font-weight: bold;
    color: #8b2252;
}

.stat-label {
    color: #777;
}

.stButton > button {
    border-radius: 12px;
    border: none;
    font-weight: 600;
    padding: 10px 20px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_women():
    try:
        response = supabase.table("women").select("*").execute()
        return response.data or []
    except Exception as e:
        st.error(f"Database error: {e}")
        return []


def get_quiz_results():
    try:
        response = supabase.table("quiz_results").select("*").execute()
        return response.data or []
    except Exception:
        return []


def get_learning_progress():
    try:
        response = supabase.table("learning_progress").select("*").execute()
        return response.data or []
    except Exception:
        return []


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown("## 🌸 Digital Saheli")
st.sidebar.caption("Women Smart & Safe")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "👩 Register Woman",
        "👥 Women Records",
        "📱 Smartphone Learning",
        "🛡️ Online Safety",
        "🧠 Safety Quiz",
        "📊 Dashboard",
        "🆘 Emergency Help"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "Learn • Practice • Stay Safe"
)


# ============================================================
# HOME
# ============================================================

if page == "🏠 Home":

    st.markdown("""
    <div class="hero">
        <h1>🌸 Digital Saheli</h1>
        <p>
        Smartphone Usage & Online Safety Platform for Women
        </p>
        <p>
        Learn digital skills, understand online safety and become
        confident in using technology.
        </p>
    </div>
    """, unsafe_allow_html=True)

    women = get_women()
    quiz_results = get_quiz_results()
    progress = get_learning_progress()

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class="stat">
            <div class="stat-number">{len(women)}</div>
            <div class="stat-label">Women Registered</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="stat">
            <div class="stat-number">{len(quiz_results)}</div>
            <div class="stat-label">Quiz Attempts</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="stat">
            <div class="stat-number">{len(progress)}</div>
            <div class="stat-label">Learning Activities</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        if quiz_results:
            scores = [
                x.get("score", 0)
                for x in quiz_results
                if x.get("score") is not None
            ]

            avg = round(sum(scores) / len(scores), 1) if scores else 0
        else:
            avg = 0

        st.markdown(f"""
        <div class="stat">
            <div class="stat-number">{avg}</div>
            <div class="stat-label">Average Score</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## ✨ What can you learn?")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>📱 Smartphone Skills</h3>
        <p>Learn calling, WhatsApp, Google, email, maps and digital payments.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>🛡️ Online Safety</h3>
        <p>Learn about OTP scams, fake links, passwords, privacy and fraud.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>🧠 Interactive Quiz</h3>
        <p>Test your knowledge and save your score in the database.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## 🌷 Why Digital Saheli?")

    st.write(
        "Digital Saheli helps women understand smartphones and "
        "use digital services safely and confidently."
    )


# ============================================================
# REGISTER WOMAN
# ============================================================

elif page == "👩 Register Woman":

    st.title("👩 Register a Woman")

    st.write(
        "Enter basic information to create a participant record."
    )

    with st.form("registration_form"):

        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Full Name *")

            age_group = st.selectbox(
                "Age Group",
                [
                    "18-25",
                    "26-35",
                    "36-45",
                    "46-55",
                    "56+"
                ]
            )

            area = st.text_input("Area / Village")

            occupation = st.selectbox(
                "Occupation",
                [
                    "Homemaker",
                    "Student",
                    "Self Employed",
                    "Farmer",
                    "Employee",
                    "Other"
                ]
            )

        with col2:

            smartphone = st.radio(
                "Uses Smartphone?",
                ["Yes", "No"]
            )

            whatsapp = st.radio(
                "Uses WhatsApp?",
                ["Yes", "No"]
            )

            upi = st.radio(
                "Uses UPI / Digital Payments?",
                ["Yes", "No"]
            )

        submitted = st.form_submit_button(
            "🌸 Register Woman"
        )

        if submitted:

            if not name.strip():
                st.warning("Please enter the woman's name.")
            else:

                data = {
                    "name": name.strip(),
                    "age_group": age_group,
                    "area": area.strip(),
                    "occupation": occupation,
                    "smartphone_user": smartphone,
                    "whatsapp_user": whatsapp,
                    "upi_user": upi,
                    "created_at": datetime.now().isoformat()
                }

                try:

                    supabase.table("women").insert(data).execute()

                    st.success(
                        f"✅ {name} has been registered successfully!"
                    )

                    st.balloons()

                except Exception as e:
                    st.error(f"Unable to save data: {e}")


# ============================================================
# WOMEN RECORDS
# ============================================================

elif page == "👥 Women Records":

    st.title("👥 Registered Women")

    women = get_women()

    if women:

        df = pd.DataFrame(women)

        search = st.text_input(
            "🔎 Search by name"
        )

        if search:
            df = df[
                df["name"]
                .astype(str)
                .str.contains(
                    search,
                    case=False,
                    na=False
                )
            ]

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.success(
            f"{len(df)} record(s) found."
        )

    else:
        st.info(
            "No women registered yet."
        )


# ============================================================
# SMARTPHONE LEARNING
# ============================================================

elif page == "📱 Smartphone Learning":

    st.title("📱 Smartphone Learning Hub")

    topics = {
        "📞 Calling & Contacts":
            "Save important contacts, make calls and block unwanted numbers.",

        "💬 WhatsApp":
            "Send messages, photos and documents. Never share OTPs or sensitive information.",

        "🌐 Google Search":
            "Use Google to search for information, government services and educational resources.",

        "📧 Email":
            "Learn how to send emails and identify suspicious messages.",

        "📍 Google Maps":
            "Search locations, get directions and share your location only when necessary.",

        "💳 Digital Payments":
            "Learn basic UPI safety. Never share your UPI PIN or OTP.",

        "📲 Installing Apps":
            "Download apps only from trusted official app stores and check permissions."
    }

    for topic, description in topics.items():

        with st.expander(topic):

            st.write(description)

            if st.button(
                f"✅ Mark '{topic}' as Completed",
                key=topic
            ):

                st.session_state[
                    "completed_" + topic
                ] = True

                st.success(
                    "Learning activity completed!"
                )


# ============================================================
# ONLINE SAFETY
# ============================================================

elif page == "🛡️ Online Safety":

    st.title("🛡️ Online Safety Center")

    safety_topics = [

        (
            "🔐 Strong Password",
            "Use a long and unique password. Avoid using your name, birthday or phone number."
        ),

        (
            "🚨 OTP Scam",
            "Never share OTP with anyone. Banks and legitimate services do not ask you to reveal OTP."
        ),

        (
            "🎣 Phishing",
            "Do not blindly click links received through unknown SMS, email or social media."
        ),

        (
            "💳 UPI Fraud",
            "You do not need to enter your UPI PIN to receive money."
        ),

        (
            "📱 Fake Apps",
            "Install applications only from trusted app stores and check the developer."
        ),

        (
            "👤 Social Media Privacy",
            "Review privacy settings and avoid publicly sharing personal information."
        ),

        (
            "📍 Location Privacy",
            "Avoid sharing your live location with unknown people."
        ),

        (
            "📞 Cyber Harassment",
            "Block, report and preserve evidence when facing online harassment."
        )
    ]

    for title, description in safety_topics:

        st.markdown(
            f"""
            <div class="card">
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# SAFETY QUIZ
# ============================================================

elif page == "🧠 Safety Quiz":

    st.title("🧠 Online Safety Quiz")

    st.write(
        "Test your knowledge about smartphone and online safety."
    )

    # Participant selection
    women = get_women()

    if not women:

        st.warning(
            "Please register at least one woman before taking the quiz."
        )

    else:

        woman_names = {
            item["name"]: item["id"]
            for item in women
        }

        selected_name = st.selectbox(
            "Select Participant",
            list(woman_names.keys())
        )

        questions = [

            {
                "question":
                "Someone asks you for your OTP. What should you do?",

                "options":
                [
                    "Share it",
                    "Ignore and report",
                    "Send a screenshot",
                    "Post it online"
                ],

                "answer":
                "Ignore and report"
            },

            {
                "question":
                "Which information should never be shared with strangers?",

                "options":
                [
                    "OTP and UPI PIN",
                    "Weather",
                    "Public news",
                    "Movie name"
                ],

                "answer":
                "OTP and UPI PIN"
            },

            {
                "question":
                "You receive a suspicious link. What should you do?",

                "options":
                [
                    "Click immediately",
                    "Forward it",
                    "Avoid clicking and verify",
                    "Enter your password"
                ],

                "answer":
                "Avoid clicking and verify"
            },

            {
                "question":
                "What should you use for account protection?",

                "options":
                [
                    "Weak password",
                    "Same password everywhere",
                    "Strong unique password",
                    "Your name"
                ],

                "answer":
                "Strong unique password"
            },

            {
                "question":
                "What is important when installing an app?",

                "options":
                [
                    "Install from unknown links",
                    "Check trusted source and permissions",
                    "Give every permission",
                    "Ignore the developer"
                ],

                "answer":
                "Check trusted source and permissions"
            }
        ]

        answers = {}

        for i, q in enumerate(questions):

            st.markdown(
                f"### Q{i+1}. {q['question']}"
            )

            answers[i] = st.radio(
                "Choose an answer",
                q["options"],
                key=f"question_{i}"
            )

        if st.button("🎯 Submit Quiz"):

            score = 0

            for i, q in enumerate(questions):

                if answers[i] == q["answer"]:
                    score += 1

            total = len(questions)

            try:

                quiz_data = {
                    "woman_id": woman_names[selected_name],
                    "score": score,
                    "total_questions": total,
                    "completed_at":
                        datetime.now().isoformat()
                }

                supabase.table(
                    "quiz_results"
                ).insert(
                    quiz_data
                ).execute()

                percentage = round(
                    (score / total) * 100
                )

                st.success(
                    f"🎉 {selected_name}, your score is "
                    f"{score}/{total} ({percentage}%)"
                )

                if percentage >= 80:
                    st.balloons()
                    st.info(
                        "🏆 Excellent! You are safety aware."
                    )

                elif percentage >= 60:
                    st.info(
                        "👍 Good job! Keep learning."
                    )

                else:
                    st.warning(
                        "📚 Keep practicing the safety topics."
                    )

            except Exception as e:

                st.error(
                    f"Could not save quiz result: {e}"
                )


# ============================================================
# DASHBOARD
# ============================================================

elif page == "📊 Dashboard":

    st.title("📊 Women Safety Dashboard")

    women = get_women()
    results = get_quiz_results()

    if not women:

        st.info(
            "Register women to generate dashboard statistics."
        )

    else:

        df = pd.DataFrame(women)

        st.subheader("👩 Participant Overview")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Total Women",
                len(df)
            )

        with c2:

            smartphone_count = (
                df["smartphone_user"]
                .eq("Yes")
                .sum()
                if "smartphone_user" in df.columns
                else 0
            )

            st.metric(
                "Smartphone Users",
                smartphone_count
            )

        with c3:

            upi_count = (
                df["upi_user"]
                .eq("Yes")
                .sum()
                if "upi_user" in df.columns
                else 0
            )

            st.metric(
                "UPI Users",
                upi_count
            )

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:

            if "age_group" in df.columns:

                age_data = (
                    df["age_group"]
                    .value_counts()
                    .reset_index()
                )

                age_data.columns = [
                    "Age Group",
                    "Count"
                ]

                fig = px.bar(
                    age_data,
                    x="Age Group",
                    y="Count",
                    title="Women by Age Group"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

        with col2:

            if "smartphone_user" in df.columns:

                phone_data = (
                    df["smartphone_user"]
                    .value_counts()
                    .reset_index()
                )

                phone_data.columns = [
                    "Smartphone User",
                    "Count"
                ]

                fig = px.pie(
                    phone_data,
                    names="Smartphone User",
                    values="Count",
                    title="Smartphone Usage"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

        if results:

            result_df = pd.DataFrame(results)

            st.subheader("🧠 Quiz Performance")

            if "score" in result_df.columns:

                st.metric(
                    "Total Quiz Attempts",
                    len(result_df)
                )

                st.dataframe(
                    result_df,
                    use_container_width=True,
                    hide_index=True
                )


# ============================================================
# EMERGENCY HELP
# ============================================================

elif page == "🆘 Emergency Help":

    st.title("🆘 Emergency & Safety Help")

    st.warning(
        "If you are in immediate danger, contact local emergency services."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card">
        <h3>🚨 Emergency</h3>
        <p>Use your country's official emergency service for immediate danger.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
        <h3>👮 Police</h3>
        <p>Contact your local police service when immediate assistance is required.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card">
        <h3>💻 Cyber Fraud</h3>
        <p>For online financial fraud in India, report it immediately through the official cybercrime reporting system.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
        <h3>👩 Women Support</h3>
        <p>Contact appropriate local women-support services for help and guidance.</p>
        </div>
        """, unsafe_allow_html=True)

    st.info(
        "Never share OTP, UPI PIN, passwords or banking credentials with anyone."
    )
