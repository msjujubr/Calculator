# Calculadora Interativa - Programação Orientada a Eventos
![VSCode](https://img.shields.io/badge/IDE-VSCode-informational)
![ISO](https://img.shields.io/badge/ISO-Linux-blueviolet)

**Disciplina**: Linguagens de Programação

**Estudo dirigido:** [📄 Programação Orientada a Eventos](https://github.com/msjujubr/Python_Calculator/blob/main/EstudoDirigido_LP.pdf)

Este projeto consiste em uma calculadora interativa desenvolvida com **HTML, CSS e JavaScript**, cujo funcionamento é baseado no paradigma de **programação orientada a eventos**. O objetivo principal é demonstrar, na prática, como os conceitos fundamentais de eventos se relacionam em uma aplicação real, identificando:

- **Produtores de eventos** (Event Producers)
- **Event listeners** (Ouvintes de eventos)
- **Event handlers** (Manipuladores de eventos)
- O fluxo completo de comunicação entre esses elementos

## Funcionalidades

- Operações matemáticas básicas (adição, subtração, multiplicação, divisão, porcentagem e raiz)
- Suporte a entrada por mouse e teclado
- Botão de limpar (clear)
- Cálculo em tempo real
- Interface responsiva e intuitiva


## Arquitetura Baseada em Eventos

### **Produtores de Eventos (Event Producers)**
Na calculadora, os **produtores de eventos** são os elementos que geram interações detectáveis pelo sistema:

#### **a) Botões da Interface (`<button>`):**
Cada botão gera eventos de `click` quando pressionado. Inclusos:
  - Botões numéricos (0-9)
  - Botões de operadores (+, -, ×, ÷, %, √)
  - Botão de igual (=)
  - Botão de limpar (C)

#### **b) Documento HTML (`document`):**
Gera eventos de teclado (`keydown`, `keypress`). Permite controle via:
  - Teclas numéricas (0-9)
  - Operadores matemáticos (+, -, *, /)
  - `Enter` (cálculo)
  - `Backspace`/`Escape` (limpar)


### **Event Listeners**

#### **Event Listener 1 — Clique nos Botões**
```javascript
document.querySelectorAll("button").forEach(botao => {
  botao.addEventListener("click", () => {
    // Event Handler (callback) dos botões
  });
});
```
- **Elementos:** Todos os elementos `<button>`
- **Tipo de Evento:** `click`
- **Escopo:** Global para todos os botões

#### **Event Listener 2 — Eventos de Teclado**
```javascript
document.addEventListener("keydown", (evento) => {
  // Event Handler (callback) do teclado
});
```
- **Elemento:** Objeto `document`
- **Tipo de Evento:** `keydown`
- **Escopo:** Página inteira


###**Event Handlers**

Os Event Handlers obtém as informações (`data-valor` e `data-acao`) do botão clicado ou da tecla pressionada, verifica o tipo de ação solicitada, executa-a e, por fim, atualiza o display 
#### **Fluxo do Handler:**
1. **Captura de Dados:** Obtém  do botão clicado ou do teclado
2. **Validação:** Verifica o tipo de ação solicitada
3. **Processamento:**
   - Adiciona valores à expressão matemática
   - Limpa o display se necessário
   - Executa cálculo quando solicitado
4. **Atualização:** Reflete mudanças na interface do usuário


#### **Event Handler 1 — Callback dos Botões**
```javascript
  document.querySelectorAll("button").forEach(botao => {
    botao.addEventListener("click", () => {
      const valor = botao.dataset.valor;
      const acao = botao.dataset.acao;

      if (valor) {
        expressao += valor;
      }

      if (acao === "clear") {
        expressao = "";
      }

      if (acao === "equals") {
        calcular();
        return;
      }

      if (acao === "sqrt") {
        expressao = Math.sqrt(Number(expressao)).toString();
      }

      if (acao === "percent") {
        expressao = (Number(expressao) / 100).toString();
      }

      atualizarDisplay();
    });
  });
```
#### **Event Handler 1 — Callback do Teclado**

```javascript
  document.addEventListener("keydown", (e) => {
    const teclasPermitidas = "0123456789+-*/.";

    if (teclasPermitidas.includes(e.key)) {
      expressao += e.key;
    }

    if (e.key === "Enter") {
      calcular();
      return;
    }

    if (e.key === "Backspace") {
      expressao = expressao.slice(0, -1);
    }

    if (e.key === "Escape") {
      expressao = "";
    }

    atualizarDisplay();
  });
```
<div> 
  <a href="https://www.youtube.com/@msjujubr" target="_blank"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" target="_blank"></a>
  <a href="https://instagram.com/msjujubr" target="_blank"><img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" target="_blank"></a>
 	<a href="https://www.twitch.tv/msjujubr" target="_blank"><img src="https://img.shields.io/badge/Twitch-9146FF?style=for-the-badge&logo=twitch&logoColor=white" target="_blank"></a>
  <a href = "mailto:juliamourasouza10@gmail.com"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
  <a href="https://www.linkedin.com/in/msjujubr/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
</div>
