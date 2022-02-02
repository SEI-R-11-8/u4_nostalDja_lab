-- settings.sql
CREATE DATABASE nostadja;
CREATE USER nostadjauser WITH PASSWORD 'nostadja';
GRANT ALL PRIVILEGES ON DATABASE nostadja TO nostadjauser;