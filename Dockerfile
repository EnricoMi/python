FROM python:3.12-alpine

LABEL repository="https://github.com/EnricoMi/python"
LABEL homepage="https://github.com/EnricoMi/python"
LABEL maintainer="Enrico Minack <github@Enrico.Minack.dev>"

LABEL com.github.actions.name="Docker action"
LABEL com.github.actions.description="A GitHub Action to inspect running docker actions."
LABEL com.github.actions.icon="check-circle"
LABEL com.github.actions.color="green"

ENTRYPOINT ["env"]
