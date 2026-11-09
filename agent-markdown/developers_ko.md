---
title: "개발자 | Innioasis 업데이터 CE에 사용자 정의 펌웨어 추가 - Innioasis 펌웨어 다운로드"
description: "Updater CE에 사용자 정의 Innioasis Y1 또는 Y2 펌웨어를 추가하기 위한 개발자 문서: 저장소 포크, rom.zip 자산 게시, slidia_manifest.xml 편집, 테스트 및 끌어오기 요청 열기."
language: "ko"
source: "https://innioasis.app/developers_ko.html"
---

# 개발자 | Innioasis 업데이터 CE에 사용자 정의 펌웨어 추가 - Innioasis 펌웨어 다운로드

펌웨어 개발자용

# Updater CE에 펌웨어를 추가하세요.

Updater CE는 맞춤형 펌웨어를 위한 커뮤니티 카탈로그이자 설치 프로그램입니다. 기본 ROM에서 프로젝트를 개발하고 이를 올바른 릴리스 자산과 함께 공개 저장소로 게시하고 모델 항목을 `slidia_manifest.xml`, 모델 필터를 테스트하고 끌어오기 요청을 엽니다. 하나의 저장소가 지원하는 모든 모델을 제공할 수 있습니다.[업데이터 CE 소스 보기](https://github.com/y1-community/Innioasis-Updater)[소프트웨어 다운로드 찾아보기](firmware_ko.html)

## 베이스 ROM에서 시작

기본 ROM은 맞춤형 펌웨어 개발자에게 무선 라디오 칩이 활성화된 깔끔한 Android 기반을 제공합니다. Y1에서는 공장 블루투스 및 FM과 함께 Wi-Fi 및 GPS를 활성화합니다. Y2에서는 공장 Bluetooth와 함께 Wi-Fi, GPS 및 FM을 활성화합니다.맞춤형 펌웨어 개발을 위한 기본 ROM 다운로드(각각 활성화되는 Android 버전 및 무선 기능 포함)[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom.zip)[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom_type_b.zip)[``](https://github.com/y1-community/y2-ata-rom/releases/download/y2-ata/rom_y2.zip)

| 다운로드 | 장치 | Android | 무선 기능 |
| --- | --- | --- | --- |
| rom.zip | Y1 · Type A | Android 4.2.2 | 공장 Bluetooth 및 FM에 Wi-Fi 및 GPS를 추가합니다(FM은 공장에서 이미 Y1에서 작동합니다). OS 2.0.0 이상과 함께 출시된 Y1 플레이어의 경우. |
| rom_type_b.zip | Y1 · Type B | Android 4.2.2 | 공장 Bluetooth 및 FM에 Wi-Fi 및 GPS를 추가합니다(FM은 공장에서 이미 Y1에서 작동합니다). 2.0.0 이전 OS와 함께 출시된 Y1 플레이어의 경우. |
| rom_y2.zip | Y2 | Android 4.4.2 | 공장 블루투스에 Wi-Fi, GPS, FM을 추가합니다. Y2 라디오 칩이 완전히 활성화되었으므로 여기에서도 FM을 사용할 수 있습니다. |

이러한 이미지는 기기 무선 라디오가 활성화된 기본 Android 기반(AOSP)이므로 맞춤 펌웨어는 라디오 스택을 교체하는 대신 네트워크 기능을 추가할 수 있습니다. 이는 아래 게시 단계의 실질적인 시작점입니다.

## 다음 릴리스 자산 이름을 사용하세요.

파일 이름은 호환성 신호의 일부입니다. 이름을 정확하게 유지하고 저장소 소스 트리뿐만 아니라 프로젝트의 릴리스 자산에 ZIP 파일을 넣으세요.펌웨어 ZIP 자산 이름 및 지원 장치``````

| 유산 | 장치 | 하드웨어 | 의미 |
| --- | --- | --- | --- |
| rom.zip | Y1 | Type A | Y1 OS 2.0.0 이상이 설치된 장치. |
| rom_type_b.zip | Y1 | Type B | Y1 2.0.0 이전 OS와 함께 제공되는 장치입니다. |
| rom_y2.zip | Y2 | Y2 | Y2 전체 설치 패키지. Y1 자산과 별도로 유지하세요. |
다른 모델에 맞게 패키지 이름을 바꾸지 마십시오. Y1과 Y2은 서로 다른 MediaTek 플랫폼 파일과 플래싱 구성을 사용합니다. 실제로 지원하는 하드웨어용 패키지를 게시합니다.

## 연결 작동 방식

업데이터 CE는 매니페스트를 카탈로그로 읽습니다. 각 `<package>` 줄은 프로젝트 이름, 저장소, 모델 및 처리기를 알려줍니다. 사용자가 해당 프로젝트를 선택하면 업데이터는 저장소의 게시된 릴리스를 확인하고 `rom*.zip` 유산.

### 명백한

프로젝트 이름을 지정하고 모델에 매핑합니다. Y1과 Y2은 저장소를 공유하는 경우에도 별도의 줄이 필요합니다.

### 출판된 릴리스

설치 가능한 ZIP 자산이 포함되어 있습니다. 단일 릴리스에는 Y1 Type A, Y1 Type B 및 Y2 패키지가 함께 포함될 수 있습니다.

### 업데이터 CE 설치

선택한 모델을 사용하여 일치하는 패키지와 모델별 플래싱 경로를 선택합니다. 사용자는 파일 이름을 추측할 필요가 없습니다.

## 5단계로 프로젝트 게시
  - Updater CE 저장소를 포크합니다. 나만의 포크 만들기 [y1-community/Innioasis-Updater](https://github.com/y1-community/Innioasis-Updater)을 클릭한 다음 포크를 로컬로 복제하세요.
  - 공개 펌웨어 저장소를 준비합니다. 저장소가 공개되어 있고 해당 릴리스에 올바른 ZIP 자산이 포함되어 있는지 확인하세요. 당신은 넣을 수 있습니다 `rom.zip`, `rom_type_b.zip`, 그리고 `rom_y2.zip` 동일한 버전에 속하면 동일한 릴리스에 있어야 합니다.
  - 매니페스트를 편집합니다. 열기 `slidia_manifest.xml` Updater CE 포크의 루트에 있습니다. 릴리스가 지원하는 각 모델에 대해 한 줄을 추가합니다(Y1 및 Y2은 공통 쌍입니다). 그만큼 `repo` 값은 저장소의 `owner/repository`; `url` 공개 프로젝트 페이지입니다.
  - 카탈로그를 테스트해 보세요. 편집된 체크아웃에서 Updater를 실행합니다. Y1을 선택하고 프로젝트에 Y1 자산이 표시되는지 확인합니다. Y2를 선택하고 Y2 릴리스가 표시되는지 확인합니다. 둘 다 게시되면 Type A와 Type B를 별도로 확인하세요.
  - 끌어오기 요청을 엽니다. 매니페스트 변경 사항을 포크로 푸시하고 업스트림 업데이터 CE 저장소에 대한 풀 요청을 엽니다. 프로젝트 링크, 지원되는 모델, 릴리스 태그, 자산 이름, 테스트한 장치를 포함하세요.

## 매니페스트 라인 생성

저장소를 채우고 릴리스가 지원하는 모든 모델을 선택하십시오. 생성기는 하나를 씁니다. `<package>` 모델별로 라인이 표시되며 사용자가 설정한 속성만 포함되므로 결과는 현재와 일치합니다. `slidia_manifest.xml` 체재. Updater CE가 읽는 모든 속성은 아래에서 사용할 수 있습니다. 선택적인 속성은 아래에 있습니다. 추가 옵션.저장소 URL공개 GitHub 저장소. 발전기가 추출합니다. `owner/repository` URL에서.소프트웨어 이름앱과 사이트 카탈로그에 표시됩니다.프로젝트 URL프로젝트 또는 릴리스 노트에 대한 사람을 향한 페이지입니다.상표모델의 기본 브랜드를 사용하려면 이 항목을 선택 취소하세요. SR1, Q3, Q5 및 Q3e는 Timmkoo 모델입니다.장치(각각 한 줄)Y1Y2A5G1G3G5R1PR1SR1Q3Q5Q3e다른 모델위에 나열되지 않은 모델의 경우. 알려진 모델은 카탈로그 철자를 유지합니다.플래그`do_not_keep_data` — 이 펌웨어에 대해 Keep Data를 제공하지 마십시오.원본 소프트웨어로 제작 — 추가 `derivative="y1-community/y1-stock-rom"`

데이터 유지는 수신 펌웨어와 설치된 펌웨어가 동일하거나 공유하는 경우에만 제공됩니다. `derivative` 뿌리. 사용자 데이터가 실제로 전달될 수 없는 경우에만 플래그를 사용하십시오.추가 옵션: 아이콘, 아트웍, 릴리스 자산, 설치 후 및 미러

#### 아이콘과 아트워크아이콘 파일저장소에 커밋할 이미지를 선택합니다. 그러면 이를 미리 보고 원시 URL을 구축합니다. 아무것도 업로드하지 않습니다.저장소의 아이콘 경로저장소 루트를 기준으로 커밋된 이미지의 경로입니다.아이콘 지점아이콘 URL직접 이미지 URL. 비어 있으면 앱은 릴리스의 `updater.png` 또는 생성된 아이콘.선택한 아이콘 미리보기

다크 모드 아이콘 URL선택적 어두운 테마 아이콘. `image_dark` 허용되는 별칭입니다.라이트 아트웍 URL2차 아트워크, 출시 후 시도한 이미지 및 `icon`.어두운 작품 URL

#### 자산 출시릴리스 자산 이름선택한 모든 모델에 대해 하나의 이름이 있습니다. 사용하려면 비워두세요. `rom.zip` Y1에 그리고 `rom_<model>.zip` 다른 곳.자산 패턴릴리스의 zip 이름이 지정되지 않은 경우 사용되는 Glob `rom*.zip`.Type A 자산Y1 Type A 패키지 이름에 해당 패키지가 명시되지 않은 경우 Glob입니다.Type B 자산Y1 Type B 패키지 이름에 해당 패키지가 명시되지 않은 경우 Glob입니다.최소 앱 버전이전 Updater CE 빌드에서 항목을 숨깁니다.

#### 링크, 미러 및 Keep Data 제품군설치 후 페이지성공적으로 설치한 후 열었습니다.설치 후 두 번째 페이지여러 페이지로 구성된 설정 가이드를 위한 선택적 두 번째 단계입니다.휴대용 지퍼 거울쉼표로 구분 `*-mirror` Portable Flashing Zip 패키지를 빌드하는 저장소.파생 저장소이 릴리스의 기반이 되는 펌웨어입니다. 관련 펌웨어는 데이터 파티션을 공유하는데, 이는 Keep Data가 확인하는 것입니다.정보 저장소이 펌웨어의 앱을 설명하는 릴리스의 앱 저장소입니다. 또한 설치 후 페이지가 필요합니다.APK 저장소APK 앱이 펌웨어 이후에 다운로드 및 설치되는 앱 저장소입니다.

#### 카탈로그 추가사항강타링크 및 저장된 설치 기록에 대한 안정적인 식별자입니다. 여러 모델을 선택하면 해당 모델이 자동으로 추가됩니다.설명`<package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y1" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" /> <package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y2" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" />`라인 복사

최신 매니페스트 로드 중…라인이 추가된 최신 매니페스트를 미리 봅니다.

발전기가 전류를 가져왔습니다. `slidia_manifest.xml` 이 저장소에서 바로 직전에 생성된 라인을 삽입했습니다. `</slidia>`.

공유 저장소에는 한 줄로는 충분하지 않습니다. Y2 줄이 누락된 경우 Y2 사용자는 다음과 같은 경우에도 모델과 일치하는 항목을 얻지 못합니다. `rom_y2.zip` 프로젝트 릴리스에 존재합니다. 릴리스가 지원하는 다른 모든 모델에서도 마찬가지입니다.

### 매니페스트가 읽는 모든 속성

이는 현재 Updater CE 빌드가 이해하는 특성입니다. 생성기는 사용자가 입력한 항목만 작성합니다. 앱은 나머지 부분에 대해 합리적인 기본값으로 돌아갑니다.slidia_manifest.xml 패키지 속성 및 의미``````````````````````````````````````````````````````````````````````````````````````````````

| 기인하다 | 필요 | 기능 |
| --- | --- | --- |
| name | 예 | 카탈로그와 설치 카드에 표시된 소프트웨어 이름입니다. |
| repo | 예 | owner/repo. 앱은 해당 저장소의 GitHub 릴리스를 읽습니다. |
| device | 예 | 대상 모델, 대문자(Y1, Y2, G1, Q3e, …). 모델당 하나의 항목을 유지합니다. |
| url | 추천 | 카탈로그에서 프로젝트 페이지 또는 릴리스 노트가 열립니다. |
| type, handler | 예, 실제로는 | type="img" 그리고 handler="Custom Firmware". 다른 유형 및 비펌웨어 처리기는 건너뜁니다. |
| brand | 선택사항 | 카탈로그 브랜드(Innioasis, Timmkoo). 비어 있음은 모델의 기본 브랜드를 사용합니다. |
| package_name | 선택사항 | 릴리스 자산 파일 이름. 기본값은 rom.zip Y1에 그리고 rom_<model>.zip 다른 모델에서는. |
| asset_pattern | 선택사항 | 펌웨어 zip 이름이 지정되지 않은 릴리스의 경우 대소문자를 구분하지 않는 glob rom*.zip (예를 들어 my-firmware-*.zip). |
| type_a_asset, type_b_asset | 선택사항 | 파일 이름에 일반적인 마커가 포함되지 않은 경우 Y1 Type A 및 Type B zip을 식별하는 글로브입니다. |
| icon | 선택사항 | 로고 URL. 릴리스 자체 이후에 사용됨 updater.png / updater.jpg, 그리고 모든 릴리스에 대한 대체 수단으로 사용됩니다. |
| icon_dark | 선택사항 | 어두운 테마 로고. image_dark 허용되는 별칭입니다. |
| image | 선택사항 | 보조 조명 아트웍, 이후 시도 icon. |
| post_install, post_install2 | 선택사항 | 성공적인 설치 후 페이지가 열렸습니다. 두 번째는 다단계 가이드를 다룹니다. |
| portable_zips | 선택사항 | 쉼표로 구분 *-mirror 즉시 실행 가능한 휴대용 패키지를 게시하는 저장소입니다. |
| derivative | 선택사항 | 펌웨어가 빌드된 리포지토리입니다. 동일한 파생 루트를 가진 펌웨어는 사용자 데이터를 유지할 수 있습니다. |
| info_repo | 선택사항 | 펌웨어가 배포하는 내용을 설명하는 릴리스가 있는 앱 저장소입니다. 필요하다 post_install 또는 post_install2. |
| apk_repo | 선택사항 | 펌웨어 이후에 앱이 설치되는 APK 앱 저장소입니다. |
| min_version | 선택사항 | Updater CE가 이 버전보다 오래된 경우 항목을 숨깁니다. |
| do_not_keep_data | 선택사항 | true (또한 1 / yes)는 이 펌웨어에 대해 데이터를 완전히 유지하는 것을 차단합니다. |
| slug | 선택사항 | 링크 및 저장된 설치 기록에 대한 안정적인 식별자입니다. 비어 있으면 이름과 모델에서 생성됩니다. |
| description | 선택사항 | 짧은 카탈로그 설명. 속성 값 또는 요소의 텍스트일 수 있습니다. |

호환성을 위해 기존 이름을 계속 읽습니다. `model`, `package`, `portable_zip`, `post_install_2`, `min_app_version` 그리고 `image_dark`. 새 항목은 위의 현재 이름을 사용해야 합니다.

### 풀 요청으로 라인 제출
  - 위에서 생성된 줄을 복사합니다. 이미 최신 매니페스트 형식과 일치합니다.
  - 편집하다 `slidia_manifest.xml` 저장소에 있습니다. 아래의 편집 링크를 사용하세요. 저장소 호스트는 자동으로 포크와 분기를 생성합니다.
  - 바로 앞에 줄을 붙여넣으세요. `</slidia>`, 기존 항목을 변경하지 않고 유지합니다.
  - 새로운 브랜치에 커밋 (예를 들어 `add-your-firmware`), 그런 다음 Updater CE 저장소에 대한 풀 요청을 엽니다.
  - PR에는 다음을 포함합니다. 프로젝트 링크, 지원되는 모델, 릴리스 태그, 자산 이름 및 테스트한 장치.
[업데이터 CE 매니페스트 편집](https://github.com/y1-community/Innioasis-Updater/edit/main/slidia_manifest.xml)[최신 매니페스트 보기](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)

모델 이름은 대문자로 유지하고, 공개 저장소의 정확한 URL을 사용하고, `type="img"` 그리고 `handler="Custom Firmware"` 펌웨어 항목의 경우.

## 릴리스를 쉽게 확인할 수 있도록 하세요.

릴리스에 명확한 태그와 릴리스 노트를 제공하십시오. 태그는 사람들에게 유용하지만 ZIP 자산 이름은 Updater CE가 설치 패키지를 식별하는 데 사용하는 것입니다.

### 릴리스 체크리스트
  - 릴리스를 공개적으로 게시합니다.
  - ZIP 파일을 릴리스 자산으로 첨부합니다.
  - 메모에 지원되는 모델과 Type A 또는 Type B을 명시하십시오.
  - 필요한 준비 사항이나 알려진 제한 사항을 나열하십시오.

### 하나의 릴리스, 세 가지 자산

공유 릴리스에는 다음이 포함될 수 있습니다. `rom.zip`, `rom_type_b.zip`, 그리고 `rom_y2.zip`. 업데이터는 이를 별도로 분류하고 모델 및 하드웨어 필터 중에서 선택합니다.

### 추측을 묶지 마세요

Y2 파일 이름 아래에 Y1 패키지를 포함하거나 테스트되지 않은 스캐터, 프리로더 또는 파티션 데이터를 추가하여 자산을 표시하지 마십시오.

## 플래싱 중에 모델 항목이 중요한 이유

매니페스트는 단순한 다운로드 메뉴가 아닙니다. 추출 후 Updater CE는 확인된 모델을 사용하여 일치하는 설치 경로를 준비합니다. Y1과 Y2에는 서로 다른 플랫폼 파일, 프리로더, 스캐터 구성 및 장치 레이아웃이 있습니다.
  - Y1: 업데이트 프로그램은 Y1 경로를 준비하고 MTKClient이 사용될 때 장치의 명명된 파티션을 사용합니다.
  - Y2: 업데이트 프로그램은 Y2 경로를 준비하고 Y2 MT6582 구성을 사용합니다. 전체 복구는 모델에 맞는 분산 데이터의 물리적 주소를 사용할 수 있습니다.
  - 크로스 플랫폼 지원: Updater CE는 추가 플래싱 도구 없이 Windows, Linux 및 macOS(Intel 및 Apple Silicon Mac 모두 지원)에서 직접 기본 플래싱을 처리합니다.
기여자는 플래시 오프셋이 아닌 올바른 펌웨어 파일을 제공해야 합니다. 잘못된 패키지를 해결하기 위해 분산 주소, 프리로더, DA 파일 또는 파티션 명령을 편집하지 마십시오. 릴리스 자산을 수정하고 의도한 모델에서 테스트합니다.

## 병합을 요청하기 전에
  - XML 파서를 사용하여 XML의 유효성을 검사합니다. 누락된 인용문 또는 마무리 `/>` 그 이후의 모든 항목을 숨길 수 있습니다.
  - 원격 새로 고침 전에 로컬 매니페스트를 로드하도록 결제에서 업데이트 프로그램을 실행하세요.
  - Y1과 Y2을 독립적으로 확인합니다. 프로젝트가 해당 패키지가 지원되는 위치에만 나타나는지 확인하세요.
  - 릴리스 목록을 확인하세요. `rom.zip`, `rom_type_b.zip`, 그리고 `rom_y2.zip` 적용 가능합니다.
  - 안정적인 USB 데이터 케이블과 원래 소프트웨어로 돌아가기 위한 복구 계획을 사용하여 의도한 장치에 실제 설치를 테스트합니다.
  - 풀 요청에서 테스트한 내용을 설명하세요. 테스트되지 않은 모델을 지원되는 것으로 설명하지 마십시오.
`python -c "from xml.etree import ElementTree as ET; ET.parse('slidia_manifest.xml'); print('manifest ok')"`

로컬 확인을 위해서는 리포지토리 루트에서 해당 명령을 실행하세요. XML 구문만 확인합니다. 이는 릴리스에 유효한 펌웨어가 포함되어 있거나 장치가 플래시해도 안전하다는 것을 증명하지 않습니다.

## 유용한 프로젝트 링크[포크 업데이터 CE](https://github.com/y1-community/Innioasis-Updater/fork)[매니페스트 보기](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)[지역 사회 기여 메모](support_devs_ko.html)[문제 해결](troubleshooting_ko.html)

## AI 에이전트를 위한 모딩 기술

저장소의 `skills/` 디렉토리는 Y1 및 Y2 하드웨어, 펌웨어, 테마 및 앱을 작업하는 에이전트를 위한 소스 기반 지식 기반입니다. 각 기술은 청구가 발생한 프로젝트 파일의 이름을 지정하므로 상담원은 장치를 변경하기 전에 사실을 확인할 수 있습니다.여기서 시작하세요

### [기술 지수 및 안전 규칙](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/README.md)

기술을 로드하는 방법, 사실이 적용되는 모델, 패키지가 작성해서는 안 되는 파티션.하드웨어

### [Y1 하드웨어](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y1-hardware/SKILL.md)

MT6572, 주요 이벤트로서의 휠, 480x360 디스플레이, FM/오디오 경로, 스토리지 및 Type A/B 파티션 맵.하드웨어

### [Y2 하드웨어](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y2-hardware/SKILL.md)

MT6582 보드, 장치 트리, GC9503V/ST7701S 패널, PMIC/DAC 레일, 파티션 및 부팅 이미지.펌웨어

### [펌웨어 패키지](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/firmware-packages/SKILL.md)

rom.zip 해부학, 분산 파일, 클래스 A 업데이트 계약 및 릴리스 체크리스트.테마

### [테마 및 스킨 제작](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/theme-authoring/SKILL.md)

Y1 config.json 테마, Rockbox WPS/SBS, Reborn 스킨 및 Y2Player 스킨 형식 v2.모든 기술

### [스킬 폴더 찾아보기](https://github.com/y1-community/Innioasis-Updater/tree/main/skills)

Rockbox Y1/Y2, 기본 Android ROM, Y2Linux, Android 앱, 실행 프로그램, 릴리스 노트 및 사이트 게시.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
