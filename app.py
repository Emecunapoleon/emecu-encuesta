import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import date

# Configuración de la interfaz
st.set_page_config(page_title="Registro EMECU Táchira", page_icon="📝")

# --- CABECERA CENTRADA ---
col_logo_1, col_logo_2, col_logo_3 = st.columns([1, 1, 1])
with col_logo_2:
    st.image("https://i.postimg.cc/NfBWMzGC/Gran14-Napoleon-blanco.png", use_container_width=True)

st.markdown("<h1 style='text-align: center;'>📝 Censo de Integrantes EMECU</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Escuela Magnética Espiritual de la Comuna Universal</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: bold;'>abril 2026</p>", unsafe_allow_html=True)

# Definición de opciones
ciudades = ["Rubio", "San Cristóbal", "Táriba"]
parroquias = ["Pedro María Morantes", "Rubio", "San Juan Bautista", "Táriba"]
municipios = ["Cárdenas", "Junín", "San Cristóbal"]
catedras = ["Beatriz Portinari", "Luz y Verdad", "Napoleón Bonaparte", "Provincial Luz Occidente"]

# Conexión con Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

with st.form(key="form_censo"):
    col1, col2 = st.columns(2)
    with col1:
        p_nombre = st.text_input("Primer Nombre*")
        p_apellido = st.text_input("Primer Apellido*")
        fecha_nac = st.date_input("Fecha de Nacimiento*", min_value=date(1920, 1, 1), format="DD/MM/YYYY")
        celular = st.text_input("Celular*")
        ciudad = st.selectbox("Ciudad*", ciudades)
        municipio = st.selectbox("Municipio*", municipios)
    with col2:
        s_nombre = st.text_input("Segundo Nombre")
        s_apellido = st.text_input("Segundo Apellido")
        cedula = st.text_input("Cédula de Identidad*")
        direccion = st.text_input("Dirección de Casa*")
        parroquia = st.selectbox("Parroquia*", parroquias)
        catedra = st.selectbox("Cátedra*", catedras)

    profesiones = st.text_area("Profesiones Estudiadas*")
    oficios = st.text_area("Trabajos y Oficios Conocidos*")
    
    submit_button = st.form_submit_button(label="Registrar Información")

    if submit_button:
        if not p_nombre or not p_apellido or not cedula:
            st.error("Por favor, rellene los campos obligatorios (*)")
        else:
            fecha_formateada = fecha_nac.strftime("%d/%m/%Y")
            
            # Asegúrate de que estos nombres sean IDÉNTICOS a tu Fila 1 en la hoja
            nuevo_registro = {
                "Primer_Nombre": p_nombre,
                "Segundo_Nombre": s_nombre,
                "Primer_Apellido": p_apellido,
                "Segundo_Apellido": s_apellido,
                "Fecha_Nacimiento": fecha_formateada,
                "Cédula_Identidad": cedula,    # <--- Agregada tilde conforme a tu hoja 
                "Dirección_Casa": direccion,   # <--- Agregada tilde conforme a tu hoja 
                "Celular": celular,
                "Profesiones_Estudiadas": profesiones,
                "Oficios_Conocidos": oficios,
                "Ciudad": ciudad,
                "Parroquia": parroquia,
                "Municipio": municipio,
                "Cátedra": catedra             # <--- Agregada tilde conforme a tu hoja 
            }

            try:
                # 2. Leer datos actuales
                df_actual = conn.read()
                
                # 3. Añadir la nueva fila al DataFrame
                df_nuevo = pd.concat([df_actual, pd.DataFrame([nuevo_registro])], ignore_index=True)
                
                # 4. Intentar actualizar (Asegúrate que en Secrets la URL termine en /edit)
                conn.update(data=df_nuevo)
                
                st.success(f"✅ ¡Registro de {p_nombre} guardado exitosamente!")
                st.balloons()
            except Exception as e:
                st.error("No se pudo guardar. Intenta refrescar la página.")
                # Esto nos dirá el error exacto en la consola de Streamlit si falla
                print(f"DEBUG ERROR: {e}")
