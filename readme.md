# Libras-TechMan

**Sistema de Reconhecimento de Gestos em Tempo Real com Machine Learning**

Um sistema baseado em visão computacional para detecção e classificação de gestos das mãos, emoções e síntese de voz. Utiliza MediaPipe para detecção de landmarks, XGBoost para classificação e DeepFace para reconhecimento de emoções.

---

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Status do Projeto](#status-do-projeto)
- [Tecnologias](#tecnologias)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Uso](#uso)
- [Componentes](#componentes)
- [API WebSocket](#api-websocket)
- [Interface Web](#interface-web)
- [Configuração](#configuração)
- [Limitações Conhecidas](#limitações-conhecidas)
- [Próximos Passos](#próximos-passos)

---

## 🎯 Visão Geral

Libras-TechMan é uma aplicação que realiza:

- **Detecção de mãos** em tempo real via câmera (MediaPipe)
- **Classificação de gestos** usando modelo XGBoost treinado
- **Reconhecimento de emoções** do usuário (DeepFace)
- **Síntese de voz** em português (pyttsx3)
- **Streaming real-time** via WebSocket (FastAPI)
- **Interface web** para visualização (Streamlit)

### O que este projeto NÃO é:

❌ Um tradutor completo de LIBRAS  
❌ Um sistema de processamento de linguagem natural  
❌ Um aplicativo com modelos pré-treinados inclusos  
❌ Uma solução de produção pronta para uso imediato

---

## 📊 Status do Projeto

**Estágio:** Prototipagem/MVP

| Componente | Status | Observação |
|-----------|--------|-----------|
| Detecção de mão | ✅ Funcional | MediaPipe 0.10 |
| Classificação ML | ⚠️ Requer treino | XGBoost (modelo não incluso) |
| Detecção de emoção | ✅ Funcional | DeepFace |
| API WebSocket | ✅ Funcional | FastAPI + Uvicorn |
| Interface Web | ✅ Funcional | Streamlit |
| Síntese de voz | ✅ Funcional | pyttsx3 (offline) |
| Engine C nativo | ⚠️ Base apenas | Não está integrado completamente |

---

## 🛠️ Tecnologias

### Backend
- **Python 3.8+** - Linguagem principal
- **FastAPI** - Framework REST + WebSocket
- **MediaPipe** 0.10 - Detecção de landmarks das mãos
- **XGBoost** - Classificação de gestos
- **DeepFace** - Reconhecimento de emoções
- **OpenCV** 4.10 - Processamento de vídeo
- **scikit-learn** - Pré-processamento e avaliação

### Frontend
- **Streamlit** - Interface web interativa
- **WebSocket** - Comunicação real-time

### Áudio
- **pyttsx3** - Síntese de fala offline em português

### Engine Nativo
- **C** - Base para processamento geométrico (não ativo)

---

## 📦 Pré-requisitos

- Python 3.8 ou superior
- Webcam/câmera
- ~2GB de espaço em disco (para modelos)
- Sistema operacional: Windows, macOS ou Linux

### Dependências
```
opencv-python==4.10.1
mediapipe==0.10.14
tensorflow==2.16.2
keras==3.6.0
scikit-learn==1.5.2
xgboost==2.1.1
fastapi==0.115.6
uvicorn==0.32.1
streamlit==1.41.1
pyttsx3==2.90
joblib==1.4.2
deepface==0.0.92
pandas==2.2.3
numpy==1.26.4
```

---

## 💻 Instalação

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/libras-techman.git
cd libras-techman
```

### 2. Criar ambiente virtual
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Treinar o modelo (OBRIGATÓRIO)
```bash
cd venv/bin/activate  # se não estiver ativado
python ia/treinamento.py
```

**Nota:** O modelo não é fornecido. Você precisa treinar com seu próprio dataset ou coletar dados primeiro.

---

## 📁 Estrutura do Projeto

```
libras-techman/
├── core/                          # Módulos centrais de IA/CV
│   ├── camera.py                  # Gerenciador de câmera
│   ├── detector_mao.py           # Detecção de landmarks (MediaPipe)
│   ├── classificador_hibrido.py  # Orquestrador de classificação
│   ├── detector_emocao.py        # Reconhecimento de emoções (DeepFace)
│   ├── desenhador.py             # Renderização de HUD
│   ├── palavras.py               # Agregador de letras em palavras
│   ├── frases.py                 # Agregador de palavras em frases
│   └── utils.py                  # Utilitários gerais
├── ia/                            # Módulos de Machine Learning
│   ├── inferencia.py             # Inferência do modelo XGBoost
│   ├── treinamento.py            # Script de treinamento
│   ├── coletor_dataset.py        # Coleta de dados para treino
│   └── modelos/                  # (vazio) Armazena modelos treinados
├── api/                           # API FastAPI
│   ├── server.py                 # Endpoints REST
│   └── realtime.py               # Endpoint WebSocket
├── ui/                            # Interface Web
│   └── app.py                    # Streamlit app
├── voz/                           # Módulos de áudio
│   └── sintetizador.py           # Text-to-speech com pyttsx3
├── engine/                        # Engine nativo (base)
│   ├── classificador.c           # Processamento geométrico em C
│   └── classificador.h           # Header C
├── config/                        # Configurações
│   └── settings.py               # Constantes do projeto
├── data/                          # Dados
│   ├── datasets/                 # (vazio) Dataset CSV
│   ├── imagens/                  # (vazio) Imagens de treino
│   └── videos/                   # (vazio) Vídeos de teste
├── main.py                        # Aplicação principal (desktop)
├── requirements.txt               # Dependências do projeto
└── readme.md                      # Este arquivo
```

---

## 🚀 Uso

### Opção 1: Aplicação Desktop (OpenCV)
```bash
python main.py
```
Abre janela com detecção em tempo real. Pressione `Q` para sair.

### Opção 2: API WebSocket (Recomendado para desenvolvimento)
```bash
uvicorn api.realtime:app --reload
```
Acessa em `ws://localhost:8000/ws` para stream de dados.

### Opção 3: Interface Web (Streamlit)
Em outro terminal:
```bash
streamlit run ui/app.py
```
Acessa em `http://localhost:8501`

### Opção 4: Coletar dados para treino
```bash
python ia/coletor_dataset.py
```
Captura landmarks de mãos e salva em CSV para treino posterior.

---

## 🔧 Componentes

### DetectorMao (core/detector_mao.py)
- Usa MediaPipe para detectar 21 landmarks da mão
- Retorna: `HandResult(encontrou_mao, landmarks, confianca)`
- Trabalha em tempo real (~30 FPS)

### ClassificadorHibrido (core/classificador_hibrido.py)
- Orquestra classificação via XGBoost
- Fallback para gestos não classificados
- Retorna: letra, confiança, método usado

### DetectorEmocao (core/detector_emocao.py)
- Usa DeepFace para 7 emoções: angry, disgust, fear, happy, neutral, sad, surprise
- Frame skipping configurável (padrão: cada 10 frames)
- Retorna: emotion, confidence

### SintetizadorVoz (voz/sintetizador.py)
- pyttsx3 offline em português
- Métodos: falar(), falar_letra(), falar_palavra(), falar_emocao()

### ConstrutorPalavras (core/palavras.py)
- Agrega letras em palavras
- Detecta pausa de 1.2s entre letras
- Limpa automaticamente palavra finalizada

### ConstrutorFrases (core/frases.py)
- Agrega palavras em frases
- Detecta pausa de 3.0s entre palavras
- Reconhece fim de frase

---

## 📡 API WebSocket

### Conectar
```javascript
const ws = new WebSocket('ws://localhost:8000/ws');
```

### Formato de dados recebidos
```json
{
  "letra": "A",
  "confianca": 0.95,
  "metodo": "ML",
  "emocao": {
    "emotion": "happy",
    "confidence": 0.82
  },
  "frame": "base64_encoded_jpeg"
}
```

### Parâmetros
| Campo | Tipo | Descrição |
|-------|------|-----------|
| letra | string | Gesto classificado (A-Z, -) |
| confianca | float | Confiança da classificação (0-1) |
| metodo | string | ML, NO_HAND, FALLBACK |
| emocao | object | Resultado de detecção emocional |
| frame | string | Frame JPEG codificado em base64 |

---

## 🖥️ Interface Web (Streamlit)

Após executar `streamlit run ui/app.py`:

- **Vídeo em tempo real** - Stream do WebSocket
- **Letra detectada** - Display e barra de confiança
- **Estado emocional** - Emoção e confiança
- **Resumo** - Panel com informações consolidadas

---

## ⚙️ Configuração

Editar `config/settings.py`:

```python
CAMERA_INDEX = 0                    # Índice da câmera
MIN_HAND_DETECTION = 0.7           # Confiança mínima detecção
MAX_HANDS = 1                      # Máximo de mãos
EMOTION_REFRESH = 10               # Frame skip detecção emoção
```

---

## ⚠️ Limitações Conhecidas

1. **Modelo não incluído** - Você deve treinar `ia/treinamento.py` com seu dataset
2. **Gestos estáticos apenas** - Não detecta movimentos contínuos (dinamismo não implementado)
3. **Dataset limitado** - Modelo treina apenas com 21 landmarks de uma mão
4. **Sem contexto linguístico** - Não compreende LIBRAS gramatical
5. **Detecção de emoção instável** - DeepFace é sensível à iluminação
6. **Engine C não ativo** - Base fornecida mas não integrada à classificação
7. **Sem persistência** - Dados de sessão não são salvos
8. **Sem logging completo** - Apenas prints no console

---

## 📝 Próximos Passos

- [ ] Treinar modelo com dataset público de LIBRAS
- [ ] Integrar engine C nativo para otimização
- [ ] Implementar detecção de sinais dinâmicos (com movimento)
- [ ] Adicionar dicionário de contexto linguístico
- [ ] Suporte a múltiplas mãos
- [ ] Logging estruturado com arquivo
- [ ] Testes unitários e integração
- [ ] Docker para deployment
- [ ] Documentação de API (OpenAPI/Swagger)

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça fork do projeto
2. Crie uma branch com sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📄 Licença

MIT License - veja LICENSE file para detalhes

---

## 📧 Contato

Para dúvidas ou sugestões, abra uma issue no repositório chame no e-mail:
matheusalmeidacarlos@gmail.com

---

**Última atualização:** 2026-07-03  
**Versão:** 0.1.0 (MVP)
