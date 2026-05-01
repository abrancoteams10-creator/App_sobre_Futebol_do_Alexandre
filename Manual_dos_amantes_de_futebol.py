import streamlit as st

# Configuração da página
st.set_page_config(page_title="Manual do Torcedor", page_icon="⚽", layout="centered")

# Estilização personalizada para as cores dos times
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #0e1117;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Banco de dados dos últimos títulos (Exemplos reais)
dados_times = {
    "Flamengo": {
        "titulo": "Copa do Brasil 2024",
        "data": "10/11/2024",
        "local": "Belo Horizonte, MG",
        "estadio": "Arena MRV",
        "placar": "Atlético-MG 0 x 1 Flamengo",
        "publico": "44.844 presentes",
        "campeonato": "Copa do Brasil",
        "cor": "#ec1c24",
        "img_url": "https://via.placeholder.com/600x300?text=Logo+Flamengo" # Substitua pelo link da imagem
    },
    "Santos": {
        "titulo": "Campeonato Paulista 2016",
        "data": "08/05/2016",
        "local": "Santos, SP",
        "estadio": "Vila Belmiro",
        "placar": "Santos 1 x 0 Audax",
        "publico": "16.018 presentes",
        "campeonato": "Campeonato Paulista",
        "cor": "#000000",
        "img_url": "https://via.placeholder.com/600x300?text=Logo+Santos"
    },
    "Internacional": {
        "titulo": "Recopa Sul-Americana 2011",
        "data": "24/08/2011",
        "local": "Porto Alegre, RS",
        "estadio": "Beira-Rio",
        "placar": "Internacional 3 x 1 Independiente",
        "publico": "39.069 presentes",
        "campeonato": "Recopa Sul-Americana",
        "cor": "#e30613",
        "img_url": "https://via.placeholder.com/600x300?text=Logo+Internacional"
    },
    "Cruzeiro": {
        "titulo": "Copa do Brasil 2018",
        "data": "17/10/2018",
        "local": "São Paulo, SP",
        "estadio": "Neo Química Arena",
        "placar": "Corinthians 1 x 2 Cruzeiro",
        "publico": "45.978 presentes",
        "campeonato": "Copa do Brasil",
        "cor": "#005baa",
        "img_url": "https://via.placeholder.com/600x300?text=Logo+Cruzeiro"
    }
}

# Título do Site
st.title("⚽ Manual do Amante de Futebol")
st.subheader("Escolha seu clube e veja os detalhes da última glória!")

# Menu de Seleção
time_escolhido = st.selectbox("Selecione um clube:", list(dados_times.keys()))

if time_escolhido:
    dados = dados_times[time_escolhido]
    
    st.divider()
    
    # Exibição de Imagem (Aqui você pode colocar a foto da taça ou do time)
    st.image(dados["img_url"], caption=f"Momento da conquista do {time_escolhido}")

    # Layout de colunas para as informações
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"### 🏆 {dados['titulo']}")
        st.write(f"**Campeonato:** {dados['campeonato']}")
        st.write(f"**Data:** {dados['data']}")
        st.write(f"**Placar:** {dados['placar']}")

    with col2:
        st.markdown("### 📍 Local e Público")
        st.write(f"**Estádio:** {dados['estadio']}")
        st.write(f"**Cidade:** {dados['local']}")
        st.write(f"**Público:** {dados['publico']}")

    st.success(f"O {time_escolhido} é gigante!")
