---
title: "Y1 (Rockbox-Y1)에 대한 Rockbox: 개요, 빌드 및 설치 가이드"
description: "Y1, Rockbox-Y1 및 rockbox-y1에 대한 Rockbox은 모두 Innioasis Y1에 대한 커뮤니티 Rockbox 펌웨어를 참조합니다. 추가되는 내용, 선택할 빌드 및 Innioasis Updater CE를 사용하여 설치하는 방법을 알아보세요."
language: "ko"
source: "https://innioasis.app/rockbox-for-y1_ko.html"
---

# Y1 (Rockbox-Y1)에 대한 Rockbox: 개요, 빌드 및 설치 가이드

[← 펌웨어 다운로드](firmware_ko.html?model=Y1&software=rockbox-y1)

Rockbox-Y1 · Innioasis Y1

# Y1에 대한 Rockbox (Rockbox-Y1)

“Rockbox”, “Rockbox-Y1” 및 “Y1에 대한 Rockbox”는 모두 Innioasis Y1에 대한 동일한 커뮤니티 Rockbox 펌웨어를 나타냅니다. 플레이어에 추가되는 내용, 선택할 빌드, Innioasis Updater CE를 사용하여 설치하는 방법은 다음과 같습니다.[Rockbox-Y1 설치](rockbox-y1/install.html)[ROM 다운로드](rockbox-y1/download.html)[서면 튜토리얼](guides/rockbox-y1.html)[Rockbox-Y1 허브](rockbox-y1/)

## 하나의 펌웨어, 여러 이름

Innioasis 업데이터 CE에서 이 펌웨어는 다음과 같이 나타납니다. Rockbox 기기 모델을 선택할 때 Y1. 가이드, 비디오 및 릴리스 노트에서도 이를 호출합니다. Rockbox-Y1 또는 Y1의 경우 Rockbox 따라서 빌드가 Y2이 아닌 Y1에 대한 것이 분명합니다.

설치하기 전에 항상 플레이어에 인쇄된 모델을 확인하십시오. Y1 및 Y2 펌웨어 패키지는 서로 바꿔 사용할 수 없습니다.

## Rockbox-Y1이(가) Y1에 추가하는 것

Rockbox-Y1은 Innioasis Y1에 대한 오픈 소스 Rockbox 음악 플레이어 펌웨어의 커뮤니티 포트입니다.
  - 태그 기반 음악 라이브러리 — 오디오 태그를 사용하여 아티스트, 앨범, 장르 및 연도별로 탐색하거나 폴더를 직접 탐색합니다.
  - 고급 오디오 재생 — 끊김 없는 재생, 크로스페이드, ReplayGain 및 전체 이퀄라이저.
  - 맞춤 테마 — 클래식 iPod 스타일 레이아웃을 포함하여 수백 개의 240p 및 360p 커뮤니티 테마 중에서 선택하세요.
  - FM 라디오 — 내장 FM 라디오 지원.
  - 선택적 추가 사항 — 지원되는 빌드에서 Wi-Fi 및 Last.fm / ListenBrainz / Maloja 스크롤을 통한 팟캐스트 다운로드.
  - 듀얼 부팅 — 지원되는 빌드에서 다시 플래시하지 않고 공장 정품 소프트웨어로 다시 전환합니다.

## 어떤 Y1 빌드를 선택해야 합니까?
  - 240p 대 360p — 240p 빌드는 클래식 320×240 Rockbox 테마에서 작동합니다. 360p 빌드는 더 선명한 480×360 Y1 테마를 사용합니다. 사용하려는 테마에 빌드 해상도를 일치시키세요([240p vs. 360p 가이드](rockbox-y1/resolution.html)).
  - Type A 대 Type B — Type A은 공장 소프트웨어 2.0.0 이상과 함께 배송된 Y1 플레이어용입니다. Type B는 이전 Y1 장치용입니다. Y1가 Type B인지 모르신다면 Type A를 선택하세요.
  - 안정적 vs. 야간 — 일상적인 청취를 위해서는 안정적인 빌드를 선택하고, 최신 변경 사항을 테스트하려면 야간 빌드를 선택하세요.

## 커뮤니티 개발자로부터 직접 다운로드

Innioasis 업데이터 CE는 항상 커뮤니티 펌웨어 개발자로부터 직접 펌웨어 패키지를 다운로드합니다([rockbox-y1/rockbox](firmware_ko.html?model=Y1&software=rockbox-y1)), 개발자 자신은 Updater CE에 소프트웨어 릴리스를 나열할 전적인 책임을 집니다.

Updater CE가 펌웨어를 자동으로 다운로드 및 설치하도록 하거나 당사에서 ROM 패키지를 다운로드할 수 있습니다. [Rockbox-Y1 다운로드 페이지](rockbox-y1/download.html) 그리고 [Rockbox ROM 다운로드 페이지](rockbox-rom-download_ko.html).[Rockbox-Y1 다운로드](rockbox-y1/download.html)[로컬 ZIP에서 설치](rockbox-y1/portable-zip.html)

## Rockbox-Y1 설치 방법
  - Innioasis 업데이터 CE를 열고 설정합니다. 기기 모델 에 Y1.
  - 선택 Rockbox 안으로 소프트웨어.
  - 안정적인 릴리스를 선택하세요(또는 야간 빌드를 활성화하여 미리보기를 테스트하세요).
  - 클릭 설치 / 복원 따라서 Updater CE는 개발자로부터 직접 패키지를 다운로드합니다.
  - Y1의 전원을 완전히 끄고 Updater CE가 메시지를 표시하면 USB 데이터 케이블로 연결하십시오.
  - 완료 메시지를 기다린 다음 플레이어의 연결을 끊고 켜십시오.

스크린샷과 자세한 설정 팁을 보려면 다음을 읽어보세요. [전체 Rockbox-Y1 튜토리얼](guides/rockbox-y1.html).

## 원본 Y1 소프트웨어 복원 중

언제든지 공장 소프트웨어로 돌아갈 수 있습니다. Y1 그리고 원본 소프트웨어 Updater CE에서 안정적인 릴리스를 선택하고 설치 / 복원. MicroSD 카드에 있는 음악은 그대로 유지됩니다. 참조 [복원 가이드](rockbox-y1/restore-stock.html) 그리고 [Y1 원본 소프트웨어 페이지](original-software-y1_ko.html).

## 자주 묻는 질문Y1의 Rockbox은 Rockbox-Y1와 동일합니까?

예. Y1에 대해 Rockbox, Rockbox-Y1, Rockbox 및 `rockbox-y1` 모두 Innioasis Y1에 대해 동일한 커뮤니티 Rockbox 포트를 참조합니다.Updater CE는 어디에서 Rockbox-Y1을 다운로드합니까?

업데이터 CE는 항상 커뮤니티 펌웨어 개발자의 자체 릴리스(`rockbox-y1/rockbox`). 개발자는 Updater CE에 자신의 소프트웨어 릴리스를 나열할 전적인 책임을 집니다.Y2에 Rockbox-Y1을(를) 설치할 수 있나요?

아니요. Y2에는 별도의 펌웨어 빌드가 있습니다. 사용 [Y2의 경우 Rockbox](rockbox-for-y2_ko.html) 대신에.Rockbox-Y1을(를) 설치하면 내 음악이 지워지나요?

아니요. 음악은 MicroSD 카드에 저장되며 플레이어의 내부 펌웨어를 업데이트해도 영향을 받지 않습니다.

## 관련 가이드

### [Rockbox-Y1 허브](rockbox-y1/)

모든 Y1 가이드: 설치, 다운로드, 테마, 복원, 듀얼 부팅 및 문제 해결.

### [Rockbox-Y1 대 Rockbox-Y2](rockbox-y1-vs-y2.html)

Y1과 Y2 Rockbox 빌드의 차이점.

### [Rockbox-Y1 테마](rockbox-y1-themes.html)

Updater CE를 사용하여 240p 및 360p 테마를 전송하는 방법.

### [Rockbox 개요](rockbox_ko.html)

Innioasis Y1 및 Y2 플레이어의 Rockbox을 소개합니다.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
