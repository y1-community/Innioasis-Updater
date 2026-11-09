---
title: "Guia de instalação de firmware e restauração de estoque | Innioasis Updater CE - Innioasis Downloads de firmware"
description: "Instale o firmware personalizado ou restaure o firmware oficial de fábrica em Innioasis Y1, Y2, G1, G3, G5, R1, PR1 e Timmkoo Q5, Q3 com Innioasis Updater CE."
language: "pt-PT"
source: "https://innioasis.app/firmware-guide_pt-PT.html"
---

# Guia de instalação de firmware e restauração de estoque | Innioasis Updater CE - Innioasis Downloads de firmware

Guia de instalação de firmware e restauração de estoque

# Instale ou restaure o firmware no seu dispositivo

Escolha o modelo impresso no seu player. Em seguida, siga as etapas em Updater CE. Ele cuida do resto.[Obtenha o atualizador CE](guide_pt-PT.html#platform)[Navegar no arquivo de firmware](firmware_pt-PT.html)[Solução de problemas](troubleshooting_pt-PT.html)

Escolha o modelo impresso no seu player e o software desejado e abra este guia. [Procure software e firmware de estoque por modelo](firmware_pt-PT.html).

## 

[Obtenha o atualizador CE](guide_pt-PT.html#download-updater)[Tutorial escrito completo](guide_pt-PT.html)

## Obter Innioasis Atualizador CE

Veja por onde começar se você ainda não tiver Updater CE.Comece Updater CEcom instalação guiada

### Windows

Baixe o instalador, abra-o e siga as instruções de configuração.[Baixe e instale o driver](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[Baixe aplicativos e drivers](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)[Bloqueado pelo Edge?](#)

Se o Windows o impedir de executar a aplicação ou não a iniciar, abra as Definições, clique em Privacidade e segurança → Segurança do Windows → Controlo de aplicações e navegadores e desative o Smart App Control. [O Windows não inicia a aplicação? Ajuda](#smart-app-control)

Você precisará reiniciar o PC após a instalação para que funcione.

### macOS

Baixe o aplicativo e mova-o para Aplicativos. Se o macOS bloquear, abra Configurações do sistema, depois Privacidade e segurança e clique em Abrir assim mesmo. [Como isso funciona](https://support.apple.com/en-gb/102445#openanyway)[Descarregue o atualizador CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

### Linux

Baixe o AppImage para sistemas Intel e AMD, torne-o executável e execute-o.[Baixe AppImage para Intel/AMD](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)[Notas de configuração do Linux](drivers_pt-PT.html#linux)Outra plataforma?

Precisa de notas mais longas sobre configuração do computador? Abra o [Windows](drivers_pt-PT.html#windows) ou [Linux](drivers_pt-PT.html#linux) guia de configuração.

## Voltando ao software original

Para voltar, escolha seu modelo, escolha Software Original, então execute Instalar / Restaurar. Isso é tudo. O Updater substitui o software do sistema para você.[Y1 guia de restauração](guides/restore-original-y1.html)[Y2 guia de restauração](guides/restore-original-y2.html)

## Guias de software por modelo

Escolha o seu modelo e abra o guia do seu software.

### Innioasis Y1

Software para Y1:

### Innioasis Y2

Software para Y2:

Uma nota sobre as duas ferramentas

## Que ferramenta devo usar?

Innioasis Atualizador CE é a maneira mais segura de atualizar seu player. Ele mantém suas músicas, vídeos e emparelhamentos Bluetooth. Ele informa quando as atualizações estão prontas. Ele roda em Windows, macOS e Linux. O Innioasis Universal Flash Tool limpa seu player e funciona em menos computadores.[Abra a comparação completa](updater-comparison_pt-PT.html)

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
