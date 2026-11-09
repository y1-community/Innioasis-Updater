---
title: "SP Flash Tool para Innioasis e Timmkoo jogadores"
description: "Encontre SP Flash Tool empacotado com Innioasis Updater no Windows e Linux, extraia rom.zip ou rom_y2.zip e atualize um Innioasis Y1 ou Y2 com o arquivo scatter correspondente."
language: "pt-br"
source: "https://innioasis.app/sp-flash-tool_pt-br.html"
---

# SP Flash Tool para Innioasis e Timmkoo jogadores

Piscando manualmente

# Ferramenta Flash para Innioasis e Timmkoo jogadores

SP Flash Tool vem dentro de Innioasis Updater em [Windows](drivers_pt-BR.html#windows) e [Linux](drivers_pt-BR.html#linux). Você já tem isso. Este guia mostra a maneira segura de usá-lo em um Innioasis Y1 ou Y2, e a rota do Updater para Timmkoo jogadores.[Retornar ao guia do atualizador](guide_pt-BR.html)[Downloads de firmware](firmware_pt-BR.html)[Solução de problemas](troubleshooting_pt-BR.html)

Comece com Innioasis Atualizador

## O atualizador faz todo o trabalho de uma só vez

O Updater faz a maioria das instalações de uma só vez. Escolha o software, siga as etapas e pronto. Ele também informa quando uma correção ou um novo lançamento chega. SP Flash Tool está dentro do Updater's Toolkit para os raros casos em que o Updater não consegue terminar. As etapas abaixo são a exceção.

## Para que serve esta ferramenta

O atualizador atualiza o player para você. SP Flash Tool é o mesmo motor, sem guarda-corpos. Use-o quando o Updater não iniciar, quando o player não se conectar ou quando você souber como lidar com um arquivo scatter.Experimente o Atualizador primeiro. Para a maioria das instalações e recuperações, o guiado [Rota do atualizador](guide_pt-BR.html) é a escolha mais segura. Use SP Flash Tool quando souber por que precisa dele e mantenha uma bateria carregada e um cabo de dados USB prontos.

## Ferramenta Flash para Innioasis jogadores

Innioasis Updater é a ferramenta flash para Innioasis jogadores. Ele instala software oficial, atualiza e restaura pacotes por meio do fluxo correspondente ao modelo e mantém suas músicas e configurações.

### Innioasis Y1 ferramenta flash

Escolha a versão Y1 no Updater e conecte o player desligado quando o aplicativo solicitar. Os mesmos pacotes Y1 funcionam com SP Flash Tool quando você precisa da rota manual.

### Innioasis Y2 ferramenta flash

Escolha um lançamento listado para Y2. Os pacotes Y2 não são intercambiáveis ​​com os pacotes Y1, portanto verifique o modelo antes de começar.

## Ferramenta Flash para Timmkoo jogadores

Timmkoo jogadores usam o mesmo fluxo de instalação do Atualizador. Ele lê os pacotes ZIP e RAR do Timmkoo diretamente, então você não precisa de uma ferramenta flash separada ou arquivo scatter.

### Timmkoo Q5 ferramenta flash

Selecione o modelo Q5 no Updater, escolha o pacote Timmkoo, execute Instalar / Restaurar e conecte o player no prompt.

### Timmkoo Q3 e Q3E ferramenta flash

A entrada Q3 abrange Q3 e Q3E igualmente. O atualizador seleciona os arquivos correspondentes do pacote que o projeto publica.

### Timmkoo A5 ferramenta flash

Selecione o modelo A5 antes de escolher um pacote e siga o mesmo prompt de instalação.

## Onde o Updater coloca

SP Flash Tool vem com a pasta de instalação do Updater, não como um download separado. Abra-o a partir daí quando precisar.

### Windows

Abra a pasta de instalação do Updater e execute `flash_tool.exe`. A pasta geralmente está em `%LOCALAPPDATA%\Innioasis Updater`. Uma pasta Toolkit com um atalho SP Flash Tool está incluída em algumas configurações.

### Linux

Execute o pacote `flash_tool` binário dentro da pasta do aplicativo Updater em x86/x86_64. O instalador do projeto prepara USB permissões com regras do udev, então o player deve aparecer quando conectado.

### macOS

SP Flash Tool não está incluído no macOS. O atualizador usa a rota MTKClient lá. Use o [instalação guiada](guide_pt-BR.html) em um Mac e mantenha SP Flash Tool para uma máquina Windows ou Linux.

A ferramenta é fornecida com o agente de download MediaTek e configuração específica do modelo, portanto, você não precisa coletar DA ou espalhar arquivos de outro lugar.

## Prepare o firmware
  - Pegue o lançamento que você deseja [Downloads de firmware](firmware_pt-BR.html). Escolher `rom.zip` para um Y1 ou `rom_y2.zip` para um Y2.
  - Extraia o ZIP em sua própria pasta. O Windows pode usar Extrair tudo. No Linux, use seu gerenciador de arquivos ou `unzip` em um terminal.
  - Verifique se o arquivo scatter está na pasta extraída. Geralmente é nomeado `MT6572_Android_scatter.txt` para Y1 pacotes e `MT6582_Android_scatter_def.txt` para pacotes Y2, embora um lançamento possa nomeá-lo com o nome de seu projeto.
Mantenha os modelos separados. A dispersão Y1 descreve um dispositivo MT6572 e a dispersão Y2 descreve um dispositivo MT6582. Piscar com o errado é como os jogadores ficam bloqueados. Se a dispersão dentro do ZIP não corresponder ao seu modelo, pare e use um pacote listado para o seu modelo.

## Carregue a dispersão e o flash
  - Abra SP Flash Tool na pasta de instalação do Updater.
  - Na guia Download, clique em Escolher ao lado de Arquivo de carregamento disperso e selecione o arquivo disperso da pasta extraída. A lista de partições será preenchida.
  - Deixe o modo flash ativado Baixar apenas a menos que você esteja deliberadamente fazendo uma recuperação completa, o que precisa Atualização de Firmware.
  - Clique Baixar. A ferramenta irá esperar pelo jogador.
  - Power the player fully off, then connect the USB data cable. Coloque o player no chão e não o mova.
  - Aguarde a marca de seleção verde. Só então desconecte o cabo e ligue o player.

Mantenha as mesmas USB regras de tempo e cabo da rota guiada: um cabo de dados, sem hub, e conecte somente quando a ferramenta estiver pronta.

## Se não piscar
  - Verifique se o scatter e o ZIP correspondem ao modelo impresso no player.
  - Confirme se o player está totalmente desligado antes de conectar.
  - No Windows, confirme o driver MediaTek instalado com a configuração do Updater; no Linux, confirme as regras do udev no instalador do projeto.
  - Reconecte o cabo somente quando a ferramenta estiver aguardando. Uma corrida portuária pode precisar de uma desconexão completa e um novo Baixar clique.

Para qualquer coisa além disso, abra [solução de problemas](troubleshooting_pt-BR.html). E lembre-se: o atualizador ainda é o caminho normal e [Y1](guides/restore-original-y1.html) e [Y2](guides/restore-original-y2.html) guias de restauração também usam.

## Isso foi útil?

Sua resposta ajuda a melhorar este guia.Sim, achei útilAinda não[Deixe-nos saber como podemos melhorar](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
