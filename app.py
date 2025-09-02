import streamlit as st
from datetime import datetime, timedelta
import random

st.title("📦 Calculadora de Tempo Estimado de Entrega")

st.write("Simulação baseada no fluxo logístico da China até o cliente no Brasil.")

# Entrada da data da compra
data_compra = st.date_input("🛒 Data da compra na China")

if st.button("Calcular previsão"):
    if data_compra:
        # Etapas logísticas (com variação aleatória dentro do intervalo)
        tempo_fornecedor_armazem = random.randint(2, 4)  # 2 a 4 dias úteis
        tempo_processamento = 1  # fixo
        tempo_envio = random.randint(7, 10)  # transporte internacional
        tempo_alfandega = random.randint(10, 15)  # liberação aduaneira
        tempo_entrega_final = random.randint(3, 7)  # Correios/transportadora

        # Cálculo total
        dias_totais = (tempo_fornecedor_armazem + tempo_processamento +
                       tempo_envio + tempo_alfandega + tempo_entrega_final)

        data_prevista = data_compra + timedelta(days=dias_totais)

        # Mostrar resultados
        st.subheader("📊 Estimativa por etapas")
        st.write(f"🏭 Fornecedor → Armazém (China): **{tempo_fornecedor_armazem} dias**")
        st.write(f"📦 Processamento no armazém: **{tempo_processamento} dia**")
        st.write(f"✈️ Transporte China → Brasil: **{tempo_envio} dias**")
        st.write(f"🛃 Alfândega Brasil: **{tempo_alfandega} dias**")
        st.write(f"🚚 Entrega final ao cliente: **{tempo_entrega_final} dias**")

        st.success(f"⏳ Tempo total estimado: **{dias_totais} dias**")
        st.info(f"📅 Previsão de entrega: **{data_prevista.strftime('%d/%m/%Y')}**")
