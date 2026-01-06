Instructions for the basic usage of the kafka setup

```bash
pip install -r requirements.txt
docker compose up
python3 kakfa/producer.py
python3 kafka/tracker.py
```

You can now try to modify `example_order` and run producer.py again to see new log sent
