---
title: "Rockbox-Y2 테마: Y2에 테마 설치 및 재설정"
description: "Innioasis Y2: 테마가 .rockbox 폴더에 있는 위치에서 Rockbox-Y2 테마를 설치, 관리 및 재설정하는 방법과 빌드 호환성을 확인하는 방법."
language: "ko"
source: "https://innioasis.app/rockbox-y2-themes_ko.html"
---

# Rockbox-Y2 테마: Y2에 테마 설치 및 재설정

[← Rockbox-Y2 허브](rockbox-y2/)

Rockbox-Y2 · 테마

# Rockbox-Y2 테마

Rockbox-Y2에 테마를 설치하는 방법, 설치된 빌드와의 테마 호환성을 확인하고 테마가 제대로 표시되지 않는 경우 테마를 재설정하는 방법입니다.[Rockbox-Y2 릴리스 노트](release-notes/rockbox-y2/index.html)[커뮤니티 테마 찾아보기](https://themes.innioasis.app/)[Rockbox-Y2 설치](rockbox-y2/install.html)

## 빌드의 테마 호환성을 확인하세요.

Rockbox-Y2은 Y1 포트와 별도로 개발되었으므로 테마 호환성은 설치한 Y2 빌드 버전을 따릅니다. 확인해보세요 [Rockbox-Y2 릴리스 노트](release-notes/rockbox-y2/index.html) 테마 팩을 설치하기 전에 해당 버전에 맞게.

보다 [Rockbox-Y1 대 Rockbox-Y2](rockbox-y1-vs-y2_ko.html) 두 포트의 전체 비교를 위해.

## Y2에 테마를 설치하는 방법

테마는 숨겨진 폴더 안의 MicroSD 카드에 저장됩니다. `.rockbox` 접는 사람.
  - Rockbox-Y2을 최소한 한 번 시작하여 `.rockbox` 폴더를 MicroSD 카드에 넣으세요.
  - 테마 파일을 추출하거나 복사하세요. `.rockbox/` (그래서 `themes`, `wps`, `fonts`, 그리고 `backdrops` 에 병합하다 `.rockbox/`).
  - 플레이어에서 다음을 엽니다. 설정 → 테마 설정 → 테마 파일 찾아보기 테마를 선택하세요.

컴퓨터의 숨겨진 폴더를 보려면 다음을 누르세요. Cmd+Shift+. macOS에서는 활성화 보기 → 숨겨진 항목 Windows에서는 다음을 누르거나 Ctrl+H 리눅스에서.

## 깨진 테마를 재설정하는 방법

테마로 인해 화면을 읽기 어려운 경우 이름을 바꾸거나 테마를 삭제하세요. `.rockbox` 폴더를 MicroSD 카드에 저장하고 플레이어를 다시 시작하세요. Rockbox-Y2은(는) 새로운 항목을 생성합니다. `.rockbox` 음악을 그대로 유지하면서 기본 테마로 폴더를 만듭니다.[.rockbox 폴더](rockbox-y2/sd-card.html)[Rockbox-Y2 업데이트 중](rockbox-y2/update.html)[Rockbox-Y2 빌드 노트](rockbox-y2/resolution.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
