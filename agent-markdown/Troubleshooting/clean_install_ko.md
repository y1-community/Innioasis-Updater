---
title: "Innioasis 업데이터 및 Y1 도우미를 새로 설치하여 수정 - Innioasis 업데이터"
description: "Innioasis 업데이터 및 Y1 도우미에 대한 단계별 새로 설치: 남은 파일을 제거하고 다시 설치한 다음 깜박이는 펌웨어로 돌아갑니다."
language: "ko"
source: "https://innioasis.app/Troubleshooting/clean_install_ko.html"
---

# Innioasis 업데이터 및 Y1 도우미를 새로 설치하여 수정 - Innioasis 업데이터

## 새로 설치가 필요한지 확인

다음 증상이 나타나면 수동 재설치를 권장합니다.
  - 업데이터가 실행되는 데 몇 분이 걸리거나 업데이트를 확인하는 동안 중단됩니다.
  - 최신 릴리스가 있어도 업데이트가 더 이상 도착하지 않습니다.
  - 장치 펌웨어 업데이트가 사용 가능한 경우에도 다운로드 또는 적용에 실패합니다.
  - 여러 릴리스를 건너뛰었고 오랫동안 업데이터를 사용하지 않았습니다.

## Windows: 새로 재설치 수행

공식 Windows 설치 프로그램을 사용하여 Windows 10 또는 Windows 11(64비트)에서 업데이터를 새로 고칩니다. 이는 이전 빌드를 완전히 대체하고 자체 업데이트 채널을 복원합니다.

설치 프로그램을 실행하기 전에 다음을 엽니다. 설정 › 앱 › 설치된 앱 (또는 유산 프로그램 추가/제거 패널)을 클릭하고 Innioasis Updater의 기존 복사본을 모두 제거합니다. 정리를 시작하면 파일 충돌이 방지됩니다.[ Windows용 클린 설치 프로그램 다운로드 ](https://github.com/y1-community/supplemental-apks/releases/download/1.0/installer.exe)1단계

### 최신 설치 프로그램을 다운로드하세요.

설치 프로그램을 다운로드 폴더에 저장합니다. 현재 실행 중인 경우 Innioasis 업데이터를 닫습니다.2단계

### 기존 설치 제거

열기 설정 › 앱 › 설치된 앱 (또는 유산 제어판 › 프로그램 추가/제거) Innioasis 업데이터를 제거하여 깨끗한 상태에서 재설치를 시작합니다.3단계

### 설치 및 다시 시작

다운로드한 설치 프로그램을 실행합니다. Windows에서 권한을 묻는 메시지를 표시합니다. 설정이 완료되면 Innioasis 업데이터를 시작합니다. 이제 자동으로 1.8.2.8을 감지하고 업데이트를 다시 선택해야 합니다.

 이는 또한 느린 시작 문제를 해결하고 업데이터가 개발자로부터 직접 펌웨어 릴리스를 다시 가져오도록 합니다. 

## macOS: DMG 설치 프로그램으로 새로 고침

macOS 설치 프로그램은 이전 파일을 지우고 1.8.2.8을 설치합니다.[ Innioasis 업데이터 다운로드 DMG ](https://github.com/y1-community/supplemental-apks/releases/download/1.0/Innioasis.Updater.for.Mac.dmg)
  - 다운로드한 DMG를 열고 Finder 창을 확장하면 재설치 옵션.
  - Reinstall 명령을 실행하여 기존 Updater 복사본을 새로 고칩니다. 이렇게 하면 새로운 기능을 차단할 수 있는 이전 도우미 파일이 제거됩니다.
  - 응용 프로그램에서 Innioasis 업데이터를 다시 시작하세요. 정보 패널 목록 버전 확인 1.8.2.8.
 재설치 후 "Innioasis 업데이터를 열 수 없습니다"라는 메시지가 표시되면 다음으로 이동하세요. 시스템 설정 › 개인 정보 보호 및 보안 그리고 선택 어쨌든 열기 앱을 승인합니다. 

## 1.8.2.8로 업데이트한 후

최신 버전을 사용하면 아래 기능에 액세스할 수 있습니다. 이는 현재 빌드에서만 사용할 수 있습니다.
  - 원클릭 설치 원본 펌웨어, 커뮤니티 릴리스 및 개발자 릴리스에서 직접 다운로드한 Rockbox 빌드의 경우.
  - 명확한 안내 단계 플레이어를 연결할 시기와 플러그를 뽑아도 안전한 시기를 알려줍니다.
  - 두 플랫폼 모두에서 일반적인 안정성이 향상되고 실행 시간이 대폭 빨라졌습니다.

 버전을 확인하는 데 도움이 필요하십니까? Innioasis 업데이터를 열고 다음을 선택하세요. 도움말 › 정보, 그리고 빌드 쇼를 확인하세요 1.8.2.8. 

## 아직도 도움이 필요하신가요?

새로 설치에 실패하면 오류 메시지를 캡처하고 Innioasis 커뮤니티 지원 채널에 문의하세요. OS 버전, 업데이터 빌드(사용 가능한 경우) 및 이미 시도한 단계를 포함하세요.

설치를 최신 상태로 유지하면 출시되는 최신 펌웨어 패키지와 도구를 항상 받을 수 있습니다.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
