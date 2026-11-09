---
title: "Problemas de inicialização de aplicativos do Windows 10/11 e solução alternativa do Smart App Control - Innioasis Atualizador"
description: "Se o Windows 10/11 ou o Smart App Control impedirem você de iniciar o aplicativo, siga a solução alternativa aqui."
language: "pt"
source: "https://innioasis.app/notices/2026-11-07-codesigning_pt.html"
---

# Problemas de inicialização de aplicativos do Windows 10/11 e solução alternativa do Smart App Control - Innioasis Atualizador

De 25/10/2026 · até 31/12/2026 · Modelos: Y1,Y2

# Problemas de inicialização de aplicativos do Windows 10/11 e solução alternativa do Smart App Control

Se o Windows 10/11 ou o Smart App Control impedirem você de iniciar o aplicativo, siga a solução alternativa aqui.

De 25/10/2026 · até 31/12/2026 · Modelos: Y1,Y2

Relatórios falso-positivos foram enviados à Microsoft para `installer.exe` e `InnioasisUpdater.exe` e acionado, mas se o Windows Endpoint Protection ou o Smart App Control ainda estiver bloqueando o aplicativo em seu computador, use esta solução alternativa:

### Solução temporária: desative o controle de aplicativos inteligentes
  - Abra as janelas Configurações (imprensa `Win + I`).
  - Vá para Privacidade e segurança > Segurança do Windows > Controle de aplicativos e navegadores.
  - Sob Controle inteligente de aplicativos, clique Configurações de controle de aplicativos inteligentes.
  - Defina o controle de aplicativos inteligentes como Desligado. Isso permite que o aplicativo seja aberto e executado imediatamente.

Se o Windows ou Edge impedir que você baixe o Updater CE, clique em mais opções (…) então Manter > Mostrar mais > Mantenha de qualquer maneira.

### Reativando o Smart App Control

Quando as definições de falso positivo terminarem de ser atualizadas em seu computador, você poderá reativar o Smart App Control por meio do Registro do Windows:
  - Imprensa Tecla Windows + R, tipo `regedit`e pressione Enter para abrir o Editor do Registro como administrador.
  - Navegue para: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` (ou `Policies`).
  - Localizar `VerifiedAndReputablePolicyState` no painel direito.
  - Clique duas vezes `VerifiedAndReputablePolicyState` e altere seus dados de valor para:

  - `1` = Ativado (Aplicado)
  - `2` = Modo de Avaliação

  - Clique em OK, feche o Editor do Registro e reinicie o computador.

[Consulte o relatório installer.exe para a Microsoft](https://www.microsoft.com/en-us/wdsi/submission/45d25b9c-0dd6-4d01-afd2-f0ea6b224dfd)[Consulte o relatório InnioasisUpdater.exe para a Microsoft](https://www.microsoft.com/en-us/wdsi/submission/1aef842b-3fda-44e7-bcfb-1a64af3ea661)

[Abra a página vinculada](https://innioasis.app/notices.html)

[← Todos os avisos](index_pt.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
