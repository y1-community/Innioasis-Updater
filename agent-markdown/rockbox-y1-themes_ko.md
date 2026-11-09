---
title: "Rockbox-Y1 테마: Updater CE로 테마 전송, 240p 대 360p 및 테마 적용"
description: "Updater CE(사용 가능한 경우 자동 푸시 또는 macOS 및 Linux에서 MTKClient 플래시 후 단계별 전송 안내)를 사용하여 Innioasis Y1에 테마를 전송하는 방법과 240p 대 360p 호환성 및 테마를 적용하는 방법입니다."
language: "ko"
source: "https://innioasis.app/rockbox-y1-themes_ko.html"
---

# Rockbox-Y1 테마: Updater CE로 테마 전송, 240p 대 360p 및 테마 적용

[← Rockbox-Y1 허브](rockbox-y1/)

Rockbox-Y1 · 테마 및 업데이터 CE

# Rockbox-Y1 테마: Updater CE로 전송하고 빌드를 선택한 다음 모양을 선택하세요.

업데이터 CE는 Rockbox-Y1 테마와 글꼴을 자동으로 처리합니다. 가능할 때마다 자동으로 Y1로 전송하고, 자동으로 수행할 수 없는 경우(예: macOS 또는 Linux에 MTKClient 펌웨어를 설치한 직후) 전송 과정을 단계별로 안내합니다.[Rockbox 및 업데이터 CE 받기](guides/rockbox-y1.html)[커뮤니티 테마 찾아보기](https://themes.innioasis.app/)[240p 대 360p](rockbox-y1/resolution.html)

## Updater CE를 사용하여 테마를 Y1로 전송 중

Rockbox은(는) Y1의 내부 플래시에 펌웨어를 저장하고 테마, 글꼴 및 사용자 설정은 숨겨진 플래시에 저장됩니다. `.rockbox` 플레이어 저장소(MicroSD 카드)의 폴더에 저장됩니다. ROM을 플래싱하고 파일을 저장소에 복사하는 것은 두 가지 다른 연결을 사용하기 때문에 업데이터 CE 운영 체제 및 설치 방법에 자동으로 적응합니다.
  - Updater CE가 플레이어에 도달할 수 있을 때 자동 전송: 360p Rockbox-Y1 빌드를 설치하거나 설정에서 자동 테마 동기화를 활성화하면 Updater CE가 선별된 360p 테마와 글꼴 팩을 백그라운드에서 다운로드하고 병합합니다. Y1에 연결할 수 있게 되자마자 ADB (Android 디버그 브리지) 또는 USB 드라이브 와 `.rockbox` 폴더에 있는 Updater CE는 수동으로 zip을 추출할 필요 없이 테마와 글꼴을 플레이어에 직접 푸시합니다.
  - 무인 전송이 불가능한 경우 단계별 전송 안내(예: macOS 및 Linux의 MTKClient): Rockbox을 사용하여 깜박일 때 MTKClient macOS 또는 Linux에서 설치 방법을 사용하면 저수준 프리로더/BROM 모드에서 Y1의 전원이 꺼진 동안 플래시가 발생합니다. — Rockbox이 처음으로 생성을 부팅하기 전에 `.rockbox` 플레이어의 저장소가 컴퓨터에 마운트되기 전입니다. Updater CE는 플래시 중에 자동으로 전송을 완료할 수 없을 때마다 자동으로 설치 후 테마 및 글꼴 지원 마무리 과정을 안내합니다. 
    - Rockbox을 먼저 부팅합니다. 업데이터 CE는 필요한 경우 USB 케이블을 분리하고 Y1의 전원을 켜라는 메시지를 표시하므로 Rockbox가 한 번 부팅되고 초기화됩니다. `.rockbox` 카드의 폴더입니다.
    - USB을 통해 다시 연결: Y1을 Mac 또는 Linux PC에 다시 연결하세요. ADB를 사용할 수 있는 경우 Updater CE는 부팅된 플레이어를 감지하고 테마 및 글꼴 팩을 자동으로 푸시합니다.
    - 또는 안내된 폴더 선택기와 함께 USB 저장소 모드를 사용하세요. ADB가 활성화되지 않았거나 직접 저장소 전송을 선호하는 경우 Updater CE는 Y1에서 USB 저장소 모드로 들어가도록 안내하고, .rockbox 폴더를 선택하세요, 숨겨진 폴더 표시(Cmd+Shift+. macOS 파일 대화상자에서 또는 Ctrl+H Linux의 경우)를 선택하고 `.rockbox` Y1 드라이브에 — 그러면 Updater CE가 모든 테마와 글꼴을 제자리에 병합합니다.

  - 필요할 때마다 테마를 추가하거나 새로 고치세요. 펌웨어를 다시 플래시하지 않고도 언제든지 동일한 자동 또는 안내 전송을 실행할 수 있습니다. Updater CE를 열고 다음을 선택하세요. 설정 → Rockbox 360p 테마 설치 (Cmd+T macOS에서는 Ctrl+T Windows 및 Linux) 또는 개별 테마를 드래그합니다. `.zip` 업데이터 CE에 포함 스마트 드롭 창문.

## 240p, 360p 및 빌드에 라벨이 있는 이유

Y1 커뮤니티 빌드는 해상도 레이블과 함께 게시되며 테마 컬렉션에는 동일한 레이블이 있습니다. 240p 빌드는 이전 테마 팩과 가장 폭넓게 호환됩니다. 360p 빌드는 최신 Y1 테마 경로용으로 만들어졌습니다. 하나를 설치하고 다른 하나를 적용하는 것은 위험하지 않습니다. 텍스트가 잘리거나 요소가 누락되거나 읽을 수 없는 인터페이스로 인해 잘못된 것처럼 보일 뿐입니다.

아직 테마 기본 설정이 없으면 최신 안정 빌드와 기본 테마를 선택한 다음 해당 레이블과 일치하는 테마를 선택하세요. 그만큼 [해결 페이지](rockbox-y1/resolution.html) 더 깊어진다; 경험상 규칙은 간단합니다. 빌드 라벨과 테마 라벨이 일치해야 합니다.

## 테마가 있는 곳

테마는 MicroSD 카드에 있는 파일입니다. `.rockbox` 폴더 — 설정과 캐시를 보관하는 동일한 폴더입니다. 펌웨어 자체는 내부 플래시에 있으므로 테마를 추가, 변경 또는 제거하려면 다시 플래시할 필요가 없습니다.
  - 테마 자체 폴더를 `.rockbox/themes` 카드에.
  - 그런 다음 플레이어의 테마 설정에서 선택하고 재부팅하여 적용되었는지 확인하세요.
  - 빌드를 업데이트하기 전에 마음에 드는 테마의 복사본을 보관하세요. 이는 설치가 아닌 파일입니다.

폴더가 보이지 않으면 먼저 숨겨진 파일을 켜십시오: macOS Cmd+Shift+., Windows 보기 → 숨김 항목, Linux Ctrl+H.

## 테마 적용 순서대로
  - 먼저 Rockbox-Y1을(를) 설치하고 부팅하세요. 테마에는 실행 중인 빌드가 필요합니다.
  - 테마 폴더를 복사하세요. `.rockbox/themes` 카드에.
  - 테마 설정을 열고 테마를 선택하세요.
  - 재부팅하면 메뉴뿐만 아니라 전체 인터페이스가 선택됩니다.
  - 깨진 것처럼 보이면 다른 테마를 선택하세요. 나중에 다시 시도하려는 경우 파일이 아직 남아 있습니다.

## 인터페이스를 깨뜨린 테마 실행 취소

플레이어가 사용할 수 없는 상태로 부팅되는 경우 펌웨어를 다시 설치할 필요가 없습니다. 이름을 바꾸거나 삭제하세요. `.rockbox` 폴더를 카드에 저장하고 플레이어를 시작합니다. 빌드에서는 기본 설정과 기본 테마로 폴더를 다시 만듭니다. 음악은 그대로 유지되며 나중에 원하는 테마를 다시 복사할 수 있습니다.[.rockbox 폴더](rockbox-y1/sd-card.html)[첫 시작](rockbox-y1/first-start.html)[빌드 업데이트](rockbox-y1/update.html)

## 사람들이 묻는 질문Updater CE가 macOS 또는 Linux에 MTKClient 설치 후 테마 전송 과정을 안내하는 이유는 무엇입니까?

MTKClient은 Rockbox가 초기화를 위해 부팅되기 전에 Y1의 전원이 저레벨 프리로더/BROM 모드에서 꺼져 있는 동안 Rockbox ROM를 내부 저장소에 플래시합니다. `.rockbox` 폴더와 MicroSD 카드가 컴퓨터에 마운트되기 전입니다. Updater CE가 부팅된 플레이어에 직접 접근할 수 있을 때마다(ADB 또는 마운트된 USB 드라이브를 통해) 테마를 자동으로 전송합니다. 플래시 중에 무인 작업을 수행할 수 없는 경우 플래시 직후 안내 테마 및 글꼴 단계가 열려 Y1의 전원을 켜고 ADB 또는 USB 스토리지 모드를 통해 전송을 완료하는 데 도움이 됩니다.Y2 테마가 Y1에서 작동합니까?

아니요. 포트는 별개이며 Y2의 테마 지원은 베타 빌드를 따릅니다. 보다 [Rockbox-Y2 테마](rockbox-y2-themes_ko.html).테마는 업데이트 후에도 유지됩니까?

일반적으로 그렇습니다. 카드에 있고 플래시가 ROM을 쓰기 때문입니다. 새 빌드에서 테마 경로를 변경하는 경우 해당 레이블과 일치하는 테마를 다시 적용하세요.왜 테마가 절반만 적용되나요?

재부팅하면 일반적으로 해결됩니다. 그렇지 않은 경우 테마 파일이 불완전한 것입니다. 개별 파일을 편집하는 대신 해당 폴더를 다시 복사하세요.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
