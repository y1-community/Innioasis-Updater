---
title: "Primeiros passos com Innioasis Updater CE | Instale ou restaure o firmware em qualquer player Innioasis ou Timmkoo - Innioasis Updater"
description: "Baixe Innioasis Updater CE para Windows, macOS ou Linux e instale ou restaure o firmware em qualquer player Innioasis ou Timmkoo em algumas etapas guiadas."
language: "pt-PT"
source: "https://innioasis.app/guide_pt-PT.html"
---

# Primeiros passos com Innioasis Updater CE | Instale ou restaure o firmware em qualquer player Innioasis ou Timmkoo - Innioasis Updater

Início rápido

# Primeiros passos com Innioasis Atualizador CE

Funciona com todos os reprodutores de áudio Innioasis e Timmkoo. Instale Innioasis Updater CE no seu computador, escolha o modelo e o software desejado e siga as instruções.

## 

[Obtenha o atualizador CE](guide_pt-PT.html#download-updater)[Tutorial escrito completo](guide_pt-PT.html)

## Obter Innioasis Atualizador CE

Innioasis Atualizador CE é o aplicativo que instala atualizações oficiais e software comunitário no seu player. Ele mantém suas músicas e configurações e funciona em Windows, macOS e Linux.

### Windows

Baixe o instalador, execute-o e reinicie o PC quando terminar.[Obtenha motoristas](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[Descarregue o atualizador CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)

If Windows stops you from running the app or won't launch it, please open Settings, click Privacy & security → Windows Security → App & browser control, and turn Smart App Control off. Smart App Control currently impacts popular applications like the Epic Overlay Service (used by Fortnite) — Updater CE is safe and verified to use. [O Windows não inicia a aplicação? Ajuda](#smart-app-control)

Reinicie o seu PC após a instalação. A ajuda do motorista está no [Notas de configuração do Windows](drivers_pt-PT.html#windows).

### macOS[Descarregue o atualizador CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

Se o seu Mac o impedir de executar a aplicação pela primeira vez, abra as Definições do Sistema, clique em Privacidade e Segurança, desloque-se para baixo até Segurança e clique em [Abrir mesmo assim](https://support.apple.com/en-gb/102445#openanyway). Também pode premir a tecla Control (ou clicar com o botão direito) na aplicação no Finder e escolher Abrir.

Funciona em Macs Intel e Apple Silicon com macOS Monterey e posterior.

### Linux

Baixe o AppImage para sistemas Intel e AMD, torne-o executável e execute-o.[Baixe AppImage para Intel/AMD](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)

[Notas de configuração do Linux](drivers_pt-PT.html#linux)Outra plataforma?

Você precisa do seu player, um cabo de dados USB que transporta dados (um cabo somente de carga não pode ser instalado) e alguns minutos. Mantenha o cabo conectado até que Updater CE diga que está pronto.

## Escolha seu modelo e software
  - Modelo do dispositivo: escolha o modelo impresso no player, Y1 ou Y2. O software feito para um modelo não pode ser instalado no outro.
  - Software e lançamento: escolha Software Original, Rockbox, Solar, JJ Launcher, Inniclassic, Y2Player ou Koensayr quando estiver listado para o seu modelo e, em seguida, escolha uma versão. Estável é a escolha segura.
  - Instalar: clique Instalar / Restaurar, desligue o player totalmente e conecte o cabo USB somente quando Updater CE solicitar.
  - Terminar: deixe o player e o cabo sozinhos até a mensagem de sucesso, depois desconecte e ligue o player.

Y1 players fornecidos com software original antes da versão 2.0.0 precisam Dispositivo Type B. Todos os outros mantêm o padrão Type A.Instruções de conexão do atualizador para conectar um player desligadoSiga o prompt Updater CE ao vivo para o seu modelo.

## Voltando ao software original

O software personalizado é reversível. Em Updater CE, escolha seu modelo, selecione Software Original, escolha uma versão estável e execute Instalar / Restaurar da mesma maneira. Não há nada para excluir manualmente.[Y1 guia de restauração](guides/restore-original-y1.html)[Y2 guia de restauração](guides/restore-original-y2.html)

Se um flash parar antes do prompt USB, verifique primeiro o cabo, a configuração da plataforma e o modelo. Ver [solução de problemas](troubleshooting_pt-PT.html) para correções, o [Y1 e Y2 guia de recuperação](guides/recovery.html) para falhas de potência e roda, e [SP Flash Tool](sp-flash-tool_pt-PT.html) para recuperação avançada.

## Guias de software por modelo

Abra o guia do seu modelo e do software que você escolheu.

### Innioasis Y1

Software para Y1:

### Innioasis Y2

Software para Y2:

## Que ferramenta devo usar?

Este guia usa Innioasis Atualizador 2.5.1, também chamado de Updater CE. Ele mantém suas músicas, vídeos e emparelhamentos Bluetooth seguros. Ele informa quando as atualizações estão prontas. O Innioasis Universal Flash Tool limpa seu player e precisa de etapas manuais. [Compare as ferramentas →](updater-comparison_pt-PT.html)

## O Windows não inicia a aplicação? Solução alternativa para o controlo de aplicações inteligentes

Windows Defender SmartScreen or Smart App Control can block newly downloaded community applications before signature reputations propagate. Smart App Control is currently impacting popular applications like the Epic Overlay Service (used by Fortnite) — Updater CE is safe and verified to use. Turning Smart App Control off allows Updater CE to open and run normally.
  - Abrir Configurações no seu PC Windows (prima Win + I).
  - Clique Privacidade e segurança na barra lateral esquerda e clique em Windows Security.
  - Clique Controlo de aplicações e navegadores.
  - Sob Controlo inteligente de aplicativos, clique Configurações de controlo de aplicações inteligentes.
  - Defina o botão de comutação para Desligado para permitir que o Updater CE seja iniciado.

Descarregado via Edge? Se o Edge bloquear o download propriamente dito, clique no botão Mais opções (…) → Mantenha → Mostrar mais → Mantenha de qualquer maneira.

Reativando o Smart App Control posteriormente: Quando quiser reativar o Smart App Control, pode reativá-lo através do Registo do Windows em `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` configurando `VerifiedAndReputablePolicyState` para `1` (Ligado) ou `2` (Modo de avaliação) e reiniciando.

### O Windows não inicia a aplicação? Como desligar o controlo de aplicações inteligentes

Windows Defender SmartScreen or Smart App Control can block newly downloaded community applications before signature reputations propagate. Smart App Control is currently impacting popular applications like the Epic Overlay Service (used by Fortnite) — Updater CE is safe and verified to use. Turning Smart App Control off allows Updater CE to open and run normally.
  - Abrir Configurações no seu PC Windows (prima Win + I).
  - Clique Privacidade e segurança na barra lateral esquerda e clique em Windows Security.
  - Clique Controlo de aplicações e navegadores.
  - Sob Controlo inteligente de aplicativos, clique Configurações de controlo de aplicações inteligentes.
  - Defina o botão de comutação para Desligado para permitir que o Updater CE seja iniciado.

Bloqueado pelo Edge? Se o Microsoft Edge bloquear o download, clique no botão Mais opções (…) → Mantenha → Mostrar mais → Mantenha de qualquer maneira.

Reativando o Smart App Control posteriormente: Quando quiser reativar o Smart App Control, pode reativá-lo através do Registo do Windows em `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` configurando `VerifiedAndReputablePolicyState` para `1` (Ligado) ou `2` (Modo de avaliação) e reiniciando.Fechar ajuda

## Isso foi útil?

Sua resposta ajuda a melhorar este guia.Sim, achei útilAinda não[Deixe-nos saber como podemos melhorar](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
