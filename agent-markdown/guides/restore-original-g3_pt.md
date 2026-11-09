---
title: "Restaure o software original em Innioasis G3 - passo a passo"
description: "Como restaurar o software original oficial em um Innioasis G3 com Innioasis Updater CE ou SP Flash Tool, usando o pacote verificado rom_g3.zip."
language: "pt"
source: "https://innioasis.app/guides/restore-original-g3_pt.html"
---

# Restaure o software original em Innioasis G3 - passo a passo

Guia de restauração · Innioasis G3

# Restaure o software original em Innioasis G3

Um retorno limpo ao software que acompanha o player. Use-o após uma falha na atualização, antes de vender o player ou sempre que um sistema personalizado não for adequado para você.[Obtenha o atualizador CE](../guide_pt.html#platform)[G3 downloads](../firmware_pt.html?model=G3)[G3 manual](../manuals/g3.html)

Guia de instalação para o seu computador

## Restaure o software original em seu G3 com seu computador

Escolha o guia para o computador que você está usando. Cada versão possui a configuração da plataforma, Updater CE etapas e o caminho de volta ao estoque.[Guia do Windows](/install/original-g3-windows.html)[guia macOS](/install/original-g3-mac.html)[Guia Linux](/install/original-g3-linux.html)

[Todos Innioasis G3 guias](/install/g3.html) · [Todos os guias de software original](/install/original-software.html)

## O que você precisa
  - Um computador Windows, macOS ou Linux. Updater CE é executado em todos os três.
  - O cabo de dados USB que acompanha o player. Cabos somente para carga não funcionarão.
  - O oficial `rom_g3.zip` pacote, que o Updater baixa para você, ou uma cópia do [G3 arquivo](../firmware_pt.html?model=G3) se você preferir piscar manualmente.
  - Carregue no player. Uma restauração que perde energia é a única maneira comum de piorar uma situação ruim.

Isso substitui o sistema e apaga o armazenamento interno. Copie músicas, gravações e fotos primeiro para um computador.

## Rota A: Updater CE (recomendado)
  - Instalar [Innioasis Atualizador CE](../guide_pt.html#platform) e abra-o.
  - Definir Modelo do dispositivo para G3. O modelo deve corresponder exatamente ao jogador.
  - Escolher Software Original na lista Software.
  - Escolha um lançamento. A versão estável mais recente é o padrão seguro.
  - Imprensa Instalar / Restaurar e espere enquanto o pacote é baixado e extraído.
  - Desligue o player totalmente e conecte o cabo USB somente quando o Updater solicitar.
  - Não toque no player ou no cabo até aparecer a mensagem de sucesso. Desconecte e inicie o player.
Nunca escolha um modelo diferente para “fazer funcionar”. Um G3 precisa de um pacote G3. Misturar modelos é como os jogadores acabam precisando de uma recuperação manual.

## Rota B: SP Flash Tool (manual)

Use isto quando um computador não consegue executar Updater CE, ou quando você já possui o pacote e prefere a ferramenta clássica.
  - Download `rom_g3.zip` do [G3 arquivo](../firmware_pt.html?model=G3) e descompacte-o.
  - Mantenha o arquivo scatter próximo às imagens. Não renomeie ou mova as imagens.
  - Abra SP Flash Tool, escolha Baixar apenase carregue o arquivo scatter.
  - Desligue o player, pressione Downloade conecte o cabo.
  - Aguarde a marca verde de sucesso antes de desconectar.

O [SP Flash Tool guia](../sp-flash-tool_pt.html) aborda os drivers e os prompts do Windows com mais detalhes. No Linux e no macOS, Updater CE é o caminho mais fácil porque traz seu próprio tratamento USB.

## Após a restauração
  - Desconecte o player e deixe-o iniciar sozinho.
  - Escolha o seu idioma e acerte o relógio.
  - Reconecte-se ao Wi-Fi ou Bluetooth se você os usar.
  - Copie sua música de volta. O [guia de transferência](../manuals/transfer-music.html) tem os nomes das pastas.

Se o player iniciar, mas a tela, a roda ou os botões ainda funcionarem mal, a restauração funcionou; essa é uma questão de hardware ou configuração, não de software. O [guia de solução de problemas](../troubleshooting_pt.html) A próxima parada é.

## Se não funcionar

### O atualizador nunca vê o player

Troque o cabo e depois a porta USB. Evite hubs. No Windows, instale o driver MediaTek do [página do motorista](../drivers_pt.html).

### O flash para mais cedo

Reconecte, carregue o player e comece novamente. Não mude para um pacote de modelo diferente.

### O jogador permanece preto

Carregue por uma hora e mantenha a energia por dez segundos. Se ainda estiver morto, leia o [guia de recuperação](../guides/recovery_pt.html) antes de tentar novamente.

## Perguntas que as pessoas fazem

### Isso excluirá minha música?

Sim, o armazenamento interno foi apagado. Os arquivos em um cartão microSD geralmente sobrevivem, mas primeiro copie-os para algum lugar seguro.

### Posso voltar para Rockbox depois?

Sim. A restauração do software original não é uma porta de mão única; a página do software personalizado para o seu modelo pode instalá-lo novamente.

### Preciso da configuração Type A / Type B?

Somente Y1 tem essa escolha, e apenas para Software Original. Todos os outros modelos usam um único pacote.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
