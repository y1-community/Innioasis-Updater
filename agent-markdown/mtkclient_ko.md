---
title: "MTKClient 및 낮은 수준 복구 가이드 - Innioasis 및 Timmkoo - Innioasis 펌웨어 다운로드"
description: "MTKClient 및 SP Flash Tool를 사용하는 Innioasis 및 Timmkoo 플레이어에 대한 낮은 수준의 MediaTek 복구, 부트로더 브릭 해제 지침 및 드라이버 진단."
language: "ko"
source: "https://innioasis.app/mtkclient_ko.html"
---

# MTKClient 및 낮은 수준 복구 가이드 - Innioasis 및 Timmkoo - Innioasis 펌웨어 다운로드

고급 진단 · MediaTek

# MTKClient 및 Unbrick 진단

MTKClient은 Innioasis 업데이터 CE에서 사용하는 기본 오픈 소스 MediaTek 플래싱 엔진입니다. 플레이어가 응답하지 않거나 표준 깜박임에 실패하는 경우 이러한 복구 진단을 사용하십시오.[일반적인 문제 해결](troubleshooting_ko.html)[드라이버 설정 참고 사항](drivers_ko.html)

Innioasis Updater으로 시작

## 저레벨 루트보다 먼저 안내 루트를 시도해 보세요.

업데이터는 한 번에 이를 수행합니다. 소프트웨어를 선택하고 화면의 단계를 따르면 완료됩니다. 또한 수정 사항이나 새 릴리스가 출시되는 시기도 알려줍니다.

## BootROM(BROM) 모드 이해

전원이 완전히 꺼지면 MediaTek MT6572 / MT6580 프로세서는 기본 부트로더를 로드하기 전에 USB 버스에서 핸드셰이크 패킷을 수신합니다. 손상된 플래시가 발생하는 경우 BROM 모드에서는 전체 복구 재작성을 허용합니다.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
