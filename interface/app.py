import streamlit as st

# Configs básicas da página
st.set_page_config(
    page_title="Rian-IC",
    page_icon="⊕",
    layout="wide",
)

# Renderização do texto em MD
# - primeiro importa as fontes
# - aplica as fontes em todo o app
# - estilo do bloco de cima com informações de cabeçalho (.hero/.herotag)
# - estilo do titulo
# - estilo do footer
# - estilo dos cards de navegação das páginas

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Libertinus+Math:ital,wght@0,400;0,500;1,400&family=Jost:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Jost', sans-serif;

.hero {
    padding: 3.5rem 0 2rem 0;
    border-bottom: 1px solid #e5e5e5;
    margin-bottom: 2.5rem;
}

.hero-tag {
    font-family: 'Libertinus Math', serif;
    font-size: 1rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
}
            
.hero-title {
    font-size: 2.6rem;
    font-weight: 300;
    line-height: 1.2;
}

.hero-title span {
    font-weight: 500;
}
            
.footer {
    margin-top: 4rem;
    padding-top: 1.5rem;
    border-top: 1px solid #e5e5e5;
    font-family: 'Libertinus Math', serif;
    font-size: 1rem;
    line-height: 1.8;
}
            
.nav-card {
    line-height: 1.2;
    border: 1px solid #e0e0e0;
    background: #CCD67F;
    border-color: #CCD67F;
    border-radius: 8px;
    padding: 1.4rem;
    height: 100%;
    transition: border-color 0.2s;
}

.nav-card:hover {
    background: #89933a;
    color: #F3E4C9;
}
            
.nav-title {
    font-family: 'Libertinus Math', serif;
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 0.4rem;
}
 
.nav-desc {
    font-size: 1rem;
    line-height: 1.5;
    font-weight: 400;
}

</style>           
""",unsafe_allow_html=True) # Permite colocar html e CSS
        
# Cria o hero em cima (o banner com o nome da instituição)
st.markdown("""
<div class="hero">
    <div class="hero-tag">Universidade Estadual de Feira de Santana - PROBIC/UEFS</div>
    <div class="hero-title"><span>Introdução a teoria de códigos corretores de erro:</span> uma aplicação computacional de anéis de grupo</div>
</div>
""", unsafe_allow_html=True)

# Cria o carde de navegação
st.markdown("""
        <div class="nav-card">
            <div class="nav-title">01) Modelagem das estruturas</div>
            <div class="nav-desc">Em construção.</div>
        </div>
        """, unsafe_allow_html=True)
            
# Cria o footer
st.markdown("""
<div class="footer">
    Orientadora: Profª. Dra. Jacqueline Costa Cintra · UEFS<br>
    Orientando: Rian da Silva Santos · Bacharelado em Engenharia de Computação (UEFS)<br>
    Grupo de pesquisa: Estudo do grupo das unidades de anel de grupo<br>
</div>
""", unsafe_allow_html=True)