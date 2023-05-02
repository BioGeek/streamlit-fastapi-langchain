mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
enableXsrfProtection=false\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
