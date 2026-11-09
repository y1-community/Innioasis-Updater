---
title: "Innioasis Y2 켜지지 않음 | Innioasis 펌웨어 아카이브 - Innioasis 펌웨어 다운로드"
description: "Innioasis Y2이 켜지지 않거나 충전되지 않나요? 강제로 다시 시작하고 컴퓨터에 표시되는지 확인한 다음 Y2 펌웨어를 복원하거나 수동 SP Flash Tool 복구를 사용하십시오."
language: "ko"
source: "https://innioasis.app/guides/y2-wont-turn-on_ko.html"
---

# Innioasis Y2 켜지지 않음 | Innioasis 펌웨어 아카이브 - Innioasis 펌웨어 다운로드

플레이어 회복 · Innioasis Y2

# Innioasis Y2이 켜지지 않습니다

검은 화면이 항상 죽은 플레이어를 의미하는 것은 아닙니다. 수동 플래시를 시도하기 전에 충전, 강제 재시작, 컴퓨터 감지 등을 수행하세요.[Updater CE 받기](../guide_ko.html#platform)[펌웨어 다운로드](../firmware_ko.html)[복구 가이드](recovery_ko.html)

## 다른 것보다 먼저 Y2을 올바르게 충전하십시오.

대부분의 "Y2이 켜지지 않음" 보고서는 배터리 방전, 충전 전용 케이블 또는 충분한 전류를 공급할 수 없는 충전기입니다. 전력이 많이 소모된 Y2의 전원을 켜면 화면에 아무것도 표시되기까지 20~30분 정도 걸릴 수 있습니다.
  - 알려진 USB 사용 데이터 충전 전용 케이블이 아닌 케이블입니다.
  - 벽면 충전기를 사용한 다음 허브가 아닌 컴퓨터 USB 포트에 직접 연결해 보십시오.
  - 30~60분 동안 연결한 상태로 두고 충전 아이콘이나 백라이트가 나타나는지 지켜보세요.
  - 계속 진행하기 전에 두 번째 케이블과 충전기를 사용해 보세요.

## 강제로 다시 시작

전원 버튼을 약 15초 동안 누르고 있다가 손을 떼고 5초간 기다린 후 전원을 한 번 누르세요. 이렇게 하면 중단된 부팅이 지워지고 반복해도 안전합니다.

화면에 로고가 표시되었다가 검게 변하면 플레이어가 시작되고 오류가 발생하는 것입니다. 아래의 펌웨어 복원으로 건너뛰세요. 아무 일도 일어나지 않으면 충전을 유지하고 30분 후에 다시 시도하십시오.

## 컴퓨터가 플레이어를 볼 수 있는지 확인

전원이 꺼진 Y2을 데이터 케이블로 연결하고 Windows에서 장치 관리자를 엽니다. `lsusb` Linux의 경우, macOS의 경우 MTKClient입니다. 작동 중인 플레이어는 공급업체 ID가 있는 MediaTek 장치로 나타납니다. `0e8d`. 나타나는 경우 화면이 어두워도 하드웨어가 다시 깜박일 만큼 살아 있는 것입니다.

아무것도 나타나지 않으면 먼저 Windows에 MediaTek 드라이버를 설치하십시오. [운전기사 가이드](../drivers_ko.html) Windows 및 Linux 권한을 다룹니다.

## Y2 재고 펌웨어 복원

플레이어가 감지되었으나 부팅되지 않는 경우 Y2 원본 소프트웨어를 다시 설치하십시오. Y2 패키지만 사용하세요. Y1 빌드는 Y2 하드웨어에서 시작되지 않습니다.
  - 열기 [업데이터 CE](../guide_ko.html#platform) 당신의 컴퓨터에서.
  - 세트 기기 모델 에 Y2.
  - 선택 원본 소프트웨어 안으로 소프트웨어 안정적인 Y2 릴리스를 선택합니다. 수동 패키지는 다음과 같습니다. `rom_y2.zip`.
  - 클릭 설치 / 복원 패키지를 추출해 보겠습니다.
  - Y2의 전원을 완전히 끄고, 업데이터가 요청할 때만 USB 데이터 케이블을 연결하고, 성공 메시지가 나타날 때까지 그대로 두십시오.
전력을 안정적으로 유지하세요. 플래시의 전원이 꺼지면 플레이어를 사용할 수 없게 될 수 있습니다. 먼저 충전한 후 컴퓨터에 직접 연결하세요.

## 업데이터가 플레이어를 볼 수 없는 경우 수동 복구

Updater CE에는 안내 설치를 완료할 수 없는 경우를 위한 수동 복구 도구가 포함되어 있습니다. [SP Flash Tool](../sp-flash-tool_ko.html) Windows 및 Linux x86에 번들로 제공되며 MTKClient 경로는 macOS를 포함합니다. 둘 다 모델과 일치하는 펌웨어 패키지가 필요합니다. [펌웨어 다운로드](../firmware_ko.html) 페이지.

즉석에서 분산 파일이나 오프셋을 만드는 대신 플랫폼에 맞는 도구 가이드를 따르세요. 어떤 도구로도 플레이어가 감지되지 않으면 배터리, 충전 포트 또는 보드에 결함이 있을 가능성이 높습니다.

## 그래도 시작되지 않는 경우

깜박임을 멈추고 하드웨어로 취급하십시오. 케이스를 열거나 배터리를 누르지 마세요. 모델이 있는 커뮤니티에 화면이 무엇을 하는지, 컴퓨터가 이를 감지하는지, 어떤 패키지를 사용해 보았는지 물어보세요. [Discord 커뮤니티](https://discord.gg/zHrT2zrcek) 서비스 경로를 식별하는 데 도움이 될 수 있습니다.

기본 복원은 시스템을 교체하므로 플래시하기 전에 플레이어의 내부 메모리에 저장된 모든 것을 백업하십시오. MicroSD 카드의 음악은 복원 시 영향을 받지 않습니다.

## Innioasis Y2 전원 FAQ

### 왜 내 Innioasis Y2이 켜지지 않나요?

일반적인 원인은 완전히 방전된 배터리, 충전 전용 케이블 또는 약한 충전기, 부팅을 중지하는 펌웨어 충돌 또는 하드웨어 결함입니다. 플레이어가 사망했다고 가정하기 전에 알려진 데이터 케이블을 사용하여 30분 동안 충전하십시오.

### Innioasis Y2을 강제로 다시 시작하려면 어떻게 해야 합니까?

전원 버튼을 약 15초 동안 누르고 있다가 손을 떼고 5초간 기다린 후 전원을 한 번 누르세요. 아무 것도 나타나지 않으면 충전한 채로 두고 30분 후에 다시 시도하십시오.

### 전원이 켜지지 않는 Y2을(를) 복구할 수 있습니까?

종종 그렇습니다. 컴퓨터가 여전히 MediaTek 장치를 감지하는 경우 Updater CE를 사용하여 Y2 원본 소프트웨어 패키지를 다시 설치하십시오. 감지되지 않으면 Updater CE에 포함된 SP Flash Tool 또는 MTKClient 복구 및 모델과 일치하는 Y2 펌웨어 파일을 사용하십시오.

### 깜박이기 전에 Y2을 충전해야 합니까?

예. 플래시의 전원이 꺼지면 플레이어를 사용할 수 없게 될 수 있습니다. 먼저 충전하고 허브를 통하지 않고 컴퓨터에 직접 연결하세요.

## 관련 수정 사항
  - [Y1이 켜지지 않습니다](y1-wont-turn-on_ko.html) — Y1에 대해 동일한 검사
  - [Y2 스크롤 휠이 작동하지 않습니다](y2-scroll-wheel-not-working_ko.html) — 부팅은 되지만 휠이 작동하지 않는 경우
  - [Innioasis 복구 가이드](recovery_ko.html) — 모든 증상 가이드가 한곳에 있습니다.
  - [SP Flash Tool 가이드](../sp-flash-tool_ko.html) — Windows 및 Linux에서 수동으로 깜박임
  - [설치 문제 해결](../troubleshooting_ko.html) — 실패한 플래시의 모습

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
