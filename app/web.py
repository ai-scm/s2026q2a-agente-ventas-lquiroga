import streamlit as st

from app.graph import run_agent

st.set_page_config(
    page_title="Agente de Ventas",
    layout="wide"
)

st.title("📊 Agente Inteligente de Ventas")

# memoria conversación
if "messages" not in st.session_state:
    st.session_state.messages = []

# mostrar historial
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        if msg["role"] == "user":
            st.write(msg["content"])

        else:

            if msg["content"]["dataframe"] is not None:

                st.dataframe(
                    msg["content"]["dataframe"]
                )

            if msg["content"]["chart"]:

                st.plotly_chart(
                    msg["content"]["chart"]
                )

            if msg["content"]["csv"]:

                with open(
                    msg["content"]["csv"],
                    "rb"
                ) as file:

                    st.download_button(
                        label="Descargar CSV",
                        data=file,
                        file_name=msg["content"]["csv"],
                        mime="text/csv"
                    )

# input chat
prompt = st.chat_input(
    "Pregunta sobre ventas..."
)

if prompt:

    # guardar usuario
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    # ejecutar agente
    result = run_agent(
        prompt,
        st.session_state.messages
    )

    # guardar respuesta
    st.session_state.messages.append({
        "role": "assistant",
        "content": result
    })

    # mostrar respuesta
    with st.chat_message("assistant"):

        if result["dataframe"] is not None:

            st.dataframe(result["dataframe"])

        if result["chart"]:

            st.plotly_chart(result["chart"])

        if result["csv"]:

            with open(result["csv"], "rb") as file:

                st.download_button(
                    label="Descargar CSV",
                    data=file,
                    file_name=result["csv"],
                    mime="text/csv"
                )
