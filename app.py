import streamlit as st

# Configuración del título de la página web
st.set_page_config(page_title="Cotizadora de Madera", page_icon="🪵", layout="centered")

st.title("🪵 Cotizadora de Madera Aserrada")
st.write("Calcule el costo de sus piezas en Pulgadas Madera Tica (PMT).")

# Base de datos de precios por defecto
PRECIOS_DEFECTO = {
    "Teca": 1600.0,
    "Melina": 800.0,
    "Cedro Cahoba": 1200.0,
    "Cedro Amargo": 1000.0,
    "Amarillón": 1000.0,
    "Otro (Personalizado)": 0.0
}

# --- SECCIÓN 1: SELECCIÓN DE MADERA Y PRECIO ---
st.header("1. Tipo de Madera y Precio")

madera_seleccionada = st.selectbox(
    "Seleccione el tipo de madera:",
    options=list(PRECIOS_DEFECTO.keys())
)

# Definir el precio sugerido
precio_sugerido = PRECIOS_DEFECTO[madera_seleccionada]

# Si es una madera personalizada, le pedimos el nombre
if madera_seleccionada == "Otro (Personalizado)":
    nombre_madera = st.text_input("Nombre de la madera personalizada:", value="Madera Especial")
    precio_por_pulgada = st.number_input("Ingrese el precio por pulgada (4 varas): ₡", min_value=0.0, value=1000.0, step=50.0)
else:
    nombre_madera = madera_seleccionada
    # Permite modificar el precio sugerido si lo desea
    precio_por_pulgada = st.number_input(
        f"Precio por pulgada para {nombre_madera} (Modificable): ₡",
        min_value=0.0,
        value=precio_sugerido,
        step=50.0
    )

st.markdown("---")

# --- SECCIÓN 2: DIMENSIONES ---
st.header("2. Dimensiones de la Pieza")

# Creamos columnas para que se vea ordenado y compacto en la web
col1, col2 = st.columns(2)

with col1:
    grosor = st.number_input("Grosor (pulgadas):", min_value=0.1, value=1.0, step=0.5)
    ancho = st.number_input("Ancho (pulgadas):", min_value=0.1, value=10.0, step=1.0)

with col2:
    largo = st.number_input("Largo (varas):", min_value=0.1, value=3.0, step=1.0)
    cantidad = st.number_input("Cantidad de piezas:", min_value=1, value=1, step=1)

# --- SECCIÓN 3: CÁLCULOS ---
pulgadas_por_pieza = (grosor * ancho * largo) / 4
pulgadas_totales = pulgadas_por_pieza * cantidad
costo_total = pulgadas_totales * precio_por_pulgada

st.markdown("---")

# --- SECCIÓN 4: RESULTADO VISUAL ---
st.header("3. Resumen de Cotización")

# Cuadro destacado con el resultado del costo total
st.success(f"### **COSTO TOTAL ESTIMADO: ₡{costo_total:,.2f}**")

# Detalles desglosados en una tabla limpia
st.markdown(f"""
| Detalle | Valor |
| :--- | :--- |
| **Madera** | {nombre_madera} |
| **Medidas** | {grosor:g}" × {ancho:g}" en {largo:g} varas |
| **Cantidad** | {cantidad} pieza(s) |
| **Pulgadas por pieza** | {pulgadas_por_pieza:.2f} p.v. |
| **Pulgadas totales** | {pulgadas_totales:.2f} p.v. |
| **Precio unitario** | ₡{precio_por_pulgada:,.0f} |
""")
