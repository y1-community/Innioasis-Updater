---
title: "Primeiros passos com Innioasis Updater CE | Instale ou restaure o firmware em qualquer player Innioasis ou Timmkoo - Innioasis Updater"
description: "Baixe Innioasis Updater CE para Windows, macOS ou Linux e instale ou restaure o firmware em qualquer player Innioasis ou Timmkoo em algumas etapas guiadas."
language: "pt"
source: "https://innioasis.app/guide_pt.html"
---

# Primeiros passos com Innioasis Updater CE | Instale ou restaure o firmware em qualquer player Innioasis ou Timmkoo - Innioasis Updater

Início rápido

# Primeiros passos com Innioasis Updater CE

Funciona com todos os reprodutores de áudio Innioasis e Timmkoo. Instale Innioasis Updater CE no seu computador, escolha o modelo e o software desejado e siga as instruções.

## 

[Obter o Updater CE](guide_pt-BR.html#download-updater)[Tutorial escrito completo](guide_pt-BR.html)

## Obtenha Innioasis Updater CE

Innioasis Atualizador CE é o aplicativo que instala atualizações oficiais e software comunitário no seu player. Ele mantém suas músicas e configurações e funciona em Windows, macOS e Linux.

### Windows

Baixe o instalador, execute-o e reinicie o PC quando terminar.[Obtenha motoristas](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[Baixe o atualizador CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)

Se o Windows impedir que você execute o aplicativo ou não o iniciar, abra Configurações, clique em Privacidade e segurança → Segurança do Windows → Controle de aplicativos e navegadores e desative o Smart App Control. O Smart App Control atualmente afeta aplicativos populares como o Epic Overlay Service (usado pelo Fortnite) – o Updater CE é seguro e verificado para uso. [O Windows não inicia o aplicativo? Ajuda](#smart-app-control)

Reinicie o seu PC após a instalação. A ajuda do motorista está no [Notas de configuração do Windows](drivers_pt-BR.html#windows).

### macOS[Baixe o atualizador CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

Se o seu Mac impedir você de executar o aplicativo pela primeira vez, abra Ajustes do Sistema, clique em Privacidade e Segurança, role para baixo até Segurança e clique em [Abrir mesmo assim](https://support.apple.com/en-gb/102445#openanyway). Você também pode clicar com a tecla Control pressionada (ou clicar com o botão direito) no aplicativo no Finder e escolher Abrir.

Funciona em Macs Intel e Apple Silicon com macOS Monterey e posterior.

### Linux

Baixe o AppImage para sistemas Intel e AMD, torne-o executável e execute-o.[Baixe AppImage para Intel/AMD](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)

[Notas de configuração do Linux](drivers_pt-BR.html#linux)Outra plataforma?

Você precisa do seu player, um cabo de dados USB que transporta dados (um cabo somente de carga não pode ser instalado) e alguns minutos. Mantenha o cabo conectado até que Updater CE diga que está pronto.

## Escolha seu modelo e software
  - Modelo do dispositivo: escolha o modelo impresso no player, Y1 ou Y2. O software feito para um modelo não pode ser instalado no outro.
  - Software e lançamento: escolha Software Original, Rockbox, Solar, JJ Launcher, Inniclassic, Y2Player ou Koensayr quando estiver listado para o seu modelo e, em seguida, escolha uma versão. Estável é a escolha segura.
  - Instalar: clique Instalar / Restaurar, desligue o player totalmente e conecte o cabo USB somente quando Updater CE solicitar.
  - Terminar: deixe o player e o cabo sozinhos até a mensagem de sucesso, depois desconecte e ligue o player.

Y1 players fornecidos com software original antes da versão 2.0.0 precisam Dispositivo Type B. Todos os outros mantêm o padrão Type A.Instruções de conexão do atualizador para conectar um player desligadoSiga o prompt Updater CE ao vivo para o seu modelo.

## Voltando ao software original

O software personalizado é reversível. Em Updater CE, escolha seu modelo, selecione Software original, escolha uma versão estável e execute Instalar / Restaurar da mesma maneira. Não há nada para excluir manualmente.[Guia de restauração Y1](guides/restore-original-y1.html)[Guia de restauração Y2](guides/restore-original-y2.html)

Se um flash parar antes do prompt USB, verifique primeiro o cabo, a configuração da plataforma e o modelo. Ver [solução de problemas](troubleshooting_pt-BR.html) para correções, o [Y1 e Y2 guia de recuperação](guides/recovery.html) para falhas de potência e roda, e [SP Flash Tool](sp-flash-tool_pt-BR.html) para recuperação avançada.

## Guias de software por modelo

Abra o guia do seu modelo e do software que você escolheu.

### Innioasis Y1

Software para Y1:

### Innioasis Y2

Software para Y2:

## Qual ferramenta devo usar?

Este guia usa Innioasis Updater 2.5.1, também chamado de Updater CE. Ele mantém suas músicas, vídeos e emparelhamentos Bluetooth seguros. Ele informa quando as atualizações estão prontas. O Innioasis Universal Flash Tool limpa seu player e precisa de etapas manuais. [Compare as ferramentas →](updater-comparison_pt-BR.html)

## Windows won't launch the app? Smart App Control workaround

O Windows Defender SmartScreen ou o Smart App Control podem bloquear aplicativos da comunidade recém-baixados antes que a reputação da assinatura se propague. O Smart App Control está atualmente impactando aplicativos populares como o Epic Overlay Service (usado pelo Fortnite) – o Updater CE é seguro e verificado para uso. Desligar o Smart App Control permite que o Updater CE abra e execute normalmente.
  - Abrir Configurações on your Windows PC (press Win + I).
  - Clique Privacy & security in the left sidebar, then click Windows Security.
  - Clique App & browser control.
  - Sob Smart App Control, click Smart App Control settings.
  - Set the toggle to Desligado to allow Updater CE to launch.

Downloaded via Edge? If Edge blocks the download itself, click the More options button (…) → Keep → Show more → Keep anyway.

Re-enabling Smart App Control later: When you want to turn Smart App Control back on, you can re-enable it via the Windows Registry under `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` by setting `VerifiedAndReputablePolicyState` para `1` (On) or `2` (Evaluation Mode) and restarting.

### Windows won't launch the app? How to turn off Smart App Control

O Windows Defender SmartScreen ou o Smart App Control podem bloquear aplicativos da comunidade recém-baixados antes que a reputação da assinatura se propague. O Smart App Control está atualmente impactando aplicativos populares como o Epic Overlay Service (usado pelo Fortnite) – o Updater CE é seguro e verificado para uso. Desligar o Smart App Control permite que o Updater CE abra e execute normalmente.
  - Abrir Configurações on your Windows PC (press Win + I).
  - Clique Privacy & security in the left sidebar, then click Windows Security.
  - Clique App & browser control.
  - Sob Smart App Control, click Smart App Control settings.
  - Set the toggle to Desligado to allow Updater CE to launch.

Bloqueado pelo Edge? If Microsoft Edge blocks the download itself, click the More options button (…) → Keep → Show more → Keep anyway.

Re-enabling Smart App Control later: When you want to turn Smart App Control back on, you can re-enable it via the Windows Registry under `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` by setting `VerifiedAndReputablePolicyState` para `1` (On) or `2` (Evaluation Mode) and restarting.Close help

## Isso foi útil?

Sua resposta ajuda a melhorar este guia.Sim, achei útilAinda não[Deixe-nos saber como podemos melhorar](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
