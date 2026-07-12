import sys
import os
from PyInstaller.utils.hooks import collect_all, collect_submodules

block_cipher = None

datas = [
    ('MT5Linux_RakiFella', 'MT5Linux_RakiFella'),
]

hiddenimports = [
    'rpyc',
    'rpyc.cli',
    'rpyc.cli.rpyc_classic',
    'rpyc.core',
    'rpyc.core.service',
    'rpyc.core.channel',
    'rpyc.lib',
    'rpyc.utils',
    'rpyc.utils.classic',
    'MT5Linux_RakiFella',
    'MT5Linux_RakiFella.metatrader5',
    'MT5Linux_RakiFella.constants',
    'ctypes',
    'socket',
    'threading',
    'time',
    'datetime',
    'struct',
    'collections',
    'inspect',
    'weakref',
    'copy',
    'functools',
    'typing',
    'numpy',
    'plumbum',
    'pyparsing',
]

a = Analysis(
    ['MT5Linux_RakiFella/__main__.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='mt5server',
    debug=False,
    bootloader_warning=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
