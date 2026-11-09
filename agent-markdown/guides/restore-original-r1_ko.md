---
title: "Innioasis R1에서 원본 소프트웨어 복원 - 단계별"
description: "검증된 rom_r1.zip 패키지를 사용하여 Innioasis 업데이터 CE 또는 SP Flash Tool이 있는 Innioasis R1에서 공식 원본 소프트웨어를 복원하는 방법."
language: "ko"
source: "https://innioasis.app/guides/restore-original-r1_ko.html"
---

# Innioasis R1에서 원본 소프트웨어 복원 - 단계별

복원 안내 · Innioasis R1

# Innioasis R1에서 원본 소프트웨어 복원

플레이어와 함께 제공된 소프트웨어로 깔끔하게 돌아갑니다. 업데이트 실패 후, 플레이어 판매 전 또는 사용자 정의 시스템이 적합하지 않을 때마다 사용하십시오.[Updater CE 받기](../guide_ko.html#platform)[R1 다운로드](../firmware_ko.html?model=R1)[R1 수동](../manuals/r1.html)

컴퓨터에 대한 설치 가이드

## 컴퓨터를 사용하여 R1의 원본 소프트웨어를 복원하세요.

사용 중인 컴퓨터에 대한 가이드를 선택하세요. 모든 버전에는 플랫폼 설정, Updater CE 단계 및 재고로 돌아가는 방법이 있습니다.[윈도우 가이드](/install/original-r1-windows.html)[macOS 가이드](/install/original-r1-mac.html)[리눅스 가이드](/install/original-r1-linux.html)

[모든 Innioasis R1 가이드](/install/r1.html) · [모든 원본 소프트웨어 가이드](/install/original-software.html)

## 필요한 것
  - Windows, macOS 또는 Linux 컴퓨터. Updater CE은 세 가지 모두에서 실행됩니다.
  - 플레이어와 함께 제공된 USB 데이터 케이블. 충전 전용 케이블은 작동하지 않습니다.
  - 공식 `rom_r1.zip` 업데이터가 다운로드하는 패키지 또는 [R1 아카이브](../firmware_ko.html?model=R1) 손으로 플래시하는 것을 선호한다면.
  - 플레이어에서 충전하세요. 전원이 꺼진 복원은 나쁜 상황을 더욱 악화시키는 유일한 일반적인 방법입니다.

이렇게 하면 시스템이 교체되고 내부 저장소가 지워집니다. 먼저 음악, 녹음, 사진을 컴퓨터에 복사하세요.

## 경로 A: Updater CE (권장)
  - 설치 [Innioasis 업데이터 CE](../guide_ko.html#platform) 그리고 그것을 엽니다.
  - 세트 기기 모델 에 R1. 모델은 플레이어와 정확히 일치해야 합니다.
  - 선택 원본 소프트웨어 소프트웨어 목록에서
  - 릴리스를 선택합니다. 최신 안정 빌드가 안전한 기본값입니다.
  - 언론 설치 / 복원 패키지가 다운로드되고 추출되는 동안 기다립니다.
  - 플레이어의 전원을 완전히 끈 다음 업데이터에서 요청할 때만 USB 케이블을 연결하세요.
  - 성공 메시지가 나타날 때까지 플레이어나 케이블을 만지지 마십시오. 플레이어를 분리하고 시작하십시오.
"작동시키기" 위해 다른 모델을 선택하지 마십시오. R1에는 R1 패키지가 필요합니다. 혼합 모델은 플레이어가 수동 복구를 필요로 하는 방법입니다.

## 경로 B: SP Flash Tool (수동)

컴퓨터가 Updater CE을(를) 실행할 수 없거나 이미 패키지가 있고 클래식 도구를 선호하는 경우 이 방법을 사용하세요.
  - 다운로드 `rom_r1.zip` 에서 [R1 아카이브](../firmware_ko.html?model=R1) 그리고 압축을 풀어주세요.
  - 이미지 옆에 스캐터 파일을 보관하세요. 이미지의 이름을 바꾸거나 이미지를 이동하지 마세요.
  - SP Flash Tool을 열고 다음을 선택하세요. 다운로드만 가능을 클릭하고 스캐터 파일을 로드합니다.
  - 플레이어의 전원을 끄고 다운로드을 탭한 다음 케이블을 연결하십시오.
  - 연결을 끊기 전에 녹색 성공 표시를 기다리십시오.

는 [SP Flash Tool 가이드](../sp-flash-tool_ko.html) 드라이버와 Windows 프롬프트를 더 자세히 다룹니다. Linux 및 macOS에서는 Updater CE이 자체 USB 처리 기능을 제공하므로 더 쉬운 경로입니다.

## 복원 후
  - 플레이어를 연결 해제하고 자체적으로 시작되도록 하십시오.
  - 언어를 선택하고 시계를 설정하세요.
  - Wi-Fi 또는 Bluetooth를 사용하는 경우 다시 연결하세요.
  - 음악을 다시 복사하세요. 는 [환승 안내](../manuals/transfer-music.html) 폴더 이름이 있습니다.

플레이어가 시작되었지만 화면, 휠 또는 버튼이 여전히 오작동하는 경우 복원이 제대로 작동한 것입니다. 이는 소프트웨어 문제가 아니라 하드웨어 또는 설정 문제입니다. 는 [문제 해결 가이드](../troubleshooting_ko.html) 다음 정류장이에요.

## 작동하지 않는 경우

### 업데이터는 플레이어를 볼 수 없습니다

케이블을 변경한 다음 USB 포트를 변경하세요. 허브를 피하세요. Windows에서는 다음에서 MediaTek 드라이버를 설치합니다. [드라이버 페이지](../drivers_ko.html).

### 플래시가 일찍 멈춥니다.

다시 연결하고 플레이어를 충전한 후 다시 시작하세요. 다른 모델의 패키지로 전환하지 마십시오.

### 플레이어는 검은색으로 유지됩니다.

한 시간 동안 충전한 후 10초 동안 전원을 유지합니다. 아직 죽었으면 다음 글을 읽어보세요 [회복 가이드](../guides/recovery_ko.html) 다시 시도하기 전에.

## 사람들이 묻는 질문

### 내 음악이 삭제되나요?

예, 내부 저장소가 지워집니다. microSD 카드에 있는 파일은 일반적으로 남아 있지만 먼저 안전한 곳에 복사하세요.

### 나중에 Rockbox(으)로 돌아갈 수 있나요?

예. 원본 소프트웨어를 복원하는 것은 일방적인 일이 아닙니다. 해당 모델의 사용자 정의 소프트웨어 페이지에서 다시 설치할 수 있습니다.

### Type A / Type B 설정이 필요합니까?

Y1만이 그러한 선택권을 갖고 있으며 원본 소프트웨어에만 해당됩니다. 다른 모든 모델은 단일 패키지를 사용합니다.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
