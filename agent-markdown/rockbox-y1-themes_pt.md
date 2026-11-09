---
title: "Rockbox-Y1 temas: transferência de temas com Updater CE, 240p vs 360p e aplicação de um tema"
description: "Como transferir temas para o Innioasis Y1 com Updater CE (push automático quando disponível ou transferência guiada passo a passo após um MTKClient flash no macOS e Linux), além de compatibilidade 240p vs 360p e aplicação de um tema."
language: "pt"
source: "https://innioasis.app/rockbox-y1-themes_pt.html"
---

# Rockbox-Y1 temas: transferência de temas com Updater CE, 240p vs 360p e aplicação de um tema

[← Rockbox-Y1 central](rockbox-y1/)

Rockbox-Y1 · temas e Updater CE

# Rockbox-Y1 temas: transfira com Updater CE, escolha a construção e depois a aparência

Updater CE cuida de Rockbox-Y1 temas e fontes para você — transferindo-os para o Y1 automaticamente sempre que possível e orientando você durante a transferência passo a passo quando ela não puder acontecer sem supervisão (por exemplo, logo após a instalação de um MTKClient firmware no macOS ou Linux).[Obtenha Rockbox e Updater CE](guides/rockbox-y1.html)[Procure temas da comunidade](https://themes.innioasis.app/)[240p versus 360p](rockbox-y1/resolution.html)

## Transferindo temas para Y1 com Updater CE

Rockbox armazena seu firmware no flash interno do Y1, enquanto temas, fontes e configurações do usuário ficam dentro do flash interno `.rockbox` pasta no armazenamento do player (cartão MicroSD). Como atualizar um ROM e copiar arquivos para armazenamento usam duas conexões diferentes, Atualizador CE adapta-se automaticamente ao seu sistema operacional e método de instalação:
  - Transferência automática quando Updater CE pode alcançar o jogador: Quando você instala uma versão 360p Rockbox-Y1 (ou habilita a sincronização automática do tema em Configurações), Updater CE baixa e mescla o tema 360p selecionado e o pacote de fontes em segundo plano. Assim que o Y1 estiver acessível BAD (Android Debug Bridge) ou montado como um USB dirigir com um `.rockbox` pasta, Updater CE envia os temas e fontes diretamente para o player para você, sem necessidade de extração manual de zip.
  - Transferência guiada passo a passo quando não puder acontecer de forma autônoma (por exemplo, MTKClient no macOS e Linux): Quando você pisca Rockbox usando um MTKClient método de instalação no macOS ou Linux, o flash acontece enquanto o Y1 está desligado no modo Pré-carregador/BROM de baixo nível - antes de Rockbox inicializar pela primeira vez para criar `.rockbox` e antes que o armazenamento do player seja montado em seu computador. Sempre que Updater CE não consegue concluir a transferência sem supervisão durante o flash, ele abre automaticamente o assistente de temas e fontes pós-instalação e orienta você na conclusão: 
    - Inicialize Rockbox primeiro: Updater CE solicita que você desconecte o cabo USB se necessário e ligue o Y1 para que Rockbox inicialize uma vez e inicialize o `.rockbox` pasta no cartão.
    - Reconecte via USB: Conecte o Y1 novamente ao seu PC Mac ou Linux. Se o ADB estiver disponível, Updater CE detecta o player inicializado e envia o tema e os pacotes de fontes automaticamente.
    - Ou use USB Modo de armazenamento com o seletor de pastas guiado: Se o ADB não estiver ativo ou você preferir transferência direta de armazenamento, Updater CE orienta você a entrar no modo de armazenamento USB em Y1, clique Selecione a pasta .rockbox, revele pastas ocultas (Cmd+Shift+. na caixa de diálogo de arquivo do macOS ou Ctrl+H no Linux) e selecione `.rockbox` na unidade Y1 - então Updater CE mescla todos os temas e fontes para você.

  - Adicione ou atualize temas a qualquer momento sob demanda: Você pode executar a mesma transferência automatizada ou guiada a qualquer momento sem atualizar o firmware - abra Updater CE e escolha Configurações → Instalar Rockbox Temas 360p (Cmd+T no macOS, Ctrl+T no Windows e Linux) ou arraste um tema individual `.zip` pacotes em Updater CE Queda Inteligente janela.

## 240p, 360p e por que o rótulo está na versão

Y1 as compilações da comunidade são publicadas com um rótulo de resolução e as coleções temáticas carregam o mesmo rótulo. As compilações de 240p têm a mais ampla compatibilidade com pacotes de temas mais antigos; Compilações em 360p são feitas para o caminho do tema Y1 mais recente. Instalar um e aplicar o outro não é perigoso – apenas parece errado, com texto cortado, elementos ausentes ou uma interface que você não consegue ler.

Se você ainda não tem preferência de tema, pegue a versão estável mais recente e seu tema padrão e escolha temas que correspondam ao seu rótulo. O [página de resolução](rockbox-y1/resolution.html) vai mais fundo; a regra prática é simples: o rótulo de construção e o rótulo do tema devem concordar.

## Onde os temas vivem

Temas são arquivos no cartão MicroSD, dentro do `.rockbox` pasta – a mesma pasta que contém configurações e caches. O firmware em si está em flash interno, portanto, adicionar, alterar ou remover um tema nunca requer atualização.
  - Copie a própria pasta do tema para `.rockbox/themes` no cartão.
  - Em seguida, escolha-o nas configurações de tema do player e reinicie para vê-lo aplicado.
  - Mantenha uma cópia de um tema de sua preferência antes de atualizar a compilação – é um arquivo, não uma instalação.

Ative os arquivos ocultos primeiro se você não conseguir ver a pasta: macOS Cmd+Shift+., Windows View → Itens ocultos, Linux Ctrl+H.

## Aplicando um tema, em ordem
  - Instale e inicialize Rockbox-Y1 primeiro; um tema precisa de uma construção em execução.
  - Copie a pasta do tema para `.rockbox/themes` no cartão.
  - Abra as configurações do tema e selecione o tema.
  - Reinicie para que toda a interface – não apenas o menu – seja ativada.
  - Se parecer quebrado, selecione outro tema; os arquivos ainda estão lá se você quiser tentar novamente mais tarde.

## Desfazendo um tema que quebrou a interface

Se o player inicializar de forma inutilizável, você não precisa reinstalar o firmware. Renomeie ou exclua o `.rockbox` pasta no cartão e inicie o player: a compilação recria a pasta com configurações padrão e um tema padrão. Sua música permanece intacta e você pode copiar os temas que desejar posteriormente.[A pasta .rockbox](rockbox-y1/sd-card.html)[Primeiro começo](rockbox-y1/first-start.html)[Atualizando a compilação](rockbox-y1/update.html)

## Perguntas que as pessoas fazemPor que Updater CE me orienta na transferência de temas após a instalação de MTKClient no macOS ou Linux?

MTKClient atualiza o Rockbox ROM para o armazenamento interno enquanto seu Y1 está desligado no modo Pré-carregador/BROM de baixo nível, antes de Rockbox inicializar para inicializar o `.rockbox` pasta e antes que a placa MicroSD seja montada em seu computador. Sempre que Updater CE puder acessar o player inicializado diretamente (via ADB ou uma unidade USB montada), ele transfere os temas automaticamente; quando não pode fazer isso sozinho durante o flash, ele abre a etapa de temas e fontes guiadas logo após o flash para ajudá-lo a ligar o Y1 e concluir a transferência via ADB ou USB modo de armazenamento.Um tema Y2 funcionará no Y1?

Não. As portas são separadas e o suporte ao tema no Y2 segue suas versões beta. Ver [Rockbox-Y2 temas](rockbox-y2-themes_pt.html).Os temas sobrevivem a uma atualização?

Geralmente sim, porque eles ficam no cartão e o flash grava o ROM. Se uma nova compilação alterar o caminho do tema, reaplique um tema que corresponda ao seu rótulo.Por que o tema é aplicado apenas pela metade?

Uma reinicialização normalmente resolve isso. Caso contrário, os arquivos do tema estarão incompletos – copie novamente a pasta em vez de editar arquivos individuais.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
