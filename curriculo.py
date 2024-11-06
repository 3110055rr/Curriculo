import streamlit as st

# Funções para cada seção do currículo
def show_about_me():
    st.title("Sobre Mim")
    st.write("""
    Olá, meu nome é [Seu Nome]! Sou um [Profissão] apaixonado por [Áreas de Interesse]. 
    Tenho experiência em [descrever sua área de atuação, especializações, interesses e metas]. 
    Gosto de [hobbies ou atividades pessoais] e estou sempre buscando me aprimorar profissionalmente e pessoalmente.
    """)

def show_skills_and_knowledge():
    st.title("Habilidades e Conhecimentos")
    st.write("""
    Aqui estão algumas das minhas habilidades e conhecimentos:
    - **Linguagens de Programação**: Python, JavaScript, C++
    - **Frameworks**: React, Django, Flask
    - **Ferramentas**: Git, Docker, Jenkins
    - **Banco de Dados**: MySQL, PostgreSQL
    - **Outros**: Machine Learning, Data Analysis, Web Development
    """)

def show_courses_and_experience():
    st.title("Cursos e Experiência")
    st.write("""
    **Cursos**
    - **[Nome do Curso]** – [Instituição] ([Ano de Conclusão])  
      Descrição breve sobre o curso ou aprendizado.

    **Experiência Profissional**
    - **[Cargo]** | [Nome da Empresa] | [Ano de Início] - [Ano de Término ou até o presente momento]  
      Descrição de responsabilidades e realizações, como:
      - [Responsabilidade ou projeto 1]
      - [Responsabilidade ou projeto 2]
      - [Responsabilidade ou projeto 3]
    """)

def show_project_library():
    st.title("Biblioteca de Projetos")
    
    # Descrição geral da biblioteca
    st.write("""
    Aqui estão alguns dos meus projetos de games, com uma breve descrição abaixo de cada um.
    Cada projeto é apresentado em um quadrado simulando a imagem.
    """)

    # Exemplo de projeto 1: Game 1
    col1, col2, col3 = st.columns(3)  # Dividindo a tela em 3 colunas

    # Adicionando a animação de zoom com CSS
    hover_css = """
    <style>
        .project-card {
            height: 150px;
            background-color: #4CAF50;
            border-radius: 10px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .project-card:hover {
            transform: scale(1.1); /* Aumenta 10% ao passar o mouse */
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        }
        .project-card h5 {
            color: white;
            text-align: center;
            padding-top: 50px;
        }
    </style>
    """
    
    # Aplicando o CSS para a animação
    st.markdown(hover_css, unsafe_allow_html=True)

    with col1:
        # Simulando o quadrado (Imagem) com animação
        st.markdown(
            """
            <div class="project-card">
                <h5>Jogo Aventura 3D</h5>
            </div>
            """, 
            unsafe_allow_html=True
        )
        st.write("""
        - Desenvolvi um jogo de aventura em 3D utilizando Unity.
        - Recursos: Mapeamento 3D, Inteligência Artificial para inimigos.
        - **Tecnologias**: Unity, C#, Blender
        - [Link para o projeto no GitHub](https://github.com/seuusuario/game1)
        """)

    with col2:
        # Simulando o quadrado (Imagem) com animação
        st.markdown(
            """
            <div class="project-card" style="background-color: #2196F3;">
                <h5>Jogo de Plataforma 2D</h5>
            </div>
            """, 
            unsafe_allow_html=True
        )
        st.write("""
        - Criação de um jogo de plataforma 2D com física de movimentação.
        - **Tecnologias**: Godot, GDScript
        - [Link para o projeto no GitHub](https://github.com/seuusuario/game2)
        """)

    with col3:
        # Simulando o quadrado (Imagem) com animação
        st.markdown(
            """
            <div class="project-card" style="background-color: #FF9800;">
                <h5>Jogo de Corrida</h5>
            </div>
            """, 
            unsafe_allow_html=True
        )
        st.write("""
        - Jogo de corrida com modo multiplayer utilizando redes.
        - **Tecnologias**: Unreal Engine, C++, Redes
        - [Link para o projeto no GitHub](https://github.com/seuusuario/game3)
        """)

def show_follow_me():
    st.title("Acompanhamento")
    st.write("""
    Acompanhe meus projetos e atividades nas minhas redes sociais! Aqui estão alguns dos meus canais para contato e interação:
    """)

    # Exibindo links e ícones das redes sociais
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <a href="https://discord.com/users/seuusuario" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/5/56/Discord_logo_2023.svg" width="60" />
            </a>
            """, unsafe_allow_html=True)
        st.write("**Discord**: seuusuario#1234")

    with col2:
        st.markdown(
            """
            <a href="https://www.youtube.com/c/seucanal" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png" width="60" />
            </a>
            """, unsafe_allow_html=True)
        st.write("**YouTube**: [seucanal](https://www.youtube.com/c/seucanal)")

    with col3:
        st.markdown(
            """
            <a href="https://www.linkedin.com/in/seuusuario" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/0/01/LinkedIn_Logo_2013.svg" width="60" />
            </a>
            """, unsafe_allow_html=True)
        st.write("**LinkedIn**: [seuusuario](https://www.linkedin.com/in/seuusuario)")

    # Adicionando mais links sociais conforme necessário
    st.write("Você também pode me encontrar em outras redes sociais como Twitter, GitHub e Instagram, basta procurar pelo meu nome!")

# Barra lateral (Sidebar)
st.sidebar.title("Menu")

# Criação de uma função para gerar a linha vermelha de destaque
def apply_sidebar_highlight(selected_option):
    # Gerando o CSS para a opção selecionada
    st.markdown(
        f"""
        <style>
            .sidebar .css-1d391kg {{
                border-bottom: 3px solid red !important;
            }}
            .sidebar .st-radio > label:nth-child({selected_option}) {{
                border-bottom: 3px solid red;
            }}
        </style>
        """, unsafe_allow_html=True)

sidebar_options = {
    "Sobre Mim": show_about_me,
    "Habilidades e Conhecimentos": show_skills_and_knowledge,
    "Cursos e Experiência": show_courses_and_experience,
    "Biblioteca (Projetos)": show_project_library,
    "Acompanhamento": show_follow_me  # Nova seção de acompanhamento
}

# Capturando a opção selecionada
option = st.sidebar.radio("Escolha uma seção", list(sidebar_options.keys()))

# Aplica a linha vermelha no item selecionado
apply_sidebar_highlight(list(sidebar_options.keys()).index(option) + 1)

# Chama a função correspondente à seção selecionada
sidebar_options[option]()
