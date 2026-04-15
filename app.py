import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import date

# Configuración de la interfaz
st.set_page_config(page_title="Registro EMECU Táchira", page_icon="📝")

st.title("📝 Censo de Integrantes de la EMECU Táchira")
st.markdown("### Escuela Magnética Espiritual de la Comuna Universal")
st.info("Por favor, introduzca sus datos con precisión para el registro oficial.")

# Definición de opciones para las listas desplegables
ciudades = ["Rubio", "San Cristóbal", "Táriba"]
parroquias = ["Pedro María Morantes", "Rubio", "San Juan Bautista", "Táriba"]
municipios = ["Cárdenas", "Junín", "San Cristóbal"]
catedras = [
    "Beatriz Portinari", 
    "Luz y Verdad", 
    "Napoleón Bonaparte", 
    "Provincial Luz Occidente"
]

# Conexión con Google Sheets (Configurada en secrets de Streamlit Cloud)
conn = st.connection("gsheets", type=GSheetsConnection)

# Formulario de entrada de datos
with st.form(key="form_censo"):
    col1, col2 = st.columns(2)
    
    with col1:
        p_nombre = st.text_input("Primer Nombre*")
        p_apellido = st.text_input("Primer Apellido*")
        fecha_nac = st.date_input("Fecha de Nacimiento", min_value=date(1920, 1, 1))
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
        # Validación básica de campos obligatorios
        if not p_nombre or not p_apellido or not cedula:
            st.error("Por favor, rellene los campos obligatorios (*)")
        else:
            # Crear el DataFrame con la estructura exacta
            nuevo_integrante = pd.DataFrame([{
                "Primer_Nombre": p_nombre,
                "Segundo_Nombre": s_nombre,
                "Primer_Apellido": p_apellido,
                "Segundo_Apellido": s_apellido,
                "Fecha_Nacimiento": str(fecha_nac),
                "Cédula_Identidad": cedula,
                "Dirección_Casa": direccion,
                "Celular": celular,
                "Profesiones_Estudiadas": profesiones,
                "Oficios_Conocidos": oficios,
                "Ciudad": ciudad,
                "Parroquia": parroquia,
                "Municipio": municipio,
                "Cátedra": catedra
            }])

            # Lógica de guardado: Lee los existentes y concatena
            try:
                data_existente = conn.read()
                updated_df = pd.concat([data_existente, nuevo_integrante], ignore_index=True)
                conn.update(data=updated_df)
                st.success("✅ ¡Registro exitoso! Ya puede cerrar esta ventana.")
                st.balloons()
            except Exception as e:
                st.error("Error al conectar con la base de datos. Verifique los permisos de la hoja.")
