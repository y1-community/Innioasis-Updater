---
title: "Correção do auxiliar Innioasis Updater e Y1 com uma instalação limpa - Innioasis Updater"
description: "Instalação limpa passo a passo para Innioasis Updater e o Y1 Helper: remova os arquivos restantes, reinstale e volte ao firmware atualizado."
language: "pt"
source: "https://innioasis.app/Troubleshooting/clean_install_pt.html"
---

# Correção do auxiliar Innioasis Updater e Y1 com uma instalação limpa - Innioasis Updater

## Confirme que você precisa de uma instalação limpa

A reinstalação manual é recomendada quando você observar algum dos seguintes sintomas:
  - O atualizador leva alguns minutos para iniciar ou trava durante a verificação de atualizações.
  - As atualizações param de chegar mesmo que existam versões mais recentes.
  - As atualizações de firmware do dispositivo não são baixadas ou aplicadas, mesmo que estejam disponíveis.
  - Você pulou vários lançamentos e não usa o atualizador há muito tempo.

## Windows: execute uma reinstalação limpa

Use o instalador oficial do Windows para atualizar o Updater no Windows 10 ou Windows 11 (64 bits). Isso substitui totalmente as compilações mais antigas e restaura o canal de autoatualização.

Antes de executar o instalador, abra Configurações › Aplicativos › Aplicativos instalados (ou o legado Adicionar/remover programas painel) e desinstale qualquer cópia existente de Innioasis Updater. Começar limpo evita conflitos de arquivos.[ Baixe o instalador limpo para Windows ](https://github.com/y1-community/supplemental-apks/releases/download/1.0/installer.exe)Passo 1

### Baixe o instalador mais recente

Salve o instalador na pasta Downloads. Feche Innioasis Updater se estiver em execução.Etapa 2

### Remova qualquer instalação existente

Abrir Configurações › Aplicativos › Aplicativos instalados (ou o legado Painel de controle › Adicionar/remover programas) e desinstale Innioasis Updater para que a reinstalação comece do zero.Etapa 3

### Instalar e reiniciar

Execute o instalador que você baixou – o Windows solicitará permissão. Quando a configuração terminar, inicie Innioasis Updater; agora ele deve detectar 1.8.2.8 automaticamente e obter atualizações novamente.

 Isso também corrige inicializações lentas e faz com que o Updater busque novamente versões de firmware diretamente dos desenvolvedores. 

## macOS: atualize com o instalador DMG

O instalador do macOS limpa os arquivos antigos e instala o 1.8.2.8.[ Baixar Innioasis Updater DMG ](https://github.com/y1-community/supplemental-apks/releases/download/1.0/Innioasis.Updater.for.Mac.dmg)
  - Abra o DMG baixado e expanda a janela do Finder para ver o Reinstale opção.
  - Execute o comando Reinstalar para atualizar a cópia existente do Updater. Isso remove arquivos auxiliares mais antigos que podem bloquear novos recursos.
  - Inicie Innioasis Updater novamente em Aplicativos. Confirme a versão das listas do painel Sobre 1.8.2.8.
 Se você vir “Innioasis Updater não pode ser aberto” após a reinstalação, vá para Configurações do sistema › Privacidade e segurança e escolha Abrir mesmo assim para aprovar o aplicativo. 

## Depois de atualizar para 1.8.2.8

Quando estiver na versão mais recente, você terá acesso aos recursos abaixo. Eles estão disponíveis apenas nas compilações atuais.
  - Instalações com um clique para firmware original, versões da comunidade e compilações Rockbox baixadas diretamente das versões dos desenvolvedores.
  - Etapas guiadas claras que informam quando conectar o player e quando é seguro desconectá-lo.
  - Melhorias gerais de estabilidade e tempos de lançamento dramaticamente mais rápidos em ambas as plataformas.

 Precisa de ajuda para verificar sua versão? Abra Innioasis Updater, escolha Ajuda › Sobree confirme os shows de compilação 1.8.2.8. 

## Ainda precisa de ajuda?

Se a instalação limpa falhar, capture todas as mensagens de erro e entre em contato com os canais de suporte da comunidade Innioasis. Inclua a versão do seu sistema operacional, a versão do atualizador (se disponível) e as etapas que você já tentou.

Manter sua instalação atualizada garante que você sempre receba os pacotes e ferramentas de firmware mais recentes à medida que são implementados.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
