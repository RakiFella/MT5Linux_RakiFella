FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml requirements.txt ./
COPY MT5Linux_RakiFella ./MT5Linux_RakiFella
COPY README.md ./

RUN pip install --no-cache-dir build && \
    python -m build && \
    pip install --no-cache-dir dist/*.whl

RUN python -c "import MT5Linux_RakiFella; import numpy; import plumbum; import pyparsing; import rpyc; print('All dependencies imported successfully!')"

CMD ["python", "-c", "from MT5Linux_RakiFella import MetaTrader5; print('MT5Linux_RakiFella ready')"]
