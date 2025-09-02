import streamlit as st
from datetime import datetime

st.title("📦 Calculadora de Tempo de Entrega")

st.write("Preencha as datas para calcular o tempo de envio da China até o cliente.")

# Entradas de datas
data_compra = st.date_input("🛒 Data da compra na China")
data_chegada_brasil = st.date_input("🇧🇷 Data da chegada no Brasil")
data_entrega = st.date_input("🏠 Data da entrega ao cliente")

if st.button("Calcular"):
    if data_compra and data_chegada_brasil and data_entrega:
        # Calcular diferenças
        tempo_china_brasil = (data_chegada_brasil - data_compra).days
        tempo_brasil_cliente = (data_entrega - data_chegada_brasil).days
        tempo_total = (data_entrega - data_compra).days

        # Mostrar resultado
        st.success(f"📦 Da China até o Brasil: **{tempo_china_brasil} dias**")
        st.success(f"🚚 Do Brasil até o cliente: **{tempo_brasil_cliente} dias**")
        st.info(f"⏳ Tempo total: **{tempo_total} dias**")
    else:
        st.warning("Por favor, preencha todas as datas.")
