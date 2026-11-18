# REA — Kevin용 메모 (openlibs 스테이징, 2026-11-18)

이 폴더는 `morluto/rea`의 고정 사본이다. 원본 스킬(`reverse-engineer-anything/SKILL.md` + `references/` 8건)은 그대로 복사했고, 이 메모만 Kevin용으로 새로 썼다. 원본 스킬은 고치지 않았다.

## 고정 버전

- 원본: `https://github.com/morluto/rea`
- 고정 커밋: `675287517c98c702ee88ad036c5e3b8dd4bcc7a7` (HEAD, 2026-11-18 13:01 +0800, "test(environment): trim scenario timing fixtures (#11990)")
- npm 패키지: `rea-agents@6.9.0` (2026-11-18 `npm view`로 최신 확인). 설치 핀은 이 버전이다. HEAD 커밋은 6.9.0 태그(`d74549e4`)보다 하루 새 것이다.
- 라이선스: MIT (`LICENSE` 참조, Copyright (c) 2026 morluto)
- Node 요구사항: Node 22.x (>=22.23.4), 24.x (>=24.22.1), 또는 26.12.1 이상 + npm. README 기준이다. (처음에 알려진 "22.19 이상"보다 엄격하므로 정정한다.)
- 설치: `npx rea-agents setup` (정식 출처 3곳만 쓴다: morluto/rea 저장소, rea.tools, rea-agents npm. 가짜 복사본·zip 내려받기는 쓰지 않는다.)

## 용도 (Kevin 프로젝트 기준)

- 파워포인트·HWP 등 로컬앱이 어떻게 동작하는지 이해하는 데 쓴다. 앱의 기능을 뜯어보고, 증거와 함께 설명하고, 다시 만드는 길을 안내한다.
- 로컬 Gemma 오프라인 멀티모달 챗봇의 로컬앱 연동 조사용이다.
- 원본 소스를 그대로 돌려주거나, 한 번에 복제하지는 않는다. 분석·설명·재구성 안내가 범위이다.

## 지켜야 할 범위 (적법 사용)

- 본인이 소유하거나 허가받은 대상, 상호운용, 연구·교육, 소프트웨어 보존 목적 안에서만 쓴다. `DISCLAIMER.md` 원문이 같은 뜻이다.
- 타인의 상용 소프트웨어를 그대로 복제하거나, 크랙·라이선스 우회를 하는 데 쓰지 않는다.
- HWP와의 관계: REA는 HWP·HWPX 파일을 만드는 도구가 아니다. HWP·HWPX 생성은 `hwpx-skill`(openlibs 기존 검토)이 직접적이다. REA는 HWP 앱의 동작을 이해하는 용도로만, 적법 범위 안에서 쓴다.
- 분석 엔진(Ghidra·IDA·Hopper 등)은 REA가 설치하지 않는다. 이미 있는 것을 쓰거나, 각자의 라이선스를 확인하고 따로 설치한다. Hopper는 `setup`이 승인 뒤에 설치할 수 있다.

## 중국산 관련 확인 (2026-11-18)

- 스킬 본문(`SKILL.md` + `references/` 8건)에 Doubao·Qwen·DeepSeek 등 중국산 모델 언급이 없다. grep으로 확인했다.
- REA 자체는 모델이 아니라 분석 도구(MCP 서버 + CLI)라, 임베딩·생성 모델 선택이 들어가지 않는다. 에이전트가 쓰는 모델은 로컬 Gemma만 쓴다.
- 미확인: 분석 엔진(Ghidra·IDA·Hopper) 각각의 라이선스·출처는 이 스테이징에서 대조하지 않았다. 엔진을 설치할 때 따로 확인한다.

## 오프라인 관련

- MCP 서버와 분석은 로컬에서 동작한다. 다만 처음 설치할 때 npm 내려받기, 분석 엔진 내려받기에는 인터넷이 필요하다.
- 스킬 안의 깊은 안내(`SKILL.md`가 가리키는 저장소 `docs/` 문서들)는 이 사본에 넣지 않았다. 필요하면 upstream에서 본다. 스킬 본체(`SKILL.md` + `references/`)만으로 동작한다.

## 제외한 것

- 저장소 전체(`src/`, `tests/`, `website/`, `third_party/`, `docs/`, `examples/`, `bridge/`, `native/` 등, 얕은 복제 기준 약 154MB) — 스킬 본체가 아니므로 복사하지 않았다.
- 개발자용 스킬 4건(`rea-tool-design`, `rea-ci-tests-audit`, `rea-changelog-update`, `rea-analysis-optimization`) — REA 자체를 개발·감사하는 용도라 Kevin용 사본에서 뺐다.
- `.cursor-plugin/skills/reverse-engineer-anything/` — `.agents/skills/` 사본과 바이트 단위로 동일함을 확인했으므로 한 벌만 넣었다.
