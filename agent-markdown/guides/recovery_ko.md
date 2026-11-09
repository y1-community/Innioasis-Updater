---
title: "Innioasis Y1 및 Y2 복구 가이드 | Innioasis 펌웨어 아카이브 - Innioasis 펌웨어 다운로드"
description: "업데이트 후 스크롤 휠이 작동하지 않거나 켜지지 않는 Innioasis Y1 및 Y2 플레이어에 대한 복구 가이드입니다. 재설정 및 펌웨어 단계."
language: "ko"
source: "https://innioasis.app/guides/recovery_ko.html"
---

# Innioasis Y1 및 Y2 복구 가이드 | Innioasis 펌웨어 아카이브 - Innioasis 펌웨어 다운로드

플레이어 회복 · Y1 및 Y2

# Innioasis Y1 및 Y2 복구 가이드

켜지지 않거나, 휠이 작동하지 않거나, 설치가 중간에 멈췄습니다. 수동 플래시로 바로 넘어가는 대신 증상부터 시작한 다음 단계를 순서대로 따르세요.[Updater CE 받기](../guide_ko.html#platform)[펌웨어 다운로드](../firmware_ko.html)[문제 해결](../troubleshooting_ko.html)

Innioasis Updater으로 시작

## 안내된 설치는 이러한 문제의 대부분을 해결합니다.

업데이터는 한 번에 이를 수행합니다. 소프트웨어를 선택하고 화면의 단계를 따르면 완료됩니다. 또한 수정 사항이나 새 릴리스가 출시되는 시기도 알려줍니다.

## 증상부터 시작하세요

이 가이드에서는 업데이트나 플래시 이후 사람들이 가장 자주 겪는 두 가지 오류를 다룹니다. 눈에 보이는 것과 일치하는 것을 고르고 순서대로 진행하세요.

### 스크롤 휠이 작동하지 않음

휠이 돌아가지만 플레이어가 이를 무시하거나 업데이트 직후에 멈췄습니다.

[Y1 스크롤 휠 가이드](y1-scroll-wheel-not-working_ko.html) · [Y2 스크롤 휠 가이드](y2-scroll-wheel-not-working_ko.html)

### 플레이어가 켜지지 않습니다

검은색 화면, 충전 안 됨 표시등 또는 로고가 나타났다가 사라집니다.

[Y1 파워 가이드](y1-wont-turn-on_ko.html) · [Y2 파워 가이드](y2-wont-turn-on_ko.html)

### 설치가 도중에 중단됨

USB 프롬프트 전후에 업데이트 프로그램이 실패했거나 릴리스 목록이 잘못된 것 같습니다.

[문제 해결 가이드](../troubleshooting_ko.html)

### 파일이 필요합니다

각 모델에 대한 원본 소프트웨어 및 맞춤형 패키지.

[펌웨어 다운로드](../firmware_ko.html)

## Y1 및 Y2 패키지는 서로 바꿔 사용할 수 없습니다.모델을 교차 플래시하지 마십시오. 에 Y1 `rom.zip` Y2 패키지가 아니고 Y2 패키지입니다. `rom_y2.zip` Y1에서는 실행되지 않습니다. 잘못된 모델을 깜박이는 것은 플레이어가 컨트롤이 작동하지 않거나 부팅 루프가 발생하는 가장 일반적인 이유 중 하나입니다.

플레이어에 인쇄된 모델을 확인한 다음 릴리스를 선택하기 전에 Updater CE에서 일치시키십시오.

## 일치하는 원본 소프트웨어를 먼저 복원하십시오.

수동 도구를 사용하기 전에 올바른 모델의 기본 펌웨어를 플레이어에 다시 설치하십시오. 이는 대부분의 업데이트 관련 휠 및 부팅 오류를 해결합니다.

Y1: Y1을 선택하고 원본 소프트웨어를 선택한 다음 안정적인 Y1 릴리스를 선택한 다음 설치/복원을 실행하세요. [전체 Y1 복원 가이드](restore-original-y1_ko.html).

Y2: Y2을 선택하고 원본 소프트웨어를 선택한 다음 안정적인 Y2 릴리스를 선택한 다음 설치/복원을 실행하세요. [전체 Y2 복원 가이드](restore-original-y2_ko.html).

업데이터에서 요청할 때만 플레이어의 전원을 끄고 USB 데이터 케이블을 연결하세요. 성공 메시지가 나타날 때까지 연결된 상태로 둡니다.

## Updater CE와 함께 제공되는 수동 복구

업데이터가 작업을 완료할 수 없는 경우 동일한 설치에 수동 도구가 포함됩니다. [SP Flash Tool](../sp-flash-tool_ko.html) Windows 및 Linux x86 시스템에 번들로 제공되며 MTKClient 경로는 macOS를 포함합니다. 둘 다 모델과 일치하는 펌웨어 패키지가 필요합니다. [펌웨어 다운로드](../firmware_ko.html) 페이지.

해당 플랫폼에 대한 가이드를 사용하고 플레이어를 충전 상태로 유지하세요. 어떤 도구도 플레이어를 전혀 감지하지 못한다면 펌웨어보다는 하드웨어에 결함이 있을 가능성이 높습니다.

## 도움을 요청할 때 포함해야 할 사항
  - 모델 — Y1 또는 Y2 —이 플레이어에 인쇄되어 있습니다.
  - 화면의 역할: 아무것도 표시되지 않음, 로고, 부팅 루프 또는 홈 화면.
  - 컴퓨터가 플레이어를 MediaTek 장치로 감지하는지 여부입니다.
  - 정확한 업데이터 메시지와 선택한 패키지.
  - 수동 도구를 포함하여 이미 시도한 것.

개인 토큰이나 관련 없는 시스템 파일을 게시하지 마십시오. 그만큼 [커뮤니티 Discord](https://discord.gg/zHrT2zrcek) 그리고 [r/innioasis](https://reddit.com/r/innioasis) 노트를 비교할 수 있는 가장 빠른 장소입니다.

## Innioasis 복구 FAQ

### 켜지지 않는 Innioasis 플레이어를 어떻게 고치나요?

알려진 데이터 케이블로 30분 동안 충전하고, 15초 동안 전원을 유지하여 강제로 다시 시작한 후 컴퓨터가 감지하는지 확인합니다. 그렇다면 모델과 일치하는 원본 소프트웨어를 복원하십시오. 그렇지 않은 경우 Updater CE에 포함된 수동 복구 도구를 사용하십시오.

### Y1 또는 Y2 스크롤 휠이 작동하지 않는 이유는 무엇입니까?

업데이트 후 휠이 멈춘 경우 이는 일반적으로 펌웨어 불일치입니다. 모델과 일치하는 원본 소프트웨어를 다시 설치하고 다시 테스트하십시오. 모든 펌웨어에서 휠이 작동하지 않으면 하드웨어 결함으로 처리하십시오.

### 복구용 펌웨어는 어디서 다운로드합니까?

innioasis.app/firmware.html의 펌웨어 다운로드 페이지는 각 모델에 대한 원본 및 사용자 정의 패키지를 호스팅합니다. 항상 플레이어와 일치하는 Y1 또는 Y2 패키지를 선택하세요.

### Updater CE에는 어떤 복구 도구가 포함되어 있나요?

Updater CE에는 일반 설치를 완료할 수 없는 경우 수동 복구를 위한 Windows 및 Linux의 SP Flash Tool 및 macOS를 포함한 MTKClient 경로가 포함되어 있습니다.

## 관련 수정 사항
  - [Y1 스크롤 휠이 작동하지 않습니다](y1-scroll-wheel-not-working_ko.html) — 업데이트 후 반응이 없는 클릭 휠
  - [Y2 스크롤 휠이 작동하지 않습니다](y2-scroll-wheel-not-working_ko.html) — Y2에 대한 동일한 검사
  - [Y1이 켜지지 않습니다](y1-wont-turn-on_ko.html) — 충전, 재시작 및 수동 복구
  - [Y2가 켜지지 않습니다](y2-wont-turn-on_ko.html) — Y2에 대한 동일한 검사
  - [SP Flash Tool 가이드](../sp-flash-tool_ko.html) — Windows 및 Linux에서 수동으로 깜박임

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
