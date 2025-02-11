cd D:\MyRepository\notebook-publish\notebook
git add .
git commit -m "auto commit"
git push origin master

mkdocs gh-deploy

Get-Process | Out-File "D:\MyRepository\notebook-publish\notebook\auto-log\process_log.txt"

Get-Service | Out-File "D:\MyRepository\notebook-publish\notebook\auto-log\service_log.txt"