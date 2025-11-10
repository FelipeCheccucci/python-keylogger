🧠 Keylogger Educacional em Python (README.md)
🚨 Aviso Importante: Uso Ético e Legal
Este projeto é estritamente educacional. O código demonstra o funcionamento básico de um keylogger (ferramenta de registro de teclado) com o único propósito de ensinar conceitos práticos de segurança digital, análise de software e programação em Python.

É proibido utilizá-lo para qualquer fim malicioso, ilegal, não autorizado ou que viole a privacidade de terceiros. O autor não se responsabiliza pelo uso indevido deste software.

✨ Propósito
O objetivo é que você compreenda como um keylogger funciona em um nível fundamental, permitindo a análise de vulnerabilidades e a criação de defesas contra esse tipo de ferramenta.

⚙️ Instalação e Execução
Para rodar este keylogger educacional, siga os passos abaixo:

1. Pré-requisitos
Certifique-se de ter o Python instalado em sua máquina.

2. Configuração do Projeto
Clone o repositório ou baixe o arquivo main.py para o seu diretório de trabalho.

3. Instalação da Dependência
Este script utiliza a biblioteca keyboard do Python. Instale-a usando o pip:

Bash

pip install keyboard
4. Execução
Execute o script a partir do terminal:

Bash

python main.py
Você verá uma confirmação no console. Siga a instrução para iniciar a captura.

5. Encerramento
Para parar de registrar as teclas, pressione a tecla Esc.

📝 Resultados
Após a execução, um arquivo chamado log.txt será criado (ou atualizado) no mesmo diretório do script, contendo todas as entradas de teclado registradas durante o período de execução.

🧩 Limitações Técnicas (Didáticas)
Este projeto foi mantido propositalmente simples para focar no princípio de funcionamento:

Tratamento Básico de Backspace: A remoção de caracteres (via backspace) é feita de forma rudimentar (lê o log, remove o último caractere e reescreve o arquivo), não cobrindo cenários complexos (como remoção de múltiplas linhas ou comandos especiais).

Foco Didático: Não inclui funcionalidades avançadas de produção como criptografia de logs, rotação de arquivos, mecanismos de persistência (manter-se rodando após o reboot), ou autenticação.

Uso em Ambiente Controlado: Este código deve ser executado apenas em ambientes de teste controlados e de sua propriedade, com total ciência e consentimento de quem estiver utilizando o teclado.

🤝 Contribuições
Este repositório é um ponto de partida. Sinta-se à vontade para explorar, modificar e aprimorar o código para fins de aprendizado e demonstração de segurança.
