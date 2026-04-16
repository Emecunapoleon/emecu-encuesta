import streamlit as st
import requests
from datetime import date

# Configuración de la interfaz
st.set_page_config(page_title="Registro EMECU Táchira", page_icon="📝")

# URL de tu Google Apps Script (El puente)
URL_SCRIPT = "https://script.google.com/macros/s/AKfycbzfy9A8zYClMi_pHmwOzza06GvyzoeAIWS7nAeGMwBu4xvtI9xWqwiu6KWFHo80wMjLtg/exec"

# --- CABECERA CENTRADA ---
col_logo_1, col_logo_2, col_logo_3 = st.columns([1, 1, 1])
with col_logo_2:
    st.image("https://i.postimg.cc/NfBWMzGC/Gran14-Napoleon-blanco.png", use_container_width=True)

st.markdown("<h1 style='text-align: center;'>📝 Censo de Integrantes EMECU</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Escuela Magnética Espiritual de la Comuna Universal</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: bold;'>abril 2026</p>", unsafe_allow_html=True)

# Formulario
with st.form(key="form_censo"):
    st.markdown("##### * Campos obligatorios")
    col1, col2 = st.columns(2)
    
    with col1:
        p_nombre = st.text_input("Primer Nombre*")
        s_nombre = st.text_input("Segundo Nombre (Opcional)")
        p_apellido = st.text_input("Primer Apellido*")
        s_apellido = st.text_input("Segundo Apellido (Opcional)")
        fecha_nac = st.date_input("Fecha de Nacimiento*", min_value=date(1920, 1, 1), format="DD/MM/YYYY")
        cedula = st.text_input("Cédula de Identidad*")

    with col2:
        celular = st.text_input("Celular*")
        direccion = st.text_input("Dirección de Casa*")
        ciudad = st.selectbox("Ciudad*", ["Rubio", "San Cristóbal", "Táriba"])
        municipio = st.selectbox("Municipio*", ["Cárdenas", "Junín", "San Cristóbal"])
        parroquia = st.selectbox("Parroquia*", ["Pedro María Morantes", "Rubio", "San Juan Bautista", "Táriba"])
        catedra = st.selectbox("Cátedra*", ["Beatriz Portinari", "Luz y Verdad", "Napoleón Bonaparte", "Provincial Luz Occidente"])

    profesiones = st.text_area("Profesiones Estudiadas*")
    oficios = st.text_area("Trabajos y Oficios Conocidos*")
    
    submit_button = st.form_submit_button(label="Registrar Información")

    if submit_button:
        # Lista de campos obligatorios para validación
        campos_obligatorios = {
            "Primer Nombre": p_nombre,
            "Primer Apellido": p_apellido,
            "Cédula": cedula,
            "Celular": celular,
            "Dirección": direccion,
            "Profesiones": profesiones,
            "Oficios": oficios
        }
        
        # Verificar si algún campo obligatorio está vacío
        faltantes = [label for label, valor in campos_obligatorios.items() if not valor.strip()]
        
        if faltantes:
            st.error(f"Faltan los siguientes campos obligatorios: {', '.join(faltantes)}")
        else:
            # Preparamos el paquete de datos
            payload = {
                "Primer_Nombre": p_nombre,
                "Segundo_Nombre": s_nombre,
                "Primer_Apellido": p_apellido,
                "Segundo_Apellido": s_apellido,
                "Fecha_Nacimiento": fecha_nac.strftime("%d/%m/%Y"),
                "Cedula_Identidad": cedula,
                "Direccion_Casa": direccion,
                "Celular": celular,
                "Profesiones_Estudiadas": profesiones,
                "Oficios_Conocidos": oficios,
                "Ciudad": ciudad,
                "Parroquia": parroquia,
                "Municipio": municipio,
                "Catedra": catedra
            }

            try:
                with st.spinner("Guardando información..."):
                    response = requests.post(URL_SCRIPT, json=payload)
                
                if response.status_code == 200:
                    st.success(f"✅ ¡Registro de {p_nombre} {p_apellido} guardado exitosamente!")
                    st.balloons()
                else:
                    st.error("Hubo un problema con el servidor de Google. Intente más tarde.")
            except Exception as e:
                st.error(f"Error de conexión: {e}")
