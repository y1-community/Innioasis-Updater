---
title: "Innioasis Y1 A roda de rolagem não funciona após a atualização | Innioasis Arquivo de firmware - Innioasis Downloads de firmware"
description: "Innioasis Y1 a roda de rolagem ou a roda de clique não funcionam após uma atualização? Reinstale o software original Y1, verifique o anel e separe o firmware das falhas de hardware."
language: "pt"
source: "https://innioasis.app/guides/y1-scroll-wheel-not-working_pt.html"
---

# Innioasis Y1 A roda de rolagem não funciona após a atualização | Innioasis Arquivo de firmware - Innioasis Downloads de firmware

Recuperação de jogador · Innioasis Y1

# Innioasis Y1 a roda de rolagem não funciona após uma atualização

A roda gira, mas nada se move ou a click wheel parou de responder logo após um flash. Veja como separar uma falha de firmware de uma falha de hardware e o que fazer primeiro.[Obtenha o atualizador CE](../guide_pt.html#platform)[Y1 downloads de software](../firmware_pt.html?model=Y1&software=original-y1)[Guia de recuperação](recovery_pt.html)

## Descubra se a roda ou o firmware estão com defeito

Em um Y1 a roda é uma entrada física, mas o firmware decide o que cada giro e clique faz. Se a roda parou no momento em que você atualizou ou atualizou o player, a causa provável é o software, não uma peça quebrada. Se ele ignorar todos os softwares que você tentar – estoque, Rockbox ou uma tela de recuperação – trate-o como hardware.
  - Funciona em um software, morto em outro: falha de firmware.
  - Morto em todas as telas, incluindo recuperação: roda, fita ou placa.
  - Apenas uma direção falha: geralmente detritos sob o anel ou desgaste.
  - A roda gira, mas nada destaca: o jogador pode estar congelado – force uma reinicialização primeiro.

## Verificações rápidas antes de reinstalar o firmware
  - Segure o botão liga / desliga por cerca de 15 segundos para forçar o desligamento do player e, em seguida, ligue-o normalmente.
  - Teste a roda na tela inicial, em Configurações e no reprodutor de música.
  - Pressione os botões físicos. Se a potência e a traseira responderem, mas a roda não, a falha é da própria roda.
  - Carregue o player por 30 minutos com um cabo de dados conhecido – uma bateria fraca pode fazer com que as entradas se comportem de maneira irregular.
  - Se você instalou Rockbox ou outra compilação personalizada, retorne ao software original e teste novamente.

## Reinstale o firmware Y1 que corresponde ao seu player

Como o volante é acionado pelo firmware, uma falha relacionada à atualização é corrigida colocando o software original Y1 correto de volta no player. Não use um pacote Y2 e não escolha uma versão que seja "próxima o suficiente" — pacotes Y1 são construídos para hardware Y1, e uma compilação Y2 em um Y1 pode deixar os controles mapeados incorretamente.
  - Abrir [Atualizador CE](../guide_pt.html#platform) no seu computador.
  - Definir Modelo do dispositivo para Y1.
  - Escolher Software Original em Programas e escolha uma versão estável Y1 - o pacote manual é `rom.zip`.
  - Clique Instalar / Restaurar e deixe o pacote ser extraído.
  - Desligue o Y1 totalmente, conecte o cabo de dados USB somente quando o Updater solicitar e aguarde até a mensagem de sucesso.
Combine o modelo e o lançamento. If the release list looks like Y2 software, stop and re-select Y1. As etapas completas estão no [Y1 guia de restauração](restore-original-y1_pt.html).

## Verifique o anel da roda quanto a detritos ou danos

Se a roda estiver rígida, emperrar ou falhar apenas em uma direção, fiapos e areia podem ficar entre o anel e a caixa. Desligue o player e limpe o anel com um pano de microfibra seco. Não pingue produtos de limpeza ou álcool na abertura e não levante o anel.

Se o anel estiver solto, rachado ou não encaixar mais, o player precisa de manutenção. A reinstalação do firmware não reparará uma roda danificada, uma fita desconectada ou danos causados ​​por líquidos.

## Se o jogador também não iniciar

Uma atualização com falha pode deixar o Y1 incapaz de inicializar, o que parece um problema de roda porque nada responde. Trabalhe através do [Y1 não ativa o guia](y1-wont-turn-on_pt.html) para etapas de carregamento, reinicialização forçada e recuperação manual.

## Innioasis Y1 perguntas frequentes sobre a roda de rolagem

### Por que minha roda de rolagem Innioasis Y1 parou de funcionar após uma atualização?

Uma atualização pode deixar o driver do volante descompasso com o resto do firmware, especialmente se o flash foi interrompido ou um pacote Y2 foi usado. Reinstale a versão do software original Y1 para o seu modelo e teste o volante na tela inicial padrão.

### Como posso saber se a click wheel Y1 está quebrada ou se o firmware está com defeito?

Teste a roda em mais de um software. Se funcionar em software padrão, mas não em Rockbox, é um problema de mapeamento de firmware. Se não fizer nada em nenhuma tela, incluindo um menu de recuperação, suspeite da roda, da faixa de opções ou do tabuleiro.

### A restauração do software original corrigirá a roda de rolagem Y1?

Ele corrige falhas causadas por uma atualização ou pacote incompatível e é a primeira coisa a tentar. Ele não reparará uma roda fisicamente danificada, uma fita solta ou danos líquidos.

### Posso usar um pacote de firmware Y2 para corrigir um problema de roda Y1?

Os pacotes Y1 e Y2 não são intercambiáveis, e atualizar o modelo errado pode piorar os controles. Combine o modelo e a versão antes de executar a instalação/restauração.

## Correções relacionadas
  - [Y2 roda de rolagem não funciona](y2-scroll-wheel-not-working_pt.html) - as mesmas verificações para Y2
  - [Y1 não liga](y1-wont-turn-on_pt.html) - recuperação de energia e inicialização
  - [Innioasis guia de recuperação](recovery_pt.html) - todos os guias de sintomas em um só lugar
  - [Solução de problemas de instalação](../troubleshooting_pt.html) - como é um flash com falha
  - [Restaurar Y1 software original](restore-original-y1_pt.html) – o passo a passo completo da restauração

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
