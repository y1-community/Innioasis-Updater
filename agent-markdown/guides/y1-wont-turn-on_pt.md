---
title: "Innioasis Y1 Não liga | Innioasis Arquivo de firmware - Innioasis Downloads de firmware"
description: "Innioasis Y1 não liga ou carrega? Force uma reinicialização, verifique se um computador o vê e, em seguida, restaure o firmware Y1 ou use a recuperação manual SP Flash Tool."
language: "pt"
source: "https://innioasis.app/guides/y1-wont-turn-on_pt.html"
---

# Innioasis Y1 Não liga | Innioasis Arquivo de firmware - Innioasis Downloads de firmware

Recuperação de jogador · Innioasis Y1

# Innioasis Y1 não liga

Uma tela preta nem sempre significa um jogador morto. Trabalhe no carregamento, na reinicialização forçada e na detecção em um computador antes de tentar um flash manual.[Obtenha o atualizador CE](../guide_pt.html#platform)[Downloads de firmware](../firmware_pt.html)[Guia de recuperação](recovery_pt.html)

## Carregue o Y1 corretamente antes de qualquer coisa

A maioria dos relatórios "Y1 não liga" são de bateria descarregada, cabo somente de carga ou carregador que não consegue fornecer corrente suficiente. Um Y1 profundamente drenado pode levar de 20 a 30 minutos ligado antes que a tela mostre alguma coisa, então espere um pouco antes de chamá-lo de morto.
  - Use um conhecido USB dados cabo, não um cabo somente de carga.
  - Experimente um carregador de parede e, em seguida, uma porta de computador USB diretamente - não um hub.
  - Deixe-o conectado por 30 a 60 minutos e observe o ícone de carregamento ou a luz de fundo.
  - Experimente um segundo cabo e carregador antes de prosseguir.

## Forçar uma reinicialização

Segure o botão liga/desliga por cerca de 15 segundos, solte-o, espere cinco segundos e pressione liga/desliga uma vez. Isso limpa uma bota travada e pode ser repetido com segurança.

Se a tela mostrar o logotipo e depois ficar preta, o player está iniciando e falhando – pule para a restauração do firmware abaixo. Se nada acontecer, mantenha-o carregado e tente novamente depois de meia hora.

## Verifique se um computador pode ver o player

Conecte o Y1 desligado com um cabo de dados e abra o Gerenciador de Dispositivos no Windows, `lsusb` no Linux ou MTKClient no macOS. A working player appears as a MediaTek device with vendor ID `0e8d`. Se aparecer, o hardware está ativo o suficiente para piscar novamente mesmo quando a tela permanece escura.

Se nada aparecer, instale primeiro o driver MediaTek no Windows - o [guia do motorista](../drivers_pt.html) cobre permissões do Windows e Linux.

## Restaurar o firmware padrão Y1

Se o player for detectado, mas não inicializar, reinstale o Y1 Software Original. Use apenas um pacote Y1; uma compilação Y2 não será iniciada no hardware Y1.
  - Abrir [Atualizador CE](../guide_pt.html#platform) no seu computador.
  - Definir Modelo do dispositivo para Y1.
  - Escolher Software Original em Programas e escolha uma versão estável Y1 - o pacote manual é `rom.zip`.
  - Clique Instalar / Restaurar e deixe o pacote ser extraído.
  - Desligue o Y1 totalmente, conecte o cabo de dados USB somente quando o Updater solicitar e aguarde até a mensagem de sucesso.
Mantenha a energia estável. Um flash que perde potência pode deixar o player inutilizável. Carregue-o primeiro e conecte-o diretamente ao computador.

## Recuperação manual quando o atualizador não consegue ver o player

O Updater CE inclui ferramentas de recuperação manual para os casos em que a instalação guiada não pode ser concluída. [SP Flash Tool](../sp-flash-tool_pt.html) está incluído no Windows e Linux x86, e a rota MTKClient cobre o macOS. Ambos precisam de um pacote de firmware compatível com o modelo do [Downloads de firmware](../firmware_pt.html) página.

Siga o guia de ferramentas da sua plataforma em vez de improvisar arquivos dispersos ou deslocamentos. Se o player não for detectado por nenhuma ferramenta, a falha provavelmente está na bateria, na porta de carregamento ou na placa.

## Se ainda não começar

Pare de piscar e trate-o como hardware. Não abra a caixa nem pressione a bateria. Pergunte à comunidade com o modelo, o que a tela faz, se um computador a detecta e quais pacotes você experimentou – o [Discord comunidade](https://discord.gg/zHrT2zrcek) pode ajudar a identificar uma rota de serviço.

Uma restauração de estoque substitui o sistema, portanto, faça backup de tudo o que estiver armazenado na memória interna do player antes de atualizar. A música em um cartão MicroSD não é alterada pela restauração.

## Innioasis Y1 Perguntas frequentes sobre energia

### Por que meu Innioasis Y1 não liga?

As causas comuns são bateria totalmente descarregada, cabo somente de carga ou carregador fraco, falha de firmware que interrompe a inicialização ou falha de hardware. Carregue-o por 30 minutos com um cabo de dados conhecido antes de presumir que o player está morto.

### Como faço para forçar a reinicialização de um Innioasis Y1?

Segure o botão liga/desliga por cerca de 15 segundos, solte-o, espere cinco segundos e pressione liga/desliga uma vez. Se nada aparecer, deixe-o carregando e tente novamente após 30 minutos.

### Posso recuperar um Y1 que não liga?

Muitas vezes sim. Se um computador ainda detectar o dispositivo MediaTek, reinstale o pacote de software original Y1 com Updater CE. Se não for detectado, use a recuperação SP Flash Tool ou MTKClient incluída com Updater CE e um arquivo de firmware Y1 compatível com o modelo.

### Um Y1 precisa ser carregado antes de piscar?

Sim. Um flash que perde potência pode deixar o player inutilizável. Carregue-o primeiro e conecte-o diretamente ao computador, em vez de através de um hub.

## Correções relacionadas
  - [Y2 não liga](y2-wont-turn-on_pt.html) - as mesmas verificações para Y2
  - [Y1 roda de rolagem não funciona](y1-scroll-wheel-not-working_pt.html) - se inicializar, mas a roda não
  - [Innioasis guia de recuperação](recovery_pt.html) - todos os guias de sintomas em um só lugar
  - [SP Flash Tool guia](../sp-flash-tool_pt.html) — flash manual no Windows e Linux
  - [Solução de problemas de instalação](../troubleshooting_pt.html) - como é um flash com falha

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
