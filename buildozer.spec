name: Android Build
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Build with Buildozer
        uses: ArtemSerebriakov/buildozer-action@v1
        with:
          buildozer_version: master
          command: buildozer android debug
          repository_root: .  # fayllar turgan asosiy papka
