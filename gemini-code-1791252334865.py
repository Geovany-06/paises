import streamlit as st

# Configuración de la página
st.set_page_config(page_title="WorldData - Buscador de Países", page_icon="🌎", layout="wide")

# Estilos visuales oscuros
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #f8fafc; }
    h1 { color: #38bdf8; text-align: center; }
    p { text-align: center; color: #94a3b8; }
    </style>
""", unsafe_allow_html=True)

st.title("🌎 WorldData - Buscador de Países")
st.write("Consulta datos, capitales, población y banderas en tiempo real")

# Base de datos local e infalible
paises = [
    {"nombre": "El Salvador", "capital": "San Salvador", "continente": "América", "poblacion": "6,314,000", "moneda": "Dólar estadounidense ($)", "bandera": "https://flagcdn.com/w320/sv.png"},
    {"nombre": "Italia", "capital": "Roma", "continente": "Europa", "poblacion": "58,940,000", "moneda": "Euro (€)", "bandera": "https://flagcdn.com/w320/it.png"},
    {"nombre": "México", "capital": "Ciudad de México", "continente": "América", "poblacion": "128,900,000", "moneda": "Peso mexicano ($)", "bandera": "https://flagcdn.com/w320/mx.png"},
    {"nombre": "España", "capital": "Madrid", "continente": "Europa", "poblacion": "47,400,000", "moneda": "Euro (€)", "bandera": "https://flagcdn.com/w320/es.png"},
    {"nombre": "Japón", "capital": "Tokio", "continente": "Asia", "poblacion": "125,700,000", "moneda": "Yen japonés (¥)", "bandera": "https://flagcdn.com/w320/jp.png"},
    {"nombre": "Guatemala", "capital": "Ciudad de Guatemala", "continente": "América", "poblacion": "17,110,000", "moneda": "Quetzal (Q)", "bandera": "https://flagcdn.com/w320/gt.png"},
    {"nombre": "Honduras", "capital": "Tegucigalpa", "continente": "América", "poblacion": "10,280,000", "moneda": "Lempira (L)", "bandera": "https://flagcdn.com/w320/hn.png"},
    {"nombre": "Costa Rica", "capital": "San José", "continente": "América", "poblacion": "5,150,000", "moneda": "Colón costarricense (₡)", "bandera": "https://flagcdn.com/w320/cr.png"},
    {"nombre": "Francia", "capital": "París", "continente": "Europa", "poblacion": "67,750,000", "moneda": "Euro (€)", "bandera": "https://flagcdn.com/w320/fr.png"},
    {"nombre": "Alemania", "capital": "Berlín", "continente": "Europa", "poblacion": "83,200,000", "moneda": "Euro (€)", "bandera": "https://flagcdn.com/w320/de.png"},
    {"nombre": "Estados Unidos", "capital": "Washington D.C.", "continente": "América", "poblacion": "331,900,000", "moneda": "Dólar estadounidense ($)", "bandera": "https://flagcdn.com/w320/us.png"},
    {"nombre": "Colombia", "capital": "Bogotá", "continente": "América", "poblacion": "51,520,000", "moneda": "Peso colombiano ($)", "bandera": "https://flagcdn.com/w320/co.png"},
    {"nombre": "Argentina", "capital": "Buenos Aires", "continente": "América", "poblacion": "45,810,000", "moneda": "Peso argentino ($)", "bandera": "https://flagcdn.com/w320/ar.png"},
    {"nombre": "Brasil", "capital": "Brasilia", "continente": "América", "poblacion": "214,300,000", "moneda": "Real brasileño (R$)", "bandera": "https://flagcdn.com/w320/br.png"},
    {"nombre": "Canadá", "capital": "Ottawa", "continente": "América", "poblacion": "38,250,000", "moneda": "Dólar canadiense ($)", "bandera": "https://flagcdn.com/w320/ca.png"},
    {"nombre": "Reino Unido", "capital": "Londres", "continente": "Europa", "poblacion": "67,330,000", "moneda": "Libra esterlina (£)", "bandera": "https://flagcdn.com/w320/gb.png"},
    {"nombre": "China", "capital": "Pekín", "continente": "Asia", "poblacion": "1,412,000,000", "moneda": "Yuan chino (¥)", "bandera": "https://flagcdn.com/w320/cn.png"}
]

# Buscador
busqueda = st.text_input("Buscar país:", placeholder="Escribe un país (ej. Italia, El Salvador, Japón)...")

# Filtrado de resultados
if busqueda:
    resultados = [p for p in paises if busqueda.lower() in p["nombre"].lower() or busqueda.lower() in p["capital"].lower() or busqueda.lower() in p["continente"].lower()]
else:
    resultados = paises

# Mostrar resultados en cuadrícula
if resultados:
    cols = st.columns(3)
    for i, p in enumerate(resultados):
        with cols[i % 3]:
            st.image(p["bandera"], use_container_width=True)
            st.subheader(p["nombre"])
            st.write(f"🏛️ **Capital:** {p['capital']}")
            st.write(f"🌍 **Continente:** {p['continente']}")
            st.write(f"👨‍👩‍👧‍‍👦 **Población:** {p['poblacion']}")
            st.write(f"💰 **Moneda:** {p['moneda']}")
            st.divider()
else:
    st.warning(f"No se encontraron resultados para '{busqueda}'")