---
title: "Innioasis Y1 e Y2 USB condutores | Driver do Windows e permissões do Linux - Innioasis Updater"
description: "Configure seu computador para Innioasis Updater: driver do Windows MediaTek e permissões do Linux USB — além de correções de cabos e temporização."
language: "pt"
source: "https://innioasis.app/drivers_pt.html"
---

# Innioasis Y1 e Y2 USB condutores | Driver do Windows e permissões do Linux - Innioasis Updater

Configuração do computador

# Prepare o computador antes do jogador.

A maioria dos problemas de conexão vem do driver, permissões, cabo ou tempo. O Windows precisa do driver MediaTek instalado. O Linux precisa das permissões USB corretas. Encontre sua plataforma abaixo.[Obter o Updater CE](guide_pt-BR.html#platform)[Solução de problemas](troubleshooting_pt-BR.html)

## Windows
  - Baixe o instalador do driver MediaTek abaixo.
  - Execute o instalador e permita que o Windows instale o driver.
  - Reinicie o computador.
  - Abra Updater CE e aguarde o prompt de conexão antes de conectar o player desligado.

Alguns sistemas Windows bloqueiam o driver por meio do isolamento do núcleo (integridade da memória). Se Updater CE ainda não conseguir ver o player após a reinicialização, desative a integridade da memória na Segurança do Windows, reinicie e reinstale o driver. Ative a configuração novamente quando terminar, se o seu sistema permitir.

Windows won't launch the app? Se a Segurança do Windows ou o Controle Inteligente de Aplicativos impedir a abertura do Updater CE, abra Configurações (press Win + I) → Privacy & security → Windows Security → App & browser control → Smart App Control settings and set it to Desligado. O Controle Inteligente de Aplicativos está atualmente afetando aplicativos populares como o Epic Overlay Service (usado pelo Fortnite) — o Updater CE é seguro e verificado. Para reativar mais tarde, defina `VerifiedAndReputablePolicyState` para `1` (On) or `2` (Evaluation Mode) under `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` no Editor do Registro.[Baixe o driver do Windows](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[Voltar ao guia principal](guide_pt-BR.html#windows) · [Downloads de software](firmware_pt-BR.html)

## Permissões USB do Linux

O Linux precisa que sua conta de usuário tenha permissão para se comunicar com o chip MediaTek USB dentro do player. Updater CE geralmente resolve isso durante a instalação, e a mesma permissão cobre SP Flash Tool, então trate isso como uma etapa de correção em vez de um estágio normal.
  - Execute Updater CE como usuário normal, não como root. O instalador solicita acesso de administrador somente quando necessário.
  - Verifique se o jogador é visto. Desligue o player, conecte o cabo e execute o comando lsusb em um terminal. Um player conectado aparece como um dispositivo MediaTek com o ID do fornecedor 0e8d.
`lsusb`
  - Se aparecer em lsusb, mas Innioasis Updater CE ou SP Flash Tool disser permissão negada ou não puder abrir a porta, seu usuário não terá acesso ao dispositivo USB. A mesma regra do udev cobre ambas as ferramentas, então adicione uma que permita ao grupo de usuários lê-la.
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

Salve essa linha em um novo arquivo chamado /etc/udev/rules.d/51-innioasis.rules e execute:`sudo udevadm control --reload && sudo udevadm trigger`
  - Desconecte totalmente o player, conecte-o novamente e tente instalar novamente.
  - Se SP Flash Tool relatar uma permissão serial ou disputa de porta, desconecte totalmente e reconecte somente quando solicitado.
Não improvise compensações de flash.Se você mudar para uma ferramenta de recuperação manual, use os arquivos e a configuração específica do modelo fornecidos com o projeto.

[Voltar ao guia principal](guide_pt-BR.html#linux) · [Downloads de software](firmware_pt-BR.html) · [SP Flash Tool guia](sp-flash-tool_pt-BR.html)

## Cabo e tempo
  - Use um cabo de dados USB conhecido.
  - Evite hubs durante a solução de problemas.
  - Desligue totalmente o modelo correto.
  - Conecte-se apenas quando solicitado.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
