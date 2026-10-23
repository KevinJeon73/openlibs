"""upstream 업데이트 확인. 표준 라이브러리 + gh CLI 만 사용. 사용: python check_updates.py [--json]
최신 태그·기본 브랜치 마지막 커밋 날짜를 pinned 와 비교해 새 버전 여부를 출력한다(복제본은 바꾸지 않는다)."""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def gh(path, jq):
    r = subprocess.run(["gh", "api", path, "--jq", jq], capture_output=True, text=True, encoding="utf-8")
    if r.returncode:
        raise RuntimeError(r.stderr.strip())
    return r.stdout.strip()


def main():
    libs = json.load(open(os.path.join(HERE, "UPSTREAM.json"), encoding="utf-8"))["libs"]
    out = []
    for name, d in libs.items():
        repo = d["repo"]
        if repo.startswith("npm:"):
            try:
                import urllib.request
                pkg = repo[4:].replace("/", "%2f")
                latest = json.load(urllib.request.urlopen(f"https://registry.npmjs.org/{pkg}/latest", timeout=15))["version"]
                out.append({"lib": name, "pinned": d["pinned_tag"], "latest_tag": latest, "new_tag": latest != d["pinned_tag"],
                            "upstream_pushed_at": "-", "url": f"https://www.npmjs.com/package/{repo[4:]}"})
            except Exception as e:
                out.append({"lib": name, "error": str(e)})
            continue
        try:
            tag = gh(f"repos/{repo}/tags?per_page=1", ".[0].name")
            pushed = gh(f"repos/{repo}", ".pushed_at")
            out.append({"lib": name, "pinned": d["pinned_tag"], "latest_tag": tag, "new_tag": tag != d["pinned_tag"],
                        "upstream_pushed_at": pushed, "url": f"https://github.com/{repo}/releases"})
        except RuntimeError as e:
            out.append({"lib": name, "error": str(e)})
    if "--json" in sys.argv:
        print(json.dumps(out, ensure_ascii=False, indent=2)); return
    for o in out:
        if "error" in o:
            print(f"{o['lib']}: 확인 실패 ({o['error']})")
        else:
            flag = "★ 새 태그 있음" if o["new_tag"] else "최신"
            print(f"{o['lib']}: 현재 {o['pinned']} / 최신 태그 {o['latest_tag']} → {flag} (upstream 마지막 push {o['upstream_pushed_at']})")


if __name__ == "__main__":
    main()
