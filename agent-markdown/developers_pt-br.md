---
title: "Desenvolvedores | Adicionar firmware personalizado a Innioasis Updater CE - Innioasis downloads de firmware"
description: "Documentação do desenvolvedor para adicionar um firmware Innioasis Y1 ou Y2 personalizado ao Updater CE: bifurque o repositório, publique os ativos rom.zip, edite slidia_manifest.xml, teste e abra uma solicitação pull."
language: "pt-br"
source: "https://innioasis.app/developers_pt-br.html"
---

# Desenvolvedores | Adicionar firmware personalizado a Innioasis Updater CE - Innioasis downloads de firmware

Para desenvolvedores de firmware

# Adicione seu firmware a Updater CE.

Updater CE é o catálogo da comunidade e instalador para firmware personalizado. Desenvolva seu projeto a partir de uma base ROM, publique-o como um repositório público com os ativos de lançamento corretos, adicione as entradas do modelo ao `slidia_manifest.xml`, test the model filters, and open a pull request. One repository can serve every model it supports.[Ver a fonte Updater CE](https://github.com/y1-community/Innioasis-Updater)[Procure downloads de software](firmware_pt-BR.html)

## Comece de uma base ROM

As ROMs básicas oferecem aos desenvolvedores de firmware personalizado uma base Android limpa com os chips de rádio sem fio habilitados. No Y1 eles habilitam Wi-Fi e GPS junto com Bluetooth e FM de fábrica; no Y2 eles habilitam Wi-Fi, GPS e FM junto com o Bluetooth de fábrica.Downloads básicos ROM para desenvolvimento de firmware personalizado, com a versão Android e recursos sem fio que cada um permite[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom.zip)[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom_type_b.zip)[``](https://github.com/y1-community/y2-ata-rom/releases/download/y2-ata/rom_y2.zip)

| Baixar | Dispositivo | Android | Recursos sem fio |
| --- | --- | --- | --- |
| rom.zip | Y1 · Type A | Android 4.2.2 | Adiciona Wi-Fi e GPS ao Bluetooth e FM de fábrica (FM já funciona no Y1 de fábrica). Para Y1 players fornecidos com OS 2.0.0 ou posterior. |
| rom_type_b.zip | Y1 · Type B | Android 4.2.2 | Adiciona Wi-Fi e GPS ao Bluetooth e FM de fábrica (FM já funciona no Y1 de fábrica). Para Y1 players fornecidos com um sistema operacional anterior a 2.0.0. |
| rom_y2.zip | Y2 | Android 4.4.2 | Adiciona Wi-Fi, GPS e FM ao Bluetooth de fábrica. O chip de rádio Y2 está totalmente habilitado, então FM também está disponível aqui. |

Essas imagens são a base padrão do Android (AOSP) com os rádios sem fio do dispositivo habilitados, portanto, um firmware personalizado pode adicionar recursos de rede em vez de substituir a pilha de rádio. Eles são o ponto de partida prático para as etapas de publicação abaixo.

## Use estes nomes de recursos de lançamento

O nome do arquivo faz parte do sinal de compatibilidade. Mantenha os nomes exatos e coloque os arquivos ZIP nos ativos de lançamento do projeto, não apenas na árvore de origem do repositório.Nomes de ativos ZIP de firmware e dispositivos suportados``````

| Ativo | Dispositivo | Hardware | Significado |
| --- | --- | --- | --- |
| rom.zip | Y1 | Type A | Y1 dispositivos fornecidos com OS 2.0.0 ou posterior. |
| rom_type_b.zip | Y1 | Type B | Y1 dispositivos fornecidos com um sistema operacional anterior a 2.0.0. |
| rom_y2.zip | Y2 | Y2 | O pacote de instalação completa Y2. Mantenha-o separado dos Y1 ativos. |
Não renomeie um pacote para ajustá-lo a outro modelo. Y1 e Y2 usam arquivos de plataforma MediaTek diferentes e configurações de atualização. Publique o pacote para o hardware que ele realmente suporta.

## Como funciona a conexão

Updater CE lê o manifesto como seu catálogo. Cada `<package>` linha informa o nome do projeto, repositório, modelo e manipulador. Quando um usuário escolhe esse projeto, o Updater verifica as versões publicadas do repositório e procura um `rom*.zip` ativo.

### Manifesto

Nomeia o projeto e o mapeia para um modelo. Y1 e Y2 precisam de linhas separadas, mesmo quando compartilham um repositório.

### Lançamento publicado

Contém os ativos ZIP instaláveis. Uma única versão pode conter os pacotes Y1 Type A, Y1 Type B e Y2 juntos.

### Updater CE instalar

Usa o modelo selecionado para escolher o pacote correspondente e o caminho intermitente específico do modelo. O usuário não deve ter que adivinhar o nome do arquivo.

## Publique um projeto em cinco etapas
  - Bifurque o repositório Updater CE. Crie seu próprio garfo de [y1-community/Innioasis-Updater](https://github.com/y1-community/Innioasis-Updater)e clone seu fork localmente.
  - Prepare um repositório de firmware público. Certifique-se de que o repositório seja público e que sua versão contenha os ativos ZIP corretos. Você pode colocar `rom.zip`, `rom_type_b.zip`, e `rom_y2.zip` na mesma versão quando pertencem à mesma versão.
  - Edite o manifesto. Abrir `slidia_manifest.xml` na raiz do seu fork Updater CE. Adicione uma linha para cada modelo que a versão suporta (Y1 e Y2 são o par comum). O `repo` o valor é o do repositório `owner/repository`; `url` é a página pública do projeto.
  - Teste o catálogo. Execute o Updater no checkout editado. Selecione Y1 e confirme se o projeto mostra os ativos Y1. Selecione Y2 e confirme que mostra a liberação Y2. Verifique Type A e Type B separadamente quando ambos forem publicados.
  - Abra uma solicitação pull. Envie a alteração do manifesto para seu fork e abra uma solicitação pull no repositório upstream Updater CE. Inclua o link do projeto, os modelos suportados, a etiqueta de lançamento, os nomes dos ativos e os dispositivos que você testou.

## Gere suas linhas de manifesto

Preencha o repositório e marque todos os modelos que o lançamento suporta. O gerador escreve um `<package>` linha por modelo e inclui apenas os atributos que você definiu, então o resultado corresponde ao atual `slidia_manifest.xml` formatar. Cada leitura de atributo Updater CE está disponível abaixo - os opcionais estão em Mais opções.URL do repositórioO repositório público GitHub. O gerador extrai `owner/repository` do URL.Nome do softwareExibido no aplicativo e no catálogo do site.URL do projetoPágina voltada para humanos do projeto ou suas notas de lançamento.MarcaDesmarque para usar a marca padrão do modelo. SR1, Q3, Q5 e Q3e são modelos Timmkoo.Dispositivos (uma linha cada)Y1Y2A5G1G3G5R1PR1SR1Q3Q5Q3eOutros modelosPara um modelo que não está listado acima. Os modelos conhecidos mantêm a grafia do catálogo.Bandeiras`do_not_keep_data` — nunca ofereça Keep Data para este firmwareConstruído a partir do software original — acrescenta `derivative="y1-community/y1-stock-rom"`

Keep Data só é oferecido quando o firmware recebido e o firmware instalado são iguais ou compartilham um `derivative` raiz. Use o sinalizador somente quando os dados do usuário realmente não puderem ser transferidos.Mais opções: ícone, arte, recursos de lançamento, pós-instalação e espelhos

#### Ícone e arteArquivo de íconeEscolha a imagem que você irá enviar para o repositório. Isso o visualiza e cria seu URL bruto; não carrega nada.Caminho do ícone no repositórioCaminho para a imagem confirmada, relativa à raiz do repositório.Ramo de íconeURL do íconeUm URL de imagem direto. Quando vazio, o aplicativo usa o lançamento `updater.png` ou um ícone gerado.Visualização do ícone selecionado

URL do ícone do modo escuroÍcone opcional de tema escuro. `image_dark` é um alias aceito.URL de arte claraArte secundária, tentada após a imagem de lançamento e `icon`.URL da arte escura

#### Liberar ativosLiberar nome do ativoUm nome para cada modelo selecionado. Deixe vazio para usar `rom.zip` em Y1 e `rom_<model>.zip` em outro lugar.Padrão de ativosGlob usado quando os zips do lançamento não são nomeados `rom*.zip`.Type A ativoGlob para o pacote Y1 Type A quando seu nome não diz isso.Type B ativoGlob para o pacote Y1 Type B quando seu nome não diz isso.Versão mínima do aplicativoOculte a entrada de compilações Updater CE mais antigas.

#### Links, espelhos e família Keep DataPágina pós-instalaçãoAberto após uma instalação bem-sucedida.Segunda página pós-instalaçãoSegunda etapa opcional para um guia de configuração de várias páginas.Espelhos zip portáteisSeparados por vírgula `*-mirror` repositórios que constroem pacotes Portable Flashing Zip.Repositório derivadoO firmware a partir do qual esta versão foi criada. Firmwares relacionados compartilham uma partição de dados, que é o que o Keep Data verifica.Repositório de informaçõesApp repo whose releases describe the apps in this firmware. Ele também precisa de uma página de pós-instalação.APK repositórioRepositório de aplicativos cujo APK o aplicativo é baixado e instalado após o firmware.

#### Extras do catálogoLesmaIdentificador estável para links e registros de instalação salvos. O modelo é anexado automaticamente quando vários modelos são selecionados.Descrição`<package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y1" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" /> <package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y2" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" />`Copiar linhas

Carregando o manifesto mais recente…Visualize o manifesto mais recente com suas linhas adicionadas

O gerador buscou a corrente `slidia_manifest.xml` deste repositório e inseriu suas linhas geradas pouco antes `</slidia>`.

Uma linha não é suficiente para um repositório compartilhado. Se a linha Y2 estiver faltando, os usuários Y2 não obterão uma entrada correspondente ao modelo, mesmo quando `rom_y2.zip` existe no lançamento do projeto. The same is true for every other model your release supports.

### Cada atributo que o manifesto lê

Estes são os atributos que as compilações atuais Updater CE entendem. O gerador grava apenas aqueles que você preenche; o aplicativo volta aos padrões sensatos para o resto.Atributos do pacote slidia_manifest.xml e seu significado``````````````````````````````````````````````````````````````````````````````````````````````

| Atributo | Necessário | O que isso faz |
| --- | --- | --- |
| name | Sim | Nome do software mostrado no catálogo e nos cartões de instalação. |
| repo | Sim | owner/repo. O aplicativo lê as versões GitHub desse repositório. |
| device | Sim | Modelo de destino, letras maiúsculas (Y1, Y2, G1, Q3e,…). Mantenha uma entrada por modelo. |
| url | Recomendado | Página do projeto ou notas de lançamento abertas no catálogo. |
| type, handler | Sim, na prática | type="img" e handler="Custom Firmware". Outros tipos e manipuladores que não sejam de firmware são ignorados. |
| brand | Opcional | Marca do catálogo (Innioasis, Timmkoo). Vazio usa a marca padrão do modelo. |
| package_name | Opcional | Liberar nome do arquivo do ativo. O padrão é rom.zip em Y1 e rom_<model>.zip em outros modelos. |
| asset_pattern | Opcional | Glob que não diferencia maiúsculas de minúsculas para versões cujos zips de firmware não são nomeados rom*.zip (por exemplo my-firmware-*.zip). |
| type_a_asset, type_b_asset | Opcional | Globs que identificam os zips Y1 Type A e Type B quando seus nomes de arquivos não contêm os marcadores usuais. |
| icon | Opcional | URL do logotipo. Usado após o próprio lançamento updater.png / updater.jpge como substituto para cada versão. |
| icon_dark | Opcional | Logotipo com tema escuro. image_dark é um alias aceito. |
| image | Opcional | Arte de luz secundária, tentada depois icon. |
| post_install, post_install2 | Opcional | Página(s) abertas após uma instalação bem-sucedida. O segundo cobre um guia de várias etapas. |
| portable_zips | Opcional | Separados por vírgula *-mirror repositórios que publicam pacotes portáteis prontos para execução. |
| derivative | Opcional | Repositório a partir do qual o firmware é construído. Firmware with the same derivative root can keep user data. |
| info_repo | Opcional | Repositório de aplicativos cujas versões descrevem o que o firmware implanta. Requer post_install ou post_install2. |
| apk_repo | Opcional | Repositório de aplicativos cujo APK o aplicativo é instalado após o firmware. |
| min_version | Opcional | Oculte a entrada quando Updater CE for anterior a esta versão. |
| do_not_keep_data | Opcional | true (também 1 / yes) bloqueia Keep Data completamente para este firmware. |
| slug | Opcional | Stable identifier for links and saved install records. Gerado a partir do nome e do modelo quando vazio. |
| description | Opcional | Breve descrição do catálogo. Pode ser o valor do atributo ou o texto do elemento. |

Os nomes legados ainda são lidos para fins de compatibilidade: `model`, `package`, `portable_zip`, `post_install_2`, `min_app_version` e `image_dark`. Novas entradas devem usar os nomes atuais acima.

### Envie as linhas como uma solicitação pull
  - Copie as linhas geradas acima. Eles já correspondem ao formato de manifesto mais recente.
  - Editar `slidia_manifest.xml` no repositório. Use o link de edição abaixo; o host do repositório cria um fork e um branch para você automaticamente.
  - Cole as linhas antes `</slidia>`, mantendo as entradas existentes inalteradas.
  - Comprometa-se com uma nova filial (por exemplo `add-your-firmware`) e, em seguida, abra uma solicitação pull no repositório Updater CE.
  - No PR, inclua o link do projeto, modelos suportados, etiqueta de lançamento, nomes de ativos e os dispositivos que você testou.
[Edite o manifesto Updater CE](https://github.com/y1-community/Innioasis-Updater/edit/main/slidia_manifest.xml)[Veja o último manifesto](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)

Mantenha os nomes dos modelos em maiúsculas, use a URL exata do seu repositório público e mantenha `type="img"` e `handler="Custom Firmware"` para uma entrada de firmware.

## Torne o lançamento fácil de verificar

Dê ao lançamento uma etiqueta clara e uma nota de lançamento. A tag é útil para as pessoas, mas os nomes dos ativos ZIP são o que Updater CE usa para identificar os pacotes de instalação.

### Lista de verificação de lançamento
  - Publique o lançamento publicamente.
  - Anexe os arquivos ZIP como recursos de lançamento.
  - Indique o modelo suportado e Type A ou Type B nas notas.
  - Liste qualquer preparação necessária ou limites conhecidos.

### Um lançamento, três ativos

Uma versão compartilhada pode conter `rom.zip`, `rom_type_b.zip`, e `rom_y2.zip`. O atualizador os classifica separadamente e escolhe entre os filtros de modelo e hardware.

### Não agrupe suposições

Não inclua um pacote Y1 sob o nome do arquivo Y2, nem adicione dados de dispersão, pré-carregador ou partição não testados apenas para fazer um ativo aparecer.

## Por que as entradas do modelo são importantes durante o flash

O manifesto não é apenas um menu de download. Após a extração, Updater CE usa o modelo resolvido para preparar o caminho de instalação correspondente. Y1 e Y2 têm diferentes arquivos de plataforma, pré-carregadores, configuração de dispersão e layouts de dispositivos.
  - Y1: o atualizador prepara o caminho Y1 e usa as partições nomeadas do dispositivo quando MTKClient é usado.
  - Y2: o atualizador prepara o caminho Y2 e usa a configuração Y2 MT6582. A recuperação completa pode usar endereços físicos dos dados de dispersão corretos do modelo.
  - Suporte multiplataforma: Updater CE lida com flashing nativo diretamente no Windows, Linux e macOS (com suporte para Macs Intel e Apple Silicon) sem ferramentas extras de flash.
Os contribuidores devem fornecer arquivos de firmware corretos, não compensações de flash. Não edite endereços de dispersão, pré-carregadores, arquivos DA ou comandos de partição para solucionar um pacote incorreto. Corrija o ativo de lançamento e teste no modelo pretendido.

## Antes de solicitar uma mesclagem
  - Valide o XML com um analisador XML. Uma citação ou fechamento ausente `/>` pode ocultar todas as entradas depois dela.
  - Inicie o atualizador em seu checkout para que ele carregue o manifesto local antes da atualização remota.
  - Verifique Y1 e Y2 independentemente. Confirm that the project appears only where its package is supported.
  - Confira a lista de lançamentos `rom.zip`, `rom_type_b.zip`, e `rom_y2.zip` conforme aplicável.
  - Teste a instalação real no dispositivo pretendido, com um cabo de dados USB confiável e um plano de recuperação para retornar ao software original.
  - Na solicitação pull, explique o que você testou. Não descreva um modelo não testado como suportado.
`python -c "from xml.etree import ElementTree as ET; ET.parse('slidia_manifest.xml'); print('manifest ok')"`

Para uma verificação local, execute esse comando na raiz do repositório. Ele verifica apenas a sintaxe XML; isso não prova que uma versão contém firmware válido ou que um dispositivo é seguro para flash.

## Links úteis do projeto[Garfo Updater CE](https://github.com/y1-community/Innioasis-Updater/fork)[Veja o manifesto](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)[Notas de contribuição da comunidade](support_devs_pt-BR.html)[Solução de problemas](troubleshooting_pt-BR.html)

## Habilidades de modificação para agentes de IA

O repositório `skills/` diretório é uma base de conhecimento baseada em fontes para agentes que trabalham em Y1 e Y2 hardware, firmware, temas e aplicativos. Cada habilidade nomeia os arquivos do projeto de onde vêm suas reivindicações, para que um agente possa verificar um fato antes de alterar um dispositivo.Comece aqui

### [Índice de competências e regras de segurança](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/README.md)

Como carregar uma habilidade, a qual modelo um fato se aplica e as partições que nenhum pacote deve gravar.Hardware

### [Y1 hardware](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y1-hardware/SKILL.md)

MT6572, a roda como eventos principais, display 480x360, caminhos FM/áudio, armazenamento e mapa de partição Type A/B.Hardware

### [Y2 hardware](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y2-hardware/SKILL.md)

Placa MT6582, árvore de dispositivos, painéis GC9503V/ST7701S, trilhos PMIC/DAC, partições e imagem de inicialização.Firmware

### [Pacotes de firmware](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/firmware-packages/SKILL.md)

rom.zip anatomia, arquivos dispersos, contratos de atualização Classe A e lista de verificação de lançamento.Temas

### [Criação de tema e skin](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/theme-authoring/SKILL.md)

Y1 temas config.json, Rockbox WPS/SBS, Reborn skins e Y2Player formato de skin v2.Todas as habilidades

### [Navegue pela pasta de habilidades](https://github.com/y1-community/Innioasis-Updater/tree/main/skills)

Rockbox Y1/Y2, estoque de ROMs Android, Y2Linux, aplicativos Android, iniciadores, notas de lançamento e publicação de sites.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
