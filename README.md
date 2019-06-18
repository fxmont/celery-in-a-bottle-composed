# Example docker project

celery (rabbitmq acts as a broker and redis as a backend) + web server (simple api with bottle)

## Running

```
docker-compose up
```

and then open localhost:5005. This will launch a celery task that divides two random numbers and outputs result as json.
