#!/bin/sh
faltan=0
for f in README.md LICENSE CONTRIBUTING.md; do
  if [ -f "$GITHUB_WORKSPACE/$f" ]; then
    echo "OK: $f existe"
  else
    echo "FALTA: $f"
    faltan=1
  fi
done
if [ "$faltan" -eq 1 ]; then
  echo "::error::Falta documentación"
  exit 1
fi