## Overview
This application takes parameter as a list of instance, then goes through each of those and remove vulnerable rule.
In general, any inbound rule that accepts any client (0.0.0.0) would be removed.

### Extending to other rules
Yet the application now only removes any inbound with 0.0.0.0 client on port 22, we can add more rules to filter out as well.
To do this, a new rule as tuple to TARGET_TO_REMOVE constant in instance.py:

e.g.:
```bash
TARGET_TO_REMOVE = [('inbound', '0.0.0.0/0', 22), ('outbound', '0.0.0.0/0', 22)]
```

### Testing:
This application uses ```pytest``` as a testing tool.

## Running locally:
```bash
### Application
python main.py

### Testing
python3 -m pytest tests

### Or with Docker
docker-compose up
```
This will print out the filtered rules.
We can modify the parameters by adding more rules


