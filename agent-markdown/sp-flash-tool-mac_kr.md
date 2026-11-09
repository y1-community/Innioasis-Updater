---
title: "Mac용 SP Flash Tool · MediaTek 스캐터 플래싱 가이드 및 대안"
description: "Updater CE를 사용하여 Mac에서 SP Flash Tool을 사용하고 Mechen H1, Innioasis Y1/Y2, Timmkoo 및 MT6580/MT6572 MP3 플레이어 및 휴대폰과 같은 플래시 MediaTek 장치에 분산 파일을 찾아보는 방법입니다."
language: "kr"
source: "https://innioasis.app/sp-flash-tool-mac_kr.html"
---

# Mac용 SP Flash Tool · MediaTek 스캐터 플래싱 가이드 및 대안

MediaTek 도구 및 크로스 플랫폼 플래싱

# Mac용 SP Flash Tool: 전체 가이드 및 Scatter Browser

공식 MediaTek SP Flash Tool이 macOS에서 실행되나요? 정확한 상태는 다음과 같습니다. 업데이터 CE Mac에서 기본 MediaTek 플래싱을 제공하고 분산 기반 MediaTek MP3 플레이어 또는 스마트폰을 플래싱하는 방법을 제공합니다.

## macOS의 SP Flash Tool에 대한 진실

MediaTek 공식 macOS 빌드를 출시한 적이 없습니다. 스마트폰 플래시 도구 (SP Flash Tool). 이 도구는 32비트/64비트 Windows 애플리케이션과 x86_64 Linux 바이너리로만 존재했습니다. macOS 커널 USB 확장이 BROM 부팅 핸드셰이크 중에 필요한 정밀도로 USB 직렬 패스스루를 허용하지 않기 때문에 Wine 또는 CrossOver를 통해 macOS에서 SP Flash Tool 에뮬레이션이 실패합니다.

해결책:업데이터 CE 자동화된 분산 검색과 함께 기본 Apple Silicon 및 Intel macOS 플래싱 라이브러리(MTKclient 하위 수준 프로토콜 엔진을 통해)를 번들로 묶어 이러한 격차를 해소합니다!

## '파일에서 설치'를 사용하여 모든 MediaTek 장치 플래싱(Scatter Browser)

업데이터 CE는 Innioasis 플레이어로 제한되지 않습니다. 필요한 모든 장치에 대해 강력한 범용 MediaTek 산란 점멸 장치로 사용할 수 있습니다. SP Flash Tool v5 이하:
  - Mechen H1 & H11: MT6580 휴대용 HiFi 안드로이드 플레이어.
  - Timmkoo Q3, Q5, G1, A5: MediaTek 터치스크린 디지털 오디오 플레이어.
  - 오일스키, 푸에트, 루오란: MediaTek MT6572 / MT6582 음악 플레이어.
  - 레거시 MediaTek 스마트폰 및 피처폰: MT6572, MT6580, MT6582, MT6735, MT6737, MT6739, MT6753 및 MT8163을 실행하는 장치.

### 업데이터 CE에서 사용자 정의 분산 파일을 로드하는 방법:
  - 공장 펌웨어 아카이브를 다운로드합니다(`.zip` 또는 `.rar`) 또는 다음이 포함된 폴더를 추출합니다. `*scatter*.txt` 파일.
  - 업데이터 CE에서 다음을 선택합니다. 파일 찾아보기… 펌웨어 선택 화면에서
  - 분산 텍스트 파일을 선택합니다(예: `MT6580_Android_scatter.txt`) 또는 펌웨어 zip 패키지.
  - Updater CE는 메모리 오프셋, 파티션 주소(프리로더, 부팅, 복구, 시스템, 사용자 데이터)를 구문 분석하고 분산 무결성을 확인합니다.
  - 화면의 실시간 프롬프트를 따르십시오. 장치의 전원을 끄고 USB 케이블을 플래시에 연결하십시오.

## 벽돌 제거를 위해 x64 컴퓨터가 필요한 경우

macOS는 표준 플래싱을 처리하고 MTKclient를 통해 사용자 정의 ROM 설치를 깔끔하게 처리하지만, 깊은 부트 루프 오류(프리로더 파티션이 지워졌거나 일치하지 않는 경우)에서 복구하려면 SP Flash Tool의 전체 파티션 테이블을 다시 빌드해야 합니다.

Mac에서 오류가 발생하는 경우 64비트 Windows PC 또는 x86_64 Linux 워크스테이션으로 전환하고 설정 > 고급 설정 표시 > 플래시 방법 > SP Flash Tool, 팩토리 스캐터 패키지를 플래시합니다.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
