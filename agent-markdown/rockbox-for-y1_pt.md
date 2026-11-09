---
title: "Rockbox para Y1 (Rockbox-Y1): visão geral, construção e guia de instalação"
description: "Rockbox para Y1, Rockbox-Y1 e rockbox-y1 referem-se ao firmware da comunidade Rockbox para Innioasis Y1. Aprenda o que ele adiciona, qual build escolher e como instalá-lo com Innioasis Updater CE."
language: "pt"
source: "https://innioasis.app/rockbox-for-y1_pt.html"
---

# Rockbox para Y1 (Rockbox-Y1): visão geral, construção e guia de instalação

[← Downloads de firmware](firmware_pt-BR.html?model=Y1&software=rockbox-y1)

Rockbox-Y1 · Innioasis Y1

# Rockbox para Y1 (Rockbox-Y1)

“Rockbox”, “Rockbox-Y1” e “Rockbox para Y1” referem-se todos ao mesmo firmware da comunidade Rockbox para Innioasis Y1. Aqui está o que ele adiciona ao seu player, qual build escolher e como instalá-lo com Innioasis Updater CE.[Instalar Rockbox-Y1](rockbox-y1/install.html)[Baixe o ROM](rockbox-y1/download.html)[Tutorial escrito](guides/rockbox-y1.html)[Hub Rockbox-Y1](rockbox-y1/)

## Um firmware, vários nomes

Em Innioasis Updater CE, este firmware aparece como Rockbox quando você seleciona o modelo do dispositivo Y1. Guias, vídeos e notas de lançamento também chamam isso Rockbox-Y1 ou Rockbox para Y1 então está claro que a compilação é para Y1 e não para Y2.

Sempre verifique o modelo impresso no seu player antes de instalar: os pacotes de firmware Y1 e Y2 não são intercambiáveis.

## O que Rockbox-Y1 adiciona ao seu Y1

Rockbox-Y1 is a community port of the open-source Rockbox music player firmware for the Innioasis Y1:
  - Biblioteca de música baseada em tags — browse by artist, album, genre, and year using audio tags, or browse folders directly.
  - Reprodução de áudio avançada — reprodução contínua, crossfade, ReplayGain e equalizador completo.
  - Temas personalizados — escolha entre centenas de temas da comunidade em 240p e 360p, incluindo layouts clássicos no estilo iPod.
  - Rádio FM — suporte integrado para rádio FM.
  - Extras opcionais - downloads de podcast por Wi-Fi e scrobbling Last.fm / ListenBrainz / Maloja em compilações suportadas.
  - Inicialização dupla - volte para o software original de fábrica sem atualizar as compilações suportadas.

## Qual compilação Y1 devo escolher?
  - 240p x 360p — As compilações de 240p funcionam com temas clássicos de 320×240 Rockbox; As compilações em 360p usam temas mais nítidos de 480×360 Y1. Combine a resolução de construção com os temas que você deseja usar ([Guia 240p vs. 360p](rockbox-y1/resolution.html)).
  - Type A versus Type B — Type A é para Y1 reprodutores fornecidos com software de fábrica 2.0.0 ou mais recente; Type B é para unidades anteriores Y1. Escolha Type A, a menos que você saiba que seu Y1 é Type B.
  - Estável vs. Noturno — Choose a stable build for everyday listening, or a nightly build to test the newest changes.

## Downloads diretos dos desenvolvedores da comunidade

Innioasis Updater CE sempre baixa pacotes de firmware diretamente dos desenvolvedores de firmware da comunidade ([rockbox-y1/rockbox](firmware_pt-BR.html?model=Y1&software=rockbox-y1)), e os próprios desenvolvedores são os únicos responsáveis ​​por listar suas versões de software em Updater CE.

Você pode permitir que Updater CE baixe e instale o firmware automaticamente ou baixe os pacotes ROM de nosso [Rockbox-Y1 página de downloads](rockbox-y1/download.html) e [Rockbox ROM página de download](rockbox-rom-download_pt-BR.html).[Rockbox-Y1 downloads](rockbox-y1/download.html)[Instalar a partir de um ZIP local](rockbox-y1/portable-zip.html)

## Como instalar Rockbox-Y1
  - Abra Innioasis Updater CE e defina Modelo do aparelho para Y1.
  - Selecione Rockbox em Software.
  - Escolha uma versão estável (ou habilite compilações noturnas para testar uma prévia).
  - Clique Instalar / Restaurar então Updater CE baixa o pacote diretamente do desenvolvedor.
  - Desligue o Y1 completamente e conecte-o com um cabo de dados USB quando Updater CE solicitar.
  - Aguarde a mensagem de conclusão, desconecte e ligue o player.

Para capturas de tela e dicas detalhadas de configuração, leia o [tutorial completo Rockbox-Y1](guides/rockbox-y1.html).

## Restaurando o software Y1 original

Você pode retornar ao software de fábrica a qualquer momento: selecione Y1 e Software original em Updater CE, escolha uma versão estável e clique Instalar / Restaurar. Sua música no cartão MicroSD é preservada. Veja o [guia de restauração](rockbox-y1/restore-stock.html) e [Y1 Página do software original](original-software-y1_pt-BR.html).

## Perguntas frequentesRockbox para Y1 é o mesmo que Rockbox-Y1?

Sim. Rockbox, Rockbox-Y1, Rockbox para Y1, e `rockbox-y1` todos se referem à mesma porta da comunidade Rockbox para Innioasis Y1.De onde Updater CE baixa Rockbox-Y1?

Updater CE sempre baixa pacotes de firmware diretamente dos próprios lançamentos dos desenvolvedores de firmware da comunidade (`rockbox-y1/rockbox`). Os desenvolvedores são os únicos responsáveis ​​por listar seus lançamentos de software em Updater CE.Posso instalar Rockbox-Y1 em um Y2?

Não. O Y2 tem sua própria compilação de firmware separada. Usar [Rockbox para Y2](rockbox-for-y2_pt-BR.html) em vez de.A instalação de Rockbox-Y1 apagará minha música?

Não. A música é armazenada no cartão MicroSD e não é afetada ao atualizar o firmware interno do player.

## Guias relacionados

### [Hub Rockbox-Y1](rockbox-y1/)

Todos os guias Y1: instalação, downloads, temas, restauração, inicialização dupla e solução de problemas.

### [Rockbox-Y1 versus Rockbox-Y2](rockbox-y1-vs-y2.html)

Como as compilações Y1 e Y2 Rockbox diferem.

### [Rockbox-Y1 temas](rockbox-y1-themes.html)

Como transferir temas 240p e 360p com Updater CE.

### [Rockbox visão geral](rockbox_pt-BR.html)

Introdução a Rockbox em Innioasis Y1 e Y2 jogadores.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
