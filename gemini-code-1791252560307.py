import streamlit as st
import requests

# Configuración de la página
st.set_page_config(page_title="WorldData - Buscador de Países", page_icon="🌎", layout="wide")

# Estilos visuales
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #f8fafc; }
    h1 { color: #38bdf8; text-align: center; }
    p { text-align: center; color: #94a3b8; }
    </style>
""", unsafe_allow_html=True)

st.title("🌎 WorldData - Buscador de Países")
st.write("Consulta datos, capitales, población y banderas en tiempo real")

# Cargar la lista completa de países desde una fuente JSON pública
@st.cache_data
def obtener_paises():
    try:
        url = "https://raw.githubusercontent.com/mledoze/countries/master/countries.json"
        res = requests.get(url, timeout=10)
        data = res.json()
        
        lista_paises = []
        for p in data:
            nombre = p.get('translations', {}).get('spa', {}).get('common') or p.get('name', {}).get('common', '')
            capitales = p.get('capital', ['No disponible'])
            capital = capitales[0] if capitales else 'No disponible'
            region = p.get('region', 'Desconocido')
            codigo = p.get('cca2', '').lower()
            bandera = f"https://flagcdn.com/w320/{codigo}.png" if codigo else ""
            
            lista_paises.append({
                "nombre": nombre,
                "capital": capital,
                "continente": region,
                "bandera": bandera
            })
        
        return sorted(lista_paises, key=lambda x: x['nombre'])
    except Exception:
        return []

paises = obtener_paises()

# Buscador con .strip() para limpiar espacios accidentales
busqueda = st.text_input("Buscar país:", placeholder="Escribe un país (ej. Afganistán, Italia, Japón)...").strip()

# Filtrado de resultados
if busqueda:
    resultados = [
        p for p in paises 
        if busqueda.lower() in p["nombre"].lower() 
        or busqueda.lower() in p["capital"].lower() 
        or busqueda.lower() in p["continente"].lower()
    ]
else:
    resultados = paises[:21] # Muestra los primeros 21 al inicio

# Mostrar resultados
if resultados:
    cols = st.columns(3)
    for i, p in enumerate(resultados):
        with cols[i % 3]:
            if p["bandera"]:
                st.image(p["bandera"], use_container_width=True)
            st.subheader(p["nombre"])
            st.write(f"🏛️ **Capital:** {p['capital']}")
            st.write(f"🌍 **Continente:** {p['continente']}")
            st.divider()
else:
    st.warning(f"No se encontraron resultados para '{busqueda}'")