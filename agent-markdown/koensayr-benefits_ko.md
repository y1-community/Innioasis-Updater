---
title: "Innioasis Y1에 Koensayr을 사용하는 이유 | Koensayr 혜택 - Innioasis 펌웨어 다운로드"
description: "Koensayr 재고 Y1 펌웨어 패치: 인터페이스 변경 없이 아티스트-앨범 탐색 및 AVRCP 1.3 Bluetooth 메타데이터 및 자동차 스테레오 제어."
language: "ko"
source: "https://innioasis.app/koensayr-benefits_ko.html"
---

# Innioasis Y1에 Koensayr을 사용하는 이유 | Koensayr 혜택 - Innioasis 펌웨어 다운로드

맞춤형 소프트웨어 · Koensayr

# Innioasis Y1이(가) Koensayr인 이유

Koensayr 당신이 알고 있는 인터페이스를 유지하고 당신을 짜증나게 하는 것을 해결합니다. 음악은 아티스트별로 탐색되며 Bluetooth는 트랙 이름을 표시하고 자동차 컨트롤과 함께 작동합니다.[업데이터에서 Koensayr 가져오기](guide_ko.html?model=Y1&software=koensayr-y1)[Y1 설치 페이지](koensayr-y1-software_ko.html)

## 모델 가용성

어떤 Innioasis 모델이 이를 실행합니까?[Y1 · 사용 가능](koensayr-y1-software_ko.html)Y2 · 사용할 수 없음

Y1 및 Y2 빌드는 별개이므로 소프트웨어 다운로드에서 플레이어용으로 만들어진 빌드를 선택하세요. 서로 바꾸지 마세요.

## 사람들이 그것을 선택하는 이유

스톡 플레이어를 유지하세요. 불편한 부분을 수정해보세요.
  - 아티스트 → 앨범 탐색 — 스톡 음악 앱에는 누락된 아티스트-앨범 흐름이 추가되었습니다. 더 이상 폴더를 뒤질 필요가 없습니다.
  - 자동차에서 작동하는 블루투스 — 사양 호환 AVRCP 1.3 메타데이터 및 컨트롤: 헤드 유닛에서 트랙 제목, 재생 헤드, 반복/셔플 상태를 볼 수 있습니다.
  - 실제로 페어링되는 페어링 — 자동 페어링 수정을 포함하여 자동차 스테레오 및 헤드셋에 맞게 조정된 오디오 및 페어링 구성입니다.
  - 필요할 때 루팅하세요 — adb 에스컬레이션을 위해 최소 setuid su가 설치되어 진단 및 수정에 유용합니다.
  - 덜 부풀어 오르다 — 한 번도 사용하지 않는 시스템 앱이 제거되어 RAM을 확보하고 백그라운드 작업을 줄입니다.
  - 학습 곡선 없음 — 인터페이스는 Y1 인터페이스입니다. Koensayr 외모가 아니라 행동을 바꿉니다.

## 커뮤니티

커뮤니티에서 말하는 내용

Koensayr은 기본 Y1 인터페이스를 좋아하고 불편한 부분을 수정하고 싶은 사람들을 위한 소프트웨어입니다. 그 이름은 스타워즈 딥컷입니다. Koensayr는 Y-Wing을 만들었고 Y-Wing은 Y1으로 연결됩니다.

커뮤니티에서 가장 많이 회자되는 승리는 Bluetooth입니다. 차량 스테레오 및 헤드셋(AVRCP 1.3)에 대한 적절한 추적 메타데이터 및 제어 기능이 있는데, 이는 기본 소프트웨어에서 잘못된 것으로 유명합니다. 당신이 차에 살고 있다면 사람들이 가리키는 소프트웨어가 바로 이것이다.
  - [r/innioasis · Koensayr 및 자동차 블루투스](https://www.reddit.com/r/innioasis/)

## 프로젝트가 제공하는 것
  - 아티스트 → 앨범 탐색이 시스템 음악 APK에 패치되었습니다.
  - AVRCP 1.3 메타데이터 및 제어: 전체 트랙 메타데이터, ms-precision 플레이헤드, 트랙 및 배터리 알림, 양방향 반복/셔플
  - Bluetooth 페어링 수정 사항: 자동차 및 헤드셋 페어링을 위한 audio.conf, auto_pairing.conf, blacklist.conf 및 build.prop 편집
  - adb 에스컬레이션을 위한 최소 setuid su를 통한 루트 액세스 재고 adbd는 그대로 유지됩니다
  - 시스템 디블로트 - 사전 설치된 블로트웨어 제거
  - build.prop의 선택적 ADB 활성화
  - 실제 하드웨어에서 Bluetooth 동작을 조사하기 위한 진단 도구

## 먼저 알아야 할 사항
  - 현재는 Y1만 가능하며 기본 인터페이스를 유지합니다. 런처가 아닌 패치 프로그램입니다.
  - 가장 기술적인 경로입니다. 패치 프로그램은 Linux 호스트에서 실행되고 MTKClient을 통해 플래시되므로 자신감 있는 사용자에게 적합합니다.
  - 이 프로젝트는 알려진 재고 소프트웨어만 패치합니다. 소프트웨어 버전이 일치하는지 확인하세요.
  - 마음이 바뀌면 모델의 원본 소프트웨어를 복원하는 것이 여전히 가능합니다.

## 시작하기

Updater에서 Y1을 선택하고 Koensayr을 선택한 후 릴리스 노트를 따릅니다. 튜토리얼에서는 패치 프로그램 흐름을 순서대로 안내합니다.[Koensayr 릴리스 찾아보기](firmware_ko.html?model=Y1&software=koensayr-y1)[Y1 튜토리얼](guides/koensayr-y1.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
