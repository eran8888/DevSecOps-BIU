CREATE TABLE users (
  full_name VARCHAR(100),
  username VARCHAR(100) PRIMARY KEY
);

CREATE TABLE follows (
  from_user VARCHAR(100),
  to_user VARCHAR(100)
);

CREATE TABLE tweets (
  id SERIAL,
  username VARCHAR(100),
  text VARCHAR(500),
  created_at DATE NOT NULL DEFAULT CURRENT_DATE
);