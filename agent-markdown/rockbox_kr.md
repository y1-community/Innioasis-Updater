---
title: "Innioasis Y1 또는 Y2 - Innioasis 업데이터에 Rockbox을(를) 설치하는 방법"
description: "업데이터를 사용하여 Innioasis Y1 또는 Y2에 Rockbox을(를) 설치합니다: 테마, 안정 릴리스, Type A 및 Type B 노트, 이후 원본 소프트웨어를 복원하는 방법."
language: "kr"
source: "https://innioasis.app/rockbox_kr.html"
---

# Innioasis Y1 또는 Y2 - Innioasis 업데이터에 Rockbox을(를) 설치하는 방법

Rockbox 참조

# Y1 또는 Y2에서 Rockbox을(를) 얻음

Rockbox은 플레이어 소프트웨어를 변경하고 더 깊은 음악 플레이어 인터페이스, 재생 제어, 정렬 및 테마 옵션을 엽니다. 설치가 안내되지만 Y1과 Y2는 별도의 여정입니다.[Y1의 Rockbox](guides/rockbox-y1.html)[Y2의 Rockbox](guides/rockbox-y2.html)[왜 Rockbox인가요?](rockbox-benefits_ko.html)

## 설치로 인해 변경되는 사항

Rockbox은 맞춤형 소프트웨어입니다. 일치하는 원본 소프트웨어 패키지를 사용할 수 있을 때 기본 인터페이스로 돌아갈 수 있는 기능은 제거되지 않습니다. 음악 탐색 및 사용자 정의를 향상시킬 수 있지만 기능, 해상도, 배터리 수명 및 테마 호환성은 빌드에 따라 다릅니다.모델을 혼합하지 마십시오. Y1 선수의 경우 Y1을 선택하고 Y2 선수의 경우 Y2를 선택합니다. 비슷한 릴리스 이름은 패키지가 호환된다는 증거로 충분하지 않습니다.

## 비디오 보기

Frawgees의 비디오. Innioasis 업데이터 경로를 보여줍니다. Y1 또는 Y2에 대해 아래에 작성된 모델별 단계를 사용하십시오.

비디오 작성자: [크리스티안 플라자](https://www.youtube.com/@CristianPlaza) (스페인어), Y1에 Rockbox을 표시합니다. 플레이어에 따라 아래의 모델별 단계를 사용하세요.

## 공유 업데이터 경로
  - 업데이터를 설치하고 메시지가 나타날 때까지 아무것도 연결하지 마십시오.
  - 플레이어에 인쇄된 모델을 선택하세요. 기기 모델.
  - 선택 Rockbox 안으로 소프트웨어.
  - 의도적으로 야간 빌드를 테스트하지 않는 한 안정적인 릴리스를 선택하세요.
  - 클릭 설치 / 복원을 누른 다음 전원 끄기 및 USB 연결 프롬프트를 따릅니다.
  - 성공 메시지 후에만 연결을 끊습니다.

## 240p, 360p 및 테마

이전 Rockbox 테마 컬렉션은 240p용으로 제작될 수 있습니다. Y1 커뮤니티 빌드도 360p 호환성 레이블을 사용합니다. 빌드를 선택하기 전에 릴리스 노트와 테마 소스를 읽어보세요. 특정 해상도나 소프트웨어 제품군용으로 만들어진 테마는 다른 해상도나 소프트웨어 제품군에서는 작동하지 않을 수 있습니다.[커뮤니티 테마 찾아보기](https://themes.innioasis.app/?lang=ko)[테마 도구](https://themes.innioasis.app/?lang=ko)

## 원래 소프트웨어로 돌아가기

동일한 모델을 다시 선택하고 원본 소프트웨어, 안정적인 릴리스를 선택하고 사용하십시오. 설치 / 복원. USB 프롬프트 이전에 오류가 발생한 경우 컴퓨터와 추출된 파일을 확인하십시오. 플레이어가 감지되었지만 플래시가 실패한 경우 다음으로 시작하십시오. [문제 해결](troubleshooting_ko.html).[Y1 복원](guides/restore-original-y1.html)[Y2 복원](guides/restore-original-y2.html)

## 자주 묻는 질문Rockbox을(를) 다시 설치했는데 아무 것도 수정되지 않았습니다.

Rockbox을(를) 다시 설치하면 동일한 파일에 동일한 빌드가 작성되므로 Rockbox이 MicroSD에 유지하는 항목을 재설정할 수 없습니다. 문제가 손상된 설정, 테마, 재생 목록 또는 카드에 있는 데이터베이스인 경우 다시 설치해도 문제가 해결되지 않습니다. 안정적인 재설정은 `.rockbox` MicroSD의 폴더 - Rockbox은 다음 부팅 시 새로운 폴더를 만듭니다.
  - 플레이어의 전원을 완전히 끄고 MicroSD 카드를 제거하거나 플레이어를 USB 드라이브로 연결하세요.
  - 폴더가 표시되도록 컴퓨터에 숨겨진 파일을 표시합니다. 숨겨진 파일을 표시하는 방법컴퓨터에 도트파일 표시Windows: 파일 탐색기에서 보다 탭과 체크 숨겨진 항목.macOS: 파인더 프레스에서 Cmd+Shift+. 숨겨진 파일을 전환합니다.Linux · 그놈 파일: 언론 Ctrl+H, 또는 메뉴를 열고 숨겨진 파일 표시.리눅스 · KDE 돌핀: 언론 Ctrl+H, 또는 사용 보기 → 숨김 파일 표시.
  - 삭제 `.rockbox` 카드 루트의 폴더입니다.
  - 카드를 다시 삽입하고 플레이어를 시작하십시오. Rockbox은 기본값으로 폴더를 다시 만듭니다.
  - 테마와 설정을 다시 적용하세요. 특정 테마 이후에만 문제가 다시 발생하는 경우 해당 테마가 원인입니다.

삭제 중 `.rockbox` Rockbox을(를) 제거하지 않고 음악을 건드리지도 않습니다. 폴더에는 설정, 테마 및 캐시가 보관되어 있으며 자동으로 재구성됩니다. 테마를 유지하려면 폴더를 외부로 복사하세요. `.rockbox` 삭제하기 전에 폴더 이름을 다음으로 바꾸세요. `.rockbox-old` 먼저.내 MicroSD에서 .rockbox 폴더를 볼 수 없는 이유는 무엇입니까?

이름이 점으로 시작하는 폴더는 대부분의 컴퓨터에서 기본적으로 숨겨져 있습니다. Rockbox을(를) 설치하기 위해 이를 볼 필요는 없습니다. — 업데이터가 파일을 처리합니다. 문제를 해결하고 삭제하려면 먼저 숨겨진 파일을 켜십시오. 숨겨진 파일을 표시하는 방법컴퓨터에 도트파일 표시Windows: 파일 탐색기에서 보다 탭과 체크 숨겨진 항목.macOS: 파인더 프레스에서 Cmd+Shift+. 숨겨진 파일을 전환합니다.Linux · 그놈 파일: 언론 Ctrl+H, 또는 메뉴를 열고 숨겨진 파일 표시.리눅스 · KDE 돌핀: 언론 Ctrl+H, 또는 사용 보기 → 숨김 파일 표시..rockbox를 삭제하면 테마와 설정이 재설정되나요?

예 - `.rockbox` Rockbox의 설정, 테마, 재생 목록 및 캐시된 데이터베이스를 보유합니다. 삭제하면 Rockbox이(가) 깨끗한 기본 상태로 돌아갑니다. 전체 폴더를 백업하거나 폴더 이름을 다음으로 바꿉니다. `.rockbox-old`) 그 중 하나를 다시 원할 경우 플레이어를 시작하고 Rockbox이 새 폴더를 만듭니다.

## 추가 Rockbox-Y1 및 Rockbox-Y2 가이드

두 모델 모두에서 설치, 다운로드, 테마 지정, 복원 및 문제 해결Rockbox에 대한 단계별 가이드를 살펴보세요.[Rockbox-Y1 허브](rockbox-y1/)[Rockbox-Y2 허브](rockbox-y2/)[Rockbox ROM 다운로드](rockbox-rom-download_ko.html)[Y1의 경우 Rockbox](rockbox-for-y1_ko.html)[Y2의 경우 Rockbox](rockbox-for-y2_ko.html)[Rockbox-Y1 대 Y2](rockbox-y1-vs-y2.html)[Rockbox-Y1 테마](rockbox-y1-themes.html)[Rockbox-Y2 테마](rockbox-y2-themes.html)

## 이 참고자료가 도움이 되었나요?

귀하의 답변은 이 가이드를 개선하는 데 도움이 됩니다.예아직은 아님[개선할 수 있는 방법을 알려주세요.](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
