export FLASK_APP=towncrier
if [[ -z "${PORT}" ]]; then
  export PORT=5000
fi
flask run --host 0.0.0.0 --port $PORT