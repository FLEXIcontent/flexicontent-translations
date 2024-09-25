#!/bin/bash

declare -a languageMap=(
  "cs-CZ"
  "de-DE"
  "el-GR"
  "en-GB"
  "es-ES"
  "fr-FR"
  "it-IT"
  "ja-JP"
  "pl-PL"
  "pt-BR"
  "pt-PT"
  "ru-RU"
  "sv-SE"
  "th-TH"
  "tr-TR"
  "zh-TW"
)

# create distribution directory
mkdir ./distribution

# create asset for each language
for lang in "${languageMap[@]}"; do
  pushd ./translations/"$lang" || exit
  zip -r "$OLDPWD"/distribution/"$lang".zip .
  popd || exit
done
