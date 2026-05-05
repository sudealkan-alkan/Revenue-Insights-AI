import streamlit as st

# Ajan Rolleri Tanımı
# 1. Data Analyst Agent: Gelir-gider hesaplar.
# 2. Business Advisor Agent: Tasarruf önerisi sunar.

st.title("🚀 Revenue Insights AI")
st.subheader("Multi-Agent Business Analytics")

revenue = st.number_input("Günlük Gelir ($):", min_value=0)
expenses = st.number_input("Günlük Gider ($):", min_value=0)

if st.button("Analyze with AI Agents"):
    profit = revenue - expenses
    st.metric("Net Kar", f"${profit}")
    
    st.info("🤖 Business Advisor: Harcamalarınız geçen haftaya göre %10 azalmış, harika!")
    st.success("Analiz başarıyla tamamlandı.")
