import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon=":house:",
)

st.markdown("""
<style>
    .st-emotion-cache-1rtdyuf {
        color: #FFFFFF;
    }

    .st-emotion-cache-1egp75f {
        color: #FFFFFF;
    }

    .st-emotion-cache-1rtdyuf {
        color: #FFFFFF;
    }
</style>
""", unsafe_allow_html=True)

st.image('casa_museo.png')

st.write("# Bienvenido al chat de La Casa Museo El Santuario! 👋")

st.markdown(
    """
    Aquí podrás encontrar un chat donde podrás preguntar sobre La Casa Museo El Santuario o sobre la 
    historia del municipio El Santuario.\n
    **👈 Selección a tu izquierda la opción que más se acerque a tu tipo de pregunta** 
    ### Quieres saber más sobre la Casa Museo?
    - Visita nuestra página web [Casa Museo El Santuario](https://fundacionaurum.com.co/casa-museo/)
    - Envíanos un correo eléctronico a: gerencia@fundacionaurum.com.co
"""
)