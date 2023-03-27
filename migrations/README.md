#### Create migration
```bash
alembic revision -m "create houses table"
alembic -n common revision -m "create houses table"
```

#### Update migration ecosystem
```bash
alembic upgrade head
```

#### Update migration realty
```bash
alembic -n common upgrade heads
```

#### Downgrade migration
```bash
alembic downgrade -1
alembic -n common downgrade -1
```

#### Autogenerate migration
```bash
alembic revision --autogenerate -m "Added account table"
```