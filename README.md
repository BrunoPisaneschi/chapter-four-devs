# chapter-four-devs
Projeto destinado a exemplificar a contextualizar sobre o uso do selenium, usando o site 4devs como exemplo

## Pré-Requisito
Para que o código funcione, o selenium exige que exista um driver (navegador), para que ele possa controlar.<br>
No projeto em questão, foi utilizado o chromedriver (driver do google chrome), onde você deve fazer o download do seu sistema operacional e versão do chrome, nesse [link](https://chromedriver.chromium.org/downloads).

## Instalação

O projeto, foi desenvolvido, de modo que é um instalável, para facilitar a execução e demonstração.<br>
Para instalar, basta criar uma venv (caso não crie, será instalado no seu python global), e executar o comando `pip install 4devs`.

## Como executar

Para executar, basta dentro da venv que foi instalado o projeto, executar o comando `4devs` e os argumentos que desejar.

## Argumentos

Digitando `4devs --help`, será exibida a lista de argumentos possíveis e o que esperá que seja enviado para cada um, sendo eles:

- `4devs -O` Retorna uma lista com as opcões de eventos para escolher.
- `4devs -o <número-da-opcao-desejada>` Espera um número, da opção desejada, para que possa realizar o fluxo utilizando selenium.