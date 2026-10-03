
import streamlit as st

st.set_page_config(page_title="Calculadora de Materiales", page_icon="🧱", layout="centered")

st.title("🧱 Calculadora de Materiales para Obras Menores")
st.write("Estima rápidamente la cantidad de insumos necesarios para tu mezcla de concreto.")

# Selección del tipo de mezcla o resistencia
tipo_concreto = st.selectbox(
    "Selecciona la resistencia o tipo de mezcla:",
    [
        "Concreto f'c = 175 kg/cm² (1:2:3)",
        "Concreto f'c = 210 kg/cm² (1:1.5:2)",
        "Concreto Pobre / Solado (1:12)"
    ]
)

st.markdown("---")
st.subheader("📍 Parámetros de Volumen")
metodo = st.radio(
    "¿Cómo deseas definir el volumen de la obra?",
    ["Ingresar Volumen Directo (m³)", "Calcular por Dimensiones (Largo x Ancho x Espesor)"]
)

volumen = 0.0

if metodo == "Ingresar Volumen Directo (m³)":
    volumen = st.number_input("Volumen total de concreto (m³):", min_value=0.1, value=1.0, step=0.1)
else:
    col1, col2, col3 = st.columns(3)
    with col1:
        largo = st.number_input("Largo (m)", min_value=0.1, value=4.0, step=0.5)
    with col2:
        ancho = st.number_input("Ancho (m)", min_value=0.1, value=3.0, step=0.5)
    with col3:
        espesor = st.number_input("Espesor / Altura (m)", min_value=0.01, value=0.2, step=0.05)
    
    # Cálculo con un 5% de desperdicio estándar en obra
    volumen_neto = largo * ancho * espesor
    volumen = volumen_neto * 1.05
    
    st.info(f"📐 Volumen Neto: **{volumen_neto:.2f} m³** | Volumen con 5% de desperdicio: **{volumen:.2f} m³**")

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🧮 CALCULAR MATERIALES", use_container_width=True):
    # Estimaciones referenciales de consumo por m3 de concreto compacto
    if "175" in tipo_concreto:
        cemento_bolsas = volumen * 9.5
        arena_m3 = volumen * 0.52
        piedra_m3 = volumen * 0.54
        agua_l = volumen * 185
    elif "210" in tipo_concreto:
        cemento_bolsas = volumen * 11.5
        arena_m3 = volumen * 0.48
        piedra_m3 = volumen * 0.52
        agua_l = volumen * 190
    else:  # Concreto Pobre
        cemento_bolsas = volumen * 3.5
        arena_m3 = volumen * 0.65
        piedra_m3 = volumen * 0.65
        agua_l = volumen * 120

    st.success("¡Cálculo procesado con éxito!")
    
    # Mostrar resultados en métricas visuales
    r1, r2 = st.columns(2)
    with r1:
        st.metric(label="🛍️ Cemento (Bolsas de 42.5 kg)", value=f"{cemento_bolsas:.1f}")
        st.metric(label="🏜️ Arena (m³)", value=f"{arena_m3:.2f}")
    with r2:
        st.metric(label="🪨 Piedra Chancada (m³)", value=f"{piedra_m3:.2f}")
        st.metric(label="💧 Agua (Litros)", value=f"{agua_l:.1f}")
        
    st.warning("⚠️ **Aviso:** Estos valores son estimaciones técnicas de referencia e incluyen el factor de desperdicio. Para proyectos estructurales críticos, valida siempre con tu diseño de mezclas oficial.")
