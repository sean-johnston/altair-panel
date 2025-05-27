pyinstaller \
  --onefile \
  --add-data altair-panel.png:. \
  --add-data "led-off.png:." \
  --add-data "led-on.png:." \
  --add-data "led-on-dim.png:." \
  --add-data "switch-down.png:." \
  --add-data "switch-middle.png:." \
  --add-data "switch-up.png:." \
  altair-panel.py
