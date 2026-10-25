"""檢查發布文件、相對連結與八張圖片；不驗證製片能力或圖中文字。"""
from pathlib import Path
import hashlib
import json
import re
import struct

root = Path(__file__).resolve().parents[1]
required = ['README.md', 'LICENSE', 'CHANGELOG.md', 'CONTRIBUTING.md',
            'ATTRIBUTION.md', 'docs/blog.md', 'docs/workflow.md', 'docs/tools.md',
            'docs/agent-instructions.md', 'docs/shot-task-card.md',
            'docs/acceptance.md', 'examples/30-second-video.md',
            'release/RELEASE_NOTES.md', 'release/PUBLISHING.md']
errors = []
for name in required:
    if not (root / name).is_file():
        errors.append('缺少檔案：' + name)
links = 0
for md in root.rglob('*.md'):
    for target in re.findall(r'\]\(([^)]+)\)', md.read_text(encoding='utf-8')):
        if target.startswith(('https:', 'http:', '#', 'mailto:')):
            continue
        links += 1
        if not (md.parent / target.split('#')[0]).exists():
            errors.append(f'失效連結：{md.relative_to(root)} → {target}')
manifest = json.loads((root / 'release/image-sha256.json').read_text())
images = sorted((root / 'assets/images').glob('*.png'))
if len(images) != 8 or len(manifest) != 8:
    errors.append('圖片數量必須為 8')
dimensions = {}
for index, image in enumerate(images, 1):
    data = image.read_bytes()
    key = image.relative_to(root).as_posix()
    if not image.name.startswith(f'{index:02d}-'):
        errors.append('頁碼檔名順序錯誤：' + key)
    if data[:8] != b'\x89PNG\r\n\x1a\n':
        errors.append('非 PNG：' + key)
    else:
        dimensions[key] = struct.unpack('>II', data[16:24])
    if hashlib.sha256(data).hexdigest() != manifest.get(key):
        errors.append('雜湊不符：' + key)
print(json.dumps({'result': 'FAIL' if errors else 'PASS', 'images': len(images),
                  'relative_links': links, 'dimensions': dimensions,
                  'errors': errors}, ensure_ascii=False, indent=2))
raise SystemExit(bool(errors))
