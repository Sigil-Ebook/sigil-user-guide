name: Trigger Website Update

on:
  release:
    types: published

  workflow_dispatch: 
    branches: [ master ]

jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - name: Remote Workflow
        run: |
          curl \
            -X POST \
            -H "Accept: application/vnd.github.v3+json" \
            -H "Authorization: token ${{ secrets.ROBO_ACTIONS }}" \
            https://api.github.com/repos/sigil-ebook/sigil-ebook.github.io/actions/workflows/check_versions.yml/dispatches \
            -d '{"ref":"master"}'
