cd D:\MyRepository\notebook-publish\notebook
git add . > "D:\MyRepository\notebook-publish\notebook\auto-log\log.txt" 2>&1
git commit -m "auto commit" > "D:\MyRepository\notebook-publish\notebook\auto-log\log.txt" 2>&1
git push origin master > "D:\MyRepository\notebook-publish\notebook\auto-log\log.txt" 2>&1

mkdocs gh-deploy > "D:\MyRepository\notebook-publish\notebook\auto-log\log.txt" 2>&1

Get-Process | Out-File "D:\MyRepository\notebook-publish\notebook\auto-log\process_log.txt" > "D:\MyRepository\notebook-publish\notebook\auto-log\log.txt" 2>&1

Get-Service | Out-File "D:\MyRepository\notebook-publish\notebook\auto-log\service_log.txt" > "D:\MyRepository\notebook-publish\notebook\auto-log\log.txt" 2>&1