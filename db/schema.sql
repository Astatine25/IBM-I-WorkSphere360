CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  role VARCHAR(20)
);

CREATE TABLE leaves (
  id SERIAL PRIMARY KEY,
  user_id INT,
  from_date DATE,
  to_date DATE,
  status VARCHAR(20)
);
