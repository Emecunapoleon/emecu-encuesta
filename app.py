import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import date

# Configuración de la interfaz
st.set_page_config(page_title="Registro EMECU Táchira", page_icon="📝")

st.title("📝 Censo de Integrantes EMECU")
st.markdown("### Escuela Magnética Espiritual de la Comuna Universal")
st.info("Por favor, introduzca sus datos con precisión para el registro oficial.")

# Definición de opciones
ciudades = ["Rubio", "San Cristóbal", "Táriba"]
parroquias = ["Pedro María Morantes", "Rubio", "San Juan Bautista", "Táriba"]
municipios = ["Cárdenas", "Junín", "San Cristóbal"]
catedras = [
    "Beatriz Portinari", 
    "Luz y Verdad", 
    "Napoleón Bonaparte", 
    "Provincial Luz Occidente"
]

conn = st.connection("gsheets", type=GSheetsConnection)

with st.form(key="form_censo"):
    col1, col2 = st.columns(2)
    
    with col1:
        p_nombre = st.text_input("Primer Nombre*")
        p_apellido = st.text_input("Primer Apellido*")
        # El widget sigue mostrando el calendario, pero capturamos el valor
        fecha_nac = st.date_input("Fecha de Nacimiento", min_value=date(1920, 1, 1), format="DD/MM/YYYY")
        celular = st.text_input("Celular (Ej: 0414-1234567)")
        ciudad = st.selectbox("Ciudad", ciudades)
        municipio = st.selectbox("Municipio", municipios)

    with col2:
        s_nombre = st.text_input("Segundo Nombre")
        s_apellido = st.text_input("Segundo Apellido")
        cedula = st.text_input("Cédula de Identidad*")
        direccion = st.text_input("Dirección de Casa")
        parroquia = st.selectbox("Parroquia", parroquias)
        catedra = st.selectbox("Cátedra", catedras)

    profesiones = st.text_area("Profesiones Estudiadas")
    oficios = st.text_area("Oficios Conocidos")
    
    submit_button = st.form_submit_button(label="Registrar Información")

    if submit_button:
        if not p_nombre or not p_apellido or not cedula:
            st.error("Por favor, rellene los campos obligatorios (*)")
        else:
            # CAMBIO CLAVE: Formateamos la fecha a DD/MM/AAAA antes de crear el DataFrame
            fecha_formateada = fecha_nac.strftime("%d/%m/%Y")
            
            nuevo_integrante = pd.DataFrame([{
                "Primer_Nombre": p_nombre,
                "Segundo_Nombre": s_nombre,
                "Primer_Apellido": p_apellido,
                "Segundo_Apellido": s_apellido,
                "Fecha_Nacimiento": fecha_formateada, # <--- Ahora es texto en formato DD/MM/AAAA
                "Cedula_Identidad": cedula,
                "Dirección_Casa": direccion,
                "Celular": celular,
                "Profesiones_Estudiadas": profesiones,
                "Oficios_Conocidos": oficios,
                "Ciudad": ciudad,
                "Parroquia": parroquia,
                "Municipio": municipio,
                "Cátedra": catedra
            }])

            try:
                data_existente = conn.read()
                updated_df = pd.concat([data_existente, nuevo_integrante], ignore_index=True)
                conn.update(data=updated_df)
                st.success(f"✅ ¡Registro de {p_nombre} exitoso!")
                st.balloons()
            except Exception as e:
                st.error("Error al guardar. Verifique la conexión con Google Sheets.")
