import streamlit as st
import requests
from datetime import date

# 1. Configuración de la interfaz y Tema
st.set_page_config(
    page_title="Censo Comuna de Amor y Ley - EMECU", 
    page_icon="📝",
    layout="centered"
)

# URL de tu Google Apps Script (El puente)
URL_SCRIPT = "https://script.google.com/macros/s/AKfycbzfy9A8zYClMi_pHmwOzza06GvyzoeAIWS7nAeGMwBu4xvtI9xWqwiu6KWFHo80wMjLtg/exec"

# --- ESTILOS PARA CORREGIR VISIBILIDAD ---
st.markdown("""
    <style>
    /* Forzar fondo oscuro para que el logo blanco siempre se vea */
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    /* Estilo para los títulos con colores claros */
    .titulo-guia {
        color: #E0E1DD !important;
        text-align: center;
        font-weight: bold;
    }
    .sub-emecu {
        color: #ffffff;
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
col_a, col_b, col_c = st.columns([1, 1, 1])
with col_b:
    # El logo blanco ahora resaltará sobre el fondo oscuro forzado
    st.image("https://i.postimg.cc/NfBWMzGC/Gran14-Napoleon-blanco.png", use_container_width=True)

st.markdown("<p class='sub-emecu'>Escuela Magnético Espiritual de la Comuna Universal (EMECU)</p>", unsafe_allow_html=True)

st.markdown("<h2 class='titulo-guia'>GUÍA DE INTRODUCCIÓN AL CENSO DE LA COMUNA</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; font-style: italic; color: #A9D6E5;'>\"Hacia la cristalización de la Comuna de Amor y Ley\"</h4>", unsafe_allow_html=True)

with st.expander("Leer Introducción y Principios del Censo", expanded=True):
    st.markdown("""
    **Estimado hermano, adherente y colaborador:**
    
    Nos encontramos en un momento histórico definido por el Maestro Joaquín Trincado como la transición hacia la Comuna de Amor y Ley. Como miembros de la Escuela Magnético-Espiritual de la Comuna Universal en el Estado Táchira, nuestra misión no es solo estudiar la doctrina en los libros, sino preparar el terreno material para su ejecución.
    
    El Maestro nos advirtió en el Código de Amor Universal que la Comuna es un régimen de justicia donde "todos producen para todos". Por ello, este censo no busca clasificar títulos ni posesiones con fines egoístas, sino organizar los Medios y las Aptitudes que el espíritu pone al servicio de la gran familia humana.
    
    **¿Por qué es necesaria esta Ficha Técnica?**
    1. **Reconocimiento de nuestra utilidad:** Necesitamos saber qué sabemos hacer y qué estamos dispuestos a aprender.
    2. **Soberanía ante la crisis:** Ante un posible escenario de cambio global hacia el 2030, la organización previa es la única garantía de paz.
    3. **Abolición del egoísmo:** Al declarar lo que tenemos, practicamos el despojo de la propiedad individual para abrazar la propiedad común de la sabiduría.
    
    **"El que no sabe, aprenda; el que sabe, enseñe; y el que no trabaja, no coma (siendo sano)." — Joaquín Trincado**
    """)

# --- FORMULARIO ---
with st.form(key="form_censo_comuna"):
    st.markdown("### I. DATOS PERSONALES Y SALUD")
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
        ciudad = st.selectbox("Ciudad*", ["Rubio", "San Cristóbal", "Táriba", "Otro"])
        parroquia = st.text_input("Parroquia*")
        municipio = st.selectbox("Municipio*", ["Cárdenas", "Junín", "San Cristóbal", "Otro"])
        catedra = st.selectbox("Cátedra*", ["Beatriz Portinari", "Luz y Verdad", "Napoleón Bonaparte", "Provincial Luz Occidente"])

    profesiones = st.text_area("Profesiones Estudiadas (Títulos)*")
    ocupacion = st.text_input("Ocupación Actual*")

    st.markdown("---")
    col_salud1, col_salud2 = st.columns([1, 2])
    with col_salud1:
        estado_salud = st.selectbox("Condición de Salud*", ["Sano", "Necesidades Especiales"])
    with col_salud2:
        necesidades_esp = st.text_input("Especificar Necesidades Especiales (Si aplica)")

    st.markdown("### II. MAPA DE APTITUDES (El Saber Hacer)")
    st.info("Marca tus áreas de dominio y especifica tu experiencia.")
    
    # Áreas de dominio en filas diferentes para mejor visibilidad móvil
    sa_check = st.checkbox("Sostén Alimentario (Siembra, cría, riego)")
    sa_especificar = st.text_input("Especificar Sostén Alimentario")
    st.markdown("---")
    
    io_check = st.checkbox("Infraestructura y Oficios (Construcción, Mecánica, Textil)")
    io_especificar = st.text_input("Especificar Infraestructura/Oficios")
    st.markdown("---")
    
    sb_check = st.checkbox("Salud y Bienestar (Medicina, Botánica, Fluidoterapia)")
    sb_especificar = st.text_input("Especificar Salud/Bienestar")
    st.markdown("---")
    
    ct_check = st.checkbox("Ciencia y Tecnología (IA, Energía, Comunicaciones)")
    ct_especificar = st.text_input("Especificar Ciencia/Tecnología")
    st.markdown("---")
    
    ea_check = st.checkbox("Educación y Arte (Doctrina, Música, Pedagogía)")
    ea_especificar = st.text_input("Especificar Educación/Arte")

    st.markdown("### III. INVENTARIO DE MEDIOS DE PRODUCCIÓN")
    herramientas = st.text_input("Herramientas Manuales/Eléctricas")
    tierra = st.text_input("Tierras/Espacios de Cultivo (Indicar Ha o m2)")
    maquinaria = st.text_input("Maquinaria/Vehículos")
    tecnologia_medios = st.text_input("Tecnología (Paneles, Radio, Computación)")

    st.markdown("### IV. DISPONIBILIDAD Y FORMACIÓN")
    aprender = st.text_input("¿Qué oficio te gustaría aprender de otros hermanos?")
    movilidad = st.radio("En un escenario de crisis, ¿estás dispuesto a la movilidad geográfica?", ["SI", "NO"])
    horas_estudio = st.number_input("¿Cuántas horas semanales dedicas hoy al estudio del Código de Amor Universal?", min_value=0)

    submit_button = st.form_submit_button(label="REGISTRAR EN LA COMUNA")

    if submit_button:
        campos_obli = {
            "Primer Nombre": p_nombre, "Primer Apellido": p_apellido, "Cédula": cedula,
            "Celular": celular, "Dirección": direccion, "Profesiones": profesiones, "Ocupación": ocupacion
        }
        faltantes = [label for label, valor in campos_obli.items() if not valor.strip()]

        if faltantes:
            st.error(f"Faltan campos obligatorios: {', '.join(faltantes)}")
        else:
            payload = {
                "Primer_Nombre": p_nombre,
                "Segundo_Nombre": s_nombre,
                "Primer_Apellido": p_apellido,
                "Segundo_Apellido": s_apellido,
                "Fecha_Nacimiento": fecha_nac.strftime("%d/%m/%Y"),
                "Cedula_Identidad": cedula,
                "Direccion_Casa": direccion,
                "Celular": celular,
                "Profesiones": profesiones,
                "Ocupacion_Actual": ocupacion,
                "Ciudad": ciudad,
                "Parroquia": parroquia,
                "Municipio": municipio,
                "Cátedra": catedra,
                "Estado_Salud": estado_salud,
                "Necesidades_Especiales": necesidades_esp,
                "Sosten_Alimentario": "X" if sa_check else "",
                "Especificar_SA": sa_especificar,
                "Infraestructura_Oficios": "X" if io_check else "",
                "Especificar_IO": io_especificar,
                "Salud_Bienestar": "X" if sb_check else "",
                "Especificar_SB": sb_especificar,
                "Ciencia_Tecnologia": "X" if ct_check else "",
                "Especificar_CT": ct_especificar,
                "Educacion_Arte": "X" if ea_check else "",
                "Especificar_EA": ea_especificar,
                "Herramientas": herramientas,
                "Tierra": tierra,
                "Maquinaria": maquinaria,
                "Tecnologia": tecnologia_medios,
                "Aprender_Oficio": aprender,
                "Movilidad_Crisis": movilidad,
                "Horas_Estudio": horas_estudio
            }

            try:
                with st.spinner("Tramitando registro en la Comuna..."):
                    response = requests.post(URL_SCRIPT, json=payload)
                if response.status_code == 200:
                    st.success("✅ ¡Hermano, su registro ha sido procesado con éxito!")
                    st.balloons()
                else:
                    st.error("Error en la conexión con la base de datos.")
            except Exception as e:
                st.error(f"Error técnico: {e}")
