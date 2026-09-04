# ============================================================
# SAFETY RECORDS
# ============================================================

elif page == "📝 Safety Records":

    st.title("📝 Online Safety Records")

    st.write(
        "Record online safety concerns reported by participants."
    )

    st.divider()

    participants = get_table(
        "participants"
    )

    participants_df = pd.DataFrame(
        participants
    )

    if participants_df.empty:

        st.warning(
            "⚠️ Please add participants first."
        )

    else:

        tab1, tab2 = st.tabs([
            "➕ Record Safety Event",
            "📋 View Records"
        ])

        # ----------------------------------------------------
        # RECORD SAFETY EVENT
        # ----------------------------------------------------

        with tab1:

            participant_options = {
                f"{row['participant_id']} - {row['name']}":
                row["participant_id"]
                for _, row in participants_df.iterrows()
            }

            with st.form("safety_event_form"):

                participant = st.selectbox(
                    "👩 Participant",
                    list(participant_options.keys())
                )

                event_type = st.selectbox(
                    "⚠️ Safety Issue",
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
                    "📅 Date"
                )

                description = st.text_area(
                    "📝 What happened?",
                    placeholder="Enter a short description..."
                )

                action_taken = st.text_area(
                    "✅ Action Taken",
                    placeholder="Enter what action was taken..."
                )

                reported = st.selectbox(
                    "🚨 Reported?",
                    ["Yes", "No"]
                )

                submitted = st.form_submit_button(
                    "💾 Save Safety Record",
                    use_container_width=True
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
                            "✅ Safety record saved successfully!"
                        )

        # ----------------------------------------------------
        # VIEW RECORDS
        # ----------------------------------------------------

        with tab2:

            safety_events = get_table(
                "safety_events"
            )

            if not safety_events:

                st.info(
                    "No safety records have been recorded yet."
                )

            else:

                events_df = pd.DataFrame(
                    safety_events
                )

                st.dataframe(
                    events_df,
                    use_container_width=True,
                    hide_index=True
                )
