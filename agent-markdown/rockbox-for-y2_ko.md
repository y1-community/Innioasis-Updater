---
title: "Y2 (Rockbox-Y2)에 대한 Rockbox: 개요, 빌드 및 설치 가이드"
description: "Y2, Rockbox-Y2 및 rockbox-y2에 대한 Rockbox은 Innioasis Y2에 대한 커뮤니티 Rockbox 펌웨어 포트를 참조합니다. 여기에 포함된 내용과 Innioasis Updater CE를 사용하여 설치하는 방법을 알아보세요."
language: "ko"
source: "https://innioasis.app/rockbox-for-y2_ko.html"
---

# Y2 (Rockbox-Y2)에 대한 Rockbox: 개요, 빌드 및 설치 가이드

[← 펌웨어 다운로드](firmware_ko.html?model=Y2&software=rockbox-y2)

Rockbox-Y2 · Innioasis Y2

# Y2에 대한 Rockbox (Rockbox-Y2)

Rockbox-Y2(Y2의 경우 "Rockbox"이라고도 함)은 Innioasis Y2에 대한 전용 커뮤니티 Rockbox 펌웨어 포트입니다. 자체 ROM 패키지를 사용합니다(`rom_y2.zip`)이며 Innioasis 업데이터 CE를 통해 직접 설치됩니다.[Rockbox-Y2 설치](rockbox-y2/install.html)[ROM 다운로드](rockbox-y2/download.html)[서면 튜토리얼](guides/rockbox-y2.html)[Rockbox-Y2 허브](rockbox-y2/)

## Innioasis Y2을 위해 특별히 제작되었습니다.

Innioasis 업데이터 CE에서 이 펌웨어는 다음과 같이 나열됩니다. Rockbox 언제 Y2 선택되었습니다. 해당 릴리스는 다음에 의해 게시됩니다. [spycemagic/y2-rockbox](firmware_ko.html?model=Y2&software=rockbox-y2) 패키지 이름이 있는 프로젝트 `rom_y2.zip`.

Y2에 Y1 펌웨어 패키지를 설치하지 마십시오. 선택 Y2 Updater CE에서는 릴리스 목록을 Y2 호환 빌드로만 자동 필터링합니다.

## Rockbox-Y2이 제공하는 것
  - 태그 기반 음악 라이브러리 — 오디오 파일 태그에서 앨범, 아티스트, 장르를 찾아보거나 폴더를 직접 찾아보세요.
  - 재생 제어 — 끊김 없는 재생, 크로스페이드, ReplayGain 및 이퀄라이저 설정.
  - 맞춤 테마 — Rockbox-Y2 빌드와 호환되는 테마를 설치합니다([Y2 테마 가이드](rockbox-y2-themes.html)).
  - 100% 오프라인 — 계정이나 구독 없이 MicroSD 카드의 로컬 파일을 재생합니다.
  - 간편한 공장 복원 — 언제든지 Updater CE에서 Y2 원본 소프트웨어로 돌아갑니다.

## Rockbox-Y2 릴리스 선택
  - 항상 선택 Y2 안으로 기기 모델 먼저.
  - 특정 버전을 테스트하지 않는 한 최신 릴리스를 선택하십시오.
  - 읽기 [Rockbox-Y2 릴리스 노트](release-notes/rockbox-y2/index_ko.html) 각 빌드에서 변경된 사항을 확인하세요.

## 커뮤니티 개발자로부터 직접 다운로드

Innioasis 업데이터 CE는 항상 커뮤니티 펌웨어 개발자로부터 직접 펌웨어 패키지를 다운로드합니다([spycemagic/y2-rockbox](firmware_ko.html?model=Y2&software=rockbox-y2)), 해당 개발자는 Updater CE에 소프트웨어 릴리스를 나열하는 데 전적인 책임이 있습니다.

Updater CE를 다운로드하고 플래시하도록 할 수 있습니다. `rom_y2.zip` 자동으로 다운로드하거나 당사에서 패키지를 다운로드하세요. [Rockbox-Y2 다운로드 페이지](rockbox-y2/download.html) 그리고 [Rockbox ROM 다운로드 페이지](rockbox-rom-download_ko.html).[Rockbox-Y2 다운로드](rockbox-y2/download.html)[로컬 ZIP에서 설치](rockbox-y2/portable-zip.html)

## Rockbox-Y2 설치 방법
  - Innioasis 업데이터 CE를 열고 설정합니다. 기기 모델 에 Y2.
  - 선택 Rockbox 안으로 소프트웨어.
  - 목록에서 Y2 릴리스를 선택합니다.
  - 클릭 설치 / 복원 따라서 Updater CE는 개발자로부터 직접 패키지를 다운로드합니다.
  - Y2의 전원을 완전히 끄고 Updater CE가 요청하면 USB 데이터 케이블로 연결하십시오.
  - 완료 메시지를 기다린 후 Y2의 플러그를 뽑고 켜십시오.

전체 단계별 연습을 보려면 다음을 읽어보세요. [Rockbox-Y2 튜토리얼](guides/rockbox-y2.html).

## 원본 Y2 소프트웨어 복원 중

공장 펌웨어로 돌아가려면 다음을 선택하세요. Y2 그리고 원본 소프트웨어 Updater CE에서 안정적인 릴리스를 선택하고 설치 / 복원. 참조 [복원 가이드](rockbox-y2/restore-stock.html) 그리고 [Y2 원본 소프트웨어 페이지](original-software-y2_ko.html).

## 자주 묻는 질문Updater CE는 어디에서 Rockbox-Y2을 다운로드합니까?

업데이터 CE는 항상 커뮤니티 펌웨어 개발자의 자체 릴리스(`spycemagic/y2-rockbox`). 개발자는 Updater CE에 자신의 소프트웨어 릴리스를 나열할 전적인 책임을 집니다.패키지 이름이 rom_y2.zip인 이유는 무엇입니까?

개발자는 Y2 펌웨어 아카이브의 이름을 지정합니다. `rom_y2.zip` 따라서 Y1과 혼동될 수 없습니다. `rom.zip`.Y1 테마가 Y2에서 작동합니까?

항상 그런 것은 아닙니다. Y2 빌드에 대한 릴리스 노트를 확인하고 [Rockbox-Y2 테마 가이드](rockbox-y2-themes.html).

## 관련 가이드

### [Rockbox-Y2 허브](rockbox-y2/)

모든 Y2 가이드: 설치, 다운로드, 테마, 복원, 듀얼 부팅 및 문제 해결.

### [Rockbox-Y1 대 Rockbox-Y2](rockbox-y1-vs-y2.html)

Y1과 Y2 Rockbox 빌드의 차이점.

### [Rockbox-Y2 테마](rockbox-y2-themes.html)

Rockbox-Y2에 테마를 설치하고 재설정하는 중입니다.

### [Y1의 경우 Rockbox](rockbox-for-y1_ko.html)

Innioasis Y1 포트에 대한 개요 및 설치 가이드입니다.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
