---
title: "펌웨어 설치 및 재고 복원 가이드 | Innioasis 업데이터 CE - Innioasis 펌웨어 다운로드"
description: "Innioasis 업데이터 CE를 사용하여 Innioasis Y1, Y2, G1, G3, G5, R1, PR1 및 Timmkoo Q5, Q3에 사용자 정의 펌웨어를 설치하거나 공식 공장 기본 펌웨어를 복원하십시오."
language: "ko"
source: "https://innioasis.app/firmware-guide_ko.html"
---

# 펌웨어 설치 및 재고 복원 가이드 | Innioasis 업데이터 CE - Innioasis 펌웨어 다운로드

펌웨어 설치 및 재고복원 안내

# 장치에 펌웨어 설치 또는 복원

플레이어에 인쇄된 모델을 선택하세요. 그런 다음 Updater CE의 단계를 따르세요. 나머지는 처리합니다.[Updater CE 받기](guide_ko.html#platform)[펌웨어 아카이브 찾아보기](firmware_ko.html)[문제 해결](troubleshooting_ko.html)

플레이어에 인쇄된 모델과 원하는 소프트웨어를 선택한 다음 이 가이드를 엽니다. [모델별로 소프트웨어 및 재고 펌웨어 찾아보기](firmware_ko.html).

## 

[Updater CE 받기](guide_ko.html#download-updater)[전체 서면 튜토리얼](guide_ko.html)

## Innioasis Updater CE 획득

아직 Updater CE를 받지 않은 경우 시작하는 방법은 다음과 같습니다.Updater CE에서 받기안내 설치

### Windows

설치 프로그램을 다운로드하고 열고 설치 메시지를 따릅니다.[드라이버 다운로드 및 설치](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[앱 및 드라이버 다운로드](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)[Edge에 의해 차단되었나요?](#)

Windows에서 앱 실행이 중지되거나 실행되지 않는 경우 설정을 열고 개인정보 및 보안 → Windows 보안 → 앱 및 브라우저 제어를 클릭한 후 스마트 앱 제어를 끄세요. [Windows에서 앱이 실행되지 않습니까? 돕다](#smart-app-control)

제대로 작동하려면 설치 후 PC를 재부팅해야 합니다.

### macOS

앱을 다운로드하고 애플리케이션으로 이동하세요. macOS가 이를 차단하는 경우 시스템 설정, 개인 정보 보호 및 보안을 차례로 열고 어쨌든 열기를 클릭합니다. [작동 방식](https://support.apple.com/en-gb/102445#openanyway)[Updater CE 다운로드](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

### Linux

Intel 및 AMD 시스템용 AppImage를 다운로드하여 실행 가능하게 만들고 실행합니다.[Intel/AMD용 AppImage 다운로드](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)[Linux 설정 참고 사항](drivers_ko.html#linux)또 다른 플랫폼?

더 긴 컴퓨터 설정 참고 사항이 필요하십니까? 열기 [Windows](drivers_ko.html#windows) 또는 [Linux](drivers_ko.html#linux) 설정 가이드.

## 원래 소프트웨어로 돌아가기

돌아가려면 모델을 선택하고 원본 소프트웨어, 그런 다음 실행 설치 / 복원. 그게 전부입니다. 업데이터는 시스템 소프트웨어를 교체합니다.[Y1 복원 가이드](guides/restore-original-y1.html)[Y2 복원 가이드](guides/restore-original-y2.html)

## 모델별 소프트웨어 가이드

모델을 선택한 다음 소프트웨어 가이드를 엽니다.

### Innioasis Y1

Y1용 소프트웨어:

### Innioasis Y2

Y2용 소프트웨어:

두 도구에 대한 참고 사항

## 어떤 도구를 사용해야 합니까?

Innioasis 업데이터 CE 플레이어를 업데이트하는 가장 안전한 방법입니다. 음악, 비디오 및 Bluetooth 페어링을 유지합니다. 업데이트가 준비되면 알려줍니다. Windows, macOS 및 Linux에서 실행됩니다. Innioasis Universal Flash Tool은 플레이어를 지우고 더 적은 수의 컴퓨터에서 작동합니다.[전체 비교 열기](updater-comparison_ko.html)

### Windows에서 앱이 실행되지 않습니까? 스마트 앱 제어를 끄는 방법

Windows Defender SmartScreen 또는 Smart App Control은 서명 평판이 전파되기 전에 새로 다운로드한 커뮤니티 응용 프로그램을 차단할 수 있습니다. Smart App Control은 현재 Epic Overlay Service(Fortnite에서 사용)와 같은 인기 애플리케이션에 영향을 미치고 있습니다. Updater CE는 안전하고 사용이 검증되었습니다. Smart App Control을 끄면 Updater CE가 정상적으로 열리고 실행될 수 있습니다.
  - 열기 설정 Windows PC에서 (누르세요. Win + I).
  - 클릭 개인정보 보호 및 보안 왼쪽 사이드바에서 Windows Security.
  - 클릭 앱 및 브라우저 제어.
  - 아래에 스마트 앱 제어, 클릭 스마트 앱 제어 설정.
  - 토글을 다음으로 설정하세요. 끄다 Updater CE가 실행되도록 허용합니다.

Edge에 의해 차단되었나요? Microsoft Edge가 다운로드 자체를 차단하는 경우 추가 옵션 버튼(…) → 유지하다 → 더 보기 → 어쨌든 유지.

나중에 스마트 앱 제어를 다시 활성화하려면: 스마트 앱 제어를 다시 켜려면 아래의 Windows 레지스트리를 통해 다시 활성화할 수 있습니다. `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` 설정으로 `VerifiedAndReputablePolicyState` 에 `1` (켜짐) 또는 `2` (평가 모드) 및 다시 시작.도움말 닫기

## 이것이 유용했나요?

귀하의 답변은 이 가이드를 개선하는 데 도움이 됩니다.네, 유용했어요아직은 아님[개선할 수 있는 방법을 알려주세요.](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
