---
title: "Innioasis 및 Timmkoo 플레이어의 경우 SP Flash Tool"
description: "Windows 및 Linux에서 Innioasis 업데이터와 함께 번들로 제공되는 SP Flash Tool을 찾아 rom.zip 또는 rom_y2.zip을 추출하고 일치하는 스캐터 파일로 Innioasis Y1 또는 Y2를 플래시합니다."
language: "ko"
source: "https://innioasis.app/sp-flash-tool_ko.html"
---

# Innioasis 및 Timmkoo 플레이어의 경우 SP Flash Tool

수동 깜박임

# Innioasis 및 Timmkoo 플레이어용 플래시 도구

SP Flash Tool이(가) Innioasis 내부에 들어옵니다. 업데이터가 켜져 있습니다. [Windows](drivers_ko.html#windows) 그리고 [Linux](drivers_ko.html#linux). 당신은 이미 그것을 가지고 있습니다. 이 가이드는 Innioasis Y1 또는 Y2에서 이를 안전하게 사용하는 방법과 Timmkoo 플레이어를 위한 업데이터 경로를 보여줍니다.[업데이터 가이드로 돌아가기](guide_ko.html)[펌웨어 다운로드](firmware_ko.html)[문제 해결](troubleshooting_ko.html)

Innioasis Updater으로 시작

## 업데이터는 한 번에 전체 작업을 수행합니다.

업데이터는 한 번에 대부분의 설치를 수행합니다. 소프트웨어를 선택하고 단계를 따르면 완료됩니다. 또한 수정 사항이나 새 릴리스가 출시되는 시기도 알려줍니다. SP Flash Tool은 업데이터가 완료할 수 없는 드문 경우를 위한 업데이터 도구 키트에 있습니다. 아래 단계는 예외입니다.

## 이 도구의 용도

업데이터가 플레이어를 플래시합니다. SP Flash Tool은(는) 가드 레일이 없는 동일한 엔진입니다. 업데이터가 시작되지 않을 때, 플레이어가 연결되지 않을 때 또는 스캐터 파일에 대한 방법을 알고 있을 때 사용하십시오.먼저 업데이터를 사용해 보세요. 대부분의 설치 및 복구에 대해 안내된 내용은 다음과 같습니다. [업데이터 경로](guide_ko.html) 더 안전한 선택입니다. 필요한 이유를 알면 SP Flash Tool을 사용하고, 충전된 배터리와 USB 데이터 케이블을 준비하세요.

## Innioasis 플레이어를 위한 플래시 도구

Innioasis 업데이터는 Innioasis 플레이어를 위한 플래시 도구입니다. 모델 일치 흐름을 통해 공식 소프트웨어, 업데이트 및 복원 패키지를 설치하고 음악과 설정을 유지합니다.

### Innioasis Y1 플래시 도구

업데이터에서 Y1 릴리스를 선택한 다음 앱에서 요청할 때 전원이 꺼진 플레이어를 연결하세요. 수동 경로가 필요할 때 동일한 Y1 패키지가 SP Flash Tool와 함께 작동합니다.

### Innioasis Y2 플래시 도구

Y2에 나열된 릴리스를 선택하십시오. Y2 패키지는 Y1 패키지와 호환되지 않으므로 시작하기 전에 모델을 확인하세요.

## Timmkoo 플레이어를 위한 플래시 도구

Timmkoo 플레이어는 동일한 업데이터 설치 흐름을 사용합니다. Timmkoo의 ZIP 및 RAR 패키지를 직접 읽으므로 별도의 플래시 도구나 스캐터 파일이 필요하지 않습니다.

### Timmkoo Q5 플래시 도구

업데이터에서 Q5 모델을 선택하고 Timmkoo 패키지를 선택한 다음 설치/복원을 실행하고 프롬프트에서 플레이어를 연결합니다.

### Timmkoo Q3 및 Q3E 플래시 도구

Q3 항목은 Q3과 Q3E를 모두 포함합니다. 업데이터는 프로젝트가 게시하는 패키지에서 일치하는 파일을 선택합니다.

### Timmkoo A5 플래시 도구

패키지를 선택하기 전에 A5 모델을 선택한 다음 동일한 설치 프롬프트를 따르십시오.

## 업데이터가 저장하는 위치

SP Flash Tool은 별도의 다운로드가 아닌 업데이터 설치 폴더와 함께 제공됩니다. 필요할 때 거기에서 열어보세요.

### Windows

업데이터 설치 폴더를 열고 실행하세요. `flash_tool.exe`. 폴더는 일반적으로 다음 위치에 있습니다. `%LOCALAPPDATA%\Innioasis Updater`. 일부 설정에는 SP Flash Tool 단축키가 있는 툴킷 폴더가 포함되어 있습니다.

### Linux

번들 실행 `flash_tool` x86/x86_64의 Updater 앱 폴더 내부 바이너리. 프로젝트 설치 프로그램은 udev 규칙을 사용하여 USB 권한을 준비하므로 연결되면 플레이어가 나타나야 합니다.

### macOS

SP Flash Tool은(는) macOS에 번들로 제공되지 않습니다. 업데이터는 대신 MTKClient 경로를 사용합니다. 사용 [안내 설치](guide_ko.html) Mac에서는 SP Flash Tool을 유지하고 Windows 또는 Linux 시스템에서는 유지합니다.

이 도구는 MediaTek 다운로드 에이전트 및 모델별 구성과 함께 제공되므로 다른 곳에서 DA 또는 분산 파일을 수집할 필요가 없습니다.

## 펌웨어 준비
  - 원하는 릴리스를 선택하세요. [펌웨어 다운로드](firmware_ko.html). 선택하다 `rom.zip` Y1 또는 `rom_y2.zip` Y2에 대해.
  - ZIP을 자체 폴더에 추출합니다. Windows에서는 모두 추출을 사용할 수 있습니다. Linux에서는 아카이브 관리자를 사용하거나 `unzip` 터미널에서.
  - 스캐터 파일이 추출된 폴더에 있는지 확인하세요. 보통 이름이 붙는다 `MT6572_Android_scatter.txt` Y1 패키지의 경우 `MT6582_Android_scatter_def.txt` Y2 패키지의 경우 릴리스에서는 프로젝트 이름을 따서 이름을 지정할 수 있습니다.
모델을 별도로 유지하십시오. Y1 분산은 MT6572 장치를 설명하고 Y2 분산은 MT6582 장치를 설명합니다. 잘못된 것으로 깜박이는 것은 플레이어가 벽돌이 되는 방식입니다. ZIP 내부의 분산이 해당 모델과 일치하지 않는 경우 중지하고 해당 모델에 나열된 패키지를 대신 사용하십시오.

## 스캐터 및 플래시 로드
  - 업데이터 설치 폴더에서 SP Flash Tool을(를) 엽니다.
  - 다운로드 탭에서 선택 스캐터 로딩 파일 옆에 있는 압축을 푼 폴더에서 스캐터 파일을 선택합니다. 파티션 목록이 채워집니다.
  - 플래시 모드를 켜두세요 다운로드만 가능 의도적으로 전체 복구를 수행하지 않는 한 펌웨어 업그레이드.
  - 클릭 다운로드. 도구는 플레이어를 기다립니다.
  - 플레이어의 전원을 완전히 끈 후 USB 데이터 케이블을 연결하세요. 플레이어를 내려놓고 움직이지 마십시오.
  - 녹색 확인 표시가 나타날 때까지 기다립니다. 그런 다음 케이블을 분리하고 플레이어를 시작하십시오.

안내 경로와 동일한 USB 케이블 및 타이밍 규칙을 유지하십시오. 즉, 데이터 케이블, 허브 없음, 도구가 준비된 경우에만 연결하십시오.

## 깜박이지 않는 경우
  - 스캐터와 ZIP이 플레이어에 인쇄된 모델과 일치하는지 확인하세요.
  - 연결하기 전에 플레이어의 전원이 완전히 꺼졌는지 확인하세요.
  - Windows에서는 업데이터 설정과 함께 설치된 MediaTek 드라이버를 확인하세요. Linux에서는 프로젝트 설치 프로그램에서 udev 규칙을 확인하세요.
  - 공구가 대기 중인 경우에만 케이블을 다시 연결하십시오. 포트 경주에는 완전히 플러그를 뽑고 새로운 연결이 필요할 수 있습니다. 다운로드 딸깍 하는 소리.

그 이상의 내용은 열려 있습니다. [문제 해결](troubleshooting_ko.html). 그리고 기억하세요: 업데이터는 여전히 일반적인 경로입니다. [Y1](guides/restore-original-y1.html) 그리고 [Y2](guides/restore-original-y2.html) 복원 가이드에서도 이를 사용합니다.

## 이것이 유용했나요?

귀하의 답변은 이 가이드를 개선하는 데 도움이 됩니다.네, 유용했어요아직은 아님[개선할 수 있는 방법을 알려주세요.](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
