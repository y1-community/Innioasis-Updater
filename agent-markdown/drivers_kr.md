---
title: "Innioasis Y1 및 Y2 USB 드라이버 | Windows 드라이버 및 Linux 권한 - Innioasis 업데이터"
description: "Innioasis 업데이터용 컴퓨터 설정: Windows MediaTek 드라이버 및 Linux USB 권한과 케이블 및 타이밍 수정."
language: "kr"
source: "https://innioasis.app/drivers_kr.html"
---

# Innioasis Y1 및 Y2 USB 드라이버 | Windows 드라이버 및 Linux 권한 - Innioasis 업데이터

컴퓨터 설정

# 플레이어보다 먼저 컴퓨터를 준비하십시오.

대부분의 연결 문제는 드라이버, 권한, 케이블 또는 타이밍으로 인해 발생합니다. Windows에는 MediaTek 드라이버가 설치되어 있어야 합니다. Linux에는 올바른 USB 권한이 필요합니다. 아래에서 귀하의 플랫폼을 찾아보세요.[Updater CE 받기](guide_ko.html#platform)[문제 해결](troubleshooting_ko.html)

## Windows
  - 아래에서 MediaTek 드라이버 설치 프로그램을 다운로드하세요.
  - 설치 프로그램을 실행하고 Windows에서 드라이버를 설치하도록 허용합니다.
  - 컴퓨터를 다시 시작합니다.
  - 전원이 꺼진 플레이어를 연결하기 전에 Updater CE를 열고 연결 프롬프트를 기다립니다.

일부 Windows 시스템은 코어 격리(메모리 무결성)를 통해 드라이버를 차단합니다. 다시 시작한 후에도 Updater CE가 여전히 플레이어를 인식할 수 없으면 Windows 보안에서 메모리 무결성을 끄고 다시 시작한 다음 드라이버를 다시 설치하십시오. 시스템에서 허용하는 경우 작업을 마친 후 설정을 다시 켜십시오.

Windows에서 앱이 실행되지 않습니까? Windows 보안 또는 스마트 앱 제어로 인해 Updater CE가 열리지 않는 경우 설정 (누르다 Win + I) → 개인정보 보호 및 보안 → Windows Security → 앱 및 브라우저 제어 → 스마트 앱 제어 설정 그리고 그것을로 설정 끄다（으）로 설정하세요. 스마트 앱 제어는 현재 Fortnite에서 사용하는 Epic Overlay Service와 같은 인기 애플리케이션에 영향을 미치고 있습니다. Updater CE는 안전하며 검증되었습니다. 나중에 다시 활성화하려면 `VerifiedAndReputablePolicyState` 에 `1` (켜짐) 또는 `2` (평가 모드) 아래 `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` 레지스트리 편집기에서.[Windows 드라이버 다운로드](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[기본 가이드로 돌아가기](guide_ko.html#windows) · [소프트웨어 다운로드](firmware_ko.html)

## Linux USB 권한

Linux에서는 플레이어 내부의 MediaTek USB 칩과 통신할 수 있도록 사용자 계정이 필요합니다. 업데이터 CE는 일반적으로 설치 중에 이를 분류하고 동일한 권한이 SP Flash Tool에 적용되므로 이를 일반 단계가 아닌 수정 단계로 처리합니다.
  - 루트가 아닌 일반 사용자로 Updater CE를 실행하십시오. 설치 프로그램은 필요할 때만 관리자 액세스를 요청합니다.
  - 플레이어가 전혀 보이는지 확인하십시오. 플레이어의 전원을 끄고 케이블을 연결한 후 터미널에서 lsusb 명령을 실행하세요. 연결된 플레이어는 공급업체 ID가 0e8d인 MediaTek 장치로 표시됩니다.
`lsusb`
  - lsusb에 표시되지만 Innioasis Updater CE 또는 SP Flash Tool에 권한이 거부되었거나 포트를 열 수 없다고 표시되면 사용자가 USB 장치에 액세스할 수 없는 것입니다. 동일한 udev 규칙이 두 도구 모두에 적용되므로 사용자 그룹이 읽을 수 있도록 규칙을 추가하세요.
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

해당 행을 /etc/udev/rules.d/51-innioasis.rules라는 새 파일에 저장한 후 다음을 실행하십시오.`sudo udevadm control --reload && sudo udevadm trigger`
  - 플레이어를 완전히 분리했다가 다시 연결한 후 다시 설치해 보세요.
  - SP Flash Tool이 직렬 권한 또는 포트 경합을 보고하는 경우 메시지가 나타날 때만 플러그를 완전히 뽑았다가 다시 연결하십시오.
즉흥적으로 플래시 오프셋을 조정하지 마십시오.수동 복구 도구로 전환하는 경우 프로젝트와 함께 제공된 파일 및 모델별 구성을 사용하십시오.

[기본 가이드로 돌아가기](guide_ko.html#linux) · [소프트웨어 다운로드](firmware_ko.html) · [SP Flash Tool 가이드](sp-flash-tool_ko.html)

## 케이블 및 타이밍
  - 알려진 USB 데이터 케이블을 사용하십시오.
  - 문제를 해결하는 동안 허브를 피하세요.
  - 해당 모델의 전원을 완전히 끄십시오.
  - 프롬프트에서만 연결하십시오.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
