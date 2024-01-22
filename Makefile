cat:
	cat Makefile

run:
	./app.py

css:
	tailwindcss -i "static/src/tw.css" -o "static/css/main.css" --watch
