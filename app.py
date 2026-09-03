# ============================================================
# QUIZ RESULT STORAGE
# ============================================================

st.subheader("🎯 Safety Quiz")

user_name = st.text_input(
    "Enter your name",
    placeholder="Enter your name before starting the quiz"
)

# Your existing quiz questions and answers remain here


if st.button("Submit Quiz", use_container_width=True):

    # Example:
    # score = your existing score calculation
    # total = len(questions)

    if not user_name.strip():
        st.warning("Please enter your name.")
    else:

        # SAVE RESULT TO SUPABASE
        try:
            supabase.table("quiz_results").insert({
                "user_name": user_name.strip(),
                "score": score,
                "total": total
            }).execute()

            st.success("✅ Quiz result saved successfully!")

        except Exception as e:
            st.error("❌ Could not save quiz result.")
            st.caption(str(e))

        # Existing result display
        st.write(f"### Your Score: {score}/{total}")

        if score == total:
            st.balloons()
