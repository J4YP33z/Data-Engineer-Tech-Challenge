FROM postgres
ENV POSTGRES_PASSWORD=mysecretpassword
ENV POSTGRES_DB=section_2
COPY create_tables.sql /docker-entrypoint-initdb.d/
