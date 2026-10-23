# Portfólio de estudos em programação

Repositório organizado com exercícios e pequenos projetos desenvolvidos durante
os estudos de Python, Java e desenvolvimento web. Os nomes originais dos
exercícios de aula foram mantidos para facilitar a consulta ao material.

## Estrutura

```text
assets/
  images/                         Imagens usadas pelos projetos
exercicios/
  java/                           Exercício de média ponderada em Java
  python/
    fundamentos/                  Exercícios de aula (fp_aula e pp_aula)
    mini_projetos/                Exercícios práticos de interface e lógica
projetos/
  python/
    automacao/                    Monitor de preços com alerta no Telegram
    dados/                        Planilha de demonstração
    desktop/                      Aplicativos gráficos em Python
  web/
    loja_virtual/                 Página demonstrativa em HTML e CSS
requirements.txt                  Dependências Python dos projetos
```

## O que os projetos demonstram

- **Fundamentos de Python:** entrada e saída, variáveis, condicionais, laços,
  funções, listas e consumo de APIs.
- **Aplicativos desktop:** interfaces com CustomTkinter, calculadora de IMC,
  calculadora de médias, análise de planilhas e visualização de dados.
- **Pokédex:** interface gráfica, requisições HTTP, JSON, imagens e tarefas em
  segundo plano usando a PokéAPI.
- **Automação:** leitura de preços com Selenium e envio de notificações pelo
  Telegram.
- **Java:** entrada de dados, validação, listas, registros e média ponderada.
- **Web:** estrutura HTML, estilos CSS e apresentação de produtos.

## Como executar

Use Python 3 e, de preferência, crie um ambiente virtual na raiz do repositório:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Exemplos de execução a partir da raiz:

```powershell
python projetos\python\desktop\central_de_ferramentas.py
python projetos\python\desktop\calculadora_imc.py
python projetos\python\desktop\calculadora_media.py
python projetos\python\desktop\pokedex.py
```

Alguns exercícios podem ser executados diretamente com `python` seguido do
caminho do arquivo. Os aplicativos que consultam serviços externos precisam de
conexão com a internet. A central de ferramentas inclui análise de planilhas;
para experimentar, informe o caminho
`projetos\python\dados\vendas.xlsx` no campo correspondente.

### Alerta de preços do Telegram

O alerta precisa de um token de bot e do identificador do chat configurados no
ambiente. No PowerShell, defina-os antes de executar:

```powershell
$env:TELEGRAM_BOT_TOKEN = "seu-token"
$env:TELEGRAM_CHAT_ID = "seu-chat-id"
python projetos\python\automacao\alerta_precos.py
```

Não coloque tokens, senhas ou chaves de API nos arquivos do projeto. O monitor
usa Selenium e pode precisar de um navegador compatível instalado.

### Exercício Java

Com um JDK 17 ou superior:

```powershell
New-Item -ItemType Directory -Force build
javac -encoding UTF-8 -d build exercicios\java\CalculadoraNotas.java
java -cp build CalculadoraNotas
```

### Página web

Abra `projetos\web\loja_virtual\index.html` em um navegador. Os botões são
apenas demonstrativos; não há integração de pagamentos ou backend.

## Observações

- Os exercícios são registros de aprendizado e não pretendem ser sistemas de
  produção.
- APIs e sites externos podem mudar, limitar requisições ou ficar indisponíveis.
- A planilha incluída serve como exemplo para as funções de análise.
- Arquivos duplicados, temporários, gerados por compilação, exemplos incompletos
  e material com dados/segredos embutidos foram excluídos desta organização.
