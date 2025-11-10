# 🧠 Keylogger Educacional em Python

> ⚠️ **Aviso Importante — Uso Ético e Legal**  
> Este projeto é estritamente **educacional**.  
> O código demonstra o funcionamento básico de um keylogger (ferramenta de registro de teclado) com o único propósito de ensinar conceitos práticos de segurança digital, análise de software e programação em Python.  
>  
> É **proibido** utilizá-lo para qualquer fim malicioso, ilegal, não autorizado ou que viole a privacidade de terceiros.  
> O autor **não se responsabiliza** por qualquer uso indevido deste software.

---

## ✨ Propósito

O objetivo deste projeto é permitir que você compreenda como um keylogger funciona em um nível fundamental, facilitando o entendimento de vulnerabilidades e o desenvolvimento de defesas contra esse tipo de ferramenta.

---

## ⚙️ Instalação e Execução

### 1. Pré-requisitos
- Tenha o **Python 3.x** instalado em sua máquina.

### 2. Configuração do Projeto
Clone o repositório ou baixe o arquivo `main.py` para o seu diretório de trabalho:

```bash
git clone <url-do-repositorio>
# ou apenas baixe main.py
```

### 3. Instalação da Dependência
Esse script utiliza a biblioteca keyboard. Instale-a usando o pip:

```bash
pip install keyboard
```
💡 Em alguns sistemas operacionais, pode ser necessário executar o terminal como administrador para permitir a captura de teclas.

### 4. Execução
Execute o script a partir do terminal:

```bash
python main.py
```
Você verá uma confirmação no console.
Siga as instruções para iniciar a captura de teclas.

### 5. Encerramento
Para parar de registrar as teclas, pressione a tecla Esc.

## 📝 Resultados 
Após a execução, um arquivo chamado log.txt será criado (ou atualizado) no mesmo diretório do script.
Ele conterá todas as entradas de teclado registradas durante o período de execução.

## 🤝 Contribuições
Contribuições são bem-vindas desde que sigam o propósito educacional e as normas éticas. Sinta-se à vontade para abrir issues ou pull requests com melhorias para fins de aprendizado (ex.: tratamento mais robusto de backspace para ambientes de teste, comentários explicativos no código, ou módulos que demonstrem técnicas de detecção/mitigação).
