---
title: "Configuração de Wi-Fi, Bluetooth e rádio FM para Reborn (Y2Linux) - Innioasis Updater"
description: "Breve guia pós-instalação para Reborn (Y2Linux / Y2Reborn) em Innioasis Y2: copie system.img e configure Wi-Fi, Bluetooth e rádio FM."
language: "pt"
source: "https://innioasis.app/y2reborn_wifibt_pt.html"
---

# Configuração de Wi-Fi, Bluetooth e rádio FM para Reborn (Y2Linux) - Innioasis Updater

Innioasis Y2 · Reborn Pós-instalação

# Configure Wi-Fi, Bluetooth e rádio FM.

Copie um arquivo para o seu player. Reborn cuida do resto.[Baixe system.img (860 MB)](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)[Guia de instalação](guides/reborn-y2linux-y2.html)[Por que Y2Reborn?](reborn-y2linux-benefits_pt-BR.html)

## Por que esse arquivo?

Wi-Fi, Bluetooth e rádio FM precisam de cinco módulos de firmware MediaTek que Reborn não podem ser fornecidos. Eles estão dentro do oficial Y2 `system.img`. Reborn extrai-os uma vez, verifica-os e exclui o arquivo.

## Configurar
  - Baixar sistema.img

Baixe o FM v3.2.0 `system.img` para o seu computador.[ Baixar sistema.img ](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)
  - Inicialize Reborn uma vez

Ligue o reprodutor. Espere por Configurando armazenamento para terminar e reinicie-o uma vez.
  - Conecte-se ao seu computador

Use um cabo de dados USB. O jogador aparece como Armazenamento Interno.Em um Mac?

Instalar [OpenMTP](https://openmtp.ganeshrvel.com/) para navegar no player. Windows e Linux montam-no automaticamente.
  - Copie system.img para firmware

Crie uma pasta chamada `Firmware` na raiz do armazenamento interno. Cópia `system.img` nisso.
  - Aguarde a conclusão da configuração

Reborn instala o firmware do rádio automaticamente e exclui `system.img`. Isso leva cerca de 10 a 20 segundos. Espere por Wi-Fi e Bluetooth estão prontos.
  - Conecte Wi-Fi, Bluetooth e rádio FM
    - Wi-fi: Configurações → Sistema → Rede → Wi-Fi. Escolha sua rede de 2,4 GHz.
    - Bluetooth: Coloque seus fones de ouvido no modo de emparelhamento. Configurações → Bluetooth → selecione-os.
    - Rádio FM: Conecte fones de ouvido com fio como antena e abra o Rádio FM.

  - Atualizar por Wi-Fi

As atualizações futuras Reborn são instaladas em Configurações → Sistema → Atualização de software. O firmware do seu rádio permanece estável.

## Este guia foi útil?

Você achou este guia de configuração pós-instalação útil? Sim, ajudou! [ Precisa de ajuda em Discord ](https://discord.gg/zHrT2zrcek) Obrigado pelo seu feedback! Aproveite sua audição sem fio em Y2Reborn.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
