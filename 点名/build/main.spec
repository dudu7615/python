# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['D:/dudu/Documents/dudu/Python/点名/main.py'],
    pathex=[],
    binaries=[],
    datas=[('D:/dudu/Documents/dudu/Python/点名/names.pkl', '.'), ('D:/dudu/Documents/dudu/Python/点名/icon.png', '.'), ('D:/dudu/Documents/dudu/Python/点名/style.qss', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['D:\\dudu\\Documents\\dudu\\Python\\点名\\icon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
