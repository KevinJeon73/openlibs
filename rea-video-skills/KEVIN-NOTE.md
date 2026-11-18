# rea-video — Kevin용 메모 (openlibs 스테이징, 2026-11-18)

이 폴더는 `JuneYaooo/rea-video`의 고정 사본이다. 원본 스킬(`rea-video/SKILL.md` + `references/` 13건)은 그대로 복사했고, 이 메모만 Kevin용으로 새로 썼다. 원본 스킬은 고치지 않았다. 원본 스킬은 중국어로 돼 있다. 한국어로 된 사용법 요약은 이 메모를 본다.

## 고정 버전

- 원본: `https://github.com/JuneYaooo/rea-video`
- 고정 커밋: `56dd8f99a43abd0d5c69ae1d972dfd887e50a81a` (HEAD, 2026-11-17 20:00 -0800, "Time generated clips to the original's moves")
- 태그 `v0.1.0`은 이 커밋보다 낡았다. 태그가 아니라 위 커밋으로 고정한다. `pyproject.toml` 버전 표기는 0.1.0이다.
- 라이선스: Apache-2.0 (`LICENSE` + `NOTICE` 참조)
- 설치 핀 (고정 커밋으로 설치):
  - `pip install "rea-video[ocr] @ git+https://github.com/JuneYaooo/rea-video@56dd8f99a43abd0d5c69ae1d972dfd887e50a81a"`
  - 또는 `pipx install "rea-video[ocr] @ git+https://github.com/JuneYaooo/rea-video@56dd8f99a43abd0d5c69ae1d972dfd887e50a81a"`
  - 요구사항: ffmpeg, Python 3.10~3.14. (3.13부터 OCR 패키지가 `rapidocr` 3으로 바뀐다. setup.md 참조.)
- 실행: `rea-video --help`, `rea-video decompose <영상> -o out/<이름>` (자세한 흐름은 스킬 본문 참조)

## 용도 (Kevin 프로젝트 기준)

- 동영상을 샷마다 뜯어봐서 실사인지, AI로 만든 것인지, 코드로 만든 것인지를 가리고, 다시 만드는 계획을 `VIDEO.md`로 쓴다. (형식 설명은 `docs/videomd.md` 사본 참조.)
- Lecturemaker 강의 영상 분석, 사후만남서비스 영상 학습, 로컬 Gemma 오프라인 멀티모달 챗봇의 동영상 이해용이다.
- 동영상을 직접 만들지는 않는다. 분해와 계획만 한다. 다시 만들기는 별도 도구(capsule-cinema·ChatCut 등, 유료)가 맡고, 이 스테이징에서는 쓰지 않는다.

## 오프라인 사용법

- 도구만 쓰는 모드는 오프라인으로 무료로 된다. 비전 모델(VLM)은 선택 사항이고, 없어도 돌아간다. 다만 실사/AI/3D 구분이 약해진다.
- VLM 없이 쓸 때: 에이전트가 직접 그림을 보고 복核하는 `rea-video review` → `apply-review` 흐름을 쓴다. 로컬 Gemma 비전이 그 자리이다. 외부 VLM 키를 쓰지 않는다.
- VLM을 쓴다면 Gemini만 쓴다. Doubao(豆包)·Qwen-VL은 쓰지 않는다. (setup.md에 예시로 나와 있으나 Kevin 금지 원칙에 따라 미사용.)
- 첫 실행 때 내려받는 것 (오프라인 사용 전에 1회 인터넷 필요): UVR MDX-Net 약 67MB + BandIt v2 약 149MB (음성·배경음 분리), YuNet 얼굴 모델. 내려받는 곳은 기본 `~/.cache/rea-video/models`이다.

## 중국산 관련 — 중요

- **로컬 음성 인식 `[asr]` 추가 기능은 설치하지 않는다.** 기본 음성 인식은 SenseVoice이며, FunASR/SenseVoice는 Alibaba(중국) 것이다. (`rea_video/capabilities/models/analysis.yaml`에 "FunASR / SenseVoice | Alibaba"로 적혀 있다. setup.md도 SenseVoice를 기본으로 안내한다.)
- 대신 전사는 Whisper(openai/whisper, 11-17 스킬 브리핑済, 로컬 오프라인)로 한다. 자막이 있으면 자막을 우선한다. `--no-asr`로 음성 인식을 끌 수 있다.
- **Doubao·Qwen-VL·Qwen 이미지/TTS·CosyVoice·MiniMax·Seedance 등 중국산 모델은 VLM·재생성 어느 쪽에도 쓰지 않는다.** 스킬·코드 안의 `capabilities/` 표에 중국산 모델이 선택지로 많이 나와 있으나(Doubao Seed 2.0 Pro, Qwen3.5, qwen-image, qwen3-tts 등), 이 스테이징이 복사한 스킬 폴더에는 그 표가 들어 있지 않고, CLI를 설치해도 선택하지 않는다. 재생성 단계 자체를 쓰지 않는다.
- 스킬 본문(`SKILL.md` + `references/`) 안의 중국산 언급: setup.md에 VLM 예시로 "Gemini, GPT-4o, 豆包, Qwen-VL"이 있고, audio.md·remake-tools.md에 Doubao TTS·MiniMax 클론이 재생성 예시로 나온다. 모두 미사용으로 정한다.
- 미확인: UVR MDX-Net·BandIt v2·YuNet 모델 각각의 출처·라이선스는 이 스테이징에서 끝까지 대조하지 않았다. 첫 실행 내려받기 전에 출처를 한 번 더 확인하는 것이 안전하다.

## 저작권·사용 범위

- 남의 영상을 그대로 복제하는 데 쓰지 않는다. 배우고, 본인 자료로 다시 만드는 용도이다. (스킬 원문도 같은 뜻이다.)
- HWP와는 무관하다. HWP·HWPX 생성은 `hwpx-skill`이 직접적이다.

## 스킬이 중국어라는 점

- `SKILL.md`와 `references/` 13건은 중국어 원문이다. 번역본은 이 스테이징에 넣지 않았다. (저장소 `i18n/`에는 README 번역본만 있고 스킬 번역은 없다. 한국어 README는 upstream `i18n/README_ko.md`에서 볼 수 있다.)
- 한국어로 쓸 때는 이 메모 + 스킬의 명령어(`rea-video ...`)만으로 충분하다. 보고서는 `--lang`으로 사용자 언어(한국어는 `--ocr-lang ko`와 함께)를 고른다.

## 제외한 것

- `docs/` 전체(얕은 복제 기준 약 77MB, 샘플 영상 `docs/cases/`가 대부분) — 단, 스킬이 직접 가리키는 형식 설명 `docs/videomd.md`(3,769바이트)만 `docs/`에 따로 복사했다.
- `eval/`(정확도 평가 자료, 112KB) — "98~100%" 같은 정확도 수치는 upstream 평가 주장이라, 이 스테이징에서 따로 검증하지 않았다.
- `i18n/`(README 번역본 10건, 256KB) — 스킬 본체가 아니다.
- `scripts/`(설치 스크립트 등, 96KB) — 설치는 위 pip/pipx 고정 커밋 명령으로 한다.
- `rea_video/` 패키지 소스(1.6MB), `pyproject.toml`, `AGENTS.md` — CLI는 pip으로 설치하는 것이고, 스킬 사본이 아니다.
- `docs/cases/` 샘플 영상 — 용량이 크고 스킬 동작에 필요 없다.
