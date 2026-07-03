# 🧠 Libras-TechMan

**Tradutor de LIBRAS em Tempo Real com Inteligência Artificial**

Um sistema avançado de tradução automática de LIBRAS (Linguagem Brasileira de Sinais) para texto e voz, utilizando visão computacional, machine learning e processamento de linguagem natural.

---

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Características](#características)
- [Arquitetura](#arquitetura)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Componentes](#componentes)
- [API REST](#api-rest)
- [Interface Web](#interface-web)
- [Configuração](#configuração)
- [Troubleshooting](#troubleshooting)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

---

## 🎯 Visão Geral

Libras-TechMan é uma aplicação que utiliza tecnologias de ponta para:

- **Detectar movimentos das mãos** em tempo real através de câmera
- **Identificar letras e sinais** de LIBRAS usando modelos híbridos (C + Machine Learning)
- **Reconhecer emoções** do usuário
- **Construir frases** a partir de sinais individuais
- **Converter para voz** via síntese de texto (TTS)
- **Fornecer interface web** para visualização em tempo real

### Casos de Uso

- ♿ Acessibilidade para pessoas surdas e mudas
- 📚 Educação e treinamento em LIBRAS
- 🎓 Ferramentas assistivas em instituições
- 🔍 Pesquisa em visão computacional e reconhecimento de gestos
- 💼 Interpretação automática de conteúdo em LIBRAS

---

## ✨ Características

### Detecção e Reconhecimento
- ✅ Detecção de mão em tempo real com **MediaPipe**
- ✅ Classificação híbrida (Engine C + TensorFlow/Keras)
- ✅ Reconhecimento de **emoções** com DeepFace
- ✅ Suporte a **múltiplos métodos** de classificação
- ✅ Confiança de detecção com scores de precisão

### Processamento de Linguagem
- ✅ Construção dinâmica de palavras
- ✅ Agrupamento inteligente de palavras em frases
- ✅ Detecção automática de pausas
- ✅ Tratamento de repetições

### Interface e Integração
- ✅ **UI Web em Tempo Real** com Streamlit
- ✅ **API REST** com FastAPI
- ✅ **WebSocket** para streaming de dados
- ✅ **Síntese de Voz** offline (pyttsx3)
- ✅ **HUD Visual** com informações em tempo real

---

## 🏗️ Arquitetura

```
┌─────────────────────────────────────────────────────────┐
│                    Interface Web (Streamlit)            │
│              Interface de Usuário em Tempo Real          │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│              API REST (FastAPI)                         │
│         WebSocket para Streaming de Frame              │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│                   CORE ENGINE                           │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  ┌────────────────┐      ┌─────────────────────┐       │
│  │ Camera Input   │      │ Hand Detection      │       │
│  │ (OpenCV)       │─────▶│ (MediaPipe)         │       │
│  └────────────────┘      └──────────┬──────────┘       │
│                                      │                  │
│  ┌────────────────┐      ┌──────────▼──────────┐       │
│  │ Emotion        │      │ Hybrid Classifier  │       │
│  │ Detection      │      │ (C + ML)           │       │
│  │ (DeepFace)     │      └──────────┬──────────┘       │
│  └────────────────┘                 │                  │
│                          ┌──────────▼──────────┐       │
│                          │ Word Builder        │       │
│                          │ (Phrase Engine)     │       │
│                          └──────────┬──────────┘       │
│                                     │                  │
│                          ┌──────────▼──────────┐       │
│                          │ Text-to-Speech     │       │
│                          │ (pyttsx3)          │       │
│                          └────────────────────┘       │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

## 📦 Pré-requisitos

### Software
- **Python 3.8+**
- **Git**
- **Webcam/Câmera** funcional
- **Windows 10+** ou **Linux**

### Dependências de Sistema
```bash
# Windows
# Instale Visual Studio Build Tools (para compilar extensões C)

# Linux (Ubuntu/Debian)
sudo apt-get install build-essential python3-dev
sudo apt-get install libopencv-dev python3-opencv
```

---

## 🚀 Instalação

### 1. Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/libras-techman.git
cd libras-techman
```

### 2. Criar Ambiente Virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configurar Arquivo de Extensão C (Opcional)
Se possuir o arquivo `classificador.dll` (Windows) ou `classificador.so` (Linux), coloque na pasta `engine/`:
```bash
cp seu_classificador.dll engine/classificador.dll  # Windows
cp seu_classificador.so engine/classificador.so    # Linux
```

---

## 💻 Uso

### Modo 1: Aplicação Desktop (Tempo Real)
```bash
python main.py
```

**Controles:**
- `Q` ou `ESC` para sair
- A detecção ocorre automaticamente
- Voz sintetizada reproduz as palavras detectadas

### Modo 2: Interface Web (Streamlit)
```bash
streamlit run ui/app.py
```

Acesse: `http://localhost:8501`

### Modo 3: API REST
```bash
python api/server.py
```

A API estará disponível em: `http://localhost:8000`

**Documentação interativa:**
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

## 📁 Estrutura do Projeto

```
libras-techman/
├── 📄 readme.md                    # Este arquivo
├── 📄 main.py                      # Ponto de entrada principal
├── 📄 requirements.txt             # Dependências Python
│
├── 📁 api/                         # API REST e WebSocket
│   ├── server.py                   # Servidor FastAPI
│   └── realtime.py                 # Endpoints WebSocket
│
├── 📁 config/                      # Configurações
│   ├── __init__.py
│   └── settings.py                 # Constantes e parametrização
│
├── 📁 core/                        # Núcleo do Sistema
│   ├── camera.py                   # Captura de vídeo (OpenCV)
│   ├── detector_mao.py             # Detecção de mão (MediaPipe)
│   ├── detector_emocao.py          # Reconhecimento de emoção (DeepFace)
│   ├── classificador.py            # Classificador em C
│   ├── classificador_hibrido.py    # Orquestração C + ML
│   ├── desenhador.py               # HUD e renderização visual
│   ├── palavras.py                 # Construtor de palavras
│   ├── frases.py                   # Construtor de frases
│   ├── utils.py                    # Utilitários gerais
│   └── __init__.py
│
├── 📁 engine/                      # Motor em C
│   ├── classificador.c             # Código-fonte C
│   ├── classificador.h             # Headers C
│   └── classificador.dll/.so       # Binário compilado
│
├── 📁 ia/                          # Machine Learning
│   ├── coletor_dataset.py          # Coleta de dados de treinamento
│   ├── inferencia.py               # Inferência TensorFlow
│   ├── treinamento.py              # Script de treinamento
│   ├── modelos/                    # Modelos treinados
│   └── __init__.py
│
├── 📁 data/                        # Dados e Recursos
│   ├── datasets/                   # Datasets de LIBRAS
│   ├── imagens/                    # Imagens de referência
│   └── videos/                     # Vídeos de teste
│
├── 📁 ui/                          # Interface Web
│   └── app.py                      # Aplicação Streamlit
│
├── 📁 voz/                         # Síntese de Voz
│   ├── sintetizador.py             # Engine TTS
│   └── __init__.py
│
├── 📁 tests/                       # Testes Automatizados
│   └── [test files]
│
└── 📁 logs/                        # Arquivos de Log
    └── [log files]
```

---

## 🔧 Componentes

### 1. **Camera** (`core/camera.py`)
Gerencia captura de vídeo em tempo real
- Inicialização com OpenCV
- Captura de frames
- Tratamento de erros de câmera

### 2. **DetectorMao** (`core/detector_mao.py`)
Detecção de mão usando MediaPipe
- 21 landmarks por mão
- Confiança de detecção
- Identificação de lado (esquerda/direita)
- Desenho de skeleton

### 3. **DetectorEmocao** (`core/detector_emocao.py`)
Análise de emoção com DeepFace
- 7 emoções: Happy, Sad, Angry, Surprised, Fear, Neutral, Disgusted
- Score de confiança
- Cache para otimização

### 4. **ClassificadorHibrido** (`core/classificador_hibrido.py`)
Orquestrador de classificação
- **Engine C**: Análise geométrica rápida
- **Engine ML**: TensorFlow para reconhecimento preciso
- Seleção automática do melhor resultado
- Score de confiança unificado

### 5. **ConstrutorPalavras** (`core/palavras.py`)
Agregação de letras em palavras
- Detecção de pausa entre sinais
- Evita repetição de letras consecutivas
- Timeout configurável

### 6. **ConstrutorFrases** (`core/frases.py`)
Agrupamento de palavras em frases
- Detecção de pausa longa entre palavras
- Processamento de linguagem natural
- Organização do fluxo de texto

### 7. **SintetizadorVoz** (`voz/sintetizador.py`)
Síntese de fala em português
- pyttsx3 para processamento offline
- Velocidade e volume configuráveis
- Reprodução de letras e palavras

### 8. **HUD** (`core/desenhador.py`)
Interface visual em tempo real
- Skeleton da mão
- Letra detectada
- Confiança
- Palavra atual
- Emoção detectada

---

## 🌐 API REST

### Endpoints Principais

#### Health Check
```bash
GET /health
```

**Resposta:**
```json
{
  "status": "ok"
}
```

#### WebSocket - Stream em Tempo Real
```bash
WS ws://localhost:8000/ws
```

**Dados recebidos:**
```json
{
  "frame": "base64_encoded_image",
  "letra": "A",
  "confianca_letra": 0.95,
  "palavra": "PALAVRA",
  "frase": "LIBRAS TECHMAN",
  "emocao": {
    "emotion": "happy",
    "confidence": 0.87
  }
}
```

---

## 🎨 Interface Web

### Streamlit App (`ui/app.py`)

A interface web oferece:
- 📹 Visualização de vídeo em tempo real
- 📊 Cards de detecção (letra, confiança)
- 😊 Indicador de emoção
- 📝 Histórico de palavras e frases
- ⚙️ Controles de configuração

**Acesso:**
```bash
streamlit run ui/app.py
```

---

## ⚙️ Configuração

### Arquivo `config/settings.py`

```python
CAMERA_INDEX = 0                 # Índice da câmera
WINDOW_NAME = "Libras-TechMan"   # Nome da janela
MIN_HAND_DETECTION = 0.7         # Confiança mínima de detecção
MAX_HANDS = 1                    # Máximo de mãos detectadas
EMOTION_REFRESH = 10             # Frames para atualizar emoção
DLL_WINDOWS = "./engine/classificador.dll"
DLL_LINUX = "./engine/classificador.so"
FONT_SCALE = 0.7                 # Escala da fonte no HUD
FONT_THICKNESS = 2               # Espessura da fonte
```

### Variáveis de Ambiente

```bash
# Opcional: definir câmera específica
export CAMERA_INDEX=0

# Opcional: modo debug
export DEBUG=1

# Opcional: porta da API
export API_PORT=8000
```

---

## 🐛 Troubleshooting

### Problema: Câmera não é detectada
**Solução:**
```bash
# Verificar câmeras disponíveis
python -c "import cv2; print(cv2.VideoCapture(0).isOpened())"

# Tentar índices diferentes em config/settings.py
CAMERA_INDEX = 1  # ou 2, 3...
```

### Problema: "Modelo não encontrado. ML desativado."
**Solução:**
- Coloque o arquivo `classificador.dll` ou `.so` em `engine/`
- Ou treine um novo modelo: `python ia/treinamento.py`

### Problema: WebSocket falha
**Solução:**
```bash
# Verificar se a API está rodando
ps aux | grep "python api/server.py"

# Reiniciar a API
python api/server.py
```

### Problema: Baixa performance
**Solução:**
```python
# Reduzir taxa de atualização em config/settings.py
EMOTION_REFRESH = 20  # Aumentar de 10 para 20

# Reduzir resolução em core/camera.py
# Adicionar:
self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
```

---

## 📊 Fluxo de Dados

```
Camera Frame
    ↓
┌─────────────────────┐
│ Hand Detection      │ ← MediaPipe
│ (Landmarks)         │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ Hybrid Classifier   │ ← C + ML
│ (Letter Detection)  │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ Word Builder        │ ← Agregação
│ (Word Formation)    │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ Phrase Builder      │ ← Agrupamento
│ (Sentence Formation)│
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ Text-to-Speech      │ ← pyttsx3
│ (Voice Synthesis)   │
└──────────┬──────────┘
           ↓
    Audio Output
    UI Display
```

---

## 🧠 Modelos de IA

### Treinamento de Novo Modelo

```bash
# 1. Coletar dataset
python ia/coletor_dataset.py

# 2. Treinar modelo
python ia/treinamento.py

# 3. Converter para formato otimizado
python ia/inferencia.py --export
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. **Fork** o repositório
2. **Crie uma branch** para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a branch (`git push origin feature/AmazingFeature`)
5. **Abra um Pull Request**

### Guidelines
- Mantenha o código limpo e documentado
- Escreva testes para novas funcionalidades
- Siga o estilo de código do projeto
- Atualize a documentação conforme necessário

---

## 📝 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 👥 Autor

Desenvolvido por **Matheus** como parte do projeto TechMan.

---

## 📞 Suporte

Para dúvidas e suporte:
- 📧 Email: matheusalmeidacarlos@gmail.com


---

## 🎓 Referências e Tecnologias

### Bibliotecas Utilizadas
- **OpenCV** - Processamento de vídeo
- **MediaPipe** - Detecção de mão
- **TensorFlow/Keras** - Deep Learning
- **DeepFace** - Reconhecimento de emoção
- **FastAPI** - API REST
- **Streamlit** - Interface Web
- **pyttsx3** - Síntese de voz
- **scikit-learn** - Machine Learning

### Documentação Oficial
- [MediaPipe Hand Detection](https://mediapipe.dev)
- [TensorFlow Documentation](https://www.tensorflow.org)
- [FastAPI](https://fastapi.tiangolo.com)
- [Streamlit](https://streamlit.io)

---

## 📈 Roadmap

- [ ] Suporte a ambas as mãos simultaneamente
- [ ] Reconhecimento de expressões faciais mais detalhadas
- [ ] Exportação de histórico de tradução
- [ ] Integração com banco de dados
- [ ] Mobile App (Flutter/React Native)
- [ ] Melhorias no reconhecimento de sinais complexos
- [ ] Suporte a outros idiomas de sinais
- [ ] Otimização de performance com ONNX
- [ ] Deploy em produção (Docker, Kubernetes)

---

## 🙏 Agradecimentos

Obrigado a todos os contribuidores e à comunidade de LIBRAS por inspirar este projeto.

---

**Libras-TechMan** © 2026 | Traduzindo gestos em palavras, conectando pessoas. ♿✋💬
