import streamlit as st

# Configurar fundo azul escuro
def aplicar_estilo():
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #1565C0; /* Azul escuro */
                color: white;
            }
            .stTitle, .stHeader, .stSubheader, .stMarkdown {
                color: white;
            }
            .stRadio label {
                color: white !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

aplicar_estilo()
import os
import streamlit as st

# Caminho correto para as imagens dentro do repositório
logo_blue_path = os.path.join(os.path.dirname(__file__), "logo_blue.png")
disc_logo_path = os.path.join(os.path.dirname(__file__), "disc_logo.jpeg")

# Criar layout com 3 colunas (imagem esquerda, título centralizado, imagem direita)
col1, col2, col3 = st.columns([2, 5, 2])

# Exibir imagens nas colunas laterais
with col1:
    st.image(logo_blue_path, width=100)  # Ajuste do tamanho da imagem

with col3:
    st.image(disc_logo_path, width=100)  # Ajuste do tamanho da imagem


# Criar layout com 3 colunas (imagem esquerda, título centralizado, imagem direita)
col1, col2, col3 = st.columns([2, 5, 2])

# Exibir imagens nas colunas laterais
with col1:
    st.image(logo_blue_path, width=1000)  # Ajuste de tamanho da logo Blue3

with col3:
    st.image(disc_logo_path, width=1000)  # Ajuste de tamanho do logo DISC
# Dicionário com os textos para cada perfil

# Dicionário com os textos para cada perfil
informacoes_perfil = {
    "Dominante": {
        "Pontos Fortes": [
            "Determinado e focado em resultados.",
            "Competitivo e motivado por desafios.",
            "Toma decisões rápidas e intuitivas.",
            "Rápido para identificar soluções e inovar.",
            "Lida bem com pressão e mudanças."
        ],
        "Pontos a Desenvolver": [
            "Nem tudo é urgente; precisa avaliar detalhes.",
            "Deve evitar retrabalho por falta de atenção.",
            "Pode ser inflexível e resistente a opiniões externas.",
            "Pode soar autoritário e impaciente.",
            "Precisa equilibrar assertividade com empatia."
        ],
        "Como se conectar com outros perfis": [
            "Com o Influente: Seja dinâmico e demonstre entusiasmo; evite ser excessivamente direto e valorize conexões pessoais.",
            "Com o Estável: Tenha paciência, escute mais e traga segurança para decisões, sem pressa.",
            "Com o Conforme: Use dados e lógica para embasar suas ideias; seja claro e evite improvisos."
        ]
    },
    "Influente": {
        "Pontos Fortes": [
            "Hábil em criar conexões e influenciar pessoas.",
            "Comunicativo, persuasivo e otimista.",
            "Criativo, flexível e adaptável a mudanças.",
            "Gosta de trabalhar com equipes e interagir socialmente.",
            "Alto nível de energia e entusiasmo."
        ],
        "Pontos a Desenvolver": [
            "Pode falar demais e precisar desenvolver escuta ativa.",
            "Tende a ser desorganizado e perder o foco.",
            "Pode exagerar na descontração e passar do ponto.",
            "Tem dificuldade em separar amizade e trabalho.",
            "Precisa equilibrar emoção com dados concretos."
        ],
        "Como se conectar com outros perfis": [
            "Com o Dominante: Vá direto ao ponto e foque em resultados; evite enrolação.",
            "Com o Estável: Mostre interesse genuíno, escute com atenção e evite ser muito impulsivo.",
            "Com o Conforme: Use dados e estrutura para embasar seus argumentos; reduza a improvisação."
        ]
    },
    "Estável": {
        "Pontos Fortes": [
            "Excelente ouvinte e empático.",
            "Planejador, gosta de previsibilidade e segurança.",
            "Focado em manter relacionamentos duradouros.",
            "Passa credibilidade e confiança para clientes.",
            "Ótimo em pós-venda e acompanhamento."
        ],
        "Pontos a Desenvolver": [
            "Dificuldade em dizer 'não' e pode ceder demais.",
            "Pode evitar conflitos e conversas difíceis.",
            "Tende a ser excessivamente prestativo e submisso.",
            "Tem receio de mudanças bruscas e prefere estabilidade.",
            "Pode demorar para tomar decisões importantes."
        ],
        "Como se conectar com outros perfis": [
            "Com o Dominante: Traga informações organizadas e seja direto, sem pressão.",
            "Com o Influente: Crie conexão emocional e interaja mais.",
            "Com o Conforme: Seja objetivo e valorize estrutura e previsibilidade."
        ]
    },
    "Conforme": {
        "Pontos Fortes": [
            "Analítico e atento aos detalhes.",
            "Racional e focado em precisão.",
            "Disciplinado e organizado em processos.",
            "Segue padrões e metodologias com eficiência.",
            "Paciente e cuidadoso em suas abordagens."
        ],
        "Pontos a Desenvolver": [
            "Pode ser excessivamente crítico e perfeccionista.",
            "Tem dificuldade em lidar com imprevistos e mudanças rápidas.",
            "Demora para tomar decisões e prefere segurança extrema.",
            "Pode parecer frio ou distante por ser mais racional.",
            "Tende a questionar demais e perder tempo com detalhes."
        ],
        "Como se conectar com outros perfis": [
            "Com o Dominante: Seja breve, direto e foque nos resultados práticos.",
            "Com o Influente: Demonstre interesse em experiências e histórias, evitando ser excessivamente crítico.",
            "Com o Estável: Respeite o ritmo mais cauteloso e demonstre segurança nas informações."
        ]
    }
}

# Dicionário para armazenar a contagem de pontos
pontuacoes = {"Dominante": 0, "Influente": 0, "Estável": 0, "Conforme": 0}


# Lista de perguntas
perguntas = [
    "Como você toma decisões sob pressão?",
    "Qual é sua abordagem ao iniciar um novo projeto?",
    "Como você lida com mudanças inesperadas?",
    "O que é mais importante para você em um ambiente de trabalho?",
    "Como você se sente ao trabalhar em equipe?",
    "Como você lida com feedbacks negativos?",
    "Quando precisa convencer alguém, qual é sua abordagem?",
    "Qual dessas frases mais se aproxima do seu pensamento?",
    "Como você organiza suas tarefas diárias?",
    "O que mais te incomoda no ambiente de trabalho?",
    "Como você prefere aprender algo novo?",
    "Como você reage a um erro seu no trabalho?",
    "Como você se sente ao precisar improvisar?",
    "Qual é seu maior diferencial profissional?",
    "Como você conduz uma reunião de trabalho?",
    "Como você lida com regras e procedimentos?",
    "Como você se sente ao precisar delegar tarefas?",
    "Quando recebe uma nova responsabilidade, como reage?",
    "O que te motiva a continuar crescendo profissionalmente?",
    "Como você reage quando precisa lidar com um cliente difícil?"
]

# Lista de opções sem os perfis visíveis + lista separada de perfis associados
opcoes_perguntas = [
    (["Rapidamente, baseado no resultado final.", "Considero as opiniões dos outros antes de decidir.", "Avalio detalhadamente os prós e contras antes de agir.", "Sigo minha intuição e tento envolver todos na decisão."], ["Dominante", "Estável", "Conforme", "Influente"]),
    (["Analiso todas as variáveis e crio um plano detalhado.", "Me envolvo entusiasmado e motivo a equipe.", "Inicio imediatamente, ajustando ao longo do caminho.", "Busco estabilidade e organização antes de agir."], ["Conforme", "Influente", "Dominante", "Estável"]),
    (["Me adapto rapidamente e busco soluções.", "Tento minimizar o impacto e seguir com cautela.", "Analiso cuidadosamente todas as implicações antes de agir.", "Vejo como uma oportunidade e busco envolver os outros."], ["Dominante", "Estável", "Conforme", "Influente"]),
    (["Desafios e reconhecimentos.", "Um ambiente harmonioso e de colaboração.", "Organização e previsibilidade.", "Relacionamentos e interações sociais."], ["Dominante", "Estável", "Conforme", "Influente"]),
    (["Adoro interagir e compartilhar ideias.", "Prefiro trabalhar sozinho e ter controle do processo.", "Gosto de colaborar, mas sem perder o foco na execução.", "Me preocupo com a harmonia e o bem-estar de todos."], ["Influente", "Conforme", "Dominante", "Estável"]),
    (["Analiso friamente e uso para melhoria.", "Aceito bem, mas gosto de receber de forma positiva.", "Posso reagir defensivamente se discordar.", "Fico reflexivo e tento evitar conflitos."], ["Conforme", "Influente", "Dominante", "Estável"]),
    (["Uso argumentos racionais e dados concretos.", "Demonstro entusiasmo e persuasão emocional.", "Vou direto ao ponto, mostrando os ganhos e perdas.", "Busco construir confiança e segurança na decisão."], ["Conforme", "Influente", "Dominante", "Estável"]),
    (["O planejamento é essencial para evitar erros.", "A colaboração entre todos é o mais importante.", "O importante é agir rápido e resolver problemas.", "Se envolver e inspirar os outros traz melhores resultados."], ["Conforme", "Estável", "Dominante", "Influente"]),
    (["Listo e priorizo tudo de forma metódica.", "Me organizo de forma flexível e adaptável.", "Priorizo as tarefas mais urgentes primeiro.", "Sigo uma rotina bem estruturada."], ["Conforme", "Influente", "Dominante", "Estável"]),
    (["Falta de organização e processos bem definidos.", "Falta de conexão entre as pessoas.", "Lerdeza e indecisão nas ações.", "Conflitos e falta de estabilidade."], ["Conforme", "Influente", "Dominante", "Estável"]),
    (["Com prática e experiência real.", "Observando outras pessoas e conversando.", "Lendo e estudando com calma.", "Acompanhando um processo estruturado."], ["Dominante", "Influente", "Conforme", "Estável"]),
    (["Assumo a responsabilidade e sigo em frente.", "Me preocupo com o impacto nas pessoas ao redor.", "Analiso o erro para evitar que aconteça novamente.", "Tento corrigir rapidamente e minimizar o problema."], ["Dominante", "Estável", "Conforme", "Influente"]),
    (["Tranquilo, sou criativo e adaptável.", "Prefiro seguir um plano bem estabelecido.", "Faço o que precisa ser feito sem perder tempo.", "Gosto de avaliar com calma antes de decidir."], ["Influente", "Conforme", "Dominante", "Estável"]),
    (["Rapidez e eficiência na execução.", "Capacidade de se conectar e influenciar pessoas.", "Planejamento e atenção aos detalhes.", "Paciência e foco na construção de relacionamentos."], ["Dominante", "Influente", "Conforme", "Estável"]),
    (["De forma estruturada, seguindo um plano.", "Criando um ambiente descontraído e engajador.", "Mantendo o foco nos objetivos e decisões rápidas.", "Buscando ouvir todos e garantir harmonia."], ["Conforme", "Influente", "Dominante", "Estável"]),
    (["Sigo rigorosamente, pois garantem qualidade.", "Tento equilibrar regras com flexibilidade.", "Prefiro agir com liberdade para alcançar resultados.", "Não me incomodo com regras, desde que não impeçam a criatividade."], ["Conforme", "Estável", "Dominante", "Influente"]),
    (["Prefiro fazer sozinho para garantir a qualidade.", "Confio na equipe, mas gosto de acompanhar.", "Delego rapidamente para otimizar tempo.", "Gosto de envolver as pessoas e motivá-las."], ["Conforme", "Estável", "Dominante", "Influente"]),
    (["Enxergo como um desafio e começo imediatamente.", "Analiso todos os detalhes antes de agir.", "Busco me adaptar à nova situação de forma equilibrada.", "Vejo como uma oportunidade de interação e aprendizado."], ["Dominante", "Conforme", "Estável", "Influente"]),
    (["O reconhecimento e impacto nas pessoas.", "A estabilidade e segurança no futuro.", "A excelência e melhoria contínua.", "A conquista de grandes resultados."], ["Influente", "Estável", "Conforme", "Dominante"]),
    (["Uso paciência e empatia para acalmá-lo.", "Mantenho a postura firme e foco no objetivo.", "Explico os fatos de forma lógica e racional.", "Tento ganhar a confiança e envolvê-lo na conversa."], ["Estável", "Dominante", "Conforme", "Influente"])
]

# Dicionário para armazenar a contagem de pontos
pontuacoes = {"Dominante": 0, "Influente": 0, "Estável": 0, "Conforme": 0}

st.title("🧠 Questionário de Perfis Comportamentais")

for i, (pergunta, (opcoes_texto, perfis_associados)) in enumerate(zip(perguntas, opcoes_perguntas)):
    resposta = st.radio(pergunta, opcoes_texto, index=None, key=f'pergunta_{i}')
    if resposta:
        perfil = perfis_associados[opcoes_texto.index(resposta)]
        pontuacoes[perfil] += 1

if st.button("✅ Finalizar"):
    # Ordenar perfis pela pontuação
    perfis_ordenados = sorted(pontuacoes, key=pontuacoes.get, reverse=True)
    perfil_primario = perfis_ordenados[0]
    perfil_secundario = perfis_ordenados[1] if pontuacoes[perfis_ordenados[1]] > 0 else None

    # Verificar se o perfil primário tem 100% dos pontos
    total_relevante = pontuacoes[perfil_primario] + (pontuacoes[perfil_secundario] if perfil_secundario else 0)
    percentual_primario = (pontuacoes[perfil_primario] / total_relevante) * 100 if total_relevante > 0 else 0
    percentual_secundario = (pontuacoes[perfil_secundario] / total_relevante) * 100 if perfil_secundario else 0

    # Exibir resultados
    st.subheader(f"✨ Seu perfil primário é: **{perfil_primario}** ({percentual_primario:.1f}%)")
    if perfil_secundario:
        st.subheader(f"🌟 Seu perfil secundário é: **{perfil_secundario}** ({percentual_secundario:.1f}%)")

    # Exibir detalhes do perfil primário
    st.markdown(f"## 🟢 Perfil Primário: {perfil_primario}")
    st.markdown("### ✅ Pontos Fortes:")
    for ponto in informacoes_perfil[perfil_primario]["Pontos Fortes"]:
        st.markdown(f"- {ponto}")

    st.markdown("### ⚠️ Pontos a Desenvolver:")
    for ponto in informacoes_perfil[perfil_primario]["Pontos a Desenvolver"]:
        st.markdown(f"- {ponto}")

    # Se houver perfil secundário, exibir os detalhes
    if perfil_secundario:
        st.markdown(f"## 🟢 Perfil Secundário: {perfil_secundario}")
        st.markdown("### ✅ Pontos Fortes:")
        for ponto in informacoes_perfil[perfil_secundario]["Pontos Fortes"]:
            st.markdown(f"- {ponto}")

        st.markdown("### ⚠️ Pontos a Desenvolver:")
        for ponto in informacoes_perfil[perfil_secundario]["Pontos a Desenvolver"]:
            st.markdown(f"- {ponto}")
# Adicionar a mensagem no final da página
st.markdown(
    '<p class="rodape">Criado por <strong>Lucas Veronezzi</strong><br>'
    'Instagram: <a href="https://www.instagram.com/lucasveronezzi_investimentos" target="_blank">@lucasveronezzi_investimentos</a></p>',
    unsafe_allow_html=True
)
