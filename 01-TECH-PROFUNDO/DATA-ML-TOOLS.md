# Ferramentas de Data Science e Machine Learning para Estudantes

## 📋 Índice
1. [GPUs e Compute Gratuitos](#gpus-e-compute-gratuitos)
2. [Plataformas MLOps](#plataformas-mlops)
3. [Notebooks e IDEs](#notebooks-e-ides)
4. [Datasets e Competições](#datasets-e-competições)
5. [Ferramentas de Visualização](#ferramentas-de-visualização)
6. [Bibliotecas e Frameworks](#bibliotecas-e-frameworks)
7. [Model Deployment](#model-deployment)

## 🖥️ GPUs e Compute Gratuitos

### Google Colab

#### Colab Free
- **GPU**: Tesla T4 ou K80
- **RAM**: 12-13 GB
- **Disco**: 108 GB
- **Tempo**: 12 horas contínuas
- **Custo**: **GRÁTIS**
- **Economia**: R$ 3.000-5.000/ano

**Limitações**:
- Não pode executar múltiplos notebooks
- Desconecta após inatividade
- GPUs podem não estar sempre disponíveis

#### Colab Pro
- **Custo Regular**: $10/mês
- **Custo Estudante**: Sem desconto oficial, mas $10 é acessível
- **GPU**: V100, A100 (priority access)
- **RAM**: Até 52 GB
- **Tempo**: 24 horas contínuas
- **Background execution**: Sim
- **Economia vs AWS**: R$ 8.000-12.000/ano

#### Colab Pro+
- **Custo**: $50/mês
- **GPU**: A100, garantia de disponibilidade
- **RAM**: Até 52 GB
- **Recommended para**: Projetos pesados de deep learning

**Setup Rápido**:
```python
# Verificar GPU disponível
!nvidia-smi

# Instalar bibliotecas
!pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Montar Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Verificar recursos
import psutil
print(f"RAM: {psutil.virtual_memory().total / (1024**3):.1f} GB")
print(f"Disco: {psutil.disk_usage('/').total / (1024**3):.1f} GB")
```

**Dicas**:
- Use `%%time` para tracking de tempo
- Salve checkpoints frequentemente no Drive
- Use `wandb` para tracking de experiments

### Kaggle Notebooks

- **GPU**: Tesla P100 (16GB VRAM)
- **TPU**: TPU v3-8 (128GB HBM)
- **Tempo**: 30 horas/semana grátis (GPU) + 30h/semana (TPU)
- **RAM**: 13 GB (GPU) / 16 GB (CPU)
- **Disco**: 73 GB temporário
- **Custo**: **GRÁTIS**
- **Economia**: R$ 5.000-8.000/ano

**Vantagens sobre Colab**:
- ✅ 30h/semana garantidas (vs 12h Colab)
- ✅ P100 é mais rápido que T4
- ✅ TPU gratuito disponível
- ✅ Datasets Kaggle pré-carregados
- ✅ Competições integradas

**Setup Rápido**:
```python
# Verificar hardware
import subprocess
print(subprocess.check_output('nvidia-smi', shell=True).decode())

# Instalar pacotes
!pip install -q wandb lightning

# Carregar dataset Kaggle
from kaggle import api
api.dataset_download_files('dataset-name', path='/kaggle/working/', unzip=True)
```

**Dicas**:
- Ative internet para usar pip install
- Use "/kaggle/input" para datasets
- Submeta para competições diretamente

### Paperspace Gradient

#### Free Tier
- **GPU**: M4000 (8GB VRAM)
- **RAM**: 30 GB
- **Tempo**: 6 horas/sessão
- **Custo**: **GRÁTIS**
- **Economia**: R$ 2.000-4.000/ano

#### Growth Plan (Estudantes)
- **Custo**: $8/mês
- **GPU**: P4000, P5000, V100
- **Tempo**: Ilimitado
- **Storage**: 200 GB

**Vantagens**:
- Interface mais profissional
- Melhor para produção
- Integração com GitHub

### Lightning AI (former Grid.ai)

- **GPU**: T4, A10
- **Tempo**: Horas grátis mensalmente
- **Custo**: Free tier generoso
- **Economia**: R$ 3.000-6.000/ano

**Vantagens**:
- Built for PyTorch Lightning
- Multi-node training
- Produção-ready

### AWS SageMaker Studio Lab

- **Compute**: 4 vCPUs, 16 GB RAM
- **GPU**: Tesla T4
- **Tempo**: 12 horas/sessão
- **Storage**: 15 GB persistente
- **Custo**: **GRÁTIS** (sem cartão de crédito!)
- **Economia**: R$ 4.000-7.000/ano

**Vantagens únicas**:
- ✅ Não precisa conta AWS
- ✅ Não precisa cartão de crédito
- ✅ Storage persistente
- ✅ Interface JupyterLab completa
- ✅ Integrado com SageMaker ecosystem

**Como obter acesso**:
1. Acesse [studiolab.sagemaker.aws](https://studiolab.sagemaker.aws/)
2. Solicite conta (aprovação geralmente em 1-3 dias)
3. Email .edu ajuda mas não é obrigatório

**Setup**:
```python
# Já vem com principais bibliotecas
import torch
import tensorflow as tf
import sklearn
import pandas as pd

# GPU check
print(torch.cuda.is_available())
```

### Microsoft Azure ML Studio

- **Compute**: Via Azure for Students
- **Créditos**: $100/ano
- **GPU**: Variável baseado em créditos
- **Economia**: R$ 3.000-6.000/ano

**Vantagens**:
- Integração com Azure ecosystem
- AutoML gratuito
- Designer visual

### Comparação de GPUs Gratuitas

| Plataforma | GPU | VRAM | Tempo/Semana | Persistência | Melhor Para |
|------------|-----|------|--------------|--------------|-------------|
| **Colab Free** | T4 | 16GB | ~12h | Não | Prototipagem rápida |
| **Kaggle** | P100 | 16GB | 30h | Não | Competições, treino |
| **SageMaker Lab** | T4 | 16GB | Ilimitado* | Sim (15GB) | Projetos longos |
| **Paperspace** | M4000 | 8GB | ~42h | Sim (5GB) | Desenvolvimento |
| **Lightning AI** | T4/A10 | 16-24GB | Variável | Sim | Produção |

*12h por sessão, mas pode abrir nova sessão

## 🔧 Plataformas MLOps

### Weights & Biases (W&B)

- **Custo**: **GRÁTIS** para uso acadêmico
- **Features**:
  - Experiment tracking ilimitado
  - Visualizações interativas
  - Hyperparameter tuning
  - Model registry
  - Dataset versioning
- **Economia**: R$ 3.000-6.000/ano

**Setup Rápido**:
```python
import wandb

# Login (uma vez)
wandb.login()

# Iniciar experimento
wandb.init(project="meu-projeto", entity="meu-time")

# Log metrics
wandb.log({"loss": 0.5, "accuracy": 0.9})

# Log artifacts
wandb.log_artifact("model.pth")
```

**Use cases**:
- Track experimentos em tempo real
- Compare múltiplos runs
- Colaboração em equipe
- Reports automáticos

### Neptune.ai

- **Custo**: **GRÁTIS** (Individual plan)
- **Limits**: 200 horas/mês tracking
- **Storage**: 100 GB
- **Economia**: R$ 2.000-4.000/ano

**Vantagens**:
- Interface muito intuitiva
- Excelente para notebooks
- Versionamento de datasets

### MLflow

- **Custo**: **GRÁTIS** (open source)
- **Deploy**: Self-hosted ou Databricks
- **Economia**: R$ 5.000-10.000/ano (vs soluções enterprise)

**Setup Local**:
```bash
pip install mlflow

# Iniciar UI
mlflow ui

# Seu código
import mlflow

with mlflow.start_run():
    mlflow.log_param("lr", 0.001)
    mlflow.log_metric("rmse", 0.85)
    mlflow.sklearn.log_model(model, "model")
```

### DVC (Data Version Control)

- **Custo**: **GRÁTIS** (open source)
- **Storage**: Use seu cloud (Google Drive, S3, etc)
- **Economia**: R$ 2.000-5.000/ano

**Setup**:
```bash
pip install dvc

# Inicializar
dvc init

# Track dataset
dvc add data/large-dataset.csv
git add data/large-dataset.csv.dvc .gitignore
git commit -m "Add dataset"

# Push para remote
dvc remote add -d storage gdrive://your-folder-id
dvc push
```

### Comet ML

- **Custo**: **GRÁTIS** (Academic)
- **Features**: Similar W&B
- **Limite**: Ilimitado para estudantes
- **Economia**: R$ 3.000-5.000/ano

**Como obter academic**:
1. Registre com email .edu
2. Ative plano academic
3. Features enterprise gratuitas

### Comparison MLOps

| Plataforma | Custo Estudante | Experiment Tracking | Dataset Versioning | Model Registry | Best For |
|------------|-----------------|---------------------|--------------------|----------------|----------|
| W&B | Grátis | ✅ Excelente | ✅ Sim | ✅ Sim | Time collaboration |
| Neptune | Grátis | ✅ Excelente | ✅ Sim | ✅ Sim | Individual/Small teams |
| MLflow | Grátis | ✅ Bom | ❌ Limitado | ✅ Sim | Self-hosted |
| DVC | Grátis | ❌ Não | ✅ Excelente | ❌ Não | Data versioning |
| Comet | Grátis | ✅ Excelente | ✅ Sim | ✅ Sim | Academic research |

## 📊 Datasets e Competições

### Kaggle

- **Datasets**: 50.000+ datasets gratuitos
- **Competições**: Prêmios até $100.000
- **Notebooks**: 30h GPU/semana
- **Courses**: Gratuitos com certificado
- **Economia**: R$ 10.000-20.000/ano (acesso a dados + compute + cursos)

**Datasets Populares**:
- ImageNet (via Kaggle API)
- COCO Dataset
- MovieLens
- Titanic (clássico)
- House Prices

**Como começar**:
```python
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

# Baixar dataset
api.dataset_download_files('paultimothymooney/chest-xray-pneumonia')

# Submeter para competição
api.competition_submit('submission.csv', 'my message', 'titanic')
```

### Hugging Face Datasets

- **Datasets**: 100.000+ datasets
- **Modelos**: 500.000+ modelos pré-treinados
- **Custo**: **GRÁTIS**
- **Economia**: R$ 15.000-30.000/ano

**Como usar**:
```python
from datasets import load_dataset

# Carregar dataset
dataset = load_dataset("squad", split="train")

# Streaming para datasets grandes
dataset = load_dataset("wikipedia", "20220301.en", streaming=True)
```

**Datasets populares**:
- GLUE, SuperGLUE (NLP benchmarks)
- ImageNet-1k
- Common Voice (speech)
- The Pile (text)

### Papers with Code

- **Datasets**: Linkados com papers
- **Benchmarks**: Leaderboards oficiais
- **Código**: Implementações oficiais
- **Custo**: **GRÁTIS**
- **Economia**: R$ 5.000-10.000/ano (tempo economizado)

### Google Dataset Search

- **Datasets**: Milhões indexados
- **Fonte**: Academia, governo, empresas
- **Custo**: **GRÁTIS**

### UCI Machine Learning Repository

- **Datasets**: 622+ datasets clássicos
- **Uso**: Acadêmico
- **Custo**: **GRÁTIS**
- **Clássicos**: Iris, Wine, Adult, MNIST

### AWS Open Data

- **Datasets**: Petabytes de dados
- **Custo**: **GRÁTIS** (sem egress fees)
- **Exemplos**: 
  - Satellite imagery
  - Genomics
  - Climate data

## 📓 Notebooks e IDEs

### JupyterLab

- **Custo**: **GRÁTIS** (open source)
- **Deploy**: Local ou cloud
- **Extensions**: Centenas disponíveis

**Setup com conda**:
```bash
conda create -n ml python=3.10
conda activate ml
conda install jupyterlab

# Extensões úteis
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter labextension install jupyterlab-plotly

jupyter lab
```

### VS Code + Jupyter Extension

- **Custo**: **GRÁTIS**
- **Vantagens**:
  - IntelliSense completo
  - Debugging avançado
  - Git integration
  - Remote development

**Extensions essenciais**:
- Python
- Jupyter
- Pylance
- GitLens

### Databricks Community Edition

- **Cluster**: 15 GB RAM
- **Storage**: Limitado
- **Custo**: **GRÁTIS**
- **Economia**: R$ 10.000-20.000/ano

**Vantagens**:
- Spark integrado
- Delta Lake
- MLflow integrado
- Colaboração em tempo real

**Limitações**:
- Cluster desliga após 2h inatividade
- 1 usuário apenas
- Recursos limitados

### DeepNote

- **Custo**: **GRÁTIS** (Education)
- **RAM**: 5 GB
- **Storage**: 5 GB
- **Colaboração**: Real-time
- **Economia**: R$ 2.000-4.000/ano

**Vantagens**:
- Interface moderna
- Integração com GCS, S3
- SQL cells
- Scheduling de notebooks

### Hex

- **Custo**: **GRÁTIS** (Community)
- **Features**:
  - SQL + Python em mesmo notebook
  - Data apps interativos
  - Version control
- **Economia**: R$ 3.000-6.000/ano

## 📈 Ferramentas de Visualização

### Plotly

- **Custo**: **GRÁTIS** (open source)
- **Chart Studio**: Grátis para públicos

```python
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
fig.show()
```

### Streamlit

- **Custo**: **GRÁTIS**
- **Deploy**: Streamlit Cloud gratuito
- **Economia**: R$ 3.000-6.000/ano

**App básico**:
```python
import streamlit as st
import pandas as pd

st.title('Meu App de ML')

uploaded_file = st.file_uploader("Escolha um CSV")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    
    if st.button('Predict'):
        predictions = model.predict(df)
        st.write(predictions)
```

### Gradio

- **Custo**: **GRÁTIS**
- **Deploy**: Hugging Face Spaces grátis
- **Economia**: R$ 2.000-4.000/ano

```python
import gradio as gr

def predict(image):
    return model(image)

demo = gr.Interface(fn=predict, inputs="image", outputs="label")
demo.launch()
```

### Dash (Plotly)

- **Custo**: **GRÁTIS** (open source)
- **Deploy**: Render.com free tier

**Melhores casos**:
- Dashboards complexos
- Aplicações enterprise-like
- Múltiplas páginas

### Tableau for Students

- **Custo**: **GRÁTIS** (1 ano renovável)
- **Full Desktop**: Sim
- **Tableau Public**: Grátis sempre
- **Economia**: R$ 4.200/ano

**Como obter**:
1. Registre com email .edu
2. [Tableau for Students](https://www.tableau.com/academic/students)
3. Download Desktop

## 🛠️ Bibliotecas e Frameworks

### PyTorch

- **Custo**: **GRÁTIS** (open source)
- **GPU**: CUDA support
- **Economia**: R$ 5.000-10.000/ano (vs implementar do zero)

**Recursos**:
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [Fast.ai](https://www.fast.ai/) - Curso grátis
- [PyTorch Lightning](https://lightning.ai/) - Produção-ready

### TensorFlow / Keras

- **Custo**: **GRÁTIS** (open source)
- **GPU**: CUDA + ROCm
- **TPU**: Gratuito via Colab

**Recursos**:
- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)
- [Keras Documentation](https://keras.io/)
- [TensorFlow Hub](https://tfhub.dev/) - Modelos pré-treinados

### Scikit-learn

- **Custo**: **GRÁTIS** (open source)
- **Use case**: ML clássico
- **Economia**: R$ 3.000-6.000/ano

**Excelente para**:
- Classification, regression
- Clustering
- Dimensionality reduction
- Pipelines

### XGBoost / LightGBM / CatBoost

- **Custo**: **GRÁTIS** (open source)
- **Use case**: Tabular data
- **Kaggle**: Dominam competições

### Transformers (Hugging Face)

- **Custo**: **GRÁTIS** (open source)
- **Modelos**: 500.000+
- **Economia**: R$ 10.000-20.000/ano

```python
from transformers import pipeline

# Text generation
generator = pipeline('text-generation', model='gpt2')
generator("Eu sou estudante e")

# Translation
translator = pipeline('translation_en_to_pt')
translator("I love machine learning")

# NER
ner = pipeline('ner', model='pierreguillou/bert-base-cased-pt-lenerbr')
ner("João mora em São Paulo")
```

## 🚀 Model Deployment

### Hugging Face Spaces

- **Custo**: **GRÁTIS** (Community)
- **GPU**: $0.60/hora (paid)
- **Frameworks**: Gradio, Streamlit, Static
- **Economia**: R$ 2.000-4.000/ano

**Deploy**:
```bash
# Criar Space no HF
# Clone localmente
git clone https://huggingface.co/spaces/username/space-name

# Adicionar app
echo "import gradio as gr..." > app.py

# Commit e push
git add app.py requirements.txt
git commit -m "Add app"
git push
```

### Streamlit Cloud

- **Custo**: **GRÁTIS**
- **Apps**: 1 app privado + ilimitados públicos
- **CPU**: 1 GB RAM
- **Economia**: R$ 2.000-4.000/ano

**Deploy**:
1. Push código para GitHub
2. Conecte Streamlit Cloud
3. Deploy automático

### Render

- **Custo**: **GRÁTIS** (free tier)
- **Limites**: 750h/mês
- **Sleep**: Após inatividade

**Bom para**:
- Flask/FastAPI apps
- Dash apps
- Background workers

### Railway

- **Custo**: $5 crédito grátis/mês
- **Deploy**: GitHub integration
- **Databases**: Postgres incluído

### Vercel

- **Custo**: **GRÁTIS** (Hobby)
- **Framework**: Next.js, SvelteKit
- **Limites**: 100 GB bandwidth/mês

**Bom para**:
- Frontend de ML apps
- APIs serverless

### Modal

- **Custo**: $30 créditos/mês grátis
- **GPU**: A10, A100 on-demand
- **Economia**: R$ 3.000-6.000/ano

**Diferencial**:
- Serverless GPU
- Escala automática
- Container-based

## 💰 Economia Total Estimada

### Por Categoria

| Categoria | Ferramentas | Economia Anual |
|-----------|-------------|----------------|
| **GPU Compute** | Colab, Kaggle, SageMaker Lab | R$ 15.000-30.000 |
| **MLOps** | W&B, Neptune, MLflow | R$ 8.000-15.000 |
| **Datasets** | Kaggle, HF, AWS Open Data | R$ 10.000-20.000 |
| **Notebooks/IDEs** | JupyterLab, Databricks, VS Code | R$ 10.000-20.000 |
| **Visualization** | Plotly, Streamlit, Tableau | R$ 7.000-14.000 |
| **Frameworks** | PyTorch, TensorFlow, Transformers | R$ 10.000-25.000 |
| **Deployment** | HF Spaces, Streamlit Cloud, Render | R$ 6.000-12.000 |

### Total Geral
**Economia Estimada: R$ 66.000-136.000 por ano**

(Comparado com pagar por serviços equivalentes enterprise)

## ✅ Checklist de Setup Completo

### Semana 1: Fundamentos
- [ ] Criar conta Kaggle e explorar datasets
- [ ] Setup Google Colab e fazer primeiro notebook
- [ ] Instalar Anaconda localmente
- [ ] Criar conta Hugging Face
- [ ] Setup W&B para experiment tracking

### Semana 2: Intermediate
- [ ] Aplicar para SageMaker Studio Lab
- [ ] Criar primeiro projeto no GitHub com DVC
- [ ] Deploy primeiro app no Streamlit Cloud
- [ ] Completar Kaggle Intro to ML course
- [ ] Participar de competição Kaggle (Titanic)

### Semana 3: Advanced
- [ ] Setup Lightning AI para treino distribuído
- [ ] Criar pipeline MLOps completo (data → train → deploy)
- [ ] Deploy modelo no Hugging Face Space
- [ ] Contribuir para projeto open source ML
- [ ] Documentar e compartilhar aprendizados

### Mês 1: Master
- [ ] Completar projeto end-to-end (problema → produção)
- [ ] Escrever blog post técnico
- [ ] Criar portfólio no GitHub
- [ ] Aplicar para estágios/posições ML
- [ ] Ensinar outros (melhores forma de aprender)

## 🎯 Dicas Profissionais

### 1. Otimize Uso de GPU Gratuitas
```python
# Libere memória GPU regularmente
import gc
import torch

def clear_memory():
    gc.collect()
    torch.cuda.empty_cache()

# Use mixed precision
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()
with autocast():
    output = model(input)
    loss = criterion(output, target)
```

### 2. Experiment Tracking desde o Início
- Sempre use W&B ou Neptune
- Track tudo: hyperparams, metrics, code version
- Compare runs facilmente
- Reprodutibilidade garantida

### 3. Versionamento de Dados
- Use DVC ou LFS
- Nunca commite dados grandes no git
- Documente origem e processamento

### 4. Code Quality
```python
# Use type hints
def train_model(data: pd.DataFrame, epochs: int = 10) -> tf.keras.Model:
    ...

# Docstrings
def preprocess(text: str) -> str:
    """
    Preprocessa texto para NLP.
    
    Args:
        text: Texto raw
        
    Returns:
        Texto limpo e tokenizado
    """
    ...

# Tests
import pytest

def test_preprocessing():
    assert preprocess("Olá!") == "olá"
```

### 5. Portfolio Building
- GitHub ReadME profissional
- Medium/Dev.to blog posts
- Kaggle notebooks públicos
- HuggingFace demos
- LinkedIn posts com resultados

## 📚 Recursos de Aprendizado

### Cursos Gratuitos
- [Fast.ai](https://www.fast.ai/) - Practical Deep Learning
- [DeepLearning.AI](https://www.deeplearning.ai/) - Coursera (audit grátis)
- [Kaggle Learn](https://www.kaggle.com/learn) - Micro-courses
- [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course)
- [MIT OpenCourseWare](https://ocw.mit.edu/) - 6.034 AI

### Livros (Gratuitos Online)
- [Dive into Deep Learning](https://d2l.ai/)
- [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/)
- [The Hundred-Page ML Book](http://themlbook.com/)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)

### Comunidades
- r/MachineLearning
- r/LearnMachineLearning
- Kaggle Forums
- Hugging Face Discord
- MLOps Community Slack

---

**Última atualização**: 2025-01-08
**Contribuidores**: Comunidade Tech Brasil
**Feedback**: Abra issue no repositório!
