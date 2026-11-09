---
title: "Windows 10/11 앱 실행 문제 및 Smart App Control 해결 방법 - Innioasis 업데이터"
description: "Windows 10/11 또는 스마트 앱 제어로 인해 앱 실행이 중단되는 경우 여기의 해결 방법을 따르세요."
language: "ko"
source: "https://innioasis.app/notices/2026-11-07-codesigning_ko.html"
---

# Windows 10/11 앱 실행 문제 및 Smart App Control 해결 방법 - Innioasis 업데이터

2026년 10월 25일 · 2026년 12월 31일까지 · 모델: Y1,Y2

# Windows 10/11 앱 실행 문제 및 스마트 앱 제어 해결 방법

Windows 10/11 또는 스마트 앱 제어로 인해 앱 실행이 중단되는 경우 여기의 해결 방법을 따르세요.

2026년 10월 25일 · 2026년 12월 31일까지 · 모델: Y1,Y2

가양성 보고서가 Microsoft에 제출되었습니다. `installer.exe` 그리고 `InnioasisUpdater.exe` 조치를 취했지만 Windows Endpoint Protection 또는 Smart App Control이 여전히 컴퓨터의 응용 프로그램을 차단하는 경우 다음 해결 방법을 사용하십시오.

### 임시 해결 방법: 스마트 앱 제어 끄기
  - 윈도우 열기 설정 (누르다 `Win + I`).
  - 이동 개인정보 보호 및 보안 > 윈도우 보안 > 앱 및 브라우저 제어.
  - 아래에 스마트 앱 제어, 클릭 스마트 앱 제어 설정.
  - 스마트 앱 제어를 다음으로 설정하세요. 끄다. 그러면 즉시 앱이 열리고 실행될 수 있습니다.

Windows 또는 Edge에서 Updater CE를 다운로드할 수 없는 경우 추가 옵션(…) 그 다음에 유지하다 > 더 보기 > 어쨌든 유지.

### 스마트 앱 제어 다시 활성화

컴퓨터에서 가양성 정의 업데이트가 완료되면 Windows 레지스트리를 통해 스마트 앱 제어를 다시 활성화할 수 있습니다.
  - 언론 윈도우 키 + R, 유형 `regedit`을 누르고 Enter 키를 눌러 관리자 권한으로 레지스트리 편집기를 엽니다.
  - 다음으로 이동하세요: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` (또는 `Policies`).
  - 위치하고 있다 `VerifiedAndReputablePolicyState` 오른쪽 창에서.
  - 두 번 클릭 `VerifiedAndReputablePolicyState` 값 데이터를 다음으로 변경합니다.

  - `1` = 켜기(강제)
  - `2` = 평가 모드

  - 확인을 클릭하고 레지스트리 편집기를 닫은 후 컴퓨터를 다시 시작하십시오.

[Microsoft에 대한 installer.exe 보고서를 참조하세요.](https://www.microsoft.com/en-us/wdsi/submission/45d25b9c-0dd6-4d01-afd2-f0ea6b224dfd)[Microsoft에 제출된 InioasisUpdater.exe 보고서를 참조하세요.](https://www.microsoft.com/en-us/wdsi/submission/1aef842b-3fda-44e7-bcfb-1a64af3ea661)

[링크된 페이지 열기](https://innioasis.app/notices.html)

[← 모든 공지사항](index_ko.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
