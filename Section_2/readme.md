docker build -t pg-img .
docker run --name pg-container -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d pg-img
