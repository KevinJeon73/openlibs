# Openlibs

proposalmaker 등에서 쓰는 오픈소스 라이브러리의 **고정 버전 사본**. 원 저작권·라이선스는 각 폴더의 LICENSE를 따른다.

| 폴더 | 원본 | 라이선스 | 고정 버전 | 용도 |
|---|---|---|---|---|
| rhwp/ | https://github.com/edwardkim/rhwp | MIT | v0.8.7 | HWP/HWPX 미리보기·렌더(WASM) |
| python-hwpx/ | https://github.com/airmang/python-hwpx | Apache-2.0 | v6.8.0 | HWPX 읽기·편집·저장 |

- 원본·고정 커밋·제외 항목은 `UPSTREAM.json`. rhwp는 용량 때문에 문서·샘플·PDF·글꼴·시험 자료를 뺐다.
- 업데이트 확인: `python check_updates.py` (gh CLI 로그인 필요). 새 태그가 있어도 자동으로 바꾸지 않고, 변경 내용을 검토한 뒤 사본과 `UPSTREAM.json`을 갱신한다.
- 사용 전 Z0(제작 주체·의존 패키지 확인)를 proposalmaker `tools_registry.json`에 등록한다.
