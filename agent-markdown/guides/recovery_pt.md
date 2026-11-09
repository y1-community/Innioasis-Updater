---
title: "Innioasis Y1 e Y2 Guia de recuperação | Innioasis Arquivo de firmware - Innioasis Downloads de firmware"
description: "Guia de recuperação para Innioasis Y1 e Y2 jogadores que não ligam ou que têm uma roda de rolagem que parou de funcionar após uma atualização. Etapas de reinicialização e firmware."
language: "pt"
source: "https://innioasis.app/guides/recovery_pt.html"
---

# Innioasis Y1 e Y2 Guia de recuperação | Innioasis Arquivo de firmware - Innioasis Downloads de firmware

Recuperação de jogador · Y1 e Y2

# Innioasis Y1 e Y2 guia de recuperação

Não liga, a roda não funciona ou a instalação parou no meio do caminho. Comece com o sintoma e siga as etapas na ordem, em vez de pular direto para o flash manual.[Obtenha o atualizador CE](../guide_pt.html#platform)[Downloads de firmware](../firmware_pt.html)[Solução de problemas](../troubleshooting_pt.html)

Comece com Innioasis Updater

## A instalação guiada corrige a maioria destes

O atualizador faz isso de uma só vez. Escolha o software, siga as etapas na tela e pronto. Ele também informa quando uma correção ou um novo lançamento chega.

## Comece com o sintoma

Esses guias cobrem as duas falhas que as pessoas enfrentam com mais frequência após uma atualização ou flash. Escolha aquele que corresponde ao que você vê e analise-o em ordem.

### A roda de rolagem não funciona

A roda gira, mas o jogador a ignora ou parou logo após uma atualização.

[Y1 guia da roda de rolagem](y1-scroll-wheel-not-working_pt.html) · [Y2 guia da roda de rolagem](y2-scroll-wheel-not-working_pt.html)

### O player não liga

Uma tela preta, luz sem carga ou um logotipo que aparece e desaparece.

[Y1 guia de energia](y1-wont-turn-on_pt.html) · [Y2 guia de energia](y2-wont-turn-on_pt.html)

### Instalação interrompida no meio do caminho

O atualizador falhou antes ou depois do prompt USB ou a lista de lançamentos parece errada.

[Guia de solução de problemas](../troubleshooting_pt.html)

### Preciso dos arquivos

Software Original e pacotes personalizados para cada modelo.

[Downloads de firmware](../firmware_pt.html)

## Os pacotes Y1 e Y2 não são intercambiáveisNunca faça flash cruzado em um modelo. Um Y1 `rom.zip` não é um pacote Y2 e um Y2 `rom_y2.zip` não será executado em um Y1. Atualizar o modelo errado é um dos motivos mais comuns pelos quais um jogador acaba com controles mortos ou um loop de inicialização.

Verifique o modelo impresso no player e combine-o no Updater CE antes de escolher uma versão.

## Restaure primeiro o software original correspondente

Antes de qualquer ferramenta manual, coloque o firmware padrão do modelo correto de volta no player. Isso corrige a maioria das falhas de roda e inicialização relacionadas à atualização.

Y1: selecione Y1, escolha Software Original, escolha uma versão estável Y1 e execute Instalar/Restaurar. [Guia completo de restauração Y1](restore-original-y1_pt.html).

Y2: selecione Y2, escolha Software Original, escolha uma versão estável Y2 e execute Instalar/Restaurar. [Guia completo de restauração Y2](restore-original-y2_pt.html).

Desligue o player e conecte o cabo de dados USB somente quando o Updater solicitar. Deixe conectado até a mensagem de sucesso.

## Recuperação manual fornecida com Updater CE

Quando o Updater não consegue concluir o trabalho, a mesma instalação inclui as ferramentas manuais. [SP Flash Tool](../sp-flash-tool_pt.html) é fornecido em máquinas Windows e Linux x86, e a rota MTKClient cobre o macOS. Ambos necessitam de um pacote de firmware compatível com o modelo, disponível no [Downloads de firmware](../firmware_pt.html) página.

Use o guia da sua plataforma e mantenha o player carregado. Se nenhuma ferramenta detectar o player, a falha provavelmente é de hardware e não de firmware.

## O que incluir quando você pede ajuda
  - O modelo — Y1 ou Y2 — impresso no player.
  - O que a tela faz: nada, um logotipo, um loop de inicialização ou a tela inicial.
  - Se um computador detecta o player como um dispositivo MediaTek.
  - A mensagem exata do atualizador e o pacote que você selecionou.
  - O que você já tentou, incluindo qualquer ferramenta manual.

Não publique tokens privados ou arquivos de sistema não relacionados. O [comunidade Discord](https://discord.gg/zHrT2zrcek) e [r/innioasis](https://reddit.com/r/innioasis) são os lugares mais rápidos para comparar notas.

## Innioasis Perguntas frequentes sobre recuperação

### Como faço para consertar um player Innioasis que não liga?

Carregue-o por 30 minutos com um cabo de dados conhecido, force a reinicialização mantendo a energia pressionada por 15 segundos e verifique se um computador o detecta. Se isso acontecer, restaure o Software Original correspondente ao modelo; caso contrário, use as ferramentas de recuperação manual incluídas em Updater CE.

### Por que minha roda de rolagem Y1 ou Y2 não está funcionando?

Se a roda parar após uma atualização, geralmente é uma incompatibilidade de firmware. Reinstale o software original correspondente ao modelo e teste novamente. Se a roda estiver morta em todos os firmwares, trate isso como uma falha de hardware.

### Onde faço o download do firmware para recuperação?

A página de downloads de firmware em innioasis.app/firmware.html hospeda pacotes originais e personalizados para cada modelo. Sempre escolha o pacote Y1 ou Y2 que corresponde ao player.

### Quais ferramentas de recuperação estão incluídas em Updater CE?

Updater CE inclui SP Flash Tool no Windows e Linux, e a rota MTKClient incluindo macOS, para recuperação manual quando a instalação normal não puder ser concluída.

## Correções relacionadas
  - [Y1 roda de rolagem não funciona](y1-scroll-wheel-not-working_pt.html) - a roda de clique não responde após uma atualização
  - [Y2 roda de rolagem não funciona](y2-scroll-wheel-not-working_pt.html) - as mesmas verificações para Y2
  - [Y1 não liga](y1-wont-turn-on_pt.html) — carregamento, reinicialização e recuperação manual
  - [Y2 não liga](y2-wont-turn-on_pt.html) - as mesmas verificações para Y2
  - [SP Flash Tool guia](../sp-flash-tool_pt.html) — flash manual no Windows e Linux

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
