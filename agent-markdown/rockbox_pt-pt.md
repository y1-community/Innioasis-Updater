---
title: "Como instalar Rockbox em seu Innioasis Y1 ou Y2 - Innioasis Updater"
description: "Instale Rockbox em um Innioasis Y1 ou Y2 com o Updater: temas, versões estáveis, Type A e Type B notas e como restaurar o software original depois."
language: "pt-pt"
source: "https://innioasis.app/rockbox_pt-pt.html"
---

# Como instalar Rockbox em seu Innioasis Y1 ou Y2 - Innioasis Updater

Rockbox referência

# Obtendo Rockbox em seu Y1 ou Y2

Rockbox altera o software do reprodutor e abre uma interface mais profunda do reprodutor de música, controles de reprodução, classificação e opções de tema. A instalação é guiada, mas Y1 e Y2 são jornadas separadas.[Rockbox em Y1](guides/rockbox-y1.html)[Rockbox em Y2](guides/rockbox-y2.html)[Por que Rockbox?](rockbox-benefits_pt-PT.html)

## O que a instalação muda

Rockbox é um software personalizado. Isso não elimina sua capacidade de retornar à interface padrão quando o pacote de software original correspondente estiver disponível. Ele pode melhorar a navegação e personalização de músicas, mas os recursos, a resolução, a duração da bateria e a compatibilidade do tema dependem da construção.Não misture modelos. Selecione Y1 para um jogador Y1 e Y2 para um jogador Y2. Um nome de lançamento com aparência semelhante não é evidência suficiente de que um pacote é compatível.

## Assista ao vídeo

Vídeo de Frawgeeys. Mostra a rota Innioasis Updater; use as etapas escritas específicas do modelo abaixo para seu Y1 ou Y2.

Vídeo de [Praça Cristian](https://www.youtube.com/@CristianPlaza) (Espanhol), mostrando Rockbox em um Y1. Use as etapas específicas do modelo abaixo para o seu player.

## A rota compartilhada do atualizador
  - Instale o Updater e não conecte nada até que ele pergunte.
  - Escolha o modelo impresso no player em Modelo do dispositivo.
  - Escolher Rockbox em Programas.
  - Escolha uma versão estável, a menos que você esteja testando deliberadamente uma compilação noturna.
  - Clique Instalar / Restaurare siga o prompt de desligamento e conexão USB.
  - Desconecte somente após a mensagem de sucesso.

## 240p, 360p e temas

Coleções de temas mais antigas Rockbox podem ser feitas para 240p. Y1 compilações de comunidade também usam rótulos de compatibilidade de 360p. Leia as notas de lançamento e a fonte do tema antes de escolher uma versão. Um tema feito para uma resolução ou família de software pode não funcionar em outra.[Procure temas da comunidade](https://themes.innioasis.app/?lang=pt-PT)[Ferramentas temáticas](https://themes.innioasis.app/?lang=pt-PT)

## Retornando ao software original

Escolha o mesmo modelo novamente, selecione Software Original, escolha uma versão estável e use Instalar / Restaurar. Se a falha ocorreu antes do prompt USB, verifique o computador e os arquivos extraídos. Se o player foi detectado, mas o flash falhou, comece com [solução de problemas](troubleshooting_pt-PT.html).[Y1 restaurar](guides/restore-original-y1.html)[Y2 restaurar](guides/restore-original-y2.html)

## Perguntas frequentesReinstalei Rockbox e não resolveu nada.

A reinstalação de Rockbox grava a mesma compilação nos mesmos arquivos, portanto, não é possível redefinir as coisas que Rockbox mantém em MicroSD. Se o problema for uma configuração, tema, lista de reprodução ou banco de dados corrompido no cartão, a reinstalação não o resolverá. A redefinição confiável está excluindo o `.rockbox` pasta do MicroSD - Rockbox cria uma nova na próxima inicialização.
  - Desligue o player totalmente e remova a placa MicroSD ou conecte o player como uma unidade USB.
  - Mostre arquivos ocultos em seu computador para que a pasta fique visível. Como mostrar arquivos ocultosMostrar dotfiles no seu computadorWindows: no Explorador de Arquivos, abra o Visualizar aba e marque Itens ocultos.macOS: no Finder pressione Cmd+Shift+. para alternar arquivos ocultos.Arquivos Linux · GNOME: imprensa Ctrl+Hou abra o menu e escolha Mostrar arquivos ocultos.Linux · KDE Golfinho: imprensa Ctrl+H, ou usar Ver → Mostrar arquivos ocultos.
  - Exclua o `.rockbox` pasta da raiz do cartão.
  - Reinsira o cartão e ligue o player. Rockbox recria a pasta com padrões.
  - Aplique novamente seu tema e configurações. Se o problema só voltar após um tema específico, esse tema é a causa.

Excluindo `.rockbox` não desinstala Rockbox e não altera sua música - a pasta contém configurações, temas e caches e é reconstruída automaticamente. Se você quiser manter seus temas, copie a pasta de `.rockbox` antes de excluí-lo ou renomeie a pasta para `.rockbox-old` primeiro.Por que não consigo ver a pasta .rockbox no meu MicroSD?

As pastas cujo nome começa com um ponto ficam ocultas por padrão na maioria dos computadores. Você não precisa vê-lo para instalar Rockbox — O atualizador cuida dos arquivos. Se você estiver solucionando problemas e quiser excluí-lo, ative primeiro os arquivos ocultos. Como mostrar arquivos ocultosMostrar dotfiles no seu computadorWindows: no Explorador de Arquivos, abra o Visualizar aba e marque Itens ocultos.macOS: no Finder pressione Cmd+Shift+. para alternar arquivos ocultos.Arquivos Linux · GNOME: imprensa Ctrl+Hou abra o menu e escolha Mostrar arquivos ocultos.Linux · KDE Golfinho: imprensa Ctrl+H, ou usar Ver → Mostrar arquivos ocultos.A exclusão de .rockbox redefinirá meu tema e configurações?

Sim - `.rockbox` contém configurações, tema, listas de reprodução e banco de dados em cache de Rockbox. Excluí-lo retorna Rockbox para um estado padrão limpo. Faça backup de toda a pasta (ou renomeie-a para `.rockbox-old`) se você quiser algo de volta, inicie o player e Rockbox crie uma nova pasta.

## Mais guias Rockbox-Y1 e Rockbox-Y2

Explore guias passo a passo para instalação, download, temas, restauração e solução de problemas Rockbox em ambos os modelos:[Rockbox-Y1 central](rockbox-y1/)[Rockbox-Y2 central](rockbox-y2/)[Rockbox ROM downloads](rockbox-rom-download_pt-PT.html)[Rockbox para Y1](rockbox-for-y1_pt-PT.html)[Rockbox para Y2](rockbox-for-y2_pt-PT.html)[Rockbox-Y1 versus Y2](rockbox-y1-vs-y2.html)[Rockbox-Y1 temas](rockbox-y1-themes.html)[Rockbox-Y2 temas](rockbox-y2-themes.html)

## Esta referência foi útil?

Sua resposta ajuda a melhorar este guia.SimAinda não[Deixe-nos saber como podemos melhorar](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
