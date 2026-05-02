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
        "titulo": "Campeão Carioca de 2026",
        "data": "08/03/2026",
        "local": "Rio de Janeiro, RJ",
        "estadio": "Estádio Mario Filho - Maracanã",
        "placar": "Flamengo 0 (5) X (4) 0 Fluminense",
        "publico": "69.315 presentes",
        "campeonato": "Campeonato Carioca de 2026",
        "cor": "#ec1c24",
        "img_url": "https://media.antenadosnofutebol.com.br/wp-content/uploads/sites/31/2026/03/08212309/AGIF26030820484728-4000x2667.webp" # Substitua pelo link da imagem
    },
    "Santos": {
        "titulo": "Campeão Paulista 2016",
        "data": "08/05/2016",
        "local": "Santos, SP",
        "estadio": "Vila Belmiro",
        "placar": "Santos 1 x 0 Audax",
        "publico": "16.018 presentes",
        "campeonato": "Campeonato Paulista 2016",
        "cor": "#000000",
        "img_url": "https://p2.trrsf.com/image/fget/cf/940/0/images.terra.com/2016/05/08/santosfestaaleviannaagenciaelevengp.jpg"
    },
    "Internacional": {
        "titulo": "Campeão Gaucho 2025",
        "data": "16/03/2025",
        "local": "Porto Alegre, RS",
        "estadio": "Beira-Rio",
        "placar": "(3) Internacional 1 X 1 Grêmio (1)",
        "publico": "50.794 presentes",
        "campeonato": "Campeonato Gaucho 2025",
        "cor": "#e30613",
        "img_url": "https://jpimg.com.br/uploads/2025/03/campeonato-gaucho.jpg"
    },
    "Cruzeiro": {
        "titulo": "Campeão Mineiro 2026",
        "data": "08/03/2026",
        "local": "Belo Horizonte, MG",
        "estadio": "Mineirão",
        "placar": "1 Cruzeiro X 0 Atlético-MG",
        "publico": "49.675 presentes",
        "campeonato": "Campeonato Mineiro 2026",
        "cor": "#005baa",
        "img_url": "https://lncimg.lance.com.br/cdn-cgi/image/width=950,quality=75,fit=pad,format=webp/uploads/2026/03/Cruzeiro-campeao-mineiro-scaled-aspect-ratio-512-320.jpg"
    },
    "Botafogo": {
        "titulo": "Campeão Brasileiro 2024",
        "data": "08/12/2024",
        "local": "Rio de Janeiro, RJ",
        "estadio": "Estádio Nilton Santos",
        "placar": "2 Botafogo X 1 São Paulo",
        "publico": "41.986 presentes",
        "campeonato": "Campeonato Brasileiro 2024",
        "musica": "hino-do-botafogo.mp3",
        "cor": "#005baa",     
        "img_url":"https://lncimg.lance.com.br/uploads/2024/12/botafogo-campeao-brasileiro-scaled-aspect-ratio-512-320.jpg"
    },
}

# Título do Site
st.title("⚽ Manual do Amante de Futebol")
st.subheader("Escolha seu clube e veja os detalhes da última glória!")

# Menu de Seleção
time_escolhido = st.selectbox("Selecione um clube:", list(dados_times.keys()))

if time_escolhido:
    dados = dados_times[time_escolhido]
    st.audio(dados["musica"], format="audio/mp3")
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
